from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str





