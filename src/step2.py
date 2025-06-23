from PyQt6.QtWidgets import  QLabel, QFileDialog, QPushButton, QLineEdit
from src.config import openocdpath
import subprocess
#Step 2 - erase

def step2(layout):

    # Step 2 variables
    step2title= QLabel("Step 2: Erase Device")
    step2title.setStyleSheet("font-size:20px; font-weight:bold;")
    step2instructions = QLabel('Plug in the wavephoenix you would like to flash, then click "Erase"')
    eraseButton = QPushButton("Erase Device")

    def erase_device():
        try:
            eraseCommand = [
                openocdpath,
                "-f", "interface\\cmsis-dap.cfg",
                "-f", "target\\efm32s2.cfg",
                "-c", "init; efm32s2_dci_device_erase; shutdown"
            ]
            eraseResult = subprocess.run(eraseCommand, capture_output=True, text=True, check=True)
            print("Erase Success\n",eraseResult.stdout)
        except subprocess.CalledProcessError as eraseError:
            print("Erase Error\n", eraseError.stderr)

    # Create layout
    layout.addWidget(step2title)
    layout.addWidget(step2instructions)
    layout.addWidget (eraseButton)
    eraseButton.clicked.connect(erase_device)