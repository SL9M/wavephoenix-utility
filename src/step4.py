from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy
import src.config
from src.config import clearLayout, createOCDworker, getLogOutput

def step4(window,layout):

    logOutput=getLogOutput()

    # Step 4 variables
    step4title= QLabel("Step 4: Flash Firmware")
    step4title.setStyleSheet("font-size:20px; font-weight:bold;")
    step4instructions = QLabel('This is the last step. Click "Flash Firmware" then your WavePhoenix will be ready!')
    step4instructions.setWordWrap(True)
    step4instructions.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

    firmwareButton = QPushButton("Flash Firmware")
    #Back button
    backGatherButton = QPushButton("Back Home")

    def runOCDcommand():
        ocdCommand = [
            src.config.openocdpath,
            "-f", "interface\\cmsis-dap.cfg",
            "-c", "transport select swd",
            "-f", "target\\efm32s2.cfg",
            "-c", f'init; halt; flash write_image erase "{src.config.receiverpath}"; exit'
        ]
        OCDErrorMessage = ('<p style="color:red; font-size:20px;"><b>Firmware flash error</b></p><p>Check your USB connection, and file paths. If that doesn not work, try restarting the whole process.</p>')
        OCDSuccessMessage = ('<p style="color:#007aff; font-size:20px;"><b>Successful firmware flash!</b></p><p>The firmware flashed with no errors. You can test pairing using the test feature. Otherwise you are ready to assemble!</p>')
        createOCDworker(ocdCommand, OCDSuccessMessage, OCDErrorMessage, window)

    # Create layout
    layout.addWidget(step4title)
    layout.addWidget(step4instructions)

    layout.addWidget(logOutput)
    
    layout.addWidget (firmwareButton)
    firmwareButton.setFixedHeight(35)
    firmwareButton.clicked.connect(runOCDcommand)
    layout.addSpacing(40)


    # Back to step1 if button is pressed
    def go_to_step1():
        from src.step1 import step1
        clearLayout(layout)
        step1(window,layout)
    layout.addWidget(backGatherButton)
    backGatherButton.setFixedHeight(35)
    backGatherButton.clicked.connect(go_to_step1)