import sys
from PySide6.QtWidgets import QApplication
from views.register import MainWindow
from db.controllers.user_controller import UserMainController
from db.base import SessionLocal
from db.init_db import init_db

def main():
    init_db()

    app = QApplication(sys.argv)

    session = SessionLocal()

    user_controller = UserMainController(session)

    window = MainWindow()

    window.signal_send_name.connect(user_controller.create_user)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
