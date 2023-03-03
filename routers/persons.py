from fastapi import APIRouter, Request, Body
from schemas.schema import Person
from models.model import Persons, session
from datetime import datetime
from sqlalchemy import Select

route_persons = APIRouter()

@route_persons.get("/persons")
def persons(dni: str):   

    query = Select(Persons).where(Persons.dni == dni)
    result = session.scalars(query).all()

    if result:
    
        return result[0]
    
    return {"message": "no existe"}

@route_persons.post("/persons")
async def persons(person: Person):

    query = Select(Persons).where(Persons.dni == person.dni) 
    result = session.scalars(query).all()

    if result:           
        return {"message": "Ya existe"}
    
    new_person = Persons(dni=person.dni, paterno=person.paterno, materno=person.materno, nombre=person.nombre, 
                         nacimiento=person.nacimiento, ingreso=person.ingreso, planilla=person.planilla, movilidad=person.movilidad, asignacion=person.asignacion, aportacion=person.aportacion, comision=person.comision, cuenta=person.cuenta, cargo=person.cargo, distrito=person.distrito, domicilio=person.domicilio, area=person.area, cuspp=person.cuspp, celular=person.celular, licencia=person.licencia, categoria=person.categoria, revalidacion=person.revalidacion, create_at=datetime.now())    

    session.add(new_person)
    session.commit()   

    return {"message": "Se registro"}

@route_persons.put("/persons")
def persons(person: Person, dni: str):

    query = Select(Persons).where(Persons.dni == dni) 
    result = session.scalars(query).all()

    if result:
        new_query = Select(Persons).where(Persons.dni == person.dni) 
        new_result = session.scalars(new_query).all()

        if new_result:
            return {"message": "dni ya existe"} 
      
        select_person = result[0]
        select_person.dni = person.dni        
        select_person.paterno = person.paterno
        select_person.materno = person.materno
        select_person.nombre = person.nombre
        select_person.nacimiento = person.nacimiento
        session.commit()

        return {"message": "Se actualizo"}       

    return {"message": "No existe"}
 
@route_persons.delete("/persons")
def persons(dni: str):

    query = Select(Persons).where(Persons.dni == dni) 
    result = session.scalars(query).all()

    if result:
        select_person = result[0]
        session.delete(select_person)
        session.commit()

        return {"message": "eliminado correctamente"}
    
    return {"message": "person no existe"}