from sqlalchemy import Column, Integer, ForeignKey
from backend.db.base import Base

class UserDegrees(Base):
    __tablename__ = "user_degrees"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    degree_id = Column(Integer, ForeignKey("degrees.id"), primary_key=True)
