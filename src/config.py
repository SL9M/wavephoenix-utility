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
    openocdpath = os.path.join(base_dir, "openocd", "bin", "openocd")
#macOS
elif system == "Darwin":
    openocdpath = os.path.join(base_dir, "openocd", "bin", "openocd")
#Windows
else:  
    openocdpath = os.path.join(base_dir, "openocd", "bin", "openocd.exe")

bootloaderpath = ""
receiverpath = ""
logOutput = None
probeTypeSelected = "CMSIS-DAP (RPI Pico, Default)"

def probe_type_changed(selection):
    global probeTypeSelected
    probeTypeSelected = selection

def getLogOutput():
    global logOutput
    if logOutput is None:
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


#OpenOCD thread worker
class OCDWorker(QThread):
    finished_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def __init__(self, commands, commandDelay=0):
        super().__init__()
        # Acceps a single (list[str]) or multiple (list[list[str]])
        if isinstance(commands[0], str):
            self.commands = [commands]
        else:
            self.commands = commands
        self.commandDelay = commandDelay

    def run(self):
        errorLog = []
        successOutput = []
        try:
            for i, cmd in enumerate(self.commands):
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
                    combined_output = result.stdout + "\n" + result.stderr
                    successOutput.append(combined_output)
                except subprocess.CalledProcessError as e:
                    errorLog.append(e.stderr)
                    break

                if i < len(self.commands) - 1 and self.commandDelay > 0:
                    self.msleep(int(self.commandDelay * 1000))

            if errorLog:
                combined_errors = "\n\n".join(errorLog)
                self.error_signal.emit(combined_errors)
            else:
                combined_output = "\n\n".join(successOutput)
                self.finished_signal.emit(combined_output)

        except Exception as e:
            self.error_signal.emit(str(e))

def createOCDworker(ocdCommand, OCDSuccessMessage, OCDErrorMessage, window=None, commandDelay=0):
    worker = OCDWorker(ocdCommand, commandDelay)

    getLogOutput().append("<b>Running OpenOCD...</b>")
    def on_success(output):
        getLogOutput().append('<p>' + output.replace('\n', '<br>') + '</p>' + OCDSuccessMessage)

    def on_error(err):
        getLogOutput().append('<p>' + err.replace('\n', '<br>') + '</p>' + OCDErrorMessage)

    def on_finish():
        if window:
            window.worker = None
            window.raise_()
            window.activateWindow()

    worker.finished_signal.connect(on_success)
    worker.error_signal.connect(on_error)
    worker.finished.connect(on_finish)
    if window:
        window.worker = worker
    worker.start()
