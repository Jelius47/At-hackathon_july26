# --- app/routers/plots.py ---
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Plot, User, Drone
from app.schemas.plot import PlotCreate, PlotOut

router = APIRouter()

@router.post("/plots", response_model=PlotOut)
def create_plot(plot: PlotCreate, db: Session = Depends(get_db)):
    # Check existence
    user = db.query(User).get(plot.user_id)
    drone = db.query(Drone).get(plot.drone_id)
    if not user or not drone:
        raise HTTPException(status_code=404, detail="User or Drone not found")

    if not drone.is_available:
        raise HTTPException(status_code=400, detail="Drone not available")

    # Mark drone as unavailable
    drone.is_available = False
    new_plot = Plot(**plot.dict())
    db.add(new_plot)
    db.commit()
    db.refresh(new_plot)
    return new_plot

@router.get("/users/{user_id}/plots", response_model=list[PlotOut])
def get_user_plots(user_id: int, db: Session = Depends(get_db)):
    return db.query(Plot).filter(Plot.user_id == user_id).all()

