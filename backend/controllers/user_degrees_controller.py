from sqlalchemy.orm import Session
from backend.db.models.user import User
from backend.db.models.degree import Degree
from backend.db.models.user_degrees import UserDegrees

class UserDegreesController:
    def __init__(self, db: Session):
        self.db = db

    def add_degree_to_user(self, user_id: int, degree_id: int):
        existing = self.db.query(UserDegrees).filter_by(user_id=user_id, degree_id=degree_id).first()
        if existing:
            return None

        link = UserDegrees(user_id=user_id, degree_id=degree_id)
        self.db.add(link)
        self.db.commit()
        return link

    def remove_degree_from_user(self, user_id: int, degree_id: int):
        link = self.db.query(UserDegrees).filter_by(user_id=user_id, degree_id=degree_id).first()
        if not link:
            return None
        self.db.delete(link)
        self.db.commit()
        return True

    def get_user_degrees(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            return []
        return user.degrees
