from fastapi import FastAPI

from app.cruds import wallet_crud
from app.routers import wallet_router
from .database import engine
from .routers import user_router, wallet_router
from . import db_models

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "backend"}

app.include_router(user_router.router)
app.include_router(wallet_router.router)
