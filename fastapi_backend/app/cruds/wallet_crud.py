from sqlalchemy.orm import Session
from .. import db_models, schemas, auth


def create_new_wallet(db: Session, wallet_name, user):
    wallet = db_models.Wallet(name=wallet_name, user_id=user.id)
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet


def get_wallet_by_user_id(db: Session, user_id: int):
    wallets = db.query(db_models.Wallet).filter(db_models.User.id == user_id).all()
    return wallets


def update_current_proj(db: Session, user: schemas.User, new_id: int):
    db_user = db.query(db_models.User).filter(
        db_models.User.id == user.id).first()
    if new_id == -1:
        db_user.current_proj_id = None
    else:
        db_user.current_proj_id = new_id
    db.commit()
    db.refresh(db_user)
    return db_user