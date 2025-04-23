from fastapi import APIRouter
from whisper.services import create_queue
import asyncio

router = APIRouter(
    prefix="/transcriptions",
    tags=["transcriptions"],
    responses={404: {"description": "No encontrado"}},
)

@router.get("/")
async def read_users():
    return {"message": "Bienvenido a la API principal de transcripcion"}

@router.post("/")
async def transcribe():
    queue = create_queue()
    return { "id": queue[0], "status": queue[2] }
