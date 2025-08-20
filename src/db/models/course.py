from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String, unique=False)
    nrc = Column(Integer, unique=True)
    credits = Column(Integer, unique=False)
    area = Column(String, unique=False, nullable=True)
