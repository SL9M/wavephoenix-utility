from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy, QApplication
import src.config
from src.config import getLogOutput, createOCDworker

def proLayout(layout, window):

    logOutput=getLogOutput()
    #Variables
    proLayoutTitle= QLabel("WIP Advanced Layout")
    proLayoutTitle.setStyleSheet("font-size:20px; font-weight:bold;")
    proLayoutInstructions = QLabel('Test')
    proLayoutInstructions.setWordWrap(True)
    proLayoutInstructions.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

    eraseButton = QPushButton("Erase Device")

    def runEraseCommand():
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
    layout.addWidget(proLayoutTitle)
    layout.addWidget(proLayoutInstructions)

    layout.addWidget(logOutput)

    layout.addWidget (eraseButton)
    eraseButton.setFixedHeight(35)
    eraseButton.clicked.connect(runEraseCommand)

    layout.addSpacing(40)    

    window.setMinimumWidth(600)
    window.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)    
    layout.invalidate()
    layout.activate()
    window.adjustSize()
    window.repaint()