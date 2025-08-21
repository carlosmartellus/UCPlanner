from sqlalchemy.orm import Session
from ..models.category import Category

def create_category(session: Session, name: str, weight: float) -> Category:
    category = Category(name=name, weight=weight)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def get_category_by_id(session: Session, category_id: int) -> Category | None:
    return session.query(Category).filter_by(id=category_id).first()

def get_all_categories(session: Session) -> list[Category]:
    return session.query(Category).all()

def update_category(session: Session, category_id: int, **kwargs) -> Category | None:
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        return None
    for key, value in kwargs.items():
        if hasattr(category, key):
            setattr(category, key, value)
    session.commit()
    session.refresh(category)
    return category

def delete_category(session: Session, category_id: int) -> bool:
    category = session.query(Category).filter_by(id=category_id).first()
    if not category:
        return False
    session.delete(category)
    session.commit()
    return True
