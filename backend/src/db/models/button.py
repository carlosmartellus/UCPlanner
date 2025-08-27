from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from ..base import Base
from .mixin import SerializableMixin


class Button(Base, SerializableMixin):
    __tablename__ = 'buttons'

    id = Column(Integer, primary_key=True)
    mesh_id = Column(Integer, ForeignKey('meshs.id'))

    mesh = relationship('Mesh', back_populates='buttons')
