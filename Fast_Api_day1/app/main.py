from fastapi import FastAPI
from app.database import Base, engine
from app.routers.user_router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI MVC + PostgreSQL Running!"}

app.include_router(user_router)