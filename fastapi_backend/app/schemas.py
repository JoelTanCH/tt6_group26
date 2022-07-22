from typing import Union
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase): # UserIn
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True