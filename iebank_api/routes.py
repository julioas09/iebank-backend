from flask import Flask, request
from iebank_api import db, app
from iebank_api.models import Recipe


@app.route('/skull', methods=['GET'])
def skull():
    return 'Hi! This is the BACKEND SKULL! 💀'


@app.route('/recipes', methods=['POST'])
def create_recipe():
    name = request.json['name']
    ingredients = request.json['ingredients']
    steps = request.json['steps']
    rating = request.json['rating']
    favorite = request.json['favorite']
    recipe = format_recipe(name, ingredients, steps, rating, favorite)
    db.session.add(recipe)
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes', methods=['GET'])
def get_all_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [format_recipe(recipe) for recipe in recipes]}

@app.route('/recipe/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get(id)
    return format_recipe(recipe)

@app.route('/recipe/<int:id>', methods=['PUT'])
def edit_recipe(id):
    recipe = Recipe.query.get(id)
    recipe.name = request.json['name']
    recipe.ingredients = request.json['ingredients']
    recipe.steps = request.json['steps']
    recipe.rating = request.json['rating']
    recipe.favorite = request.json['favorite']
    db.session.commit()
    return format_recipe(recipe)

@app.route('/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    return format_recipe(recipe)

def format_recipe(recipe):
    return {
        'id': recipe.id,
        'name': recipe.name,
        'ingredients': recipe.ingredients,
        'steps': recipe.steps,
        'rating': recipe.rating,
        'favorite': recipe.favorite
    }