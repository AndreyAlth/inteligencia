# main.py
from fastapi import FastAPI
from whisper.app import router as whisper_router

app = FastAPI()

app.include_router(whisper_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API principal de inteligencia"}