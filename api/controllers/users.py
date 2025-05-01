from sqlalchemy.orm import Session
from ..models.users import User
from ..schemas.users import UserCreate

def create(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def read_all(db: Session):
    return db.query(User).all()

def read_one(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for field, value in user.dict().items():
            setattr(db_user, field, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return {"message": "User deleted"}
