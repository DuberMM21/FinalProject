# routers/index.py
from fastapi import APIRouter
from .menu import router as menu_router
from .order_details import router as order_details_router
from .orders import router as orders_router
from .payments import router as payments_router
from .users import router as users_router

router = APIRouter()

def load_routes(app):
    app.include_router(menu_router, prefix="/menu", tags=["Menu"])
    app.include_router(order_details_router, prefix="/order-details", tags=["Order Details"])
    app.include_router(orders_router, prefix="/orders", tags=["Orders"])
    app.include_router(payments_router, prefix="/payments", tags=["Payments"])
    app.include_router(users_router, prefix="/users", tags=["Users"])
