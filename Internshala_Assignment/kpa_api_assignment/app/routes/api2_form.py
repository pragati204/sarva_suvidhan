from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Form
from app.schemas import FormOut
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/form/all", response_model=list[FormOut])
def get_all_forms(db: Session = Depends(get_db)):
    return db.query(Form).all()
