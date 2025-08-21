from sqlalchemy.orm import Session
from sqlalchemy import insert, delete, update, select
from PySide6.QtCore import QObject, Signal
from sqlalchemy.exc import IntegrityError
from db.models.degree import Degree

from db.models.associations import user_degrees, current_user_course, user_course_history


class AssociationMainController(QObject):
    signal_get_degrees_for_user = Signal(list)
    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    # =========================
    # USER <-> DEGREE
    # =========================
    def add_user_degree(self, user_id: int, degree_id: int):
        try:
            stmt = insert(user_degrees).values(user_id=user_id, degree_id=degree_id)
            self.session.execute(stmt)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            return None
        return {"user_id": user_id, "degree_id": degree_id}

    def remove_user_degree(self, user_id: int, degree_id: int):
        stmt = delete(user_degrees).where(
            (user_degrees.c.user_id == user_id) & (user_degrees.c.degree_id == degree_id)
        )
        result = self.session.execute(stmt)
        self.session.commit()
        return result.rowcount > 0

    def get_degrees_for_user(self, user_id: int):
        stmt = select(user_degrees.c.degree_id).where(user_degrees.c.user_id == user_id)
        result = self.session.execute(stmt).scalars().all()
        self.signal_get_degrees_for_user.emit(result)

    # =========================
    # USER <-> CURRENT COURSES
    # =========================
    def add_current_course(self, user_id: int, course_id: int):
        try:
            stmt = insert(current_user_course).values(user_id=user_id, course_id=course_id)
            self.session.execute(stmt)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            return None
        return {"user_id": user_id, "course_id": course_id}

    def remove_current_course(self, user_id: int, course_id: int):
        stmt = delete(current_user_course).where(
            (current_user_course.c.user_id == user_id) & (current_user_course.c.course_id == course_id)
        )
        result = self.session.execute(stmt)
        self.session.commit()
        return result.rowcount > 0

    def get_degrees_for_user(self, user_id: int):
        stmt = (
            select(Degree.id, Degree.name, Degree.school, Degree.total_credits)
            .join(user_degrees, Degree.id == user_degrees.c.degree_id)
            .where(user_degrees.c.user_id == user_id)
        )
        result = self.session.execute(stmt).all()
        degrees = [dict(row._mapping) for row in result]
        self.signal_get_degrees_for_user.emit(degrees)


    # =========================
    # USER <-> COURSE HISTORY
    # =========================
    def add_course_to_history(self, user_id: int, course_id: int, grade: float, passed: bool):
        try:
            stmt = insert(user_course_history).values(
                user_id=user_id, course_id=course_id, grade=grade, passed=passed
            )
            self.session.execute(stmt)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            return None
        return {"user_id": user_id, "course_id": course_id, "grade": grade, "passed": passed}

    def update_course_history(self, user_id: int, course_id: int, grade: float = None, passed: bool = None):
        stmt = update(user_course_history).where(
            (user_course_history.c.user_id == user_id) & (user_course_history.c.course_id == course_id)
        )
        values = {}
        if grade is not None:
            values["grade"] = grade
        if passed is not None:
            values["passed"] = passed

        if not values:
            return None

        stmt = stmt.values(**values)
        self.session.execute(stmt)
        self.session.commit()
        return {"user_id": user_id, "course_id": course_id, **values}

    def get_course_history_for_user(self, user_id: int):
        stmt = select(user_course_history).where(user_course_history.c.user_id == user_id)
        result = self.session.execute(stmt).all()
        return [dict(row._mapping) for row in result]
