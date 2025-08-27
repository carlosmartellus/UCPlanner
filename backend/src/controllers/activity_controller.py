from sqlalchemy.orm import Session
from db.models.activity import Activity

def create_activity(session: Session, name: str, weight: float, category_id: int) -> Activity:
    activity = Activity(name=name, weight=weight, category_id=category_id)
    session.add(activity)
    session.commit()
    session.refresh(activity)
    return activity

def get_activity_by_id(session: Session, activity_id: int) -> Activity | None:
    return session.query(Activity).filter_by(id=activity_id).first()

def get_all_activities(session: Session) -> list[Activity]:
    return session.query(Activity).all()

def update_activity(session: Session, activity_id: int, **kwargs) -> Activity | None:
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if not activity:
        return None
    for key, value in kwargs.items():
        if hasattr(activity, key):
            setattr(activity, key, value)
    session.commit()
    session.refresh(activity)
    return activity

def delete_activity(session: Session, activity_id: int) -> bool:
    activity = session.query(Activity).filter_by(id=activity_id).first()
    if not activity:
        return False
    session.delete(activity)
    session.commit()
    return True
