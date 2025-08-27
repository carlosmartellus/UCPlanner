from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
from .mixin import SerializableMixin

class Curriculum(Base, SerializableMixin):
    __tablename__ = "curriculums"

    id = Column(Integer, primary_key=True)
    degree_id = Column(Integer, ForeignKey("degrees.id"))

    degree = relationship("Degree", back_populates="curriculums")
    courses = relationship("Course", secondary="curriculum_courses", back_populates="curriculums")
    meshes = relationship("Mesh", back_populates="curriculum")

    prerequisites = relationship("Prerequisite", back_populates="curriculum")