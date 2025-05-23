from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    username: str
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
