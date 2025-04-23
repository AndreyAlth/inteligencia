# main.py
from fastapi import FastAPI

app = FastAPI()

# app.include_router(users.router)
# app.include_router(items.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API principal de inteligencia"}