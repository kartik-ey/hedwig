from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database.repository.avis import list_avis
from database.session import get_db


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    avis = list_avis(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "avis": avis}
    )
