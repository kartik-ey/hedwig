from sqlalchemy.orm import Session
from schemas.schemas import CreateAvis
from database.models import Avis


def create_new_avis(avis: CreateAvis, db: Session, user_id: int):
    avis = Avis(**avis.dict(), user_id=user_id)
    db.add(avis)
    db.commit()
    db.refresh(avis)
    return avis
