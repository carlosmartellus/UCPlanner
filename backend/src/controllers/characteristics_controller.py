from sqlalchemy.orm import Session
from db.models.characteristics import Characteristic
from PySide6.QtCore import QObject, Signal
from typing import List


class CharacteristicsMainController(QObject):
    signal_send_characteristics = Signal(list)
    signal_send_characteristic = Signal(dict)

    def __init__(self, session: Session):
        super().__init__()
        self.session = session

    def create_characteristic(self, name: str, color: str):
        characteristic = Characteristic(name=name, color=color)
        self.session.add(characteristic)
        self.session.commit()
        self.session.refresh(characteristic)
        self.signal_send_characteristic.emit(self.characteristic_to_dict(characteristic))

    def get_all_characteristics(self):
        characteristics = self.session.query(Characteristic).all()
        result = []
        for characteristic in characteristics:
            result.append(self.characteristic_to_dict(characteristic))
        self.signal_send_characteristics.emit(result)

    def get_characteristic_by_id(self, characteristic_id: int):
        characteristic = self.session.query(Characteristic).filter(Characteristic.id == characteristic_id).first()
        self.signal_send_characteristic.emit(self.characteristic_to_dict(characteristic))

    def get_characteristic_by_name(self, name: str | None = None):
        characteristic = self.session.query(Characteristic).filter(Characteristic.name == name).first()
        self.signal_send_characteristic.emit(self.characteristic_to_dict(characteristic))

    def update_characteristic(self, characteristic_id: int, **kwargs):
        characteristic = self.session.query(Characteristic).filter(Characteristic.id == characteristic_id).first()
        if not characteristic:
            return
        for key, value in kwargs.items():
            if hasattr(characteristic, key):
                setattr(characteristic, key, value)
        self.session.commit()
        self.session.refresh(characteristic)
        self.signal_send_characteristic.emit(self.characteristic_to_dict(characteristic))

    def delete_characteristic(self, characteristic_id: int):
        characteristic = self.session.query(Characteristic).filter(Characteristic.id == characteristic_id).first()
        if not characteristic:
            return
        self.session.delete(characteristic)
        self.session.commit()

    def characteristic_to_dict(self, characteristic: Characteristic) -> dict:
        return {
            "id": characteristic.id,
            "name": characteristic.name,
            "color": characteristic.color
        }
