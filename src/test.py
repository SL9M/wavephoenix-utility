from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy
import src.config
import os
import subprocess
from src.config import createOCDworker, getLogOutput, clearLayout

def testPhoenix(window,layout):

    logOutput=getLogOutput()
    # Test phoenix variables
    testphoenixtitle= QLabel("Test Your Device")
    testphoenixtitle.setStyleSheet("font-size:20px; font-weight:bold;")
    testphoenixinstructions = QLabel('Unplug and plug back in your WavePhoenix. Click "Test Device" sending this command will allow it to function while connected to the probe.')
    testphoenixinstructions.setStyleSheet("padding-bottom:1px;")
    testphoenixinstructions.setWordWrap(True)    
    testphoenixinstructions.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.MinimumExpanding)

    readmemoryButton = QPushButton("Test Device")
    readmemoryButton.setStyleSheet("""
        QPushButton {
            background-color: #007aff;
            color: white;
        }
        QPushButton:hover {
            background-color: #005bb5;
        }
        QPushButton:pressed {
            background-color: #003e85;
        }
    """)
    #Back button
    backGatherButton = QPushButton("Back Home >")


    def runOCDcommand():
        ocdCommand = [
            src.config.openocdpath,
            "-f", os.path.normpath("interface/cmsis-dap.cfg"),
            "-c", "transport select swd",
            "-f", os.path.normpath("target/efm32s2.cfg"),
            "-c", "init; reset init; exit"
        ]
        OCDErrorMessage = ("<p style='font-size:20px;'><b>Command sent! Try pressing the pair button, if it blinks you're ready to assemble!</b></p>")
        OCDSuccessMessage = ('<p style="font-size:20px;"><b>Device appears to be blank or in bootloader mode. Try power cycling or re-flashing.</b></p>')
        createOCDworker(ocdCommand, OCDSuccessMessage, OCDErrorMessage, window)
       

    # Create layout
    layout.addWidget(testphoenixtitle)
    layout.addWidget(testphoenixinstructions)

    layout.addWidget(logOutput)
    layout.addSpacing(10)

    layout.addWidget (readmemoryButton)
    readmemoryButton.setFixedHeight(35)
    readmemoryButton.clicked.connect(runOCDcommand)
    layout.addSpacing(30)

    window.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    layout.invalidate()
    layout.activate()
    window.adjustSize()
    window.repaint()

    # Back to step1 if button is pressed
    def go_to_step1():
        from src.step1 import step1
        clearLayout(layout)
        step1(window,layout)
    layout.addWidget(backGatherButton)
    backGatherButton.setFixedHeight(35)
    backGatherButton.clicked.connect(go_to_step1)