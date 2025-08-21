from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from db.base import SessionLocal
from db.init_db import init_db
from views.menu import MenuWindow
from views.register import RegisterWindow
from views.login import LoginWindow
from views.degree import DegreeWindow
from db.controllers.user_controller import UserMainController
from db.controllers.degree_controller import DegreeMainController
from src.utils.center import center

class PlannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PlannerUC')
        self.resize(600, 600)
        center(self)

        init_db()
        self.session = SessionLocal()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.menu_page = MenuWindow()
        self.register_page = RegisterWindow()
        self.login_page = LoginWindow()
        self.degree_page = DegreeWindow(user={'user_name': '', 'user_id': 0})

        self.user_controller = UserMainController(self.session)
        self.degree_controller = DegreeMainController(self.session)

        for page in [self.menu_page, self.register_page, self.login_page, self.degree_page]:
            self.stack.addWidget(page)

        # Connections Menu Page
        self.menu_page.signal_open_register.connect(self.show_register)
        self.menu_page.signal_open_login.connect(self.show_login)
        self.menu_page.signal_exit_app.connect(self.close)

        self.register_page.signal_back_to_menu.connect(self.show_menu)
        self.register_page.signal_send_name.connect(self.user_controller.create_user)
        self.register_page.signal_open_degrees.connect(self.show_degree)
        
        # Connections Login Page
        self.login_page.signal_back_to_menu.connect(self.show_menu)
        self.login_page.signal_get_users.connect(self.user_controller.get_all_users)
        self.login_page.signal_open_degrees.connect(self.show_degree)

        # Connections User Controller
        self.user_controller.signal_send_users.connect(self.login_page.get_users)
        self.user_controller.signal_send_user.connect(self.register_page.handle_user_signal)

        # Connections Degree Page
        self.degree_page.signal_back_to_menu.connect(self.show_menu)
        self.degree_page.signal_create_new_degree.connect(self.degree_controller.create_degree)


        self.stack.setCurrentWidget(self.menu_page)

    def show_menu(self):
        self.stack.setCurrentWidget(self.menu_page)

    def show_register(self):
        self.stack.setCurrentWidget(self.register_page)

    def show_login(self):
        self.login_page.signal_get_users.emit()
        self.stack.setCurrentWidget(self.login_page)

    def show_degree(self, user: dict[str, int]):
        self.degree_page.user = user
        self.stack.setCurrentWidget(self.degree_page)

