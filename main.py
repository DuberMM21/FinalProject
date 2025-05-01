from fastapi import FastAPI
from api.routers import index

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Load all routers from index.py
index.load_routes(app)
