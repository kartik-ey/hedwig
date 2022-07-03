from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    username: str
    email: EmailStr

    class Config:
        orm_mode = True


class CreateAvis(BaseModel):
    body: str
    user: ShowUser

