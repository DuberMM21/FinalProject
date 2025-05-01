from sqlalchemy.orm import Session
from ..models.payments import Payment
from ..schemas.payments import PaymentCreate

def create(db: Session, payment: PaymentCreate):
    db_payment = Payment(**payment.dict())
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

def read_all(db: Session):
    return db.query(Payment).all()

def read_one(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()

def update(db: Session, payment_id: int, payment: PaymentCreate):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment:
        for field, value in payment.dict().items():
            setattr(db_payment, field, value)
        db.commit()
        db.refresh(db_payment)
    return db_payment

def delete(db: Session, payment_id: int):
    db_payment = db.query(Payment).filter(Payment.id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
    return {"message": "Payment deleted"}
