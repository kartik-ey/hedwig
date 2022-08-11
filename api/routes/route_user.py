from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import CreateUser, ShowUser, UserBase
from database.session import get_db
from database.repository.users import create_new_user, get_user_by_id, list_users, edit_user_by_id, delete_user_by_id,\
    exist_user, get_username
from database.models import User
from api.routes.route_login import get_current_user


router = APIRouter(tags=["user"])


@router.post('/create_user', response_model=ShowUser, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    user_exist = exist_user(user.email, db=db)
    if user_exist:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"User with email:{user.email} already exists.")

    user = create_new_user(user=user, db=db)
    return user


@router.get('/get_user', response_model=ShowUser)
def get_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = get_user_by_id(user_id=current_user.user_id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{current_user.user_id} not found")
    return user


@router.get('/all_users', response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    users = list_users(db=db)
    return users


@router.put('/edit_user', status_code=status.HTTP_200_OK)
def edit_user(user: UserBase, db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)):
    update_user = edit_user_by_id(user_id=current_user.user_id, user=user, db=db)
    if not update_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{current_user.user_id} not found.")
    return {"msg": "User updated successfully."}


@router.delete('/delete_user', status_code=status.HTTP_200_OK)
def delete_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    deleted_user = delete_user_by_id(user_id=current_user.user_id, db=db)
    if not deleted_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id:{current_user.user_id} not found.")
    return {"msg": "User deleted successfully."}


@router.get('/username')
def getusernameby_id(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    username = get_username(user_id = current_user.user_id, db=db)
    return username
