# Item Catalog Project

## Table of Contents

- [Instructions](#instructions)
- [Description](#descriptions)
- [Attributions](#attributions)
- [Contributing](#contributing)

## Instructions

This is my solution to the "Item Catalog" project from Udacity's "Full Stack Web Developer" nanodegree course.

### To install and run the website:

- The project relies on a Vagrant virtual machine (VM) that was pre-setup by Udacity. Instructions for setting up the VM can be found here: https://www.udacity.com/wiki/ud088/vagrant. The VM is a Linux server that will serve up this project's website.
- In your own OS (not the VM), browse to GitHub and log into your personal GitHub account. Navigate to the repository for this project: https://github.com/udacity/fullstack-nanodegree-vm
- Fork the repository and clone it to your computer (see the instructions at https://www.udacity.com/wiki/ud088/vagrant)
- cd into the .../vagrant/catalog folder
- Run the virtual machine (vagrant up) and log into it (vagrant ssh)
- To set up the website's database on the VM:
  - cd to /vagrant/catalog
  - run "python database_setup.py" to create the database ("orchestra.db")
  - run "python database_fill.py" to fill up the tables with data
  - run "python application.py" to start the server
- To see the project website
  - Fire up your browser of choice on your computer (not the VM)
  - Browse to http://localhost:5000

## Description

For this project I elected to create a database of the musical instruments found in a typical symphony orchestra. The "categories" are the sections of the orchestra and the "items" are the instruments.

Using the project website should be relatively self-explanatory. Choose a category on the left and choose an item on the right. You have to be logged in to create, modify or delete an item.

The app is marginally responsive at smaller screen sizes.

## Attributions

The text of the descripiions of sections and instruments are all taken from wikipeeia.org.

The photos are mostly taken from wikipedia.org. Hover the mouse over a photo to see its attribution credit.

All the new code is my own, based on snippets from the course materials.

There is one citation in styles.sss for some css code I borrowed to show the photo captions.

## Contributing

This is a class project. We will not accept pull requests.
