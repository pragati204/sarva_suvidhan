from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas import UserLogin
from app.models import User
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/user/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    if not user.phone or not user.password:
        raise HTTPException(status_code=400, detail="Phone and password are required")

    db_user = db.query(User).filter(User.phone == user.phone, User.password == user.password).first()
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "user_id": db_user.id}
