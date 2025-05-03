from api.schemas import orders as schema
from api.controllers import orders as controller

def test_create_order(db_session):
    order_data = {
        "customer_name": "John Doe",
        "description": "Test order"
    }
    order_obj = schema.OrderCreate(**order_data)
    result = controller.create(db_session, order_obj)
    assert result.customer_name == "John Doe"
