from pydantic import BaseModel
from typing import Optional, List

# =========================
# Shared Base Model
# =========================
class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None

# =========================
# Schema for Creation
# =========================
class UserCreate(UserBase):
    pass

# =========================
# Schema for Return (with ID)
# =========================
class User(UserBase):
    id: int

    class Config:
        orm_mode = True
