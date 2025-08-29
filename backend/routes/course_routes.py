from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.base import SessionLocal
from backend.controllers.course_controller import CourseMainController
from backend.schemas.course_schema import CourseCreate, CourseRead

router = APIRouter(prefix="/courses", tags=["Courses"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[CourseRead])
def get_courses(db: Session = Depends(get_db)):
    return CourseMainController(db).get_all_courses()

@router.get("/{course_id}", response_model=CourseRead)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = CourseMainController(db).get_course_by_id(course_id)
    if course:
        return course
    raise HTTPException(status_code=404, detail="Course not found")

@router.post("/", response_model=CourseRead)
def create_course(course_data: CourseCreate, db: Session = Depends(get_db)):
    course = CourseMainController(db).create_course(course_data)
    if course:
        return course
    raise HTTPException(status_code=400, detail="Course already exists or invalid")
