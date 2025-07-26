from pydantic import BaseModel

class DroneBase(BaseModel):
    name: str

class DroneOut(DroneBase):
    id: int
    is_available: bool

    class Config:
        orm_mode = True

