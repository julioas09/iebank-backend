import pytest
from iebank_api.models import Recipe
from iebank_api import db, app


@pytest.fixture
def testing_recipe(scope='module'):
    db.create_all()
    recipe = Recipe('Test recipe', 'random shit, penis', 'ninja cooking moves', 4, True)
    db.session.add(recipe)
    db.session.commit()

    with app.test_recipe() as testing_recipe:
        yield testing_recipe

    db.drop_all()