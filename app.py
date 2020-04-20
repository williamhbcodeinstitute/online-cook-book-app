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
    return render_template("index.html", menus=mongo.db.menu.find())


@app.route('/menu/<menu_type>')
def get_menu_details(menu_type):
    title = ''
    if menu_type == 'breakfast':
        title = 'Breakfast Menu'
    elif menu_type == 'lunch':
        title = 'Lunch Menu'
    elif menu_type == 'dinner':
        title = 'Dinner Menu'
    elif menu_type == 'dessert':
        title = 'Dinner Menu'
    return render_template('menu_details.html', recipes=mongo.db.recipes.find({"menu_type": menu_type}), title=title)


@app.route('/menus/add_recipe')
def add_recipe():
    return render_template("addrecipe.html",  menus=mongo.db.menu.find())

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('get_menus'))

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_recipes = mongo.db.recipes.find()
    return render_template('editrecipe.html', recipes=the_recipe,
                           recipe=all_recipes)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    recipe.update({'_id': ObjectId(recipe_id)},
    {
        'menu_type': request.form.get('menu_type'),
        'dish': request.form.get('dish'),
        'time': request.form.get('time'),
        'cost': request.form.get('cost'),
        'ingredients': request.form.get('ingredients'),
        'preparation': request.form.get('preparation')
    })
    return redirect(url_for('get_menus'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)
