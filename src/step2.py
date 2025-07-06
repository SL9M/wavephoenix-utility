from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy
import src.config
import subprocess
from src.step3 import step3



def step2(layout, window):

    # Step 2 variables
    step2title= QLabel("Step 2: Erase Device")
    step2title.setStyleSheet("font-size:20px; font-weight:bold;")
    step2instructions = QLabel('Plug in the WavePhoenix you would like to flash, then click "Erase"')
    step2instructions.setWordWrap(True)
    step2instructions.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

    eraseButton = QPushButton("Erase Device")
    # Next Button
    nextbootloaderButton = QPushButton("Next Step")

    def erase_device():
        try:
            eraseCommand = [
                src.config.openocdpath,
                "-f", "interface\\cmsis-dap.cfg",
                "-f", "target\\efm32s2.cfg",
                "-c", "init; efm32s2_dci_device_erase; shutdown"
            ]
            print(eraseCommand)
            eraseResult = subprocess.run(eraseCommand, capture_output=True, text=True, check=True)
            print("Erase success\n",eraseResult.stdout)
        except subprocess.CalledProcessError as eraseError:
            print("Erase error\n", eraseError.stderr)

    # Create layout
    layout.addWidget(step2title)
    layout.addWidget(step2instructions)
    layout.addWidget (eraseButton)
    eraseButton.clicked.connect(erase_device)

    layout.addSpacing(40)    

    layout.addWidget(nextbootloaderButton)

    window.setFixedWidth(300)
    window.setMinimumHeight(300)
    window.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)    
    layout.invalidate()
    layout.activate()
    window.adjustSize()
    window.repaint()

    # Proceed to step3 if button is pressed
    def go_to_step3():
        while layout.count():
            clearEach = layout.takeAt(0)
            if clearEach.widget():
                clearEach.widget().deleteLater()
        
        step3(window ,layout)
    nextbootloaderButton.clicked.connect(go_to_step3)