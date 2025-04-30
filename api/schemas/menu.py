from pydantic import BaseModel
from typing import Optional

...

class MenuBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class MenuCreate(MenuBase):
    id: int

class Menu(MenuBase):
    id: int

    class Config:
        orm_mode = True