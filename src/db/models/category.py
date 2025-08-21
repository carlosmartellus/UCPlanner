from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from ..base import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    weight = Column(Float, nullable=False)

    activities = relationship('Activity', back_populates='category')
