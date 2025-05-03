from fastapi.testclient import TestClient
from api.controllers import reviews as controller
from main import app
import pytest
from api.schemas import review as schema

client = TestClient(app)

@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_create_review(db_session):
    review_data = {
        "reviewer_name": "Alice",
        "content": "Great sandwich!"
    }
    review_obj = schema.ReviewCreate(**review_data)
    result = controller.create(db_session, review_obj)
    assert result.reviewer_name == "Alice"
    assert result.content == "Great sandwich!"
