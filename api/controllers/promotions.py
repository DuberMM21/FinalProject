from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models import promotions as models
from ..schemas import promotions as schemas

router = APIRouter()

@router.post("/", response_model=schemas.Promotion)
def create_promotion(promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    db_promotion = models.Promotion(**promotion.dict())
    db.add(db_promotion)
    db.commit()
    db.refresh(db_promotion)
    return db_promotion

@router.get("/", response_model=list[schemas.Promotion])
def get_promotions(db: Session = Depends(get_db)):
    return db.query(models.Promotion).all()

@router.get("/{promotion_id}", response_model=schemas.Promotion)
def get_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion

@router.put("/{promotion_id}", response_model=schemas.Promotion)
def update_promotion(promotion_id: int, updated_promotion: schemas.PromotionCreate, db: Session = Depends(get_db)):
    promotion = db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    for key, value in updated_promotion.dict().items():
        setattr(promotion, key, value)
    db.commit()
    db.refresh(promotion)
    return promotion

@router.delete("/{promotion_id}")
def delete_promotion(promotion_id: int, db: Session = Depends(get_db)):
    promotion = db.query(models.Promotion).filter(models.Promotion.id == promotion_id).first()
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    db.delete(promotion)
    db.commit()
    return {"detail": "Promotion deleted successfully"}
