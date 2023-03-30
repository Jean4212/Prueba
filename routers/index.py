from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models.model import Persons, session
from sqlalchemy import Select

templates = Jinja2Templates(directory="templates")

route_index = APIRouter()

@route_index.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@route_index.get("/trabajadores", response_class=HTMLResponse)
def trabajadores(request: Request):
    query = Select(Persons)
    data = session.scalars(query).all()  

    return templates.TemplateResponse("trabajadores.html", {"request": request, "data": data})

@route_index.get("/asistencia", response_class=HTMLResponse)
def asistencia(request: Request):
    data = []
    for num in range(100):
        line = {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
            "dni": num, "cargo": "Asistente", "distrito": "Chorrillos",
            "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
            "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}
        data.append(line)
    return templates.TemplateResponse("asistencia.html", {"request": request, "data": data})

@route_index.get("/desarrollo", response_class=HTMLResponse)
def desarrollo(request: Request):
    return templates.TemplateResponse("desarrollo.html", {"request": request})

@route_index.get("/planilla", response_class=HTMLResponse)
def planilla(request: Request):
    return templates.TemplateResponse("planilla.html", {"request": request})