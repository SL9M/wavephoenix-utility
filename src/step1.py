from PyQt6.QtWidgets import  QLabel, QFileDialog, QPushButton, QLineEdit, QComboBox
from src.config import openocdpath, bootloaderpath, receiverpath
import src.config
from src.step2 import step2
import src.config
import os

def step1(layout):
    #Next step button logic
    nextButton = QPushButton("Next Step")
    nextButton.setFixedHeight(50)
    nextButton.setStyleSheet("font-size: 15px;")
    #nextButton.setEnabled(False)

    # Probe type dropdown variables
    probeTypeDropdown = QComboBox()
    probeTypeDropdown.addItems(["CMSIS-DAP (RPI Pico, Default)", "ST-Link"])

    #Download variables
    bootloaderlink = QLabel('<a href="https://github.com/loopj/wavephoenix/releases">Download</a>')
    receiverlink = QLabel('<a href="https://github.com/loopj/wavephoenix/releases">Download')
    bootloaderlink.setOpenExternalLinks(True)
    receiverlink.setOpenExternalLinks(True)

    #Upload Dialogs and path storage
    def file_dialog_openocd():
        openocdpath, _ = QFileDialog.getOpenFileName(None, "Select OpenOCD Executable", "", "All Files (*)")
        if openocdpath:
            print(f"Selected file: {openocdpath}")
            uploadOpenOcdInput.setText(openocdpath)
            return openocdpath
    def file_dialog_bootloader():
        selected, _ = QFileDialog.getOpenFileName(None, "Open Hex File", "", "Hex Files (*.hex);;All Files (*)")
        if selected:
            src.config.bootloaderpath = selected
            uploadBootloaderInput.setText(src.config.bootloaderpath)
    def file_dialog_receiver():
        selected, _ = QFileDialog.getOpenFileName(None, "Open Hex File", "", "Hex Files (*.hex);;All Files (*)")
        if selected:
            src.config.receiverpath = selected
            uploadReceiverInput.setText(src.config.receiverpath)


    # Conditionally change border color based on file path for openocdpath
    def updateInputBorder(widget, path):
        path = path.strip()
        color = "green" if path and os.path.isfile(path) else "red"
        widget.setStyleSheet(f"""
            QLineEdit {{
                border: 1px solid {color};
                border-radius: 4px;
                padding: 4px;
            }}
        """)
    def updateOpenocdBorder():
        updateInputBorder(uploadOpenOcdInput, src.config.openocdpath)
    def updateBootloaderBorder():
        updateInputBorder(uploadBootloaderInput, src.config.bootloaderpath)
    def updateReceiverBorder():
        updateInputBorder(uploadReceiverInput, src.config.receiverpath)

    #Step 1 Upload variables
    uploadOpenOcdButton = QPushButton("Browse")
    uploadOpenOcdButton.setFixedHeight(35)
    uploadBootloaderButton = QPushButton("Browse")
    uploadBootloaderButton.setFixedHeight(35)
    uploadReceiverButton = QPushButton("Browse")
    uploadReceiverButton.setFixedHeight(35)
    #Step 1 Button behavior settings
    uploadOpenOcdButton.clicked.connect(file_dialog_openocd)
    uploadBootloaderButton.clicked.connect(file_dialog_bootloader)
    uploadReceiverButton.clicked.connect(file_dialog_receiver)
    # Input fields
    uploadOpenOcdInput = QLineEdit()
    uploadOpenOcdInput.setText(src.config.openocdpath)
    uploadBootloaderInput = QLineEdit()
    uploadBootloaderInput.setText(src.config.bootloaderpath)
    uploadReceiverInput = QLineEdit()
    uploadReceiverInput.setText(src.config.receiverpath)


    #Handle manual text entry variable updating
    def uploadOpenOcdInput_changed():
        src.config.openocdpath = uploadOpenOcdInput.text()
        print(f"Updated OpenOCD path to {src.config.openocdpath}")
        updateOpenocdBorder()
    def uploadBootloaderInput_changed():
        src.config.bootloaderpath = uploadBootloaderInput.text()
        print(f"Updated bootloader path to {src.config.bootloaderpath}")
        updateBootloaderBorder()
    def uploadReceiverInput_changed():
        src.config.receiverpathpath = uploadReceiverInput.text()
        print(f"Updated firmware path to {src.config.receiverpath}")
        updateReceiverBorder()

    uploadOpenOcdInput.textChanged.connect(uploadOpenOcdInput_changed)
    uploadBootloaderInput.textChanged.connect(uploadBootloaderInput_changed)
    uploadReceiverInput.textChanged.connect(uploadReceiverInput_changed)


    # Step 1 Layout

    updateOpenocdBorder()
    updateBootloaderBorder()
    updateReceiverBorder()

    #H1 Title Step 1
    step1title= QLabel("Step 1: Pre-Flashing Setup")
    step1title.setStyleSheet("font-size:20px; font-weight:bold;")
    layout.addWidget(step1title)
    layout.addSpacing(10)

    #H2 OpenOCD Upload
    openocdtitle = QLabel("OpenOCD Path (Included by default)")
    openocdtitle.setStyleSheet("font-size:15px; font-weight:bold; ")
    layout.addWidget(openocdtitle)
    layout.addWidget(uploadOpenOcdInput)
    layout.addWidget(uploadOpenOcdButton)

    #H3 Probe Type
    probetitle = QLabel("Probe Type")
    probetitle.setStyleSheet("font-size:13px; font-weight:bold; ")
    layout.addWidget(probetitle)
    layout.addWidget(probeTypeDropdown)
    layout.addSpacing(20)

    #H2 Bootloader Title
    bootloadertitle = QLabel("Bootloader Hex Path")
    bootloadertitle.setStyleSheet("font-size:15px; font-weight:bold; ")
    layout.addWidget(bootloadertitle)
    layout.addWidget(bootloaderlink)
    layout.addWidget(uploadBootloaderInput)
    layout.addWidget(uploadBootloaderButton)

    #H2 Receiver Title
    receivertitle = QLabel("Receiver Hex Path")
    receivertitle.setStyleSheet("font-size:15px; font-weight:bold;")
    layout.addWidget(receivertitle)
    layout.addWidget(receiverlink)
    layout.addWidget(uploadReceiverInput)
    layout.addWidget(uploadReceiverButton)

    layout.addSpacing(20)

    layout.addWidget(nextButton)

    # Proceed to step2 if button is pressed
    def go_to_step2():
        while layout.count():
            clearEach = layout.takeAt(0)
            if clearEach.widget():
                clearEach.widget().deleteLater()
        
        step2(layout)
    nextButton.clicked.connect(go_to_step2)