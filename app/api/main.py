from enum import Enum
from fastapi import FastAPI

from app.api import endpoint1

app = FastAPI(title="API for fun")


class TestModel(str, Enum):
    jonathan = "jonathan"
    alex = "alex"

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/name")
async def name(name: TestModel):
    return {"name": name}


app.include_router(endpoint1.router)
