# api/schemas/payments.py

from pydantic import BaseModel
from typing import Literal, Optional

class PaymentBase(BaseModel):
    payment_type: Literal['card', 'cash']
    status: Optional[Literal['pending', 'completed', 'failed']] = 'pending'

class PaymentCreate(PaymentBase):
    order_id: int

class Payment(PaymentBase):
    id: int
    order_id: int

    class Config:
        orm_mode = True
