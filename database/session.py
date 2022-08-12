from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SQLALCHAMY_DB_URL = 'sqlite:///database/data.db'
# engine = create_engine(SQLALCHAMY_DB_URL, connect_args={'check_same_thread': False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
