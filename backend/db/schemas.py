from typing import Optional, Union, List, Dict
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    

class ResponseModel(BaseModel):
    class Config:
        orm_mode = True

    error: bool = False
    number: int = 1
    message: Union[List, Dict, str]
    
    
    