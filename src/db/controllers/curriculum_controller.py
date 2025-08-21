from sqlalchemy.orm import Session
from db.models.curriculum import Curriculum


def create_curriculum(session: Session, degree_id: int, course_id: int, characteristic_id: int, semester: str):
    curriculum_entry = Curriculum(
        degree_id=degree_id,
        course_id=course_id,
        characteristic_id=characteristic_id,
        semester=semester
    )
    session.add(curriculum_entry)
    session.commit()
    session.refresh(curriculum_entry)
    return curriculum_entry


def get_all_curriculum(session: Session):
    return session.query(Curriculum).all()


def get_curriculum_by(session: Session, degree_id: int, course_id: int):
    return session.query(Curriculum).filter(
        Curriculum.degree_id == degree_id,
        Curriculum.course_id == course_id
    ).first()

def update_curriculum(session: Session, degree_id: int, course_id: int, characteristic_id: int = None, semester: str = None):
    curriculum_entry = session.query(Curriculum).filter(
        Curriculum.degree_id == degree_id,
        Curriculum.course_id == course_id
    ).first()
    if not curriculum_entry:
        return None
    
    if characteristic_id is not None:
        curriculum_entry.characteristic_id = characteristic_id
    if semester is not None:
        curriculum_entry.semester = semester
    
    session.commit()
    session.refresh(curriculum_entry)
    return curriculum_entry


def delete_curriculum(session: Session, degree_id: int, course_id: int):
    curriculum_entry = session.query(Curriculum).filter(
        Curriculum.degree_id == degree_id,
        Curriculum.course_id == course_id
    ).first()
    if not curriculum_entry:
        return None
    
    session.delete(curriculum_entry)
    session.commit()
    return curriculum_entry
