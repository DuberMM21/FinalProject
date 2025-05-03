from api.schemas import order_detail as schema
from api.controllers import order_details as controller

def test_create_order_detail(db_session):
    detail_data = {
        "order_id": 1,
        "menu_id": 1,
        "quantity": 2
    }
    detail_obj = schema.OrderDetailCreate(**detail_data)
    result = controller.create(db_session, detail_obj)
    assert result.quantity == 2
