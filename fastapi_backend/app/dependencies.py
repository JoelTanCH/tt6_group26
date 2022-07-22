# from fastapi import Depends
# from .database import get_db
# from . import schemas
# from sqlalchemy.orm import Session
# from jose import JWTError, jwt, ExpiredSignatureError
# from . import auth
# from .cruds import user_crud
# from .exceptions import (
#     credentials_exception,
#     user_not_found_exception,
#     expired_access_token_exception,
#     empty_access_token_exception,
# )


# def check_token(token: str = Depends(auth.oauth2_scheme)):
#     if token == "":
#         raise empty_access_token_exception
#     try:
#         payload = jwt.decode(token, auth.ACCESS_SECRET_KEY, algorithms=[auth.ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise user_not_found_exception
#         token_data = schemas.TokenData(username=username)
#     except ExpiredSignatureError:
#         raise expired_access_token_exception
#     except JWTError:
#         raise credentials_exception
#     return token_data


# def check_token_n_username(
#     token_data: schemas.TokenData = Depends(check_token), db: Session = Depends(get_db)
# ):
#     user = user_crud.get_user_by_username(db=db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
