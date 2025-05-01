from fastapi import FastAPI, HTTPException, Depends, status
from api.dependencies.database import Base, engine
import api.models.menu


from api.routers import menu
from pydantic import BaseModel
from sqlalchemy import create_engine
from fastapi import FastAPI
from api.routers import index

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

Base.metadata.create_all(bind=engine)

app.include_router(menu.router)


# Load all routers from index.py
index.load_routes(app)
