from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base

class Characteristic(Base):
    __tablename__ = 'characteristics'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    color = Column(String)
