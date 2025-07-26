from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import voicemail

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(voicemail.router, prefix="/api", tags=["Voicemail"])

@app.get("/")
def root():
    return {"message": "Drone Management API"}
