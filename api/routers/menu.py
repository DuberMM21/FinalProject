# routers/menu.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from api.schemas import menu as schema
from api.controllers import menu as controller
from api.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=schema.Menu, status_code=status.HTTP_201_CREATED)
def create_menu(item: schema.MenuCreate, db: Session = Depends(get_db)):
    return controller.create(db, item)

@router.get("/", response_model=List[schema.Menu])
def read_all_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return controller.read_all(db, skip=skip, limit=limit)

@router.get("/{item_id}", response_model=schema.Menu)
def read_menu(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id)

@router.put("/{item_id}", response_model=schema.Menu)
def update_menu(item_id: int, item: schema.MenuCreate, db: Session = Depends(get_db)):
    return controller.update(db, item_id, item)

@router.delete("/{item_id}")
def delete_menu(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, item_id)
