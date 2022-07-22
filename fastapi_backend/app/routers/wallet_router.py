from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..cruds import wallet_crud, user_crud
from ..exceptions import registration_exception, credentials_exception


router = APIRouter(prefix="/wallets")

@router.post("/new/{user_id}")
def create_user(user_id, wallet_name: schemas.WalletName, db: Session = Depends(get_db)):
    print(wallet_name)
    print(user_id)
    db_user = user_crud.get_user_by_id(db=db, user_id=user_id) 
    return wallet_crud.create_new_wallet(db=db, wallet_name=wallet_name, user=db_user)

@router.get("/{user_id}")
def get_wallet(user_id: int, db: Session = Depends(get_db)):
    wallet = wallet_crud.get_wallet_by_user_id(db=db, user_id=user_id)
    return wallet