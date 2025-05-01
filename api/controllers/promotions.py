from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError
from ..models import promotions as model
from ..schemas import promotions as schema
from datetime import datetime


def create_promotion(db: Session, request: schema.PromotionCreate):
    new_promo = model.Promotion(
        code=request.code,
        expiration_date=request.expiration_date
    )

    try:
        db.add(new_promo)
        db.commit()
        db.refresh(new_promo)
    except SQLAlchemyError as e:
        error = str(e.__dict__["orig"])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_promo


def get_promotions(db: Session):
    try:
        return db.query(model.Promotion).all()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


def get_promotion_by_code(db: Session, code: str):
    promo = db.query(model.Promotion).filter(model.Promotion.code == code).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promo


def delete_promotion(db: Session, promo_id: int):
    promo = db.query(model.Promotion).filter(model.Promotion.id == promo_id).first()
    if not promo:
        raise HTTPException(status_code=404, detail="Promotion not found")

    try:
        db.delete(promo)
        db.commit()
    except SQLAlchemyError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {"detail": "Promotion deleted"}
