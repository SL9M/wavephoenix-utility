from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PyQt6.QtGui import QMovie

# Initialize application and main window with layout
app = QApplication([])
window = QWidget()
background = QLabel(window)
layout = QVBoxLayout()
# Initialize UI Componenets
layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
window.setWindowTitle("Upload Files - WavePhoenix Utility")
label = QLabel("Get Started. (Hello World)")
start_button_home = QPushButton("Get Started")
start_button_home.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)






# Window Content
layout.addWidget(label)
layout.addWidget(start_button_home)
window.setLayout(layout)





# Finalize GUI and run the app
window.resize(300, 100)
window.show()
app.exec()

