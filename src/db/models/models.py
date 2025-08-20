from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float, Boolean
from sqlalchemy.orm import relationship
from ..base import Base

# Association Tables
user_course_history = Table(
    "user_course_history", Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("course_id", Integer, ForeignKey("courses.id")),
    Column("grade", Float),
    Column("passed", Boolean)
)

current_user_course = Table(
    "current_user_course", Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("course_id", Integer, ForeignKey("courses.id"))
)

# Models

# Example: Test1, Test2, Midterm, FinalExam, Assignment1, Assignment2
class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    weight = Column(Float, nullable=False)

    categories = relationship("Category", back_populates="activity")


# Example: Lecture, Project
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    activity_id = Column(Integer, ForeignKey("activities.id"), nullable=False)
    weight = Column(Float, nullable=False)

    activity = relationship("Activity", back_populates="categories")
    courses = relationship("Course", back_populates="category")


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True)
    name = Column(String, unique=False)
    nrc = Column(Integer, unique=True)
    credits = Column(Integer, unique=False)
    area = Column(String, unique=False, nullable=True)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="courses")

    curriculum_entries = relationship("Curriculum", back_populates="course")


class Degree(Base):
    __tablename__ = "degrees"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    school = Column(String, nullable=True)
    total_credits = Column(Integer, nullable=False)

    curriculum_entries = relationship("Curriculum", back_populates="degree")


class Curriculum(Base):
    __tablename__ = "curriculum"

    degree_id = Column(Integer, ForeignKey("degrees.id"), primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    characteristic_id = Column(Integer, ForeignKey("characteristics.id"))
    semester = Column(String)

    degree = relationship("Degree", back_populates="curriculum_entries")
    course = relationship("Course", back_populates="curriculum_entries")
    characteristic = relationship("Characteristic")

class Characteristic(Base):
    __tablename__ = "characteristics"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    color = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    course_history = relationship("Course", secondary=user_course_history)
    current_courses = relationship("Course", secondary=current_user_course)
