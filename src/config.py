import sys
import os

# Default bundled openocd path logic
if getattr(sys, 'frozen', False):  # PyInstaller
    base_dir = sys._MEIPASS
else:  # Python script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

#Default global variables
openocdpath = os.path.join(base_dir, "openocd", "bin", "openocd.exe")
bootloaderpath = ""
receiverpath = ""