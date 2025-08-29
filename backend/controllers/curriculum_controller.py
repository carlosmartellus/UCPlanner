from sqlalchemy.orm import Session
from db.models.curriculum import Curriculum
from PySide6.QtCore import QObject, Signal


class CurriculumMainController(QObject):
    signal_send_curriculums = Signal(list)
    signal_send_curriculum = Signal(object)

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def create_curriculum(self, degree: dict):
        print('[DEBUG Curriculum Controller] Degree received: ', degree)
        curriculum = Curriculum(degree_id=degree['id'])
        self.session.add(curriculum)
        self.session.commit()
        self.session.refresh(curriculum)

        print('[DEBUG Curriculum Controller] Curriculum created: ', self.curriculum_to_dict(curriculum))
        
        self.signal_send_curriculum.emit(self.curriculum_to_dict(curriculum))
        return self.curriculum_to_dict(curriculum)

    def get_all_curriculum(self):
        curriculums = self.session.query(Curriculum).all()
        result = []
        for curriculum in curriculums:
            result.append(self.curriculum_to_dict(curriculum))

    def get_curriculum_by_degree(self, degree_id: int) -> list[dict]:
        query = self.session.query(Curriculum)
        if degree_id is not None:
            query = query.filter(Curriculum.degree_id == degree_id)

        curriculums = query.all()
        result = [self.curriculum_to_dict(c) for c in curriculums]
        return result

    def get_or_create_curriculum(self, degree: dict) -> dict:
        result = self.get_curriculum_by_degree(degree['id'])

        if not result:
            print('[DEBUG Curriculum Controller] No curriculum found, creating new one')
            return self.create_curriculum(degree)

        print('[DEBUG Curriculum Controller] Found curriculum: ', result[0])
        self.signal_send_curriculum.emit(result[0])
        return result[0]


    def delete_curriculum(self, degree_id: int):
        curriculum = self.session.query(Curriculum).filter(
            Curriculum.degree_id == degree_id,
        ).first()
        if not curriculum:
            return
        
        self.session.delete(curriculum)
        self.session.commit()

    def curriculum_to_dict(self, curriculum: Curriculum) -> dict:
        return {
            "id": curriculum.id,
            "degree_id": curriculum.degree_id
        }
