from api.schemas import menu as schema
from api.controllers import menu as controller

def test_create_menu_item(db_session):
    menu_data = {
        "name": "Veggie Wrap",
        "price": 5.49
    }
    menu_obj = schema.MenuCreate(**menu_data)
    result = controller.create(db_session, menu_obj)
    assert result.name == "Veggie Wrap"
    assert result.price == 5.49
