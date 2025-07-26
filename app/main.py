
# --- Update app/main.py ---
from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers import payment, voicemail, auth, drones, plots
from app.routers import voicemail, auth, drones, plots

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(voicemail.router, prefix="/api", tags=["Voicemail"])
app.include_router(auth.router, prefix="/api", tags=["Auth"])
app.include_router(drones.router, prefix="/api", tags=["Drones"])
app.include_router(plots.router, prefix="/api", tags=["Plots"])
app.include_router(payment.router, prefix="/api", tags=["Payments"])

@app.get("/")
def root():
    return {"message": "Drone Management System Ready"}
