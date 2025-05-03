from pydantic import BaseModel

class ReviewBase(BaseModel):
    user_id: int
    reviewer_name: str
    comment: str
    rating: int
    approved: bool

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int

    class Config:
        from_attributes = True
