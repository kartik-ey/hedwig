from sqlalchemy.orm import Session
from schemas.schemas import CreateUser
from database.models import User
from hashing import Hasher


def create_new_user(user: CreateUser, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        password=Hasher.hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user




