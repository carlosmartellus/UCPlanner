from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.base import SessionLocal
from backend.controllers.degree_controller import DegreeMainController
from backend.schemas.degree_schema import DegreeCreate, DegreeRead
from backend.db.models.user import User
from backend.db.models.user_degrees import UserDegrees
from backend.db.models.degree import Degree

router = APIRouter(prefix="/degrees", tags=["Degrees"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[DegreeRead])
def get_degrees(db: Session = Depends(get_db)):
    return DegreeMainController(db).get_all_degrees()

@router.get("/{degree_id}", response_model=DegreeRead)
def get_degree(degree_id: int, db: Session = Depends(get_db)):
    degree = DegreeMainController(db).get_degree_by_id(degree_id)
    if degree:
        return degree
    raise HTTPException(status_code=404, detail="Degree not found")

@router.post("/", response_model=DegreeRead)
def create_degree(degree_data: DegreeCreate, db: Session = Depends(get_db)):
    degree = DegreeMainController(db).create_degree(
        degree_data.name,
        degree_data.school,
        degree_data.total_credits
    )
    if degree:
        return degree
    raise HTTPException(status_code=400, detail="Degree already exists or invalid")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/find-or-create/{user_id}", response_model=DegreeRead)
def find_or_create_degree(user_id: int, degree_data: DegreeCreate, db: Session = Depends(get_db)):
    """
    degree_data: { "name": "Degree Name", "school": "School", "total_credits": 100 }
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    degree = db.query(Degree).filter(Degree.name == degree_data.name).first()
    if not degree:
        degree = Degree(
            name=degree_data.name,
            school=degree_data.school,
            total_credits=degree_data.total_credits
        )
        db.add(degree)
        db.commit()
        db.refresh(degree)

    existing_link = db.query(UserDegrees).filter_by(user_id=user.id, degree_id=degree.id).first()
    if not existing_link:
        link = UserDegrees(user_id=user.id, degree_id=degree.id)
        db.add(link)
        db.commit()

    return degree
