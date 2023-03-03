from fastapi import APIRouter, UploadFile, File
from os import path, getcwd

route_file = APIRouter()

@route_file.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):

    #file_location = path.join(getcwd() + "/static/" + file.filename)
    #with open(file_location, "wb+") as file_object:
    #    file_object.write(file.file.read())
   
    return {"filename": file.filename}   

@route_file.post("/uploadfiles")
async def create_upload_file(files: list[UploadFile] = File(...)):       # files: list[UploadFile] = File(...)):

    #file_location = path.join(getcwd() + "/static/" + file.filename)
    #with open(file_location, "wb+") as file_object:
    #    file_object.write(file.file.read())
       

    return {"filenames": [file.filename for file in files]}