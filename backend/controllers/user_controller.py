from sqlalchemy.orm import Session
from ..db.models.user import User

class UserMainController:
    def __init__(self, db: Session):
        self.db = db

    def get_all_users(self):
        return self.db.query(User).all()

    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, name: str):
        existing = self.db.query(User).filter(User.name == name).first()
        if existing:
            return None

        new_user = User(name=name)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
