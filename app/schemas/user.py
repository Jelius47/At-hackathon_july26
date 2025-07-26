from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    phone_number: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    phone_number: str
    email: EmailStr

    class Config:
        orm_mode = True
