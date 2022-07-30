from webapps.avis import route_avis
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_avis.router, prefix="", tags=["avis-webapp"])
