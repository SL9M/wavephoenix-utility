import sys
import os

# Default openocd path
if getattr(sys, 'frozen', False):  # Running as a PyInstaller bundle
    base_dir = sys._MEIPASS
else:  # Running as a normal Python script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


openocdpath = os.path.join(base_dir, "openocd", "bin", "openocd.exe")