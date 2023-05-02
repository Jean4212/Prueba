from fastapi import	APIRouter
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

ruta = APIRouter()

@ruta.post("/login")
def login_user(user: User):
    print(user.username)
    print(user.password)