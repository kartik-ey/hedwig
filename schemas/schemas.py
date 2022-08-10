from pydantic import BaseModel, EmailStr
from datetime import datetime, date


class UserBase(BaseModel):
    fullname: str
    username: str
    email: EmailStr
    dob: date


class CreateUser(UserBase):
    password: str


class ShowUser(UserBase):
    user_id: int
    created_on: date
    is_active: bool
    is_superUser: bool

    class Config:
        orm_mode = True


class AvisBase(BaseModel):
    body: str

    class Config:
        orm_mode = True


class EditAvis(AvisBase):
    avis_id: int


class ShowAvis(AvisBase):
    avis_id: int
    user_id: int
    fullname: str
    username: str
    created_on: date
    time_created: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
