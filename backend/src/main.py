from .db.models.user import User
from .controllers.user_controller import UserMainController
from .db.base import Base, engine


def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database initialized!")

if __name__ == "__main__":
    init_db()
    print("Backend listo para usar")
