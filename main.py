from fastapi import FastAPI
from api.routers import index

app = FastAPI()

# Load all routers from index.py
index.load_routes(app)
