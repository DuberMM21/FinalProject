from fastapi import FastAPI, HTTPException, Depends, status
from api.dependencies.database import Base, engine
import api.models.menu


from api.routers import users, menu, promotions
from pydantic import BaseModel
from sqlalchemy import create_engine

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

Base.metadata.create_all(bind=engine)

app.include_router(menu.router)
app.include_router(promotions.router)
app.include_router(users.router)