from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base
from .associations import user_course_history, current_user_course

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    course_history = relationship('Course', secondary=user_course_history)
    current_courses = relationship('Course', secondary=current_user_course)
