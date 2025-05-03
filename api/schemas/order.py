from pydantic import BaseModel

class OrderBase(BaseModel):
    customer_name: str
    description: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        from_attributes = True
