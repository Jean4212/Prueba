from fastapi import APIRouter, UploadFile, File, Form, Request
from os import path, getcwd
from schemas.schema import Person
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

route_file = APIRouter()

templates = Jinja2Templates(directory="templates")

@route_file.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...)):

    file_location = path.join(getcwd() + "/static/uploads/" + file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
   
    return {"success": True}

@route_file.post("/uploadfiles")
async def create_upload_files(files: list[UploadFile] = File(...)):

    for file in files:
        file_location = path.join(getcwd() + "/static/uploads/" + file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

    return {"success": True}



@route_file.post("/upp")
async def create_upload_file(username: str = Form(...), file: UploadFile = File(...)):

    #print(person)
    print(username)
    print(file.filename)

    #file_location = path.join(getcwd() + "/static/uploads/" + file.filename)
    #with open(file_location, "wb+") as file_object:
    #    file_object.write(file.file.read())
   
    return {"success": True}

@route_file.get("/up", response_class=HTMLResponse)
async def create_upload_file(request: Request):

    #print(person)
    

    #file_location = path.join(getcwd() + "/static/uploads/" + file.filename)
    #with open(file_location, "wb+") as file_object:
    #    file_object.write(file.file.read())
   
    return templates.TemplateResponse("/up.html", {"request": request, "message": "hola"})