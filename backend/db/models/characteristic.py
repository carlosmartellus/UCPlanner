# characteristic.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db.base import Base
from .mixin import SerializableMixin

class Characteristic(Base, SerializableMixin):
    __tablename__ = "characteristics"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    color = Column(String) 

    degree_courses = relationship("DegreeCourses", back_populates="characteristic")
