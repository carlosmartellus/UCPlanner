from sqlalchemy.orm import Session
from db.models.course import Course
from typing import List


def create_course(
    session: Session,
    code: str,
    name: str,
    nrc: int,
    credits: int,
    area: str | None = None
) -> Course:
    course = Course(
        code=code,
        name=name,
        nrc=nrc,
        credits=credits,
        area=area,
    )
    session.add(course)
    session.commit()
    session.refresh(course)
    return course


def get_course_by_id(session: Session, course_id: int) -> Course | None:
    return session.query(Course).filter(Course.id == course_id).first()

def get_course_by_code(session: Session, code: str) -> Course | None:
    return session.query(Course).filter(Course.code == code).first()

def get_all_courses(session: Session) -> List[Course]:
    return session.query(Course).all()

def get_course_by(
        session: Session,
        code: str | None = None,
        name: str | None = None,
        nrc: int | None = None,
        credits: int | None = None,
        area: str | None = None
    ) -> List[Course]:

    query = session.query(Course)

    if code is not None:
        query = query.filter(Course.code == code)
    if name is not None:
        query = query.filter(Course.name.ilike(f'%{name}%'))
    if nrc is not None:
        query = query.filter(Course.nrc == nrc)
    if credits is not None:
        query = query.filter(Course.credits == credits)
    if area is not None:
        query = query.filter(Course.area == area)

    return query.all()

def update_course(
    session: Session,
    course_id: int,
    **kwargs
) -> Course | None:
    course = get_course_by_id(session, course_id)
    if not course:
        return None
    for key, value in kwargs.items():
        if hasattr(course, key):
            setattr(course, key, value)
    session.commit()
    session.refresh(course)
    return course


def delete_course(session: Session, course_id: int) -> bool:
    course = get_course_by_id(session, course_id)
    if not course:
        return False
    session.delete(course)
    session.commit()
    return True
