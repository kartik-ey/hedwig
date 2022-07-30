from sqlalchemy.orm import Session
from schemas.schemas import CreateAvis
from database.models import Avis


def create_new_avis(avis: CreateAvis, db: Session, user_id: int):
    avis = Avis(**avis.dict(), user_id=user_id)
    db.add(avis)
    db.commit()
    db.refresh(avis)
    return avis


def get_avis_by_id(avis_id: int, db: Session):
    avis = db.query(Avis).filter(Avis.avis_id == avis_id).first()
    return avis


def list_avis(db: Session):
    avis = db.query(Avis).all()
    return avis


def edit_avis_by_id(avis_id: int, avis: CreateAvis, db: Session, user_id):
    existing_avis = db.query(Avis).filter(Avis.avis_id == avis_id)
    if not existing_avis.first():
        return 0
    avis.__dict__.update(user_id=user_id)
    existing_avis.update(avis.__dict__)
    db.commit()
    return 1


def delete_avis_by_id(avis_id: int, db: Session, user_id):
    existing_avis = db.query(Avis).filter(Avis.avis_id == avis_id)
    if not existing_avis.first():
        return 0
    existing_avis.delete(synchronize_session=False)
    db.commit()
    return 1
