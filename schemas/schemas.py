from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):
    fullname: str
    username: str
    email: EmailStr
    password: str


class ShowUser(BaseModel):
    user_id: int
    fullname: str
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True


class AvisBase(BaseModel):
    body: str

    class Config:
        orm_mode = True


class CreateAvis(AvisBase):
    body: str


class ShowAvis(CreateAvis):
    avis_id: int
    user_id: int
    fullname: str
    username: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
