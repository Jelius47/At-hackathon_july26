from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Drone, DroneRequest
from app.schemas.drone import DroneOut, DroneRequestCreate, DroneRequestOut

router = APIRouter(prefix="/drones", tags=["Drones"])


@router.get("/available", response_model=list[DroneOut])
def get_available_drones(db: Session = Depends(get_db)):
    return db.query(Drone).filter(Drone.is_available == True).all()


@router.post("/request", response_model=DroneRequestOut)
def request_drone(data: DroneRequestCreate, db: Session = Depends(get_db)):
    # Optional logic: validate number of drones available
    available_count = db.query(Drone).filter(Drone.is_available == True).count()
    if available_count < data.number_of_drones:
        raise HTTPException(status_code=400, detail="Not enough drones available")

    drone_request = DroneRequest(**data.dict(), status="pending")
    db.add(drone_request)
    db.commit()
    db.refresh(drone_request)
    return drone_request


@router.get("/requests", response_model=list[DroneRequestOut])
def get_all_drone_requests(db: Session = Depends(get_db)):
    return db.query(DroneRequest).order_by(DroneRequest.created_at.desc()).all()
