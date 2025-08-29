from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base
from .mixin import SerializableMixin

class User(Base, SerializableMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    degrees = relationship(
        "Degree",
        secondary="user_degrees",
        back_populates="users"
    )
    