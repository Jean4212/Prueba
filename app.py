from fastapi import FastAPI

app = FastAPI()

bd = []

@app.get("/")
def Home():
    return {"message": "hello world"}

@app.get("/dni{dni}")
def Get_Person(dni: str):
    if dni == "48555618":
        return {"message": "Jeancarlos"}
    else:
        return {"message": "Not Found"}

