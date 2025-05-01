from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import promotions as controller
from ..schemas.promotions import PromotionCreate, Promotion
from ..dependencies.database import get_db

router = APIRouter(
    prefix="/promotions",
    tags=["Promotions"]
)

@router.post("/", response_model=Promotion)
def create_promotion(request: PromotionCreate, db: Session = Depends(get_db)):
    return controller.create_promotion(db, request)


@router.get("/", response_model=list[Promotion])
def get_promotions(db: Session = Depends(get_db)):
    return controller.get_promotions(db)


@router.get("/{code}", response_model=Promotion)
def get_promotion_by_code(code: str, db: Session = Depends(get_db)):
    return controller.get_promotion_by_code(db, code)


@router.delete("/{promo_id}", status_code=204)
def delete_promotion(promo_id: int, db: Session = Depends(get_db)):
    return controller.delete_promotion(db, promo_id)
