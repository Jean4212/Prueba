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
    ingreso: str
    planilla: str
    movilidad: str
    asignacion: str
    aportacion: str
    comision: str
    cuenta: str
    cargo: str
    distrito: str
    domicilio: str
    area: str
    cuspp: str
    celular: str
    licencia: str
    categoria: str
    revalidacion: str
