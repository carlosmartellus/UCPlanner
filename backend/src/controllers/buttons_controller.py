from PySide6.QtCore import QObject, Signal
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.models.button import Button

class ButtonMainController(QObject):
    signal_send_buttons_by_mesh_id = Signal(object)
    signal_send_button = Signal(dict)
    signal_error = Signal(str)

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def create_button(self, mesh: dict):
        button = Button(mesh_id=mesh['id'])
        self.session.add(button)
        try:
            self.session.commit()
            self.session.refresh(button)
            print(f'[DEBUG Button Controller] Button created: ({button.id}, {button.mesh_id})')
            self.signal_send_button.emit(self.button_to_dict(button))
        except IntegrityError:
            self.session.rollback()
            self.signal_error.emit(f"No se pudo crear el botón para la malla {mesh['id']}")

    def get_buttons_by_mesh_id(self, mesh: dict):
        print('[DEBUG Button Controller] Mesh received: ', mesh)
        buttons = self.session.query(Button).filter(Button.mesh_id == mesh['id']).all()
        self.signal_send_buttons_by_mesh_id.emit([self.button_to_dict(btn) for btn in buttons])

    def button_to_dict(self, button: Button) -> dict:
        return {
            'id': button.id,
            'mesh_id': button.mesh_id
        }
