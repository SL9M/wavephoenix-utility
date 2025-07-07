import sys
import os
import platform

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

def clearLayout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()
        elif item.layout():
            clearLayout(item.layout())