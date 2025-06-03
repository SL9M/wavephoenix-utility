from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

# Initialize application and main window with layout
app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

window.setWindowTitle("WavePhoenix Utility")
label = QLabel("Get Started. (Hello World)")

# Finalize GUI setup and run the app
layout.addWidget(label)
window.setLayout(layout)
window.resize(900, 600)
window.show()
app.exec()

