from fastapi import FastAPI
from controllers import users, payments

app = FastAPI()

app.include_router(users.router)
app.include_router(payments.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
