from pydantic import BaseModel

class PlotCreate(BaseModel):
    size_in_acres: float
    number_of_drones: int
    user_id: int
    drone_id: int

class PlotOut(BaseModel):
    id: int
    size_in_acres: float
    number_of_drones: int
    user_id: int
    drone_id: int

    class Config:
        orm_mode = True