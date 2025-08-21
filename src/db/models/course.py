from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..base import Base

class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String)
    nrc = Column(Integer, unique=True)
    credits = Column(Integer)
    area = Column(String, nullable=True)

    curriculum_entries = relationship("Curriculum", back_populates="course")
