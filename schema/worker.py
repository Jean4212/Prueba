from pydantic import BaseModel

class Worker(BaseModel):
    dni: str
    nombre: str