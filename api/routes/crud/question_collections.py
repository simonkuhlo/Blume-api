from fastapi import APIRouter

prefix: str = "/question_collections"

router = APIRouter(prefix=prefix)

@router.get("/hello")
async def hello():
    return {"hello": "world"}