from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import users as schema
from ..dependencies.database import get_db
from ..controllers import users as controller

router = APIRouter(tags=["Users"], prefix="/users")

@router.post("/", response_model=schema.User)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):
    return controller.create(db, user=user)

@router.get("/", response_model=list[schema.User])
def read_users(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{user_id}", response_model=schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, user_id=user_id)

@router.put("/{user_id}", response_model=schema.User)
def update_user(user_id: int, user: schema.UserCreate, db: Session = Depends(get_db)):
    return controller.update(db, user_id=user_id, user=user)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, user_id=user_id)
