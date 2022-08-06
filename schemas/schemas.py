from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, time, datetime


class CreateUser(BaseModel):
    fullname: str
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    user_id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class AvisBase(BaseModel):
    body: str
    time_created: Optional[time] = datetime.now().timetz()


class CreateAvis(AvisBase):
    body: str


class ShowAvis(AvisBase):
    body: str
    time_created: time

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
