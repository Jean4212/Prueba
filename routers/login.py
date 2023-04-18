from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from fastapi.security import OAuth2PasswordRequestForm
from datetime import  timedelta
from config.jwt import authenticate_user, create_access_token, decode_token


login = APIRouter()
templates = Jinja2Templates(directory="templates")



@login.post("/token")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):

    username = form_data.username
    password = form_data.password
    user = authenticate_user(username, password)  

    if not user:
        raise HTTPException(status_code=400, detail="Usuario o contraseña inválidos")
    
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user["username"]}, expires_delta=access_token_expires)
       
    response = RedirectResponse(url="/", status_code=303)    
    response.set_cookie(key="access_token", value=access_token, max_age=None, httponly=True, secure=True, samesite="strict")
      
    return response
  
@login.get("/login", response_class=HTMLResponse)
def login_user(request: Request):
 
    access_token = request.cookies.get('access_token')

    if access_token is None:
        return templates.TemplateResponse("login.html", {"request": request})
        
    token_verify = decode_token(access_token)

    if token_verify:
        return RedirectResponse("/")    

@login.get("/protected", response_class=HTMLResponse)
async def protected_route(request: Request):

    access_token = request.cookies.get('access_token') 

    if access_token is None:
        return RedirectResponse("/login") 

    token_verify = decode_token(access_token)

    if token_verify:      
        return templates.TemplateResponse("planilla.html", {"request": request})
  
@login.get("/", response_class=HTMLResponse)
def login_user(request: Request):
 
    access_token = request.cookies.get('access_token')   

    if access_token is None:
        return RedirectResponse("/login") 
        
    token_verify = decode_token(access_token)

    if token_verify:
        return templates.TemplateResponse("index.html", {"request": request})
    

@login.get("/logout")
def logout_user(request: Request):
    response = RedirectResponse(url="/")
    response.delete_cookie(key="access_token")
    return response