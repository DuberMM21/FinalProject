from fastapi.testclient import TestClient
from api.controllers import resources as controller
from main import app
import pytest
from api.schemas import resource as schema

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_resource(db_session):
    resource_data = {
        "name": "Spoon",
        "quantity": 200
    }
    resource_obj = schema.ResourceCreate(**resource_data)
    result = controller.create(db_session, resource_obj)
    assert result.name == "Spoon"
    assert result.quantity == 200
