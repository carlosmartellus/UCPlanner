from .base import Base, engine
from .models.user import User
from .models.course import Course
from .models.activity import Activity
from .models.category import Category
from .models.characteristics import Characteristic
from .models.curriculum import Curriculum
from .models.degree import Degree
from .models.prerequisite import Prerequisite
from .models.associations import user_course_history, current_user_course

Base.metadata.create_all(bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)