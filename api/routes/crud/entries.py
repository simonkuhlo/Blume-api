from fastapi import APIRouter

prefix: str = "/entries"

router = APIRouter(prefix=prefix)

@router.get("/hello")
async def hello():
    return {"hello": "world"}