from fastapi import FastAPI
from .database import engine
from .routers import user_router
from . import db_models

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def root():
    return {"message": "backend"}

app.include_router(user_router.router)
