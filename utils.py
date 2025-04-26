
from pydub import AudioSegment

def ogg_to_wav(audio_url):
    output_path = audio_url.replace('.ogg', '.wav')
    try:
        # Cargar el archivo .ogg
        audio = AudioSegment.from_file(audio_url, format="ogg")

        # Exportar el audio como .wav
        audio.export(output_path, format="wav", codec="pcm_s16le")

        print(f"Archivo convertido exitosamente: {output_path}")
        return output_path
    except Exception as e:
        raise ValueError(f"Error al convertir el archivo: {e}")