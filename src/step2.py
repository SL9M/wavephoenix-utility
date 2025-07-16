from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy, QApplication
import src.config
from src.step3 import step3
from src.config import clearLayout, getLogOutput, createOCDworker

def step2(layout, window):

    logOutput=getLogOutput()
    # Step 2 variables
    step2title= QLabel("Step 2: Erase Device")
    step2title.setStyleSheet("font-size:20px; font-weight:bold;")
    step2instructions = QLabel('Plug in the WavePhoenix you would like to flash, then click "Erase"')
    step2instructions.setWordWrap(True)
    step2instructions.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

    eraseButton = QPushButton("Erase Device")
    # Next Button
    nextbootloaderButton = QPushButton("Next Step >")

    def runOCDcommand():
        ocdCommand = [
            src.config.openocdpath,
            "-f", "interface\\cmsis-dap.cfg",
            "-f", "target\\efm32s2.cfg",
            "-c", "init; efm32s2_dci_device_erase; shutdown"
        ]
        OCDErrorMessage = ('<p style="font-size:20px;"><b>Erase error</b></p><p><b>Make sure you device is plugged in. If your device already has a firmware then you need to put it in bootloader mode by hold the pairing button for 3 seconds.</b></p>')
        OCDSuccessMessage = ('<p style="font-size:20px;"><b>Erase success!</b></p><p><b>Unplug your probe from USB and proceed to next step.</b></p>')
        createOCDworker(ocdCommand, OCDSuccessMessage, OCDErrorMessage, window)
       

    # Create layout
    layout.addWidget(step2title)
    layout.addWidget(step2instructions)

    layout.addWidget(logOutput)

    layout.addWidget (eraseButton)
    eraseButton.setFixedHeight(35)
    eraseButton.clicked.connect(runOCDcommand)

    layout.addSpacing(40)    

    layout.addWidget(nextbootloaderButton)
    nextbootloaderButton.setFixedHeight(35)

    window.setMinimumWidth(500)
    window.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)    
    layout.invalidate()
    layout.activate()
    window.adjustSize()
    window.repaint()

    # Proceed to step3 if button is pressed
    def go_to_step3():
        clearLayout(layout)
        step3(window,layout)
    nextbootloaderButton.clicked.connect(go_to_step3)