from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class Role(str, Enum):
    customer = "customer"
    admin = "admin"
    kitchen = "kitchen"
    manager = "manager"

# =========================
# Shared Base Model
# =========================
class UserBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None
    role: Optional[str] = Role.customer

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
