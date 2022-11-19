from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from schema.worker import User


router = APIRouter()
templates = Jinja2Templates(directory="./templates")



@router.get("/", response_class=HTMLResponse, status_code=200)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "hellow"})  
   




@router.post("/user")
def user(user: User):
    if user.user == "Jean" and user.password == "1234":
        return {"message": "Exito"}

    return {"message": "Fail"}

