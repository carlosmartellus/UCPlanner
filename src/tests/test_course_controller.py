import pytest
from db.controllers.course_controller import (
    create_course, get_course_by_id, get_all_courses,
    get_course_by_code, get_course_by, update_course, delete_course
)


def test_create_and_get_course(session):
    course = create_course(session, code="INF123", name="Algoritmos", nrc=1001, credits=10)

    assert course.id is not None
    assert course.name == "Algoritmos"

    found = get_course_by_id(session, course.id)
    assert found is not None
    assert found.code == "INF123"

def test_get_course_by_code(session):
    course = create_course(session, code="MAT001", name="Álgebra", nrc=2001, credits=8)
    found = get_course_by_code(session, "MAT001")
    assert found is not None
    assert found.name == "Álgebra"

def test_get_all_courses(session):
    create_course(session, code="CS101", name="Intro Comp", nrc=3001, credits=6)
    create_course(session, code="CS102", name="POO", nrc=3002, credits=6)
    courses = get_all_courses(session)
    assert len(courses) == 2

def test_get_course_by_filters(session):
    create_course(session, code="FIS101", name="Física I", nrc=4001, credits=7, area="Ciencias")
    create_course(session, code="FIS102", name="Física II", nrc=4002, credits=7, area="Ciencias")

    results = get_course_by(session, name="Física")
    assert len(results) == 2

    results = get_course_by(session, code="FIS101")
    assert len(results) == 1
    assert results[0].name == "Física I"

def test_update_course(session):
    course = create_course(session, code="HIS101", name="Historia", nrc=5001, credits=5)
    updated = update_course(session, course.id, name="Historia Universal", credits=6)
    assert updated.name == "Historia Universal"
    assert updated.credits == 6

def test_delete_course(session):
    course = create_course(session, code="BIO101", name="Biología", nrc=6001, credits=5)
    deleted = delete_course(session, course.id)
    assert deleted is True

    found = get_course_by_id(session, course.id)
    assert found is None
