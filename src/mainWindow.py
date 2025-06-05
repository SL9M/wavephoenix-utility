def mainWindow():
    from PyQt6.QtCore import Qt
    from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
    from PyQt6.QtGui import QIcon
    import sys
    import os

    # Handle icon path for compiled apps
    if getattr(sys, 'frozen', False):  # Check if running in a packaged app (frozen state)
        icon_path = os.path.join(sys._MEIPASS, 'resources', 'icon.ico')
    else:
        icon_path = 'resources/icon.ico'

    # Initialize application and main window with layout
    app = QApplication([])
    app.setWindowIcon(QIcon(icon_path)) # Set App icon
    window = QWidget()
    layout = QVBoxLayout()
    # Initialize UI Componenets
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    window.setWindowIcon(QIcon(icon_path))

    return app, window, layout # Allow portable use of these functions

