from pydantic import BaseModel
from typing import Optional

...

class MenuCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class Menu(MenuCreate):
    id: int

    class Config:
        orm_mode = True