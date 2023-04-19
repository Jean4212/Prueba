from uvicorn import run
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


from routers.users import route_users
from routers.persons import route_persons
from routers.index import route_index
from routers.file import route_file
from routers.record import route_record
from routers.login import login

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.exception_handler(exc_class_or_status_code=404)
async def http_exception_handler(request, exc):
    access_token = request.cookies.get('access_token')   

    if access_token is None:
        return RedirectResponse(url="/login")
     
    return RedirectResponse("/")

@app.exception_handler(exc_class_or_status_code=500)
async def general_exception_handler(request, exc):   
    access_token = request.cookies.get('access_token')   

    if access_token is None:
        return RedirectResponse(url="/login")
     
    return RedirectResponse("/")

app.include_router(login)

if __name__ == "__main__":
    run("app:app", host="0.0.0.0", reload=True)