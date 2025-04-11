from pydantic import BaseModel
from typing import Optional

# ========================
# Shared Review Fields
# ========================
class ReviewBase(BaseModel):
    rating: int  # Expected to be 1–5
    text: Optional[str] = None
    customer_id: int
    order_id: int

# ========================
# For Creating a Review
# ========================
class ReviewCreate(ReviewBase):
    pass

# ========================
# For Returning a Review
# ========================
class Review(ReviewBase):
    id: int

    class Config:
        orm_mode = True
