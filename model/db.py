
from sqlite3 import connect


class Database:

    def __init__(self, path: str) -> None:

        path_db = path       
        
        try:            
            connect(path_db)
            self.active = True
            
        except: 
            self.active = False
            
               
    def select(self, query:str, multiline: bool) -> None:
        if self.active:
            engine = connect()
            session = engine.cursor()                
            result = session.execute(query).fetchall()

            return result

                 
    

# engine = create_engine("sqlite:///./data/db.db")
# session = sessionmaker(bind=engine)
# new_session = session()
# base = declarative_base()
aa = Database("./data/db.sqlite3")




def __conexion(query: str):
    try:
        path = "./data/db.sqlite3"
        engine = connect(path)
        session = engine.cursor()
        session.execute(query)
        engine.commit()
        engine.close()
        return True
    except:      
        return False
          
def insert(query: str):
    return __conexion(query)
      
def select(query: str):
    try:
        path = "./db.db"
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

