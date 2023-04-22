from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from config.token import decode_token

templates = Jinja2Templates(directory="templates")
supervision = APIRouter()

@supervision.route("/supervision", methods=["GET", "POST"])
async def Supervision(request: Request):
    access_token = request.cookies.get('access_token')   

    if access_token is None:      
        return RedirectResponse(url="/login")
            
    user = await decode_token(access_token)

    if user:
        if user["category"] < 1:
            return RedirectResponse(url="/")
        #datos = session.query(Persons).all()
        return templates.TemplateResponse("supervision.html", {"request": request, "user": user})#, "data": datos})