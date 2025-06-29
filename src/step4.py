from PyQt6.QtWidgets import  QLabel, QPushButton
import src.config
import subprocess

def step4(layout):

    # Step 4 variables
    step4title= QLabel("Step 4: Flash Firmware")
    step4title.setStyleSheet("font-size:20px; font-weight:bold;")
    step4instructions = QLabel('This is the last step. Click "Flash Firmware" then you should be able to pair a controller by pressing X+Y.')
    firmwareButton = QPushButton("Flash Firmware")
    #Back button
    backGatherButton = QPushButton("Flash Another")


    def flash_firmware():
        try:
            firmwareCommand = [
                src.config.openocdpath,
                "-f", "interface\\cmsis-dap.cfg",
                "-c", "transport select swd",
                "-f", "target\\efm32s2.cfg",
                "-c", f'init; halt; flash write_image erase "{src.config.receiverpath}"; exit'
            ]
            print(firmwareCommand)
            firmwarerResult = subprocess.run(firmwareCommand, capture_output=True, text=True, check=True)
            print("Flash firmware success\n",firmwarerResult.stdout)
        except subprocess.CalledProcessError as firmwareError:
            print("Flash firmware error\n", firmwareError.stderr)

    # Create layout
    layout.addWidget(step4title)
    layout.addWidget(step4instructions)
    layout.addWidget (firmwareButton)
    firmwareButton.clicked.connect(flash_firmware)
    layout.addSpacing(40)


    # Back to step1 if button is pressed
    def go_to_step1():
        from src.step1 import step1
        while layout.count():
            clearEach = layout.takeAt(0)
            if clearEach.widget():
                clearEach.widget().deleteLater()
        
        step1(layout)
    layout.addWidget(backGatherButton)
    backGatherButton.clicked.connect(go_to_step1)