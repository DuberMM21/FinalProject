from pydantic import BaseModel
from datetime import datetime

# Base schema used for creation
class PromotionBase(BaseModel):
    code: str
    expiration_date: datetime

# For creating a new promotion
class PromotionCreate(PromotionBase):
    pass

# For reading a promotion (e.g., returning data)
class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True
