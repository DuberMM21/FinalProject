from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from api.models.user import User
from api.schemas.user import UserCreate

def create(db: Session, item: UserCreate):
    new_user = User(**item.model_dump())
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def read_all(db: Session):
    return db.query(User).all()

def read_one(db: Session, item_id: int):
    user = db.query(User).filter(User.id == item_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def update(db: Session, item_id: int, item: UserCreate):
    db_user = db.query(User).filter(User.id == item_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    for field, value in item.model_dump().items():
        setattr(db_user, field, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete(db: Session, item_id: int):
    db_user = db.query(User).filter(User.id == item_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
