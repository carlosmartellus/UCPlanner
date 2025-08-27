from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
from .mixin import SerializableMixin

class Mesh(Base, SerializableMixin):
    __tablename__ = 'meshs'

    id = Column(Integer, primary_key=True)
    curriculum_id = Column(Integer, ForeignKey('curriculums.id'))

    curriculum = relationship('Curriculum', back_populates='meshes')
    buttons = relationship('Button', back_populates='mesh')
