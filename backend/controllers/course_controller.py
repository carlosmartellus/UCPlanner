from PySide6.QtCore import QObject, Signal
from sqlalchemy.orm import Session
from db.models.course import Course
from typing import List


class CourseMainController(QObject):
    signal_send_course = Signal(dict)
    signal_send_courses = Signal(list)
    signal_error = Signal(str)

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def create_course(self, code: str, name: str, nrc: int, credits: int, area: str | None = None):
        print('[DEBUG Course Controller] Creating course ', name)
        course = Course(code=code, name=name, nrc=nrc, credits=credits, area=area)
        self.session.add(course)
        try:
            self.session.commit()
            self.session.refresh(course)
            self.signal_send_course.emit(self.course_to_dict(course))
        except Exception as e:
            self.session.rollback()
            self.signal_error.emit(f'Error al crear curso: {str(e)}')

    def get_all_courses(self):
        courses = self.session.query(Course).all()
        result = [self.course_to_dict(c) for c in courses]
        self.signal_send_courses.emit(result)

    def get_course_by(
        self,
        code: str | None = None,
        name: str | None = None,
        nrc: int | None = None,
        credits: int | None = None,
        area: str | None = None
    ):
        query = self.session.query(Course)
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
        courses = query.all()
        result = [self.course_to_dict(c) for c in courses]
        self.signal_send_courses.emit(result)

    def update_course(self, course_id: int, **kwargs):
        course = self.session.query(Course).filter(Course.id == course_id).first()
        if not course:
            self.signal_error.emit(f'Curso con ID {course_id} no encontrado')
            return
        for key, value in kwargs.items():
            if hasattr(course, key):
                setattr(course, key, value)
        self.session.commit()
        self.session.refresh(course)
        self.signal_send_course.emit(self.course_to_dict(course))

    def delete_course(self, course_id: int):
        course = self.session.query(Course).filter(Course.id == course_id).first()
        if not course:
            self.signal_error.emit(f'Curso con ID {course_id} no encontrado')
            return
        self.session.delete(course)
        self.session.commit()
        self.signal_send_course.emit(self.course_to_dict(course))

    def course_to_dict(self, course: Course) -> dict:
        return {
            "id": course.id,
            "code": course.code,
            "name": course.name,
            "nrc": course.nrc,
            "credits": course.credits,
            "area": course.area
        }
