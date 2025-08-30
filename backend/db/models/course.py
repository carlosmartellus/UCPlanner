from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db.base import Base
from .mixin import SerializableMixin

class Course(Base, SerializableMixin):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    nrc = Column(Integer, unique=True)
    credits = Column(Integer)
    area = Column(String, nullable=True)

    degree_courses = relationship("DegreeCourses", back_populates="course")
