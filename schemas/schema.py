from pydantic import BaseModel

class User(BaseModel):
    
    username: str
    password: str

class Person(BaseModel):
    
    dni: str
    paterno: str
    materno: str
    nombre: str
    nacimiento: str