from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.controllers import user_controller
from app.schemas.user import UserCreate, UserUpdate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return user_controller.list_users(db)

@router.post("/", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_new_user(db, data)

@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    return user_controller.update_existing_user(db, user_id, data)

@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_controller.delete_existing_user(db, user_id)
