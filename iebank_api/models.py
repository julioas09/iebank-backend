from iebank_api import db
from datetime import datetime
import string, random

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False, default=0)
    favorite = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, name, ingredients, steps, rating, favorite):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps
        self.rating = rating
        self.favorite = favorite