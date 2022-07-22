from sqlalchemy.orm import Session
from .. import db_models, schemas, auth

def get_user_by_username(db: Session, username: str):
    return db.query(db_models.User).filter(db_models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_hashed_password(user.password)
    db_user = db_models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def get_user_by_username(db: Session, username: str):
#     return db.query(db_models.User).filter(db_models.User.username == username).first()
# # def get_user_by_username(db: Session, username: str):
# #     return db.query(db_models.User).options(joinedload(db_models.User.projects).joinedload(db_models.Project.documents)).filter(db_models.User.username == username).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(db_models.User).filter(db_models.User.id == user_id).first()




# def get_all_users(db: Session):
#     return db.query(db_models.User).all()


# def update_refresh_token(db: Session, user: schemas.UserInDB, refresh_token: str):
#     user.refresh_token = refresh_token
#     db.commit()
#     db.refresh(user)
#     return user


# def update_current_proj(db: Session, user: schemas.User, new_id: int):
#     db_user = db.query(db_models.User).filter(
#         db_models.User.id == user.id).first()
#     if new_id == -1:
#         db_user.current_proj_id = None
#     else:
#         db_user.current_proj_id = new_id
#     db.commit()
#     db.refresh(db_user)
#     return db_user