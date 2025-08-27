from PySide6.QtCore import QObject, Signal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models.mesh import Mesh

class MeshMainController(QObject):
    signal_send_mesh = Signal(object)
    signal_error = Signal(str)

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def create_mesh(self, curriculum: dict):
        mesh = Mesh(curriculum_id=curriculum['id'])
        self.session.add(mesh)
        try:
            self.session.commit()
            self.session.refresh(mesh)
            self.signal_send_mesh.emit(self.mesh_to_dict(mesh))
            print('[DEBUG Mesh Controller] Mesh created: ', self.mesh_to_dict(mesh))
        except IntegrityError:
            self.session.rollback()

    def mesh_to_dict(self, mesh: Mesh) -> dict:
        return {
            'id': mesh.id,
            'curriculum_id': mesh.curriculum_id
        }
