from pydantic import BaseModel

class SandwichBase(BaseModel):
    name: str
    description: str
    ingredients: str
    price: float
    available: bool
    menu_id: int

class SandwichCreate(SandwichBase):
    pass

class Sandwich(SandwichBase):
    id: int

    class Config:
        from_attributes = True
