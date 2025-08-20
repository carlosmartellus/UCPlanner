from sqlalchemy.orm import Session
from db.models.characteristics import Characteristic
from typing import List


def create_characteristics(
    session: Session,
    name: str,
    color: str
) -> Characteristic:
    characteristics = Characteristic(name=name, color=color)
    session.add(characteristics)
    session.commit()
    session.refresh(characteristics)
    return characteristics


def get_characteristics_by_id(session: Session, characteristics_id: int) -> Characteristic | None:
    return session.query(Characteristic).filter(Characteristic.id == characteristics_id).first()

def get_all_characteristics(session: Session) -> List[Characteristic]:
    return session.query(Characteristic).all()

def get_characteristics_by_name(session: Session, name: str | None = None) -> Characteristic:
    return session.query(Characteristic).filter(Characteristic.name == name).first()

def update_characteristics(
    session: Session,
    characteristics_id: int,
    **kwargs
) -> Characteristic | None:
    characteristics = get_characteristics_by_id(session, characteristics_id)
    if not characteristics:
        return None
    for key, value in kwargs.items():
        if hasattr(characteristics, key):
            setattr(characteristics, key, value)
    session.commit()
    session.refresh(characteristics)
    return characteristics


def delete_characteristics(session: Session, characteristics_id: int) -> bool:
    characteristics = get_characteristics_by_id(session, characteristics_id)
    if not characteristics:
        return False
    session.delete(characteristics)
    session.commit()
    return True
