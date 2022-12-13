from fastapi import APIRouter
from app.logic.logic import Logic

router = APIRouter(prefix="/endpoint1", tags=["endpoint1"])

@router.get("/")
async def test():
    return {"response": "test1"}

@router.get("/logic")
async def logic():
    return Logic.do_logic()