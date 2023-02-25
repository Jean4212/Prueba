
from fastapi import FastAPI
from uvicorn import run

from routers.users import route_users
from routers.persons import route_persons

app = FastAPI()

app.include_router(route_users)
app.include_router(route_persons)

if __name__ == "__main__":
    run("app:app", reload=True)