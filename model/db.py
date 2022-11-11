from sqlite3 import connect

def __conexion(query: str):
    try:
        path = "../fastAPI/db.db"
        con = connect(path)   
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        con.close()
        return {"message": "registro exitoso"}
    except:      
        return {"message": "ocurrio un error"}
          
def insert(query: str):
    return __conexion(query)

      
def select(query: str):
    try:
        path = "../fastAPI/db.db"
        con = connect(path)   
        cur = con.cursor()       
        data = cur.execute(query).fetchall()       
        con.commit()
        con.close()
        return data
    except:      
        return {"message": "ocurrio un error"}



def update(query: str):
    __conexion(query, False, False)    

def delete(query: str, foreignkey: bool):
    __conexion(query, False, foreignkey)  

