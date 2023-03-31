
from uvicorn import run
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.users import route_users
from routers.persons import route_persons
from routers.index import route_index
from routers.file import route_file
from routers.record import route_record
from routers.login import Login

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(route_index)
app.include_router(route_users)
app.include_router(route_persons)
app.include_router(route_file)
app.include_router(route_record)
app.include_router(Login)

if __name__ == "__main__":
    run("app:app", reload=True)