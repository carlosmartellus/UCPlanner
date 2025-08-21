from PySide6.QtCore import QObject, Signal
from sqlalchemy.orm import Session
from db.models.degree import Degree
from sqlalchemy.exc import IntegrityError

class DegreeMainController(QObject):
    signal_send_degree = Signal(dict)
    signal_send_degrees = Signal(list)
    signal_error = Signal(str)

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def create_degree(self, name: str, school: str, total_credits: int):
        degree = Degree(name=name, school=school, total_credits=total_credits)
        self.session.add(degree)
        try:
            self.session.commit()
            self.session.refresh(degree)
            self.signal_send_degree.emit(self.degree_dict(degree))
        except IntegrityError:
            self.session.rollback()
            self.signal_error.emit(f'El grado {name} ya existe')

    def get_all_degrees(self):
        degrees = self.session.query(Degree).all()
        self.signal_send_degrees.emit([self.degree_dict(d) for d in degrees])

    def get_degree_by_id(self, degree_id: int):
        degree = self.session.query(Degree).filter(Degree.id == degree_id).first()
        if degree:
            self.signal_send_degree.emit(self.degree_dict(degree))

    def update_degree(self, degree_id: int, name: str = None, school: str = None, total_credits: int = None):
        degree = self.session.query(Degree).filter(Degree.id == degree_id).first()
        if not degree:
            self.signal_error.emit(f'Degree con ID {degree_id} no encontrado')
            return
        
        if name is not None:
            degree.name = name
        if school is not None:
            degree.school = school
        if total_credits is not None:
            degree.total_credits = total_credits
        
        try:
            self.session.commit()
            self.session.refresh(degree)
            self.signal_send_degree.emit(self.degree_dict(degree))
        except IntegrityError:
            self.session.rollback()
            self.signal_error.emit(f'El grado {name} ya existe')

    def delete_degree(self, degree_id: int):
        degree = self.session.query(Degree).filter(Degree.id == degree_id).first()
        if not degree:
            self.signal_error.emit(f'Degree con ID {degree_id} no encontrado')
            return
        
        self.session.delete(degree)
        self.session.commit()
        self.signal_send_degree.emit(self.degree_dict(degree))

    @staticmethod
    def degree_dict(degree: Degree) -> dict:
        return {
            'id': degree.id,
            'name': degree.name,
            'school': degree.school,
            'total_credits': degree.total_credits
        }
