from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
from .mixin import SerializableMixin

class Prerequisite(Base, SerializableMixin):
    __tablename__ = 'prerequisites'

    curriculum_id = Column(Integer, ForeignKey('curriculums.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    course_prerequisite_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)

    curriculum = relationship('Curriculum', back_populates='prerequisites')
    course = relationship('Course', foreign_keys=[course_id])
    prerequisite_course = relationship('Course', foreign_keys=[course_prerequisite_id])
