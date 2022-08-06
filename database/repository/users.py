from sqlalchemy.orm import Session
from schemas.schemas import CreateUser
from database.models import User
from hashing import Hasher


def create_new_user(user: CreateUser, db: Session):
    new_user = User(
        fullname=user.fullname,
        username=create_username(user.username),
        email=user.email,
        password=Hasher.hash_password(user.password),
        is_active=True,
        is_superUser=False)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_id(user_id: int, db: Session):
    user = db.query(User).filter(User.user_id == user_id).first()
    return user


def list_users(db: Session):
    users = db.query(User).filter(User.is_active == "True").all()
    return users


def edit_user_by_id(user_id: int, user: CreateUser, db: Session):
    existing_user = db.query(User).filter(User.user_id == user_id)
    if not existing_user.first():
        return 0
    user.__dict__.update(user_id=user_id)
    existing_user.update(user.__dict__)
    db.commit()
    return 1


def delete_user_by_id(user_id: int, db: Session):
    existing_user = db.query(User).filter(User.user_id == user_id)
    if not existing_user.first():
        return 0
    existing_user.delete(synchronize_session=False)
    db.commit()
    return 1


def exist_user(email: str, db: Session):
    existing_user = db.query(User).filter(User.email == email)
    if not existing_user.first():
        return 0
    return 1


def create_username(username):
    return '@'+username
