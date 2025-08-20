from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base


class Curriculum(Base):
    __tablename__ = "curriculum"

    degree_id = Column(Integer, ForeignKey("degrees.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    characteristic_id = Column(Integer, ForeignKey("characteristics.id"))
    semester = Column(String)

    degree = relationship("Degree", back_populates="curriculum_entries")
    course = relationship("Course", back_populates="curriculum_entries")
    characteristic = relationship("Characteristic")