from whisper.src import transcribe_audio_whisper
from whisper.services import insert_transcription
from embeddings.modules import add_embeddings_meilisearch
import asyncio

def conevrt_data(segments):
    list = []
    for segment in segments:
        new_segment = {
            "start": segment.start,
            "end": segment.end,
            "text": segment.text
        }
        list.append(new_segment)
    return list


async def transcribe_audio(queue_id, audio_url):
    data = transcribe_audio_whisper(audio_url)
    transcription = {
        "duration": data.duration,
        "language": data.language,
        "text": data.text,
        "segments": conevrt_data(data.segments) 
    }
    insert_transcription(queue_id, transcription)
    asyncio.create_task(add_embeddings_meilisearch(queue_id))
    # return transcription