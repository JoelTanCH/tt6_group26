from fastapi import HTTPException, status, Response
from typing import Optional
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from .cruds import user_crud
from .exceptions import invalid_refresh_token_exception, user_not_found_exception
from . import schemas, db_models
from sqlalchemy.orm import Session
from config import ACCESS_SECRET_KEY, REFRESH_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # ./token (relative)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# def authenticate_user(db, username: str, password: str):
#     user = user_crud.get_user_by_username(db=db, username=username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user


def get_hashed_password(password):
    return pwd_context.hash(password)


# def create_access_token(data: dict, expire_time: datetime):
#     to_encode = data.copy()
#     to_encode.update({"exp": expire_time})
#     encoded_jwt = jwt.encode(to_encode, ACCESS_SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# def create_refresh_token(data: dict, expire_time: datetime):
#     to_encode = data.copy()
#     to_encode.update({"exp": expire_time})
#     encoded_jwt = jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# def authenticate_refresh_token(refresh_token: str, user_id: int, db: Session):
#     user = db.query(db_models.User).filter(db_models.User.id == user_id).first()
#     if user is None:
#         raise user_not_found_exception
#     if user.refresh_token != refresh_token:  # use '!=' NOT 'is not'
#         raise invalid_refresh_token_exception
#     try:
#         payload = jwt.decode(refresh_token, REFRESH_SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise user_not_found_exception
#         # for future adding more data to "sub"
#         # token_data = schemas.TokenData(username=username)
#         user = user_crud.get_user_by_username(db=db, username=username)
#         if user is None:
#             raise user_not_found_exception
#     except JWTError:
#         raise invalid_refresh_token_exception
#     return user


# def generate_both_tokens(username: str):
#     access_token_expires_in = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token_expire_time = datetime.utcnow() + access_token_expires_in
#     refresh_token_expire_in = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
#     refresh_token_expire_time = datetime.utcnow() + refresh_token_expire_in
#     access_token = create_access_token(
#         data={"sub": username}, expire_time=access_token_expire_time
#     )
#     refresh_token = create_refresh_token(
#         data={"sub": username}, expire_time=refresh_token_expire_time
#     )
#     both_tokens = schemas.BothTokens(
#         access_token=access_token, refresh_token=refresh_token
#     )
#     return both_tokens


# def set_refresh_token(
#     response: Response, refresh_token: str, db: Session, user: schemas.UserInDB
# ):
#     response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)
#     user_crud.update_refresh_token(db=db, user=user, refresh_token=refresh_token)
