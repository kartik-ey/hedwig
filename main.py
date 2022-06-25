from fastapi import FastAPI
from models import Base
from database.database import engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get('/')
def hello():
    return 'hello'
