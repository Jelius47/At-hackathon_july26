from pydantic import BaseModel

class DroneBase(BaseModel):
    name: str

class DroneOut(DroneBase):
    id: int
    is_available: bool

    class Config:
        orm_mode = True

# app/schemas/drone.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DroneRequestCreate(BaseModel):
    phone_number: str
    plot_size: int
    number_of_drones: int
    total_price_per_hour: int

class DroneRequestOut(DroneRequestCreate):
    id: int
    status: str
    created_at: datetime

    class Config:
        orm_mode = True

