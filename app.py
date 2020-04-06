import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cook_book'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)


@app.route('/')
@app.route('/menus')
def get_menus():
    return render_template("recipe.html", menus=mongo.db.menu.find())


@app.route('/menus/breakfast')
def get_breakfast():
    return render_template("breakfast.html", recipes=mongo.db.recipes.find({"menu_type": "breakfast"}))

@app.route('/menus/lunch')
def get_lunch():
    return render_template("lunch.html", recipes=mongo.db.recipes.find({"menu_type": "lunch"}))

@app.route('/menus/dinner')
def get_dinner():
    return render_template("dinner.html", recipes=mongo.db.recipes.find({"menu_type": "dinner"}))

@app.route('/menus/desert')
def get_desert():
    return render_template("desert.html", recipes=mongo.db.recipes.find({"menu_type": "desert"}))


@app.route('/menus/addrecipe')
def add_recipe():
    return render_template("addrecipe.html",  menus=mongo.db.menu.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_menus'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
