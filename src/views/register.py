from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from PySide6.QtCore import Signal
from re import fullmatch

class RegisterWindow(QWidget):
    signal_send_name = Signal(str)
    signal_back_to_menu = Signal()
    signal_open_degrees = Signal(dict)


    def __init__(self):
        super().__init__()
        self.setWindowTitle('Registro')

        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.top_label = QLabel('Cualquier información entregada no será publicada')
        layout.addWidget(self.top_label)

        self.input_name = QLineEdit()
        self.input_name.setPlaceholderText('Ingrese su nombre')
        layout.addWidget(self.input_name)

        btn_send = QPushButton('Enviar')
        btn_send.clicked.connect(self.on_send)
        layout.addWidget(btn_send)

        btn_back = QPushButton('Volver al menú')
        btn_back.clicked.connect(lambda: self.signal_back_to_menu.emit())
        layout.addWidget(btn_back)

    def on_send(self):
        name = self.input_name.text().strip()
        if name:
            if fullmatch(r'[A-Za-z0-9_\- ]+', name):
                self.signal_send_name.emit(name)

            else:
                self.top_label.setText(
                    'Nombre inválido: solo se permiten letras, números, guiones y guiones bajos'
                )
        else:
            self.top_label.setText('No se puede ingresar un nombre en blanco')
    
    def handle_user_signal(self, data):
        if 'error' in data:
            self.top_label.setText(data['error'])
        else:
            self.signal_open_degrees.emit(data['name'], data['id'])

