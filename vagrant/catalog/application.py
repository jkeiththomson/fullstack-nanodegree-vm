from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Instrument

app = Flask(__name__)

engine = create_engine('sqlite:///orchestra.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


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
    app.debug = True
    app.run(host='0.0.0.0', port=5000)