from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys
import os

def mainWindow():
    #Handle Icon Path in exe build
    if getattr(sys, 'frozen', False):  # Check if running in a packaged app (frozen state)
        icon_path = os.path.join(sys._MEIPASS, 'resources', 'icon.ico')
    else:
        icon_path = 'resources/icon.ico'

    # Configure Main Window
    window = QWidget()
    window.setWindowTitle("WavePhoenix Utility")
    window.setWindowIcon(QIcon(icon_path))


    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    window.setLayout(layout)

    return window, layout, icon_path