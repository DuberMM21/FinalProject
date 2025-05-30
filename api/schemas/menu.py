from pydantic import BaseModel

class MenuBase(BaseModel):
    name: str
    description: str
    price: float

class MenuCreate(MenuBase):
    pass

class Menu(MenuBase):
    id: int

    class Config:
        from_attributes = True
