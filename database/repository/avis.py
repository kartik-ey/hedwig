from sqlalchemy.orm import Session
from schemas.schemas import AvisBase
from database.models import Avis, User
from datetime import datetime


def create_new_avis(avis: AvisBase, db: Session, user_id: int):
    avis = Avis(**avis.dict(), user_id=user_id)
    avis.__dict__.update(time_created=datetime.utcnow())
    avis.__dict__.update(created_on=datetime.utcnow().date())
    db.add(avis)
    db.commit()
    db.refresh(avis)
    return avis


def get_avis_by_id(avis_id: int, db: Session):
    avis = db.query(Avis).filter(Avis.avis_id == avis_id).first()
    return avis


def list_avis(db: Session):
    avis = db.query(User, Avis).join(Avis).order_by(Avis.time_created.desc()).all()
    return avis


def edit_avis_by_id(avis_id: int, avis: AvisBase, db: Session, user_id):
    existing_avis = db.query(Avis).filter(Avis.avis_id == avis_id)
    if not existing_avis.first():
        return False
    avis.__dict__.update(user_id=user_id)
    existing_avis.update(avis.__dict__)
    db.commit()
    return True


def delete_avis_by_id(avis_id: int, db: Session):
    existing_avis = db.query(Avis).filter(Avis.avis_id == avis_id)
    if not existing_avis.first():
        return False
    existing_avis.delete(synchronize_session=False)
    db.commit()
    return True


def get_avis_by_user_id(db: Session, user_id: int):
    avis = db.query(User, Avis).join(Avis).filter(Avis.user_id == user_id).order_by(Avis.time_created.desc()).all()
    return avis
