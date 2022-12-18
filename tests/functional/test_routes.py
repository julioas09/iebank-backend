from iebank_api import app
import pytest

def test_get_recipe(testing_recipe):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_recipe.get('/recipes')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_recipe() as recipe:
        response = recipe.get('/wrong_path')
        assert response.status_code == 404

def test_create_recipe(testing_recipe):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_recipe.post('/recipes', json={'name': 'Schnitzel', 'ingredients': 'meat, eggs, flour, breadcrumbs, cranberries, lemons', 'steps': 'do a bunch of shit', 'rating': 4, 'favorite':False})
    assert response.status_code == 200


