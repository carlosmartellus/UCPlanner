from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal

class LoginWindow(QWidget):
    signal_back_to_menu = Signal()
    signal_get_users = Signal()
    signal_open_degrees = Signal(dict)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.signal_get_users.emit()

        self.users: dict[str, int] = {}

        main_layout = QVBoxLayout(self)

        main_layout.addWidget(QLabel('Usuarios registrados:'))

        self.users_container_widget = QWidget()
        self.users_container_layout = QVBoxLayout(self.users_container_widget)
        main_layout.addWidget(self.users_container_widget)

        btn_back = QPushButton('Volver al menú')
        btn_back.clicked.connect(lambda: self.signal_back_to_menu.emit())
        main_layout.addWidget(btn_back)

    def get_users(self, users: list[dict]):
        for i in reversed(range(self.users_container_layout.count())):
            widget = self.users_container_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        for user in users:
            self.users[user['name']] = user['id']
            btn_user = QPushButton(user['name'])
            self.users_container_layout.addWidget(btn_user)

            btn_user.clicked.connect(lambda checked, name=user['name']: self.on_user_clicked(name))

            
        print('[DEBUG] Users in dictionary: ', self.users)
        self.users_container_layout.addStretch(1)

    def on_user_clicked(self, name: str):
        user_id = self.users[name]
        print(f'[DEBUG] Pressed button: name: {name}, ID: {user_id}')
        self.signal_open_degrees.emit({'name': name, 'id': user_id})
