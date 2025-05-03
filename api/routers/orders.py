from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.controllers import orders as controller
from api.schemas import order as schema
from api.dependencies.database import get_db

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schema.Order)
def create_order(order: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.create(db, order)

@router.get("/", response_model=list[schema.Order])
def get_orders(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{order_id}", response_model=schema.Order)
def get_order(order_id: int, db: Session = Depends(get_db)):
    db_order = controller.read_one(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}", response_model=schema.Order)
def update_order(order_id: int, order: schema.OrderCreate, db: Session = Depends(get_db)):
    return controller.update(db, order_id, order)

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, order_id)
