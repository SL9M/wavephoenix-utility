from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy, QApplication
import src.config
from src.step3 import step3
from src.config import clearLayout, getLogOutput, EraseWorker

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

    def erase_device():
        eraseCommand = [
            src.config.openocdpath,
            "-f", "interface\\cmsis-dap.cfg",
            "-f", "target\\efm32s2.cfg",
            "-c", "init; efm32s2_dci_device_erase; shutdown"
        ]
        worker = EraseWorker(eraseCommand)
        def on_success(output):
            logOutput.append("Erase success\n" + output)
        def on_error(err):
            logOutput.append("Erase error\n" + err)
        def on_finish():
            window.worker = None
        worker.finished_signal.connect(on_success)
        worker.error_signal.connect(on_error)
        worker.finished.connect(on_finish)
        window.worker = worker
        worker.start()
       

    # Create layout
    layout.addWidget(step2title)
    layout.addWidget(step2instructions)

    layout.addWidget(logOutput)

    layout.addWidget (eraseButton)
    eraseButton.setFixedHeight(35)
    eraseButton.clicked.connect(erase_device)

    layout.addSpacing(40)    

    layout.addWidget(nextbootloaderButton)
    nextbootloaderButton.setFixedHeight(35)

    window.setMinimumWidth(500)
    #window.setMinimumHeight(350)
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