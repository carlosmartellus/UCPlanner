from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.base import SessionLocal
from backend.controllers.user_controller import UserMainController
from backend.schemas.user_schema import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["Users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UserRead])
def get_users(db: Session = Depends(get_db)):
    return UserMainController(db).get_all_users()

@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserMainController(db).get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=UserRead)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = UserMainController(db).create_user(user_data.name)
    if user:
        print(user)
        return user
    raise HTTPException(status_code=400, detail="User already exists")
