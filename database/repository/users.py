from sqlalchemy.orm import Session
from schemas.schemas import CreateUser
from database.models import User
from hashing import Hasher


def create_new_user(user: CreateUser, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        password=Hasher.hash_password(user.password),
        is_active=True,
        is_superUser=False)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    return user


def list_users(db: Session):
    users = db.query(User).filter(User.is_active == True).all()
    return users
