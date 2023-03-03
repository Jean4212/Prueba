from fastapi import APIRouter, UploadFile, File
from os import path, getcwd

route_file = APIRouter()

@route_file.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):

    file_location = path.join(getcwd() + "/static/" + file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
   
    return {"success": True}

@route_file.post("/uploadfiles")
async def create_upload_file(files: list[UploadFile] = File(...)):

    for file in files:
        file_location = path.join(getcwd() + "/static/" + file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

    return {"success": True}