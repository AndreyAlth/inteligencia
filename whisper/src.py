from openai import OpenAI
from dotenv import load_dotenv
from utils import ogg_to_wav

load_dotenv()
client = OpenAI()

def transcribe_audio_whisper(file_path):
    audio_converted = ogg_to_wav(file_path)

    audio_file = open(audio_converted, "rb")

    translation = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format="verbose_json",
        timestamp_granularities=["segment"],
    )
    return translation