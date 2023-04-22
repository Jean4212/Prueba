from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from config.token import decode_token
from models.model import Persons, session

templates = Jinja2Templates(directory="templates")
trabajadores = APIRouter()

@trabajadores.route("/trabajadores", methods=["GET", "POST"])
async def Trabajadores(request: Request):
    access_token = request.cookies.get('access_token')   

    if access_token is None:      
        return RedirectResponse(url="/login")
            
    user = await decode_token(access_token)

    if user:
        datos = session.query(Persons).all()
        return templates.TemplateResponse("trabajadores.html", {"request": request, "data": datos, "user": user})