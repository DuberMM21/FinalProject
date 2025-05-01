from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.menu import Menu, MenuCreate
from ..dependencies import get_db
from ..controllers.menu import create, read_all, read_one, update, delete

router = APIRouter(prefix="/menu", tags=["menu"])

@router.post("/", response_model=Menu)
def create_menu_item(menu: MenuCreate, db: Session = Depends(get_db)):
    return create(db=db, menu=menu)

@router.get("/", response_model=list[Menu])
def read_menu_items(db: Session = Depends(get_db)):
    return read_all(db)

@router.get("/{menu_id}", response_model=Menu)
def read_menu_item(menu_id: int, db: Session = Depends(get_db)):
    return read_one(db, menu_id)

@router.put("/{menu_id}", response_model=Menu)
def update_menu_item(menu_id: int, menu: MenuCreate, db: Session = Depends(get_db)):
    return update(db, menu_id, menu)

@router.delete("/{menu_id}")
def delete_menu_item(menu_id: int, db: Session = Depends(get_db)):
    return delete(db, menu_id)
