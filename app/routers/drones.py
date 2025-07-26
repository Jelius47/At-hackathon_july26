# --- app/routers/drones.py ---
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Drone
from app.schemas.drone import DroneOut

router = APIRouter()

@router.get("/drones/available", response_model=list[DroneOut])
def get_available_drones(db: Session = Depends(get_db)):
    return db.query(Drone).filter(Drone.is_available == True).all()
