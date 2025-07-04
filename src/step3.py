from PyQt6.QtWidgets import  QLabel, QPushButton
import src.config
import subprocess
from src.step4 import step4

def step3(layout):

    # Step 3 variables
    step3title= QLabel("Step 3: Flash Bootloader")
    step3title.setStyleSheet("font-size:20px; font-weight:bold;")
    step3instructions = QLabel('Unplug and plug back in your WavePhoenix, then click "Flash Bootloader"')
    bootloaderButton = QPushButton("Flash Bootloader")
    # Next Button
    nextfirmwareButton = QPushButton("Next Step")

    def flash_bootloader():
        try:
            bootloaderCommand = [
                src.config.openocdpath,
                "-f", "interface\\cmsis-dap.cfg",
                "-c", "transport select swd",
                "-f", "target\\efm32s2.cfg",
                "-c", f'init; halt; flash write_image erase "{src.config.bootloaderpath}"; exit'
            ]
            print(bootloaderCommand)
            bootloaderResult = subprocess.run(bootloaderCommand, capture_output=True, text=True, check=True)
            print("Flash bootloader success\n",bootloaderResult.stdout)
        except subprocess.CalledProcessError as bootloaderError:
            print("Flash bootloader error\n", bootloaderError.stderr)

    # Create layout
    layout.addWidget(step3title)
    layout.addWidget(step3instructions)
    layout.addWidget (bootloaderButton)
    bootloaderButton.clicked.connect(flash_bootloader)
    layout.addSpacing(40)

    # Proceed to step4 if button is pressed
    def go_to_step4():
        while layout.count():
            clearEach = layout.takeAt(0)
            if clearEach.widget():
                clearEach.widget().deleteLater()
        
        step4(layout)
    layout.addWidget(nextfirmwareButton)
    nextfirmwareButton.clicked.connect(go_to_step4)