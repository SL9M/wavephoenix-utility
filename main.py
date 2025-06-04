from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon

# Handle resource path for packaged app
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




# Window Content
window.setWindowTitle("Upload Files - WavePhoenix Utility")
layout.addWidget(QLabel("First we need to download a few things."))
layout.addWidget(QPushButton("Get Started"))




# Finalize GUI and run the app
window.setLayout(layout)
window.resize(600, 300)
window.show()
app.exec()