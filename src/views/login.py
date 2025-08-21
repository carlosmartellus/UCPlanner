from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal, Qt

class LoginWindow(QWidget):
    signal_back_to_menu = Signal()
    signal_get_users = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(QLabel('Usuarios registrados:'))

        self.users_container = QVBoxLayout()
        self.main_layout.addLayout(self.users_container)
        self.main_layout.addStretch(3)

        btn_back = QPushButton('Volver al menú')
        btn_back.clicked.connect(lambda: self.signal_back_to_menu.emit())
        self.main_layout.addWidget(btn_back)

    def get_users(self, users: list[dict]):
        for i in reversed(range(self.users_container.count())):
            widget = self.users_container.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for user in users:
            btn_user = QPushButton(user['name'])
            self.users_container.addWidget(btn_user)
