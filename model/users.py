
from sqlite3 import connect

def Connection(query: str, select: bool):
    path = "./data/users.sqlite3"    
    engine = connect(path)
    session = engine.cursor()

    create_table = """ CREATE TABLE IF NOT EXISTS "users" (
	    "ID"    INTEGER,
	    "user"	VARCHAR(10) NOT NULL UNIQUE,
	    "password"  VARCHAR(10) NOT NULL,
	    PRIMARY KEY ("ID" AUTOINCREMENT)) """
    session.execute(create_table)
    engine.commit()

    if select:
        result = session.execute(query).fetchall()
        session.close()
        engine.close()
        return result

    session.execute(query)
    engine.commit()
    session.close()
    engine.close()
    return None

def Select(user: str):
    query = f""" SELECT * FROM users WHERE user = "{user}" """
    result = Connection(query, True)    
    if not result:
        return result

    return result

def Insert(user: str, password: str) -> dict:
    if Select(user):
        return {"Message": "Not Found"}

    query = f""" INSERT INTO users (user, password) VALUES ("{user}", "{password}") """
    Connection(query, False)
    return {"Message": "Succes"}

def Update(user: str, new_user: str, new_password: str) -> dict:
    if not Select(user):
        return {"Message": "Not Found"}

    query = f""" UPDATE users SET user = "{new_user}", password = "{new_password}" WHERE user = "{user}" """   
    Connection(query, False)   
    return {"Message": "Succes"} 

def Delete(user: str) -> dict:
    if not Select(user):
        return {"Message": "Not Found"}

    query = f""" DELETE FROM users WHERE user = "{user}" """
    Connection(query, False)  
    return {"Message": "Succes"}