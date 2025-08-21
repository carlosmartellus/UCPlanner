from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel,
    QHBoxLayout, QGridLayout, QApplication, QLineEdit
)
from PySide6.QtCore import Signal, Qt
import sys


class Curriculum(QWidget):
    signal_back_to_menu = Signal()
    signal_get_degrees = Signal(int)
    signal_create_new_degree = Signal(str, str, int)
    signal_add_user_degree = Signal(int, int)

    def __init__(self, degree: dict):
        super().__init__()
        self.user = degree
        self.setWindowTitle('Carreras')

        print('[DEBUG] Curriculum for degree ', degree)

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        layout_courses = QHBoxLayout()

        layout_create_courses = QVBoxLayout()

        course_code = QLineEdit()
        course_code.setPlaceholderText('Sigla')

        course_name = QLineEdit()
        course_name.setPlaceholderText('Nombre del curso')

        course_nrc = QLineEdit()
        course_nrc.setPlaceholderText('NRC')

        course_credits = QLineEdit()
        course_credits.setPlaceholderText('Créditos')

        course_area = QLineEdit()
        course_area.setPlaceholderText('Área de OFG (Nulo si no es OFG)')

        layout_create_courses.addWidget(course_code)
        layout_create_courses.addWidget(course_name)
        layout_create_courses.addWidget(course_nrc)
        layout_create_courses.addWidget(course_credits)
        layout_create_courses.addWidget(course_area)

        self.btn_create_course = QPushButton('Crear Curso')
        layout_create_courses.addWidget(self.btn_create_course)

        self.container_courses = QWidget()
        self.courses_layout = QGridLayout(self.container_courses)

        # Courses as example

        courses = [
            'Matemáticas I', 'Física I', 'Química',
            'Álgebra Lineal', 'Programación', 'Estructuras de Datos',
            'Bases de Datos', 'Redes', 'Compiladores'
        ]

        for i, curso in enumerate(courses):
            fila = i // 3
            col = i % 3
            self.courses_layout.addWidget(QPushButton(curso), fila, col)

        layout_courses.addLayout(layout_create_courses, 1)
        layout_courses.addWidget(self.container_courses, 3)

        self.main_layout.addLayout(layout_courses)

        options_layout = QHBoxLayout()
        btn_schedule = QPushButton('Horario')
        info_label = QLabel('PPA\tCréditos\n7\t50/405')
        btn_calendar = QPushButton('Calendario')
        options_layout.addWidget(btn_schedule)
        options_layout.addWidget(info_label, alignment=Qt.AlignmentFlag.AlignCenter)
        options_layout.addWidget(btn_calendar)

        self.main_layout.addLayout(options_layout)

