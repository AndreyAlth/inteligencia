from fastapi import APIRouter
from fastapi import Request, Response
from whisper.services import create_queue, error_queue
from whisper.modules import transcribe_audio
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
async def transcribe(request: Request):
    body = await request.json()
    url = body.get("url")

    if len(url) == 0:
        return Response(content=f"No se encontró la url del audio", status_code=409)

    queue = create_queue()

    try:
        asyncio.create_task(transcribe_audio(queue[0], url))
        return { "id": queue[0], "status": queue[2] }
    except:
        error_queue(queue[0])
