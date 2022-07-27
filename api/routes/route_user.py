from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.schemas import CreateUser, ShowUser
from database.session import get_db
from database.repository.users import create_new_user


router = APIRouter(tags=["user"])


@router.post('/create_user', response_model=ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)
    return user
