from fastapi import APIRouter
from schemas.schema import User
from models.model import Users, session
from datetime import datetime

route_users = APIRouter()

@route_users.post("/user")
def user(user: User):
    
    result = session.query(Users).filter(Users.username == user.username).all()
   
    if result:           
        return {"message": "Ya existe"}
    
    new_user = Users(username=user.username, password=user.password, name=user.name, category=user.category, create_at=datetime.now())    
    session.add(new_user)
    session.commit()   

    return {"message": "success"}

