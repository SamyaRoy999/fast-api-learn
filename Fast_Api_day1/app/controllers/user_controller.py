from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.services import user_service
from app.schemas.user import UserCreate, UserUpdate

def list_users(db: Session):
    return user_service.get_users(db)

def create_new_user(db: Session, data: UserCreate):
    return user_service.create_user(db, data)

def update_existing_user(db: Session, user_id: int, data: UserUpdate):
    user = user_service.update_user(db, user_id, data)
    if not user:
        raise HTTPException(404, "User not found")
    return user

def delete_existing_user(db: Session, user_id: int):
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return {"message": "User deleted successfully"}
