from flask import Flask, flash
app = Flask(__name__)

@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
	return("This page will show all restaurants")

@app.route('/restaurant/new')
def newRestaurant():
	return("This page will allow me to add a new restaurant")

@app.route('/restaurant/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
	return("This page will be for editing restaurant %s" % restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
	return("This page will delete a restaurant %s" % restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
	return("This page will show the menu for restaurant %s" % restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/new')
def newMenuItem(restaurant_id):
	return("This page will add a new menu item to restaurant %s" % restaurant_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit')
def editMenuItem(restaurant_id,menu_id):
	return("This page will edit menu item %s" % menu_id)

@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete')
def deleteMenuItem(restaurant_id,menu_id):
	return("This page will delete menu item %s" % menu_id)


if __name__ == '__main__':
	app.secret_key = 'this_is_my_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
