from fastapi import APIRouter, UploadFile, File
from os import path, getcwd

from models.model import Persons, session
from sqlalchemy import select

route_file = APIRouter()

@route_file.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):

    file_location = path.join(getcwd() + "/static/uploads/" + file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
   
    return {"success": True}

@route_file.post("/uploadfiles")
async def create_upload_files(files: list[UploadFile] = File(...)):

    for file in files:

        print(file.filename)

        nombrefile = file.filename.split(".")[0].split("-")[1]
        dni = file.filename.split(".")[0].split("-")[0]
        
        query = select(Persons).where(Persons.dni == dni)
        datos = session.scalars(query).one()        

        if nombrefile == "foto":
            datos.foto = file.filename
        elif nombrefile == "dni":
            datos.fotodni = file.filename
        elif nombrefile == "licencia":
            datos.fotolicencia = file.filename
        elif nombrefile == "policial":
            datos.fotopolicial = file.filename

        session.commit()

        file_location = path.join(getcwd() + "/static/uploads/" + file.filename)

        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

    return {"success": True}
