from fastapi import	APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from models.model import Users, session
from datetime import datetime, timedelta
from jwt import encode, decode
from pymongo import MongoClient

class User(BaseModel):
    username: str
    password: str

class ValidationResponse(BaseModel):
    valid: bool = False
    token: str = ""
    name: str = ""   

ruta = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
ALGORITHM = "HS256"
SECRET_KEY = "e8c45edd00c78200a1913b46eac799a375a97e76"

async def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)    
   
    return encoded_jwt

async def decode_token(token: str = Depends(oauth2_scheme)):    
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user = payload.get("sub")    
    except:
        return    
      
    return user

@ruta.post("/login")
async def login_user(user: User):

    exist_user = session.query(Users).filter(Users.username == user.username).all()  
    response = ValidationResponse()

    if exist_user:
        selectUser = exist_user[0]
        if selectUser.password == user.password:
            token = await create_access_token({"username": user.username})
            response.valid = True
            response.token = token
            response.name = selectUser.name
 
    return response


@ruta.get("/personal")
async def get_persons():

    my_lista = []
    for num in range(80):
        my_dict = {"dni": "48555618", "paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Marcelo", "ingreso": "01/01/2020", "cargo": "Operador de grua liviana"}
        
        if num == 79:
            my_dict = {"dni": "48555618", "paterno": "Garcia", "materno": "Guivin", "nombre": "Claret", "ingreso": "01/01/2020", "cargo": "Operador de Grua Semi Pesada"}

        my_lista.append(my_dict)

    return my_lista

@ruta.get("/horario")
async def get_calendar():
    my_lista = []

    for num in range(10):
        my_dict = { "unidad": "SUR1",
                    "trabajadores": ["Oropeza Jeancarlos", "Valdarrago Enrique", "Bolaños Oswaldo"],
                    "turnos": {
                        "dia": [3, 3, 3, 3, 9, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1],
                        "noche": [2, 2, 2, 2, 3, 3, 3, 3, 1, 9, 0, 1, 2, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]},
                    "apoyos": [
                        {"dia": 5, "nombre": "Guerrero Marcos", "turno": "dia"},
                        {"dia": 10, "nombre": "Yurivilca Yone", "turno": "noche"}]
                }
        
        my_lista.append(my_dict)

    return my_lista




@ruta.get("/mongo")
async def fdsfdsfdsfds():    
    client = MongoClient("mongodb+srv://jean:1234@cluster0.1vtzmcu.mongodb.net/?retryWrites=true&w=majority")
    db = client.prueba
    colecction = db.posts

    new_post = {
    "author": "Karina",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"]}
    
    colecction.insert_one(new_post).inserted_id

       
    return "created"

@ruta.get("/mongo/gg")
async def fdsfdsfdsfds():    
    client = MongoClient("mongodb+srv://jean:1234@cluster0.1vtzmcu.mongodb.net/?retryWrites=true&w=majority")
    db = client.prueba
    collection = db.posts
    result = collection.find().sort("author", 1)
    
    lista = []
    
    for item in result:       
        del item["_id"]
        lista.append(item)      
       
    
    return lista
