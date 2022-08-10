from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from schemas.schemas import EditAvis, ShowAvis, AvisBase
from database.session import get_db
from database.repository.avis import create_new_avis, get_avis_by_id, list_avis, edit_avis_by_id, delete_avis_by_id, \
    get_avis_by_user_id
from database.models import User
from api.routes.route_login import get_current_user

router = APIRouter(tags=["avis"])


@router.post('/create_avis', response_model=AvisBase)
def create_avis(avis: AvisBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    avis = create_new_avis(avis=avis, db=db, user_id=current_user.user_id)
    return avis


@router.get('/get_avis/{avis_id}', response_model=EditAvis)
def show_avis(avis_id: int, db: Session = Depends(get_db)):
    avis = get_avis_by_id(avis_id=avis_id, db=db)
    if not avis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Avis with id:{avis_id} not found.")
    return avis


@router.get('/all_avis', response_model=List[ShowAvis])
def show_all_avis(db: Session = Depends(get_db)):
    result = list_avis(db=db)
    new_result = []
    for users, avis in result:
        new_result.append({"username": users.username, "fullname": users.fullname, "user_id": avis.user_id,
                           "body": avis.body, "time_created": avis.time_created, "avis_id": avis.avis_id})
#   print(new_result)
    return new_result


@router.put('/edit_avis/{avis_id}')
def edit_avis(avis_id: int, avis: AvisBase, db: Session = Depends(get_db),
              current_user: User = Depends(get_current_user)):
    update_avis = edit_avis_by_id(avis_id=avis_id, avis=avis, db=db, user_id=current_user.user_id)
    if not update_avis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Avis with id:{avis_id} not found.")
    return {"msg": "Successfully updated Avis."}


@router.delete('/delete_avis/{avis_id}', status_code=status.HTTP_200_OK)
def delete_avis(avis_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    avis = get_avis_by_id(avis_id=avis_id, db=db)
    if not avis:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Avis with id:{avis_id} not found.")
    if avis.user_id == current_user.user_id or current_user.is_superUser:
        delete_avis_by_id(avis_id=avis_id, db=db)
        return {"msg": f"Successfully deleted Avis by user:{current_user.username}."}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f"Permission Denied!!")


@router.get('/avis_by_user', response_model=List[ShowAvis])
def get_avis_by_user(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    result = get_avis_by_user_id(user_id=current_user.user_id, db=db)
    new_result = []
    for users, avis in result:
        new_result.append({"username": users.username, "fullname": users.fullname, "user_id": avis.user_id,
                           "body": avis.body, "time_created": avis.time_created, "avis_id": avis.avis_id})
    #   print(new_result)
    return new_result
