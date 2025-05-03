from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.dependencies import get_db
from api.schemas import order_detail as schema
from api.controllers import order_details as controller

router = APIRouter()

@router.post("/", response_model=schema.OrderDetail)
def create_order_detail(item: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db, item)

@router.get("/", response_model=List[schema.OrderDetail])
def read_all_order_details(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.OrderDetail)
def read_order_detail(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.OrderDetail)
def update_order_detail(item_id: int, item: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, item)

@router.delete("/{item_id}")
def delete_order_detail(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
