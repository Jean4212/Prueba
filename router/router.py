from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from schema.worker import User

router = APIRouter()
templates = Jinja2Templates(directory="./templates")



@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 

@router.post("/")
async def home(user:User):
    print(user)
    if user.user == "jean" and user.password == "1234":       
        return {"message": True}

    return {"message": False}



