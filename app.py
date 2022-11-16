
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import run
from router.router import router

app = FastAPI()
app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    run("app:app", host="0.0.0.0", port=8000, reload=True)