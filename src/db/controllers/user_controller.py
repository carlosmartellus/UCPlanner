from sqlalchemy.orm import Session
from db.models.user import User
from db.models.course import Course
from PySide6.QtCore import Signal, Qt

class UserMainController:
    signal_send_user = Signal(dict)
    signal_send_users = Signal(list[dict])

    def create_user(self, session: Session, name: str):
        user = User(name=name)
        session.add(user)
        session.commit()
        session.refresh(user)
        self.signal_send_user.emit(self.user_dict(user))


    def get_all_users(self, session: Session):
        users = session.query(User).all()
        result = []
        for user in users:
            result.append(self.user_dict(user))
        self.signal_send_users.emit(result)

    def get_user_by_id(self, session: Session, user_id: int):
        user = session.query(User).filter(User.id == user_id).first()
        self.signal_send_user.emit(self.user_dict(user))


    def update_user(self, session: Session, user_id: int, name: str = None):
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        if name is not None:
            user.name = name
        session.commit()
        session.refresh(user)
        self.signal_send_user.emit(self.user_dict(user))

    def delete_user(self, session: Session, user_id: int):
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        session.delete(user)
        session.commit()
        self.signal_send_user.emit(self.user_dict(user))

    # History and current courses

    def add_course_to_history(self, session: Session, user_id: int, course_id: int):
        user = session.query(User).filter(User.id == user_id).first()
        course = session.query(Course).filter(Course.id == course_id).first()
        if not user or not course:
            return None
        user.course_history.append(course)
        session.commit()
        session.refresh(user)
        self.signal_send_user.emit(self.user_dict(user))


    def add_current_course(self, session: Session, user_id: int, course_id: int):
        user = session.query(User).filter(User.id == user_id).first()
        course = session.query(Course).filter(Course.id == course_id).first()
        if not user or not course:
            return None
        user.current_courses.append(course)
        session.commit()
        session.refresh(user)
        self.signal_send_user.emit(self.user_dict(user))


    def remove_course_from_history(self, session: Session, user_id: int, course_id: int):
        user = session.query(User).filter(User.id == user_id).first()
        course = session.query(Course).filter(Course.id == course_id).first()
        if not user or not course:
            return None
        if course in user.course_history:
            user.course_history.remove(course)
            session.commit()
        self.signal_send_user.emit(self.user_dict(user))


    def remove_current_course(self, session: Session, user_id: int, course_id: int):
        user = session.query(User).filter(User.id == user_id).first()
        course = session.query(Course).filter(Course.id == course_id).first()
        if not user or not course:
            return None
        if course in user.current_courses:
            user.current_courses.remove(course)
            session.commit()
        self.signal_send_user.emit(self.user_dict(user))

    def user_dict(self, user: User) -> dict:
        return {
            "id": user.id,
            "name": user.name
        }
