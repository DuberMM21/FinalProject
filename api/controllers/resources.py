from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.models.resource import Resource
from api.schemas.resource import ResourceCreate

def create(db: Session, item: ResourceCreate):
    new_item = Resource(**item.model_dump())
    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def read_all(db: Session):
    return db.query(Resource).all()

def read_one(db: Session, item_id: int):
    item = db.query(Resource).filter(Resource.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Resource not found")
    return item

def update(db: Session, item_id: int, item: ResourceCreate):
    db_item = db.query(Resource).filter(Resource.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Resource not found")
    for field, value in item.model_dump().items():
        setattr(db_item, field, value)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete(db: Session, item_id: int):
    db_item = db.query(Resource).filter(Resource.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Resource not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Resource deleted successfully"}
