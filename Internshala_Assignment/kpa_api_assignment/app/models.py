from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True)
    password = Column(String)

class Form(Base):
    __tablename__ = "forms"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
