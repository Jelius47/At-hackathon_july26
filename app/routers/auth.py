from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.core.database import SessionLocal
from app.models.models import User

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(name: str, email: str, phone_number: str, password: str, db: Session = Depends(get_db)):
    user_exists = db.query(User).filter(User.email == email).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = pwd_context.hash(password)
    new_user = User(
        name=name,
        email=email,
        phone_number=phone_number,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}
