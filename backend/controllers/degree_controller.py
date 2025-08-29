from sqlalchemy.orm import Session
from ..db.models.degree import Degree

class DegreeMainController:
    def __init__(self, db: Session):
        self.db = db

    def get_all_degrees(self):
        return self.db.query(Degree).all()

    def get_degree_by_id(self, degree_id: int):
        return self.db.query(Degree).filter(Degree.id == degree_id).first()

    def create_degree(self, name: str, school: str, total_credits: int):
        print(f'Data received: {name, school, total_credits}')
        existing = self.db.query(Degree).filter(Degree.name == name).first()
        if existing:
            return None

        new_degree = Degree(
            name=name,
            school=school,
            total_credits=total_credits
        )
        self.db.add(new_degree)
        self.db.commit()
        self.db.refresh(new_degree)
        return new_degree
