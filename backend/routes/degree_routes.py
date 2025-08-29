from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.base import SessionLocal
from backend.controllers.degree_controller import DegreeMainController
from backend.schemas.degree_schema import DegreeCreate, DegreeRead

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
    degree = DegreeMainController(db).create_degree(degree_data)
    if degree:
        return degree
    raise HTTPException(status_code=400, detail="Degree already exists or invalid")
