from src.step1 import step1
from src.mainWindow import mainWindow
from PyQt6.QtWidgets import  QApplication
from PyQt6.QtGui import QIcon

#Initialize App
app = QApplication([])
window, layout, icon_path = mainWindow()
app.setWindowIcon(QIcon(icon_path)) # Set App icon

# Start flashing process
step1(window, layout)

window.show()
app.exec()