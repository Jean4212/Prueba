import sqlite3
from sqlite3 import Error
from fastapi import FastAPI
from pydantic import BaseModel
import requests

class Trabajador(BaseModel):
    dni: str
    nombre: str
    apellido: str
    edad: int

def create_connection():   
    conn = None
    try:
        conn = sqlite3.connect("sqlite.db")
        print(sqlite3.version)

        cursor = conn.cursor()
        # Creating table
        table = """ CREATE TABLE IF NOT EXISTS trabajador (
                    dni VARCHAR(8) NOT NULL,
                    nombre CHAR(30) NOT NULL,
                    apellido CHAR(30),
                    edad INT   ); """
        cursor.execute(table)
        conn.commit()

    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

app = FastAPI()

@app.get("/")
def Home():   

    url = 'http://127.0.0.1:8000/personal'
    datos = {   "dni": "48555618",
                "nombre": "string",
                "apellido": "string",
                "edad": 50  }
    requests.post(url, json = datos) 

    return {"message": "hello world"}

@app.post("/personal")
def Get_Person(datos: Trabajador):  
    
    try:
        conn = sqlite3.connect("sqlite.db")    
        cursor = conn.cursor()    
        query = f""" INSERT INTO trabajador ( dni, nombre, apellido, edad ) 
                        VALUES ("{datos.dni}", "{datos.nombre}", "{datos.apellido}", {datos.edad}) """               
        cursor.execute(query)
        conn.commit()    
        conn.close()
        return datos.dict()
   
    except Error as e:
        print(e)
        return {"response": e}
        
@app.get("/trabajador")   
def Get_Trabajador():
    try:
        conn = sqlite3.connect("sqlite.db")    
        cursor = conn.cursor()    
        query = """SELECT * FROM trabajador"""             
        trabajadores = cursor.execute(query).fetchall()   
        conn.close()
        
        data = {}
        for index, trabajador in enumerate(trabajadores):
            midyct = {"dni": trabajador[0],
                    "nombre": trabajador[1],
                    "apellido": trabajador[2],
                    "edad": trabajador[3]}            

            data[f'{index}'] = midyct    

        return data
   
    except Error as e:
        print(e)
        return {"response": e} 

