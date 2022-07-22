from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import DB_NAME, DB_PASSWORD, DB_USERNAME

SQLALCHEMY_DATABASE_URI = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URI
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
