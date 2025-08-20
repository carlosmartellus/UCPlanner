from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..base import Base

# Example: Test1, Test2, Midterm, FinalExam, Assignment1, Assignment2
class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    weight = Column(Float, nullable=False)

    categories = relationship("Category", back_populates="activity")