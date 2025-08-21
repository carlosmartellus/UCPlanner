from sqlalchemy.orm import Session
from db.models.user import User
from db.models.course import Course


def create_user(session: Session, name: str):
    user = User(name=name)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_all_users(session: Session):
    return session.query(User).all()


def get_user_by_id(session: Session, user_id: int):
    return session.query(User).filter(User.id == user_id).first()


def update_user(session: Session, user_id: int, name: str = None):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    if name is not None:
        user.name = name
    session.commit()
    session.refresh(user)
    return user

def delete_user(session: Session, user_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    session.delete(user)
    session.commit()
    return user

# History and current courses

def add_course_to_history(session: Session, user_id: int, course_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    course = session.query(Course).filter(Course.id == course_id).first()
    if not user or not course:
        return None
    user.course_history.append(course)
    session.commit()
    session.refresh(user)
    return user


def add_current_course(session: Session, user_id: int, course_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    course = session.query(Course).filter(Course.id == course_id).first()
    if not user or not course:
        return None
    user.current_courses.append(course)
    session.commit()
    session.refresh(user)
    return user


def remove_course_from_history(session: Session, user_id: int, course_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    course = session.query(Course).filter(Course.id == course_id).first()
    if not user or not course:
        return None
    if course in user.course_history:
        user.course_history.remove(course)
        session.commit()
    return user


def remove_current_course(session: Session, user_id: int, course_id: int):
    user = session.query(User).filter(User.id == user_id).first()
    course = session.query(Course).filter(Course.id == course_id).first()
    if not user or not course:
        return None
    if course in user.current_courses:
        user.current_courses.remove(course)
        session.commit()
    return user
