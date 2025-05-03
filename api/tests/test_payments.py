from api.schemas import payments as schema
from api.controllers import payments as controller

def test_create_payment(db_session):
    payment_data = {
        "order_id": 1,
        "amount": 25.00,
        "paid": True
    }
    payment_obj = schema.PaymentCreate(**payment_data)
    result = controller.create(db_session, payment_obj)
    assert result.amount == 25.00
