from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models import order as model
from ..schemas import order as schema

def create(db: Session, order: schema.OrderCreate):
    db_order = model.Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def read_all(db: Session):
    return db.query(model.Order).all()

def read_one(db: Session, order_id: int):
    order = db.query(model.Order).filter(model.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

def update(db: Session, order_id: int, updated_order: schema.OrderCreate):
    db_order = db.query(model.Order).filter(model.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    for field, value in updated_order.model_dump().items():
        setattr(db_order, field, value)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete(db: Session, order_id: int):
    db_order = db.query(model.Order).filter(model.Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    db.delete(db_order)
    db.commit()
    return {"message": "Order deleted successfully"}
