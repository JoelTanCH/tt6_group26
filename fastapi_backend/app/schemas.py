from typing import Union
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    # access_token_expiry: datetime


class TokenData(BaseModel):
    # username: Optional[str] = None
    username: str


class BothTokens(BaseModel):
    access_token: str
    refresh_token: str

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase): # UserIn
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserInDB(User): 
    hashed_password: str
    refresh_token: str

class WalletName(BaseModel):
    wallet_name: str