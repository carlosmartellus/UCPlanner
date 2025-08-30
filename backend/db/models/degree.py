from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db.base import Base
from .mixin import SerializableMixin

class Degree(Base, SerializableMixin):
    __tablename__ = "degrees"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    school = Column(String, nullable=True)
    total_credits = Column(Integer, nullable=False)

    users = relationship(
        "User",
        secondary="user_degrees",
        back_populates="degrees"
    )

    degree_courses = relationship("DegreeCourses", back_populates="degree")
