from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..cruds import user_crud
from ..exceptions import registration_exception


router = APIRouter(prefix="/users")

@router.post("/register/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    print(user)
    db_user = user_crud.get_user_by_username(db=db, username=user.username)
    if db_user:
        raise registration_exception
    return user_crud.create_user(db=db, user=user)