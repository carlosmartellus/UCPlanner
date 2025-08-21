from sqlalchemy.orm import Session
from db.models.degree import Degree


def create_degree(session: Session, name: str, school: str, total_credits: int):
    degree = Degree(name=name, school=school, total_credits=total_credits)
    session.add(degree)
    session.commit()
    session.refresh(degree)
    return degree


def get_all_degrees(session: Session):
    return session.query(Degree).all()


def get_degree_by_id(session: Session, degree_id: int):
    return session.query(Degree).filter(Degree.id == degree_id).first()


def update_degree(session: Session, degree_id: int, name: str = None, school: str = None, total_credits: int = None):
    degree = session.query(Degree).filter(Degree.id == degree_id).first()
    if not degree:
        return None
    
    if name is not None:
        degree.name = name
    if school is not None:
        degree.school = school
    if total_credits is not None:
        degree.total_credits = total_credits
    
    session.commit()
    session.refresh(degree)
    return degree


def delete_degree(session: Session, degree_id: int):
    degree = session.query(Degree).filter(Degree.id == degree_id).first()
    if not degree:
        return None
    
    session.delete(degree)
    session.commit()
    return degree
