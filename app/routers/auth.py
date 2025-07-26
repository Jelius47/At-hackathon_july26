# --- app/routers/auth.py ---
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.core.database import get_db
from app.models.models import User
from app.schemas.user import UserCreate, UserOut

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup", response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = pwd_context.hash(user.password)
    new_user = User(
        name=user.name,
        phone_number=user.phone_number,
        email=user.email,
        password_hash=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



