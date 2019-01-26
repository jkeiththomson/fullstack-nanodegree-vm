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
        'login.html', STATE=state)

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

    # use gogle+ api to get some user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()

    # grab the desired user info from the returned data oebject
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    # user_id = getUserID(data["email"])
    # if not user_id:
    #     user_id = createUser(login_session)
    # login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    # flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# User Helper Functions


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

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
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# MAIN SCREEN - Orchestra page with no category selected
@app.route('/')
@app.route('/orchestra/')
def showOrchestra():
    categories = session.query(Category).all()
    return render_template(
        'showorchestra.html', categories=categories)

# CATEGORY SCREEN - Orchestra page with a category selected
@app.route('/category/<int:category_id>/')
def showCategory(category_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(id=category_id).one()
    instruments = session.query(Instrument).filter_by(category_id=category_id)
    return render_template(
        'showcategory.html', categories=categories, category=category, instruments=instruments,
        category_id=category_id)

# INSTRUMENT DETAILS SCREEN
@app.route('/category/<int:category_id>/instrument/<int:instrument_id>/')
def showInstrument(category_id, instrument_id):
    instrument = session.query(Instrument).filter_by(id=instrument_id).one()
    category = session.query(Category).filter_by(id=instrument.category_id).one()
    return render_template(
        'showinstrument.html', instrument=instrument, category=category)

# NEW INSTRUMENT SCREEN
@app.route('/category/<int:category_id>/instrument/new')
def newInstrument(category_id):
    if request.method == 'POST':
        newItem = Instrument(
            name=request.form['name'],
            description=request.form['description'],
            category=getCategoryId(request.form['category']))
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategory', category_id=newItem.category_id))
    else:
        return render_template('newinstrument.html', category_id=category_id)

# EDIT INSTRUMENT SCREEN
@app.route('/category/<int:category_id>/instrument/<int:instrument_id>/edit',
           methods=['GET', 'POST'])
def editInstrument(category_id, instrument_id):
    categories = session.query(Category).all()
    editedInstrument = session.query(Instrument).filter_by(id=instrument_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedInstrument.name = request.form['name']
        if request.form['description']:
            editedInstrument.description = request.form['description']
        if request.form['category']:
            catName = request.form['category']
            for c in categories:
                if c.name == catName:
                    editedInstrument.category_id = c.id

        session.add(editedInstrument)
        session.commit()
        return redirect(url_for('showInstrument', category_id=editedInstrument.category_id,
            instrument_id=editedInstrument.id   ))
    else:
        return render_template(
            'editinstrument.html', categories=categories, item=editedInstrument)

# DELETE INSTRUMENT SCREEN
@app.route('/category/<int:category_id>/instrument/<int:instrument_id>/delete',
           methods=['GET', 'POST'])
def deleteInstrument(category_id, instrument_id):
    itemToDelete = session.query(Instrument).filter_by(id=instrument_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showCategory', category_id=category_id))
    else:
        return render_template('deleteInstrument.html', item=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'a_really_really_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)