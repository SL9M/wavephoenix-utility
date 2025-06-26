from PyQt6.QtWidgets import  QLabel, QPushButton
from src.config import openocdpath
import subprocess

def step4(layout):

    # Step 4 variables
    step4title= QLabel("Step 4: Flash Firmware")
    step4title.setStyleSheet("font-size:20px; font-weight:bold;")
    step4instructions = QLabel('This is the last step. Click "Flash Firmware" then you should be able to pair a controller by pressing X+Y.')
    firmwareButton = QPushButton("Flash Firmware")

    def flash_firmware():
        try:
            firmwareCommand = [
                openocdpath,
                "-f", "interface\\cmsis-dap.cfg",
                "-c", "transport select swd",
                "-f", "target\\efm32s2.cfg",
                "-c", "init; halt; flash write_image erase receiver.hex; exit"
            ]
            firmwarerResult = subprocess.run(firmwareCommand, capture_output=True, text=True, check=True)
            print("Flash Firmware Success\n",firmwarerResult.stdout)
        except subprocess.CalledProcessError as firmwareError:
            print("Flash Firmware Error\n", firmwareError.stderr)

    # Create layout
    layout.addWidget(step4title)
    layout.addWidget(step4instructions)
    layout.addWidget (firmwareButton)
    firmwareButton.clicked.connect(flash_firmware)