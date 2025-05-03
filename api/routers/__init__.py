from .menu import router as menu_router
from .order_details import router as order_details_router
from .orders import router as orders_router
from .payments import router as payments_router
from .users import router as users_router


def load_routes(app):
    routes = [
        (menu_router, "/menu", ["Menu"]),
        (order_details_router, "/order-details", ["Order Details"]),
        (orders_router, "/orders", ["Orders"]),
        (payments_router, "/payments", ["Payments"]),
        (users_router, "/users", ["Users"]),
    ]

    for router, prefix, tags in routes:
        app.include_router(router, prefix=prefix, tags=tags)
