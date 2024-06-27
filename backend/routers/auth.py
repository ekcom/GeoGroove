from fastapi import APIRouter

router = APIRouter(
    tags=["auth"],
)

@router.get("/test2")
async def test2():
    return "herro"
