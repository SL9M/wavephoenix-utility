from PyQt6.QtWidgets import  QLabel, QFileDialog, QPushButton, QLineEdit, QComboBox, QSizePolicy, QHBoxLayout, QVBoxLayout
from src.config import openocdpath, bootloaderpath, receiverpath, clearLayout
import src.config
from src.step2 import step2
import src.config
import os
from PyQt6.QtCore import QSize

def step1(window, layout):

    #Next step button logic
    nextButton = QPushButton("Next Step >")
    nextButton.setStyleSheet("""
        QPushButton {
            background-color: #007aff;  /* iOS/macOS blue */
            color: white;
        }
        QPushButton:hover {
            background-color: #005bb5;
        }
        QPushButton:pressed {
            background-color: #003e85;
        }
    """)
    nextButton.setFixedHeight(35)

    #Test device logic
    testButton = QPushButton("Test Device")
    testButton.setFixedHeight(35)


    #nextButton.setEnabled(False)

    # Probe type dropdown variables
    probeTypeDropdown = QComboBox()
    probeTypeDropdown.addItems(["CMSIS-DAP (RPI Pico, Default)"])


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

    #Left columns bootloader hex
    bootloaderhexLayout = QVBoxLayout()
    bootloadertitle = QLabel('Bootloader Hex Path - <a href="https://github.com/loopj/wavephoenix/releases">Download</a>')
    bootloadertitle.setStyleSheet("font-size:15px; font-weight:bold; ")
    bootloadertitle.setOpenExternalLinks(True)
    bootloaderhexLayout.addWidget(bootloadertitle)
    bootloaderhexLayout.addWidget(uploadBootloaderInput)
    bootloaderhexLayout.addWidget(uploadBootloaderButton)

    #Right columns Receiver hex
    receiverhexLayout = QVBoxLayout()
    receivertitle = QLabel('Receiver Hex Path - <a href="https://github.com/loopj/wavephoenix/releases">Download</a>')
    receivertitle.setStyleSheet("font-size:15px; font-weight:bold;")
    receivertitle.setOpenExternalLinks(True)
    receiverhexLayout.addWidget(receivertitle)
    receiverhexLayout.addWidget(uploadReceiverInput)
    receiverhexLayout.addWidget(uploadReceiverButton)
    hexColumnsLayout = QHBoxLayout()

    #Add to row
    hexColumnsLayout.addLayout(bootloaderhexLayout)
    hexColumnsLayout.addLayout(receiverhexLayout)
    layout.addLayout(hexColumnsLayout)

    layout.addSpacing(20)

    layout.addWidget(nextButton)
    layout.addWidget(testButton)


    #Adjust Size
    window.setMinimumSize(QSize(0, 0))
    window.setFixedWidth(520)
    window.setMinimumHeight(0)
    window.setMaximumHeight(10000)
    window.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
    layout.invalidate()
    layout.activate()
    window.adjustSize()
    window.repaint()


    # Proceed to step2 if button is pressed
    def go_to_step2():
        clearLayout(layout)
        step2(layout, window)
    nextButton.clicked.connect(go_to_step2)

    def go_to_testdevice():
        from src.test import testPhoenix
        clearLayout(layout)
        testPhoenix(window, layout)
    testButton.clicked.connect(go_to_testdevice)