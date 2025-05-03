from api.schemas import users as schema
from api.controllers import users as controller

def test_create_user(db_session):
    user_data = {
        "name": "Test User",
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "securepassword123"
    }
    user_obj = schema.UserCreate(**user_data)
    result = controller.create(db_session, user_obj)
    assert result.username == "testuser"
