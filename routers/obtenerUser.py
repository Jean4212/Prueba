from fastapi import	APIRouter
from pydantic import BaseModel
from models.model import Users, session
from passlib.context import CryptContext

class UserResponse(BaseModel):
    username: bool = False
    password: bool = False
    token: str = ""
    name: str = ""

class User(BaseModel):
    username: str
    password: str

ruta = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")    

@ruta.post("/login")
async def login_user(user: User):

    exist_user = session.query(Users).filter(Users.username == user.username).all()  
    userResponse = UserResponse()

    if exist_user:
        userData = exist_user[0]
        password_verified = pwd_context.verify(user.password, userData.password)

        if password_verified:  
            userResponse.username = True          
            userResponse.password = True           
            userResponse.name = userData.name
            return userResponse

        userResponse.username = True    
        return userResponse
 
    return userResponse