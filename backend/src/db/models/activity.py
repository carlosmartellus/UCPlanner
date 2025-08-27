from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
from .mixin import SerializableMixin


class Activity(Base, SerializableMixin):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    weight = Column(Float, nullable=False)

    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category', back_populates='activities')
