from fastapi import APIRouter

prefix: str = "/answers"

router = APIRouter(prefix=prefix)

@router.get("/hello")
async def hello():
    return {"hello": "world"}