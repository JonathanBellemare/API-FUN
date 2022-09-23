from fastapi import APIRouter

router = APIRouter(prefix="/endpoint1", tags=["endpoint1"])

@router.get("/")
async def test():
    return {"response": "test1"}