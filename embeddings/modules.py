from embeddings.src import create_embeddings
from whisper.services import get_queue, update_transcription
from embeddings.meilisearch import create_index
import uuid
import json

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

async def add_documents_meilisearch(id):
    """
    Function to add embeddings to the database.
    """
    transcription = get_queue(id)

    if (not transcription):
        return {"message": "No se encontro la transcripcion"}
    
    list = []

    for segment in transcription[1]['segments']:
        transcription_data = {
            "id": str(uuid.uuid4()),
            "id_transcription": transcription[0],
            "title": f"Transcription {transcription[0]}",
            "start": segment['start'],
            "end": segment['end'],
            "text": segment['text'],
        }
        list.append(transcription_data)
    with open('datos.json', 'w', encoding='utf-8') as archivo:
        json.dump(list, archivo, ensure_ascii=False, indent=2)
    await create_index('datos.json', 'transcriptions')
    
    