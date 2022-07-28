from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import CreateUser, ShowUser
from database.session import get_db
from database.repository.users import create_new_user, get_user_by_id, list_users


router = APIRouter(tags=["user"])


@router.post('/create_user', response_model=ShowUser)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user = create_new_user(user=user, db=db)

    if user is not None:
        raise HTTPException()
    return user


@router.get('/get_user/{user_id}', response_model=ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(user_id=user_id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id-{user_id} not found")
    return user


@router.get('/all_users', response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users
