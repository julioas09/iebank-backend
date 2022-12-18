from iebank_api.models import Recipe
import pytest

def test_create_recipe():

    recipe = Recipe('Schnitzel', 'meat, eggs, flour, breadcrumbs, oil, cranberries, lemons', 'do a bunch of shit', 4, False)
    assert recipe.name == 'Schnitzel'
    assert recipe.ingredients == 'meat, eggs, flour, breadcrumbs, oil, craberries, lemons'
    assert recipe.steps == 'do a bunch of shit'
    assert recipe.rating == 4
    assert recipe.favorite == False