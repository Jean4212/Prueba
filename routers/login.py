from fastapi import APIRouter, HTTPException, Response, Request, Form, Cookie
from fastapi.security import HTTPBearer
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import jwt

from models.model import Users, session
from sqlalchemy import Select
from datetime import datetime, timedelta

secret_key = "mi_clave_secreta"

templates = Jinja2Templates(directory="templates")
Login = APIRouter()

@Login.get("/login", response_class=HTMLResponse)
def login_user(request: Request, token: str = Cookie(None)): 
    try:
        if token:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            username = payload.get("username")
            name = payload.get("name")
        
            if username and name:
                return templates.TemplateResponse("index.html", {"request": request, "username": username})
        else:
            raise ValueError("No se proporcionó ningún token")
            
    except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.ExpiredSignatureError, jwt.exceptions.DecodeError) as e:
        print(f"Error al decodificar el token: {e}")
    
    return templates.TemplateResponse("login.html", {"request": request})

@Login.post("/login", response_class=HTMLResponse)
def verify_user(request: Request, response: Response, username: str = Form(...), password: str = Form(...), token: str = Cookie(None)):

    if token:
        try:
            payload = jwt.decode(token, secret_key, algorithms=["HS256"])
            username = payload.get("username")
            name = payload.get("name")
        
            if username and name:
                return RedirectResponse(url="/")
        except (jwt.exceptions.InvalidSignatureError, jwt.exceptions.ExpiredSignatureError):
            pass
    
    query = Select(Users).filter(Users.username == username)

    try:
        user = session.scalars(query).one()

        if user.password != password:
            return templates.TemplateResponse("login.html", {"request": request})
    except:
        return templates.TemplateResponse("login.html", {"request": request})
        
    payload = {"username": user.username, "name": user.name, 'exp': datetime.utcnow() + timedelta(days=1)}
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    response = RedirectResponse(url='/')
    response.set_cookie(key="token", value=token)
    
    return response
