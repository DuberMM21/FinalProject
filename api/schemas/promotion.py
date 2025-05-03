from pydantic import BaseModel

class PromotionBase(BaseModel):
    title: str
    description: str
    discount: float
    active: bool

class PromotionCreate(PromotionBase):
    pass

class Promotion(PromotionBase):
    id: int

    class Config:
        from_attributes = True  # for Pydantic v2 compatibility
