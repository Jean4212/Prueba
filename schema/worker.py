from pydantic import BaseModel
from model.users import Select

class User(BaseModel):
    user: str
    password: str





