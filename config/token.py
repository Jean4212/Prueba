from fastapi import HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jwt import encode, decode, ExpiredSignatureError, InvalidTokenError
from models.model import session, Users

# Configuración de seguridad
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"
SECRET_KEY = "e8c45edd00c78200a1913b46eac799a375a97e76"

# Datos del usuario

datos = session.query(Users).all()
users = {}
for user in datos:
    dic = {"id": user.id, "name": user.name, "username": user.username, "password": user.password, "category": user.category, "create_at": user.create_at}
    users[user.username] = dic
    
# Funciones de autenticación
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(username: str):    
    if username in users:  
        user_dict = users[username]
        return user_dict

def authenticate_user(username: str, password: str):    
    user = get_user(username)
    
    if not user:
        return False
    
    if not verify_password(password, user["password"]):
        return False
    
    return user

# Funciones de token
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)    
   
    return encoded_jwt

# Verificar token
def decode_token(token: str = Depends(oauth2_scheme)):    
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            #return RedirectResponse(url="/login")
            raise HTTPException(status_code=401, detail="Invalid token")
        
        
        token_data = {"username": username}

    except ExpiredSignatureError:
        #return RedirectResponse(url="/login")
        raise HTTPException(status_code=401, detail="Token has expired")
    
    except InvalidTokenError:
        #return RedirectResponse(url="/login")
        raise HTTPException(status_code=401, detail="Invalid token")
      
    return token_data
