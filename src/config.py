from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import QThread, pyqtSignal
import sys
import os
import platform
import subprocess

# Default bundled openocd path logic
if getattr(sys, 'frozen', False):  # PyInstaller
    base_dir = sys._MEIPASS
else:  # Python script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

#Default global variables
system = platform.system()
#Linux
if system == "Linux":
    openocdpath = os.path.join(base_dir, "openocd", "openocd", "bin", "openocd")
#macOS
elif system == "Darwin":
    openocdpath = os.path.join(base_dir, "openocd", "bin", "openocd")
#Windows
else:  
    openocdpath = os.path.join(base_dir, "openocd", "bin", "openocd.exe")

bootloaderpath = ""
receiverpath = ""
logOutput = None

def getLogOutput():
    global logOutput
    if logOutput is None or sip.isdeleted(logOutput):
        logOutput = QTextEdit()
        logOutput.setPlainText("")
        logOutput.setReadOnly(True)
        logOutput.setMinimumHeight(300)
    return logOutput

def clearLayout(layout):
    global logOutput
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            if item.widget() is logOutput:
                logOutput = None
            item.widget().deleteLater()
        elif item.layout():
            clearLayout(item.layout())

class EraseWorker(QThread):
    finished_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            result = subprocess.run(self.command, capture_output=True, text=True, check=True)
            self.finished_signal.emit(result.stdout)
        except subprocess.CalledProcessError as e:
            self.error_signal.emit(e.stderr)