from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

SQLALCHEMY_DATABASE_URL = 'postgresql://rxsjzystoetdsd:da1f3b252385e34908dc6e8ddc07daaa066c121db65cfa43e46c808221cc02d8' \
                          '@ec2-44-208-88-195.compute-1.amazonaws.com:5432/d9p5r92cv2i4f2 '


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
