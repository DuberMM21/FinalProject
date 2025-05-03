# controllers/menu.py
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from api.models.menu import Menu as MenuModel
from api.schemas.menu import MenuCreate

def create(db: Session, item: MenuCreate):
    new_item = MenuModel(**item.model_dump())
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def read_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MenuModel).offset(skip).limit(limit).all()

def read_one(db: Session, item_id: int):
    item = db.query(MenuModel).filter(MenuModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return item

def update(db: Session, item_id: int, item: MenuCreate):
    existing = db.query(MenuModel).filter(MenuModel.id == item_id).first()
    if existing is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    for key, value in item.model_dump().items():
        setattr(existing, key, value)
    db.commit()
    db.refresh(existing)
    return existing

def delete(db: Session, item_id: int):
    item = db.query(MenuModel).filter(MenuModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Menu item not found")
    db.delete(item)
    db.commit()
    return {"message": "Menu item deleted successfully"}
