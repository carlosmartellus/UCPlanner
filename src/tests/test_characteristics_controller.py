import pytest
from db.controllers.characteristics_controller import (
    create_characteristics, get_characteristics_by_id, get_all_characteristics,
    get_characteristics_by_name, update_characteristics, delete_characteristics
)


def test_create_and_get_characteristics(session):
    characteristic = create_characteristics(session, name='Minimo', color='#ff0000')

    assert characteristic.id is not None
    assert characteristic.name == 'Minimo'

    found = get_characteristics_by_id(session, characteristic.id)
    assert found is not None
    assert found.color == '#ff0000'

def test_get_characteristics_by_name(session):
    characteristic = create_characteristics(session, name='Minimo', color='#ff0000')
    found = get_characteristics_by_name(session, name='Minimo')
    assert found is not None
    assert found.name == 'Minimo'

def test_get_all_characteristics(session):
    create_characteristics(session, name='Optativo', color='#ffff00')
    create_characteristics(session, name='Minimo', color='#ff0000')
    characteristics = get_all_characteristics(session)
    assert len(characteristics) == 2

def test_update_characteristics(session):
    characteristic = create_characteristics(session, name='Minimo', color='#ff0000')
    updated = update_characteristics(session, characteristic.id, color='#ffff00')
    assert updated.color == '#ffff00'

def test_delete_course(session):
    characteristic = create_characteristics(session, name='Minimo', color='#ff0000')
    deleted = delete_characteristics(session, characteristic.id)
    assert deleted is True

    found = get_characteristics_by_id(session, characteristic.id)
    assert found is None
