from uvicorn import run
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from routers.login import login
from routers.index import index
from routers.trabajadores import trabajadores
from routers.supervision import supervision
from routers.sstma import sstma
from routers.rrhh import rrhh

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
app.include_router(index)
app.include_router(trabajadores)
app.include_router(supervision)
app.include_router(sstma)
app.include_router(rrhh)

if __name__ == "__main__":
    run("app:app", host="0.0.0.0", reload=True)