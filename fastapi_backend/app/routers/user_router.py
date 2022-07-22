from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..cruds import user_crud
from ..exceptions import registration_exception, credentials_exception



router = APIRouter(prefix="/users")

@router.post("/register/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(user)
    db_user = user_crud.get_user_by_username(db=db, username=user.username)
    if db_user:
        raise registration_exception
    return user_crud.create_user(db=db, user=user)

# def get_current_user(token_data: schemas.TokenData = Depends(check_token), db: Session = Depends(get_db)):
#     user = user_crud.get_user_by_username(
#         db=db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

@router.get("/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_id(db=db, user_id=user_id)
    return user
