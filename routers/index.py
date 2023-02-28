from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

route_index = APIRouter()

@route_index.get("/", response_class=HTMLResponse)
def index(request: Request):

    return templates.TemplateResponse("index.html", {"request": request, "dni": "0000000000"})