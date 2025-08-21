from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QScrollArea,
    QHBoxLayout, QLineEdit
)
from PySide6.QtCore import Signal, Qt

class DegreeWindow(QWidget):
    signal_back_to_menu = Signal()
    signal_get_degrees = Signal()
    signal_create_new_degree = Signal(str, str, int)
    signal_add_user_degree = Signal(int, int)

    def __init__(self, user: dict):
        super().__init__()
        self.user = user
        self.setWindowTitle('Carreras')
        self.resize(500, 500)

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.main_layout.addWidget(QLabel(f'Carreras registradas para el usuario {self.user['user_name']}:' ))

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.degree_container_widget = QWidget()
        self.degree_container_layout = QVBoxLayout(self.degree_container_widget)
        self.scroll_area.setWidget(self.degree_container_widget)
        self.main_layout.addWidget(self.scroll_area)

        self.new_degree_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText('Nombre')
        self.school_input = QLineEdit()
        self.school_input.setPlaceholderText('Escuela')
        self.credits_input = QLineEdit()
        self.credits_input.setPlaceholderText('Créditos')

        self.new_degree_layout.addWidget(self.name_input)
        self.new_degree_layout.addWidget(self.school_input)
        self.new_degree_layout.addWidget(self.credits_input)
        self.main_layout.addLayout(self.new_degree_layout)

        self.btn_create_degree = QPushButton('Crear Carrera')
        self.btn_create_degree.clicked.connect(self.create_new_degree)
        self.main_layout.addWidget(self.btn_create_degree)

        self.btn_back = QPushButton('Volver al menú')
        self.btn_back.clicked.connect(lambda: self.signal_back_to_menu.emit())
        self.main_layout.addWidget(self.btn_back)

        self.degree_buttons = {}


    def create_new_degree(self):
        name = self.name_input.text().strip()
        school = self.school_input.text().strip()
        credits = self.credits_input.text().strip()
        if name and school and credits:
            print(f'[DEBUG] Args: ({name}, {school}, {credits})')
            self.signal_create_new_degree.emit(name, school, int(credits))
        else:
            print('Todos los campos son obligatorios')
    
    def add_user_degree(self, degree: dict):
        print(f'[DEBUG] Adding {self.user} to {degree}')
        self.signal_add_user_degree.emit(degree['id'], self.user['id'])
