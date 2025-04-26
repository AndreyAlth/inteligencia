# main.py
from fastapi import FastAPI
from whisper.app import router as whisper_router
#cors
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

app.include_router(whisper_router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API principal de inteligencia"}