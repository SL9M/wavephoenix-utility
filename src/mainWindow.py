from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys
import os
import platform

def mainWindow():
    # Determine platform for icon
    if platform.system() == 'Darwin':
        icon_filename = 'icon.icns'
    else:
        icon_filename = 'icon.ico'

    # Pyscript or PyInstaller check
    if getattr(sys, 'frozen', False):  # Running from PyInstaller
        icon_path = os.path.join(sys._MEIPASS, 'resources', icon_filename)
    else:
        icon_path = os.path.join('resources', icon_filename)

    # Configure Main Window
    window = QWidget()
    window.setWindowTitle("WavePhoenix Utility")
    window.setWindowIcon(QIcon(icon_path))


    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    window.setLayout(layout)

    return window, layout, icon_path