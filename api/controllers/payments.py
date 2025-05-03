from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.models.payment import Payment
from api.schemas.payment import PaymentCreate

def create(db: Session, item: PaymentCreate):
    new_payment = Payment(**item.model_dump())
    try:
        db.add(new_payment)
        db.commit()
        db.refresh(new_payment)
        return new_payment
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def read_all(db: Session):
    return db.query(Payment).all()

def read_one(db: Session, item_id: int):
    payment = db.query(Payment).filter(Payment.id == item_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

def update(db: Session, item_id: int, item: PaymentCreate):
    db_payment = db.query(Payment).filter(Payment.id == item_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    for field, value in item.model_dump().items():
        setattr(db_payment, field, value)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def delete(db: Session, item_id: int):
    db_payment = db.query(Payment).filter(Payment.id == item_id).first()
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    db.delete(db_payment)
    db.commit()
    return {"message": "Payment deleted successfully"}
