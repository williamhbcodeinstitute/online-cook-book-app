# Milestone Project 3: Online Cook Book.

## UX
_____

The task for this project was to design an online cook book that uses a database to access and display the 
information on the webpage. The two choices of databases to be used are SQL and MongoDB. I chose MongoDB for my
project which is a flat based style of database meaning no nesting is required with ID's. I designed the site
based on a savers cook book which includes cheap and easy meals to cook from scratch. I wanted the user to
be able to follow the CRUD functionality of Create, Read, Edit and Delete. You can find the wireframes for
the site  in a seperate directory named **"static/wireframes"** embedded in my project.

## Features
___________

My site includes six pages home, add recipe menus/breakfast/lunch/dinner/dessert. 

* index.html: This file is for the home page of the site and includes the the four menus to select from, with 
an appropriate image displayed above each one. Each of the menu h2's is an anchor tag that when clicked will
take you to the recipe page for that type of meal e.g. clicking breakfast takes you the breakfast recipe page.
If you do not choose to navigate through the site this way you can also click the dropdown box on the navigation
bar titled 'Menu' and select through there.

* base.html: Includes the general layout that will be displayed over each page on the site. This will be the
layout for the navigation bar, heading and footer. The footer section contains links to social media pages.

* menu_details.html: This page will show the different type of menu. Using a function in my app.py file named
'get_menu_details' the type of menu that will be rendered depends on which one clicked e.g. breakfast, luch or dinner and 
displayes the title depending on each selected. This page includes seperate buttons to delete and edit a recipe.
Clicking the edit recipe button takes you to 'editrecipe.html' which has a form where you can edit each section
of the recipe, after making these changes there is a button at the bottom of the form that when clicked updates
the data to MongoDB and the site.

* addrecipe.html: The add recipe page includes a similar styled form to the edit recipe page but rather than
already having data from a previous recipe, this form has empty fields for the user to fill in that will add
a new recipe to the database. The user can get to this page via the navbar by selecting the add recipe link.
After doing this the site will re-direct you to the home page.

## Technologies used
______________________

* HTML5
* CSS3
* Bootstrap 4.3.1
* PyMongo - To help with using MongoDB
* Jinja - Used to help with displaying back-end development to html
* Flask framework


Links to libraries;
"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
"https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" type="text/css" />
"https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"
"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"
"https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"

## Testing
___________

* I started with an individual page and function for breakfast, lunch, dinner, dessert. But decided to reduce
the repetition of code to condense to one page named menu_details.html. Using an if statement in my app.py file, Flask
is able to render the page suited for which menu_type that is selected.

* To use the form for addrecipe.html you start by using a dropdown select menu which gives the options of menu_type.
Following this are textarea boxes that can be used to fill in the other parts of the information for the database e.g.
Dish, Cost, Time, Ingredients and Preparation. 

* Testing the layout of index.html I decided it would be visably better for the images to be displayed in two
seperate rows to cover more of the page leaving less empty spaces.

* With the drop down menu on edit_recipe it is always set to 'breakfast' as default which could confuse the
user updating the recipe. For the future I would create another if statement to show the menu_type that had been
selected.

## Deployment
______________

I have deployed my site through github and heroku.

GitHub link:  https://williamhbcodeinstitute.github.io/online-cook-book-app/
Heroku link:  https://milestone-project-3-cook-book.herokuapp.com/

### Heroku Deployment
______________________

started by pushing from git to heroku: https://www.heroku.com/

1. install heroku CLI - 'heroku login'

2. create requirements.txt file - 'pip freeze --local > requirements.txt'

3. create Procfile - 'echo web: python app.py > Procfile'

4. Deploy changes to Heroku using Git:
* git add .
* git commit -m ""
* git push -u heroku master

5. on the heroku dashboard, click on "Settings" > "Reveal Config Vars", setting them to:
IP: 0.0.0.0
PORT: 5000
MONGO_URI: mongodb+srv://<username>:<password>@cluster0-puroi.mongodb.net/cook_book?retryWrites=true&w=majority




