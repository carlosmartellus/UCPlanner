from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.base import SessionLocal
from backend.controllers.user_degrees_controller import UserDegreesController

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/user-degrees", tags=["UserDegrees"])

@router.post("/{user_id}/{degree_id}")
def add_degree(user_id: int, degree_id: int, db: Session = Depends(get_db)):
    link = UserDegreesController(db).add_degree_to_user(user_id, degree_id)
    if not link:
        return {"detail": "Degree already linked to user"}
    return {"detail": "Degree added successfully"}

@router.delete("/{user_id}/{degree_id}")
def remove_degree(user_id: int, degree_id: int, db: Session = Depends(get_db)):
    success = UserDegreesController(db).remove_degree_from_user(user_id, degree_id)
    if not success:
        return {"detail": "Link not found"}
    return {"detail": "Degree removed successfully"}

@router.get("/{user_id}")
def get_degrees(user_id: int, db: Session = Depends(get_db)):
    degrees = UserDegreesController(db).get_user_degrees(user_id)
    return degrees
