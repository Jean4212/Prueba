from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates




router = APIRouter()
templates = Jinja2Templates(directory="./templates")



@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 

@router.post("/", response_class=HTMLResponse)
async def home(request: Request):
    return "hola" #templates.TemplateResponse("index.html", {"request": request})  




   
@router.post("/login", response_class=HTMLResponse)
async def uuuuu(request: Request, username: str = Form(...), password: str = Form(...)):
    
    if username == "jean" and password == "1234":
        print("hola")
        return templates.TemplateResponse("user.html", {"request": request})  
    
    return RedirectResponse("/")  