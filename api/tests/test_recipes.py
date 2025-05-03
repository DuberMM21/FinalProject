from fastapi.testclient import TestClient
from api.controllers import recipes as controller
from main import app
import pytest
from api.schemas import recipe as schema

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_recipe(db_session):
    recipe_data = {
        "title": "Classic BLT",
        "description": "Bacon, lettuce, and tomato on toasted bread."
    }
    recipe_obj = schema.RecipeCreate(**recipe_data)
    result = controller.create(db_session, recipe_obj)
    assert result.title == "Classic BLT"
    assert result.description == "Bacon, lettuce, and tomato on toasted bread."
