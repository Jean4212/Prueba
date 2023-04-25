from fastapi import APIRouter, Request, Response, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from config.token import authenticate_user, create_access_token, decode_token

login = APIRouter()
templates = Jinja2Templates(directory="templates")

@login.post("/login")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password
    user = await authenticate_user(username, password) 

    if not user:
        message = "No Autorizado !"
        response = RedirectResponse(url="/login", status_code=303)
        response.set_cookie(key="X-Message", value=message)
        return response       
    
    del user["password"]
   
    access_token = await create_access_token(data={"sub": user})       
    
    response = RedirectResponse(url="/", status_code=303)    
    response.set_cookie(key="access_token", value=access_token, max_age=None, httponly=True)#, secure=True, samesite="strict")
    return response

@login.get("/login")
async def login_user(request: Request): 
    access_token = request.cookies.get('access_token')

    if access_token is None:     
        message = request.cookies.get("X-Message")     
        response = templates.TemplateResponse("login.html", {"request": request, "message": message})
        
        if message:
            response.delete_cookie(key="X-Message")
     
        return response
        
    token_verify = await decode_token(access_token)

    if token_verify:        
        return RedirectResponse(url="/")    
  
@login.get("/logout")
async def logout_user(request: Request, response: Response):
    access_token = request.cookies.get('access_token')   
    #response = RedirectResponse(url="/login")
    
    #if access_token is None:      
    #    return response     

    #token_verify = await decode_token(access_token)

    if access_token: #token_verify:     
        response.delete_cookie(key="access_token")
        #return response

    if access_token is None:
        return RedirectResponse(url="/login")