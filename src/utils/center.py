from PySide6.QtWidgets import QApplication, QWidget

def center(window: QWidget) -> None:
    """Centers a window"""
    screen_geometry = QApplication.primaryScreen().availableGeometry()
    window_geometry = window.frameGeometry()
    x = (screen_geometry.width() - window_geometry.width()) // 2
    y = (screen_geometry.height() - window_geometry.height()) // 2
    window.move(x, y)
