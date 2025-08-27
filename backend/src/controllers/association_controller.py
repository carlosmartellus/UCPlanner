from sqlalchemy.orm import Session
from sqlalchemy import insert, delete, update, select
from PySide6.QtCore import QObject, Signal
from sqlalchemy.exc import IntegrityError
from db.models.degree import Degree

from db.models.associations import user_degrees, current_user_course, user_course_history


class AssociationMainController(QObject):
    signal_send_degrees = Signal(list)
    def __init__(self, session: Session):
        super().__init__()
        self.session = session
        self.user_id = None
        self.degree_id = None

    # =========================
    # USER <-> DEGREE
    # =========================
    def add_user_degree(self, data: dict[str, int]):
        '''Creates a new record, awaits for both ids in order to being send by different signals'''
        if 'user_id' in data.keys():
            self.user_id = data['user_id']
        if 'degree_id' in data.keys():
            self.degree_id = data['degree_id']
        print(f'[DEBUG Association Controller] Current data; user_id: {self.user_id} degree_id: {self.degree_id}')

        if self.user_id and self.degree_id:
            try:
                stmt = insert(user_degrees).values(user_id=self.user_id, degree_id=self.degree_id)
                self.session.execute(stmt)
                self.session.commit()
                print(f'[DEBUG Association Controller] User {self.user_id} added to {self.degree_id}')
                return {"user_id": self.user_id, "degree_id": self.degree_id}
            except IntegrityError:
                self.session.rollback()
                print(f'[DEBUG Association Controller] User {self.user_id} already added to {self.degree_id}')
                return None
            finally:
                self.user_id = None
                self.degree_id = None
            
    def get_user_degrees(self, user_id: int):
        '''Returns degrees as dictionary from a user id'''
        stmt = (
            select(Degree)
            .join(user_degrees, Degree.id == user_degrees.c.degree_id)
            .where(user_degrees.c.user_id == user_id)
        )
        result = self.session.execute(stmt).scalars().all()

        degrees = [self.to_dict(degree) for degree in result]
        self.signal_send_degrees.emit(degrees)

        return degrees
 