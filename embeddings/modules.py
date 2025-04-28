from embeddings.src import create_embeddings
from whisper.services import get_queue, update_transcription
from embeddings.meilisearch import create_index
import uuid

async def add_embeddings(id):
    """
    Function to add embeddings to the database.
    """
    transcription = get_queue(id)

    if (not transcription):
        return {"message": "No se encontro la transcripcion"}

    list = []
    for segment in transcription.data.segments:
        embeddings = await create_embeddings(segment.text)
        new_segment = {
            "start": segment.start,
            "end": segment.end,
            "text": segment.text,
            "embedding": embeddings.data[0].embedding
        }
        list.append(new_segment)

    transcription.data.segments = list
    update_transcription(transcription.id, transcription)
    return list

async def add_embeddings_meilisearch(id):
    """
    Function to add embeddings to the database.
    """
    transcription = get_queue(id)

    if (not transcription):
        return {"message": "No se encontro la transcripcion"}

    list = []
    for segment in transcription.data.segments:
        transcription = {
            "id": uuid.uuid4(),
            "transcription_id": transcription.id,
            "title": "Transcription {transcription.id}",
            "start": segment.start,
            "end": segment.end,
            "text": segment.text,
        }
        await create_index(transcription, 'transcriptions')
    
    