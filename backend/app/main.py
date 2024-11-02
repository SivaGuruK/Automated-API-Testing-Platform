from fastapi import FastAPI
from app.config import celery_app

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Testing Platform is running!"}
