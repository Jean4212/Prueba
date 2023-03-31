from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from typing import Optional

template = Jinja2Templates(directory="templates")
Login = APIRouter()

# Usuarios de prueba para demostración
users = [
    {"username": "user1", "password": "password1", "roles": ["admin"]},
    {"username": "user2", "password": "password2", "roles": ["user"]},
]

# Función para verificar las credenciales del usuario
def verify_user(credentials: HTTPBasicCredentials):
    for user in users:
        if user["username"] == credentials.username and user["password"] == credentials.password:
            return user
    raise HTTPException(status_code=401, detail="Invalid username or password")

# Objeto HTTPBasic para autenticación
security = HTTPBasic()


def get_token(request: Request):
    """
    Obtiene el token de autenticación de la solicitud HTTP.
    """
    authorization_header = request.headers.get("Authorization")
    print(authorization_header)
    if authorization_header is None:
        return None
    auth_scheme, auth_param = authorization_header.split(" ", 1)
    if auth_scheme.lower() != "bearer":
        return None
    return auth_param

@Login.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    # Verificar si el usuario ya tiene un token almacenado
    token = get_token(request)
    print(token)
    if token:
        return RedirectResponse(url="/protected")

    # Si no hay un token almacenado, mostrar la página de inicio de sesión
    return template.TemplateResponse("login.html", {"request": request})

# Ruta de login para obtener un token de acceso
@Login.post("/login")
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    user = verify_user(credentials)
    return {"token": user["username"]}

# Ruta protegida para usuarios autenticados
@Login.get("/protected")
async def protected(user: str = Depends(security)):
    return {"message": "Welcome to the protected area!"}