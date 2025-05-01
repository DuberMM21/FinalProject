from sqlalchemy.orm import Session
from ..models.menu import Menu
from ..schemas.menu import MenuCreate

def create(db: Session, menu: MenuCreate):

    existing_menu = db.query(Menu).filter(Menu.name == menu.name).first()
    if existing_menu:
        print(f"Menu item with name {menu.name} already exists")
        return existing_menu

    db_menu = Menu(
        name=menu.name,
        description=menu.description,
        price=menu.price,
    )
    print(f"Created Menu: {db_menu}")

    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)

    print(f"Menu after commit: {db_menu}")

    return db_menu

def read_all(db: Session):
    return db.query(Menu).all()

def read_one(db: Session, menu_id: int):
    return db.query(Menu).filter(Menu.id == menu_id).first()

def update(db: Session, menu_id: int, menu: MenuCreate):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if db_menu:
        db_menu.name = menu.name
        db_menu.description = menu.description
        db_menu.price = menu.price
        db.commit()
        db.refresh(db_menu)
        return db_menu
    return None

def delete(db: Session, menu_id: int):
    db_menu = db.query(Menu).filter(Menu.id == menu_id).first()
    if db_menu:
        db.delete(db_menu)
        db.commit()
        return {"detail": "Menu item deleted successfully"}
    return {"detail": "Menu item not found"}
