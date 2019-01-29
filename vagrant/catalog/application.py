from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Instrument
from flask import session as login_session
import random,  string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog"

engine = create_engine('sqlite:///orchestra.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

############## AUTHENITCATION ##################

# LOGIN SCREEN - Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template(
        'showlogin.html', STATE=state)

# GOOGLE CONNECT - user logs in with Google+ credentials
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # if state token from server doesn't match ours, return an error
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # otherise get one-time authorization code from server
    code = request.data

    try:
        # exchange the one-time authorization code for a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        # oops, the exchange failed, return error
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # see if there's a valid access token inside the credentials object
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])

    # if google didn't verify the access token, return an error
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # verify that the access token is used for the intended user
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # verify that the access token is valid for this app
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    # see if user is already logged in
    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # login was successful, store access token in the session for later use
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # use google+ api to get some user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()

    # grab the desired user info from the returned data oebject
    if 'name' in data:
        login_session['username'] = data['name']
    else:
        login_session['username'] = data['email']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += 'Login successful: '
    output += login_session['username']
    output += ' is now logged in!'
    return output

# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['email']
        del login_session['picture']
        del login_session['username']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return redirect(url_for('showOrchestra'))
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


############## USER INTERFACE SCREENS ##################

# HOME SCREEN - Orchestra page with no category selected
@app.route('/')
@app.route('/orchestra/')
def showOrchestra():
    categories = session.query(Category).all()
    uname = getUsername()
    return render_template(
        'showorchestra.html', username=uname, categories=categories)

# CATEGORY SCREEN - Orchestra page with a category selected
@app.route('/category/<int:category_id>/')
def showCategory(category_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    instruments = session.query(Instrument).filter_by(category_id=category_id)
    uname = getUsername()
    return render_template(
        'showcategory.html', username=uname, categories=categories,
        category=category, instruments=instruments, category_id=category_id)

# INSTRUMENT DETAILS SCREEN
@app.route('/category/<int:category_id>/instrument/<int:instrument_id>/')
def showInstrument(category_id, instrument_id):
    instrument = session.query(Instrument).filter_by(id=instrument_id).one()
    category = session.query(Category).filter_by(id=instrument.category_id).one()
    uname = getUsername()
    return render_template(
        'showinstrument.html', username=uname,
        instrument=instrument, category=category)

# NEW INSTRUMENT SCREEN
@app.route('/category/<int:category_id>/instrument/new', methods=['GET', 'POST'])
def newInstrument(category_id):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    categories = session.query(Category).all()
    uname = getUsername()
    if request.method == 'POST':
        cat_id = getCategoryId(request.form['category'])
        newItem = Instrument(
            name=request.form['name'],
            description=request.form['description'],
            picture_url=request.form['picture_url'],
            picture_attr=request.form['picture_attr'],
            category_id=cat_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategory', category_id=cat_id))
    else:
        return render_template(
            'newinstrument.html', username=uname,
            category_id=category_id, categories=categories)

# EDIT INSTRUMENT SCREEN
@app.route('/category/<int:category_id>/instrument/<int:instrument_id>/edit',
           methods=['GET', 'POST'])
def editInstrument(category_id, instrument_id):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    categories = session.query(Category).all()
    editedInstrument = session.query(Instrument).filter_by(id=instrument_id).one()
    uname = getUsername()
    if request.method == 'POST':
        if request.form['name']:
            editedInstrument.name = request.form['name']
        if request.form['description']:
            editedInstrument.description = request.form['description']
        if request.form['picture_url']:
            editedInstrument.picture_url = request.form['picture_url']
        if request.form['picture_attr']:
            editedInstrument.picture_attr = request.form['picture_attr']
        if request.form['category']:
            editedInstrument.category_id = getCategoryId(request.form['category'])
        session.add(editedInstrument)
        session.commit()
        return redirect(url_for('showInstrument', category_id=editedInstrument.category_id,
            instrument_id=editedInstrument.id   ))
    else:
        return render_template(
            'editinstrument.html', username=uname,
            categories=categories, item=editedInstrument)

# DELETE INSTRUMENT SCREEN
@app.route('/category/<int:category_id>/instrument/<int:instrument_id>/delete',
           methods=['GET', 'POST'])
def deleteInstrument(category_id, instrument_id):
    if 'username' not in login_session:
        return redirect(url_for('showLogin'))
    itemToDelete = session.query(Instrument).filter_by(id=instrument_id).one()
    uname = getUsername()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showCategory', category_id=category_id))
    else:
        return render_template(
            'deleteInstrument.html', username=uname, item=itemToDelete)

# HELPER FUNCTIONS
# given a category name, return its ID
def getCategoryId(catName):
    categories = session.query(Category).all()
    for c in categories:
        if c.name == catName:
            return c.id
    return None

# get logged in user's name
def getUsername():
    if 'username' in login_session:
        return login_session['username']
    return None


############## HANDLE API REQUESTS ##################

# API - Return all categories
@app.route('/categories/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(Categories=[c.serialize for c in categories])

# API - Return a single category
@app.route('/category/<int:category_id>/JSON')
def categoryJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    return jsonify(Category=category.serialize)

# API - Return all instruments
@app.route('/instruments/JSON')
def instrumentsJSON():
    instruments = session.query(Instrument).all()
    return jsonify(Instruments=[i.serialize for i in instruments])

# API - Return a single instrument
@app.route('/instrument/<int:instrument_id>/JSON')
def instrumentJSON(instrument_id):
    instrument = session.query(Instrument).filter_by(id=instrument_id).one()
    return jsonify(Instrument=instrument.serialize)


if __name__ == '__main__':
    app.secret_key = 'a_really_really_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)