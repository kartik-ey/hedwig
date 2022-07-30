from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import CreateAvis, ShowAvis
from database.session import get_db
from database.repository.avis import create_new_avis, get_avis_by_id, list_avis, edit_avis_by_id, delete_avis_by_id
from database.models import User
from api.routes.route_login import get_current_user


router = APIRouter(tags=["avis"])


@router.post('/create_avis', response_model=ShowAvis)
def create_avis(avis: CreateAvis, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    avis = create_new_avis(avis=avis, db=db, user_id=current_user.user_id)
    return avis


@router.get('/get_avis/{avis_id}', response_model=ShowAvis)
def show_avis(avis_id: int, db: Session = Depends(get_db)):
    avis = get_avis_by_id(avis_id=avis_id, db=db)
    if not avis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Avis with id:{avis_id} not found.")
    return avis


@router.get('/all_avis', response_model=List[ShowAvis])
def show_all_avis(db: Session = Depends(get_db)):
    avis = list_avis(db=db)
    return avis


@router.put('/edit_avis/{avis_id}')
def edit_avis(avis_id: int, avis: CreateAvis, db: Session = Depends(get_db)):
    current_user = 1
    update_avis = edit_avis_by_id(avis_id=avis_id, avis=avis, db=db, user_id=current_user)
    if not update_avis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Avis with id:{avis_id} not found.")
    return {"msg": "Successfully updated Avis."}


@router.delete('/delete_avis/{avis_id}')
def delete_avis(avis_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    avis = get_avis_by_id(avis_id=avis_id, db=db)
    if not avis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Avis with id:{avis_id} not found.")
    if avis.user_id == current_user.user_id or current_user.is_superUser:
        delete_avis_by_id(avis_id=avis_id, db=db, user_id=current_user)
        return {"msg": f"Successfully deleted Avis by user:{current_user.username}."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Permission Denied!!")

