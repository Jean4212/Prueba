from fastapi import	APIRouter
from pydantic import BaseModel
from models.model import Users, session

class User(BaseModel):
    username: str
    password: str

ruta = APIRouter()

@ruta.post("/login")
def login_user(user: User):

    exist_user = session.query(Users).filter(Users.username == user.username).all()
        
    if exist_user:

        if exist_user[0].password == user.password:                    
            return {"message": "ok"}
            
        return {"message": "invalid password"}
        
    return {"message": "invalid username"}
    
    #print(user.username)
    #print(user.password)