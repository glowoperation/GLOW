from fastapi import FastAPI
from app.api.controllers.video_controller import router as video_router

app = FastAPI(title="GLOW API")

app.include_router(video_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "GLOW backend is running"}