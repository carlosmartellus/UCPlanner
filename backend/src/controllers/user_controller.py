from sqlalchemy.orm import Session
from ..db.models.user import User
from ..db.models.course import Course
from PySide6.QtCore import Signal, QObject
from sqlalchemy.exc import IntegrityError


class UserMainController(QObject):
    signal_send_user = Signal(dict)
    signal_send_users = Signal(list)
    def __init__(self, session: Session):
        self.session = session
        super().__init__()

    def create_user(self, name: str):
        user = User(name=name)
        self.session.add(user)
        try:
            self.session.commit()
            self.session.refresh(user)
            self.signal_send_user.emit(self.user_dict(user))
            print('[DEBUG User Controller] User created: ', self.user_dict(user))
        except IntegrityError:
            self.session.rollback()
            self.signal_send_user.emit({'error': f'El nombre {name} ya existe'})

    def get_all_users(self):
        users = self.session.query(User).all()
        result = []
        for user in users:
            result.append(self.user_dict(user))
        
        print('[DEBUG User Controller] Sending ', result, ' users')
        self.signal_send_users.emit(result)

    def get_user_by_id(self, user_id: int):
        user = self.session.query(User).filter(User.id == user_id).first()
        self.signal_send_user.emit(self.user_dict(user))


    def user_dict(self, user: User) -> dict:
        return {
            'id': user.id,
            'name': user.name
        }
