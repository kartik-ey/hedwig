from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from models import Base
from database.database import engine


def get_application() -> FastAPI:
    application = FastAPI(title='hedwig')

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))
    # application.include_router(api.router, prefix="/api")

    return application


Base.metadata.create_all(bind=engine)

app = get_application()


@app.get('/')
def hello():
    return 'hello'
