from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.models import promotion as model
from api.schemas import promotion as schema
from api.dependencies.database import get_db

router = APIRouter()

@router.post("/", response_model=schema.Promotion)
def create_promotion(promotion: schema.PromotionCreate, db: Session = Depends(get_db)):
    new_promotion = model.Promotion(
        title=promotion.title,
        description=promotion.description,
        discount=promotion.discount,
        active=promotion.active
    )
    try:
        db.add(new_promotion)
        db.commit()
        db.refresh(new_promotion)
        return new_promotion
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
