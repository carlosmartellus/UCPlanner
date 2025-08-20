from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..base import Base

class Degree(Base):
    __tablename__ = 'degrees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    school = Column(String, nullable=True)
    total_credits = Column(Integer, nullable=False)

    curriculum_entries = relationship('Curriculum', back_populates='degree')