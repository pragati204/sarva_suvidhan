from pydantic import BaseModel

class UserLogin(BaseModel):
    phone: str
    password: str

class FormOut(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True
