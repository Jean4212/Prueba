from uvicorn import run
from fastapi import FastAPI, HTTPException, Request
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


#app.include_router(route_index)
#app.include_router(route_users)
#app.include_router(route_persons)
#app.include_router(route_file)
#app.include_router(route_record)


@app.exception_handler(exc_class_or_status_code=404)
async def http_exception_handler(request, exc):
    print("hola")
    return RedirectResponse("/login")


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    print("mama")

    return RedirectResponse("/login")

app.include_router(login)


if __name__ == "__main__":
    run("app:app", reload=True)