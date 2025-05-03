from pydantic import BaseModel

class OrderDetailBase(BaseModel):
    order_id: int
    menu_id: int
    quantity: int

class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetail(OrderDetailBase):
    id: int

    class Config:
        from_attributes = True
