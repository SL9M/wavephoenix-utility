from PyQt6.QtWidgets import  QLabel, QFileDialog, QPushButton, QLineEdit
from src.config import openocdpath
#Step 2 - erase

def step2(layout):

    step2title= QLabel("Step 2: Erase Device")
    step2title.setStyleSheet("font-size:20px; font-weight:bold;")
    layout.addWidget(step2title)