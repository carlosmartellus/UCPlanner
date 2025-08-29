from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..base import Base
from .mixin import SerializableMixin

class Degree(Base, SerializableMixin):
    __tablename__ = "degrees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True, index=True)
    school = Column(String, nullable=True)
    total_credits = Column(Integer, nullable=False)

    users = relationship(
        "User",
        secondary="user_degrees",
        back_populates="degrees"
    )
