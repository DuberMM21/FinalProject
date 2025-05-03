from api.schemas import sandwiches as schema
from api.controllers import sandwiches as controller

def test_create_sandwich(db_session):
    sandwich_data = {
        "name": "Chicken Club",
        "description": "Grilled chicken with bacon",
        "price": 7.99,
        "ingredients": "Grilled chicken, bacon, lettuce, tomato, mayo",
        "available": True
    }
    sandwich_obj = schema.SandwichCreate(**sandwich_data)
    result = controller.create(db_session, sandwich_obj)
    assert result.name == "Chicken Club"
