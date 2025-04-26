from embeddings.src import create_embeddings
from whisper.services import get_queue, update_transcription

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
    
    