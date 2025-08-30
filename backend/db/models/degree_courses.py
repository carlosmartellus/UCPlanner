from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.db.base import Base
from .mixin import SerializableMixin

class DegreeCourses(Base, SerializableMixin):
    __tablename__ = "degree_courses"

    degree_id = Column(Integer, ForeignKey("degrees.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"), primary_key=True)
    characteristics_id = Column(Integer, ForeignKey("characteristics.id"), primary_key=True) 

    characteristic = relationship(
        "Characteristic",
        back_populates="degree_courses"
    )
    
    degree = relationship("Degree", back_populates="degree_courses")
    course = relationship("Course", back_populates="degree_courses")
