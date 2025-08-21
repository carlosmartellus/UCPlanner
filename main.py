import sys
from PySide6.QtWidgets import QApplication
from src.app.planner import PlannerApp

def main():
    app = QApplication(sys.argv)
    window = PlannerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
