# main.py

from fastapi import FastAPI
from api.controllers import users, payments
from api.routers import menu


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Include your routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(menu.router, prefix="/menu", tags=["Menu"])

