from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    weight = Column(Float, nullable=False)

    activity = relationship("Activity", back_populates="categories")
    courses = relationship("Course", back_populates="category")
