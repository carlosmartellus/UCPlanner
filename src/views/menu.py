from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QApplication

class MenuWindow(QWidget):
    signal_open_register = Signal()
    signal_exit_app = Signal()
    signal_open_login = Signal()
    signal_open_config = Signal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu')

        layout = QVBoxLayout(self)
        label = QLabel('Bienvenido a PlannerUC')
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        # Register
        btn_register = QPushButton('Registrarse')
        btn_register.clicked.connect(lambda: self.signal_open_register.emit())
        layout.addWidget(btn_register)

        # Login
        btn_login = QPushButton('Login')
        btn_login.clicked.connect(lambda: self.signal_open_login.emit())
        layout.addWidget(btn_login)

        # Config
        btn_config = QPushButton('Config')
        btn_config.clicked.connect(lambda: self.signal_open_config.emit())
        layout.addWidget(btn_config)

        # Exit
        btn_exit = QPushButton('Salir')
        btn_exit.clicked.connect(lambda: self.signal_exit_app.emit())
        layout.addWidget(btn_exit)
