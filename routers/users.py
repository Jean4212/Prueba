from fastapi import APIRouter
from schemas.schema import User
from models.model import Users, session
from datetime import datetime
from sqlalchemy import Select

route_users = APIRouter()

@route_users.get("/users")
def users():   

    query = Select(Users)
    result = session.scalars(query).all()
    
    return {"users": result}

@route_users.post("/users")
def users(user: User):

    query = Select(Users).where(Users.username == user.username) 
    result = session.scalars(query).all()
   
    if result:           
        return {"message": "Ya existe"}
    
    new_user = Users(username=user.username, password=user.password, create_at=datetime.now())    

    session.add(new_user)
    session.commit()   

    return {"message": "Se registro"}