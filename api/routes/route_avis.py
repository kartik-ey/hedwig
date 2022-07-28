from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.schemas import CreateAvis, ShowAvis
from database.session import get_db
from database.repository.avis import create_new_avis


router = APIRouter(tags=["avis"])


@router.post('/create_avis', response_model=ShowAvis)
def create_avis(avis: CreateAvis, db: Session = Depends(get_db)):
    current_user = 1
    avis = create_new_avis(avis=avis, db=db, user_id=current_user)
    return avis
