from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from api.schemas import payment as schema
from api.controllers import payments as controller
from api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schema.Payment, status_code=status.HTTP_201_CREATED)
def create_payment(item: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.create(db, item)

@router.get("/", response_model=List[schema.Payment])
def read_all_payments(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Payment)
def read_payment(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.Payment)
def update_payment(item_id: int, item: schema.PaymentCreate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, item)

@router.delete("/{item_id}")
def delete_payment(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
