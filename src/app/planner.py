from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from db.base import SessionLocal
from db.init_db import init_db
from views.register import RegisterWindow
from views.menu import MenuWindow
from views.login import LoginWindow
from db.controllers.user_controller import UserMainController
from src.utils.center import center
import sys

class PlannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PlannerUC')
        self.resize(600, 600)
        center(self)

        # Initialize DB
        init_db()
        self.session = SessionLocal()

        # Initialize Controllers
        self.user_controller = UserMainController(self.session)

        # Window Stack
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Views
        self.menu_page = MenuWindow()
        self.register_page = RegisterWindow()
        self.login_page = LoginWindow()

        # Add windows to stack
        self.stack.addWidget(self.menu_page)
        self.stack.addWidget(self.register_page)
        self.stack.addWidget(self.login_page)
        self.stack.setCurrentWidget(self.menu_page)

        # Conections
        self.menu_page.signal_open_register.connect(self.show_register)
        self.menu_page.signal_open_login.connect(self.show_login)
        self.menu_page.signal_exit_app.connect(self.close)

        self.register_page.signal_send_name.connect(self.user_controller.create_user)
        self.register_page.signal_back_to_menu.connect(self.show_menu)

        self.login_page.signal_back_to_menu.connect(self.show_menu)
        self.login_page.signal_get_users.connect(self.user_controller.get_all_users)

        self.user_controller.signal_send_users.connect(self.login_page.get_users)

    def show_register(self):
        self.stack.setCurrentWidget(self.register_page)

    def show_menu(self):
        self.stack.setCurrentWidget(self.menu_page)

    def show_login(self):
        self.stack.setCurrentWidget(self.login_page)
        self.login_page.signal_get_users.emit()


