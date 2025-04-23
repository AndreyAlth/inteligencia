from whisper.src import transcribe_audio_whisper
from whisper.services import insert_transcription

async def transcribe_audio(queue_id, audio_url):
    transcription = transcribe_audio_whisper(audio_url)
    insert_transcription(queue_id, transcription)
    return transcription