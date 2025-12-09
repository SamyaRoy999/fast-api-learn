from sqlalchemy.orm import Session
from app.models.user import User  
from app.schemas.user import UserCreate, UserUpdate  

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, data: UserCreate):
    user = User(**data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user(db: Session, user_id: int, data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in data.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
