from fastapi import FastAPI
from app.routes import api1_login, api2_form
from app.models import Base
from app.database import engine

# Auto create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(api1_login.router)
app.include_router(api2_form.router)
