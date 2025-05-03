from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.models.order_detail import OrderDetail
from api.schemas.order_detail import OrderDetailCreate

def create(db: Session, item: OrderDetailCreate):
    new_item = OrderDetail(**item.model_dump())
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def read_all(db: Session):
    return db.query(OrderDetail).all()

def read_one(db: Session, item_id: int):
    item = db.query(OrderDetail).filter(OrderDetail.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Order detail not found")
    return item

def update(db: Session, item_id: int, item: OrderDetailCreate):
    db_item = db.query(OrderDetail).filter(OrderDetail.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Order detail not found")
    for key, value in item.model_dump().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete(db: Session, item_id: int):
    db_item = db.query(OrderDetail).filter(OrderDetail.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Order detail not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Order detail deleted successfully"}
