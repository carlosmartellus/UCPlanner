from sqlalchemy import Column, Integer, ForeignKey, Table, Float, Boolean
from .base import Base

user_course_history = Table(
    'user_course_history', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('grade', Float),
    Column('passed', Boolean)
)

current_user_course = Table(
    'current_user_course', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)