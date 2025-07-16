from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy
import src.config
import time
from src.config import clearLayout, getLogOutput, createOCDworker

def step3(window, layout):

    logOutput=getLogOutput()

    # Step 3 variables
    step3title= QLabel("Step 3: Flash Bootloader & Firmware")
    step3title.setStyleSheet("font-size:20px; font-weight:bold;")
    step3instructions = QLabel('Reconnect your WavePhoenix, click "Flash Device," then your device will be ready!')
    step3instructions.setWordWrap(True)
    step3instructions.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    
    bootloaderButton = QPushButton("Flash Device")
    # Next Button
    backHomeButton = QPushButton("Back Home >")

    def runOCDcommand():
        bootloaderOCDCommand = [
            src.config.openocdpath,
            "-f", "interface\\cmsis-dap.cfg",
            "-c", "transport select swd",
            "-f", "target\\efm32s2.cfg",
            "-c", f'init; halt; flash write_image erase "{src.config.bootloaderpath}"; exit'
        ]
        bootloaderOCDSuccessMessage = ('<p style="font-size:20px;"><b>Successful bootloader flash!</b></p><p>You can proceed to the next step.</p>')
        
        firmwareOCDCommand = [
            src.config.openocdpath,
            "-f", "interface\\cmsis-dap.cfg",
            "-c", "transport select swd",
            "-f", "target\\efm32s2.cfg",
            "-c", f'init; halt; flash write_image erase "{src.config.receiverpath}"; exit'
        ]
        OCDErrorMessage = ('<p style="font-size:20px;"><b>Device flash error</b></p><p>Check your USB connection, and file paths. If that doesn not work, try restarting the process.</p>')
        OCDSuccessMessage = ('<p style="font-size:20px;"><b>Successful bootloader & firmware flash!</b></p><p>The bootloader and firmware flashed with no errors. You can test pairing using the test feature. You are ready to assemble!</p>')


        createOCDworker([bootloaderOCDCommand, firmwareOCDCommand], OCDSuccessMessage, OCDErrorMessage, window, commandDelay=2)

    # Create layout
    layout.addWidget(step3title)
    layout.addWidget(step3instructions)

    layout.addWidget(logOutput)
    
    layout.addWidget (bootloaderButton)
    bootloaderButton.setFixedHeight(35)
    bootloaderButton.clicked.connect(runOCDcommand)
    layout.addSpacing(40)

    # Go home if button is pressed
    def go_to_step1():
        from src.step1 import step1
        clearLayout(layout)
        step1(window,layout)
    layout.addWidget(backHomeButton)
    backHomeButton.setFixedHeight(35)
    backHomeButton.clicked.connect(go_to_step1)