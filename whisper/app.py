from fastapi import APIRouter
from fastapi import Request, Response
from whisper.services import create_queue, error_queue, get_queue
from whisper.modules import transcribe_audio
import asyncio

router = APIRouter(
    prefix="/transcriptions",
    tags=["transcriptions"],
    responses={404: {"description": "No encontrado"}},
)

@router.get("/{id}")
async def read_users(id: str):
    if (not id):
        return {"message": "No se encontro la transcripcion"}
    
    trascription = get_queue(id)
    if (not trascription):
        return {"message": "No se encontro la transcripcion"}
    return {
        "id": trascription[0],
        "status": trascription[1],
        "transcription": trascription[2],
        "created":  trascription[3]
    }

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
