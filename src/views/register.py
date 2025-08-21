from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QApplication
from PySide6.QtCore import Signal, Qt
from sys import exit

class MainWindow(QMainWindow):
    signal_send_name = Signal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.resize(600, 600)
        self.center()

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        self.label_welcome = QLabel(
            "Bienvenido a PlannerUC.\nPor favor ingresa tu nombre para referirnos a ti correctamente.\n"
            "Recuerda que este Planner es no oficial, por lo que el PPA o los créditos que aparecen pueden "
            "no ser los que aparecen en PortalUC."
        )
        self.label_welcome.setWordWrap(True)

        self.label_welcome.setAlignment(Qt.AlignCenter)

        self.user_name = QLineEdit()
        self.user_name.setPlaceholderText("Ingrese su nombre")

        btn_send = QPushButton('Enviar')
        btn_send.clicked.connect(self.send_name)

        btn_close = QPushButton('Salir')
        btn_close.clicked.connect(self.close_window)

        main_layout.addWidget(self.label_welcome)
        main_layout.addWidget(self.user_name)
        main_layout.addWidget(btn_send)
        main_layout.addWidget(btn_close)

    def center(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        x = (screen_geometry.width() - window_geometry.width()) // 2
        y = (screen_geometry.height() - window_geometry.height()) // 2
        self.move(x, y)

    def send_name(self):
        name = self.user_name.text().strip()
        if name:
            self.signal_send_name.emit(name)
        else:
            self.label_welcome.setText(
                "No se puede ingresar un nombre vacío"
            )

    def close_window(self):
        exit()
