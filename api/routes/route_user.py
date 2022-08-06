from fastapi import APIRouter, Depends, HTTPException, status, Form
from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import CreateUser, ShowUser
from database.session import get_db
from database.repository.users import create_new_user, get_user_by_id, list_users, edit_user_by_id, delete_user_by_id,\
    exist_user


router = APIRouter(tags=["user"])


@router.post('/create_user', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_exist = exist_user(user.email, db=db)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with email:{user.email} already exists.")

    user = create_new_user(user=user, db=db)
    return user


@router.get('/get_user/{user_id}', response_model=ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(user_id=user_id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{user_id} not found")
    return user


@router.get('/all_users', response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users


@router.put('/edit_user/{user_id}', status_code=status.HTTP_200_OK)
def edit_user(user_id: int, user: CreateUser, db: Session = Depends(get_db)):
    update_user = edit_user_by_id(user_id=user_id, user=user, db=db)
    if not update_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{user_id} not found.")
    return {"msg": "User updated successfully."}


@router.delete('/delete_user/{user_id}')
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user_by_id(user_id=user_id, db=db)
    if not deleted_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{user_id} not found.")
    return {"msg": "User deleted successfully."}
