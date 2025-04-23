from fastapi import APIRouter

router = APIRouter(
    prefix="/transcriptions",
    tags=["transcriptions"],
    responses={404: {"description": "No encontrado"}},
)

@router.get("/")
async def read_users():
    return {"message": "Bienvenido a la API principal de transcripcion"}
