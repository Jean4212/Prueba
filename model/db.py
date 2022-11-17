
from sqlite3 import connect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


engine = create_engine("sqlite:///./data/db.db")
session = sessionmaker(bind=engine)
new_session = session()
base = declarative_base()

class Users(base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    user = Column(String(10), nullable=False, unique=True)
    password = Column(String(10), nullable=False)

    def __init__(self, user, password):
        self.user = user
        self.password = password

    #def __repr__(self):
    #    return f"({self.user}, {self.password})"

    def __str__(self):
        return self.user



base.metadata.create_all(engine)

def create_user():    
    new_user = Users("Jeancarlos55", "1234")
    new_session.add(new_user)
    new_session.commit()
    print(new_user.id)

def select_user(user):
    query = f""" SELECT * FROM users WHERE user = "{user}" """
    query = new_session.execute(query).fetchall()
    #result = new_session.execute(query).fetchone()
    #user = query[0]
    #password = query[1]
    for item in query:
        print(item)
    #print(query)
    #print({"user": user, "password": password})

#create_user()
select_user("Jeancarlos12")





with engine.connect() as conn:
    pass

def __conexion(query: str):
    try:
        path = "./data/db.db"
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

