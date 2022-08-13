from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from api.routes import route_user, route_avis, route_login
from database.models import Base
from database.session import engine


def get_application() -> FastAPI:
    application = FastAPI(title='hedwig')

    origins = ["*"]
    application.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


Base.metadata.create_all(bind=engine, checkfirst=True)

app = get_application()

app.include_router(route_login.router)
app.include_router(route_user.router)
app.include_router(route_avis.router)
