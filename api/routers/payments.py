from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import payments as schema
from ..dependencies.database import get_db
from ..controllers import payments as controller

router = APIRouter(tags=["Payments"], prefix="/payments")

@router.post("/", response_model=schema.Payment)
def create_payment(payment: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db, payment=payment)

@router.get("/", response_model=list[schema.Payment])
def read_all_payments(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{payment_id}", response_model=schema.Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, payment_id=payment_id)

@router.put("/{payment_id}", response_model=schema.Payment)
def update_payment(payment_id: int, payment: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.update(db, payment_id=payment_id, payment=payment)

@router.delete("/{payment_id}")
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, payment_id=payment_id)
