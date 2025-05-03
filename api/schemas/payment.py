from pydantic import BaseModel

class PaymentBase(BaseModel):
    order_id: int
    amount: float
    paid: bool

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        from_attributes = True
