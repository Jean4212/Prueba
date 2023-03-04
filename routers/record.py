from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

route_record = APIRouter()

@route_record.get("/registracion", response_class=HTMLResponse)
def save_person(request: Request):

    return templates.TemplateResponse("savePerson.html", {"request": request})