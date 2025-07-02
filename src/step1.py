from PyQt6.QtWidgets import  QLabel, QFileDialog, QPushButton, QLineEdit, QComboBox
from src.config import openocdpath, bootloaderpath, receiverpath
import src.config
from src.step2 import step2
import src.config
import os

def step1(layout):

    #Next step button logic
    nextButton = QPushButton("Next Step")
    #nextButton.setEnabled(False)

    # Probe type dropdown variables
    probeTypeDropdown = QComboBox()
    probeTypeDropdown.addItems(["CMSIS-DAP (RPI Pico)", "ST-Link"])

    #Download variables
    bootloaderlink = QLabel('<a href="https://github.com/loopj/wavephoenix/releases">bootloader.hex</a>')
    receiverlink = QLabel('<a href="https://github.com/loopj/wavephoenix/releases">receiver.hex')
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
            print(f"Updated bootloader path: {src.config.bootloaderpath}")
            uploadBootloaderInput.setText(src.config.bootloaderpath)
    def file_dialog_receiver():
        selected, _ = QFileDialog.getOpenFileName(None, "Open Hex File", "", "Hex Files (*.hex);;All Files (*)")
        if selected:
            src.config.receiverpath = selected
            print(f"Updated firmware path: {src.config.receiverpath}")
            uploadReceiverInput.setText(src.config.receiverpath)


    # Conditionally change border color based on file path for openocdpath
    def updateOpenocdBorder():
        path = src.config.openocdpath.strip()  # get the current config variable
        if path == "" or not os.path.isfile(path):
            uploadOpenOcdInput.setStyleSheet("""
                QLineEdit {
                    border: 1px solid red;
                    border-radius: 4px;
                    padding: 4px;
                }
            """)
        else:
            uploadOpenOcdInput.setStyleSheet("""
                QLineEdit {
                    border: 1px solid green;
                    border-radius: 4px;
                    padding: 4px;
                }
            """)      
    def updateBootloaderBorder():
        path = src.config.bootloaderpath.strip()  # get the current config variable
        if path == "" or not os.path.isfile(path):
            uploadBootloaderInput.setStyleSheet("""
                QLineEdit {
                    border: 1px solid red;
                    border-radius: 4px;
                    padding: 4px;
                }
            """)
        else:
            uploadBootloaderInput.setStyleSheet("""
                QLineEdit {
                    border: 1px solid green;
                    border-radius: 4px;
                    padding: 4px;
                }
            """)     
    def updateReceiverBorder():
        path = src.config.receiverpath.strip()  # get the current config variable
        if path == "" or not os.path.isfile(path):
            uploadReceiverInput.setStyleSheet("""
                QLineEdit {
                    border: 1px solid red;
                    border-radius: 4px;
                    padding: 4px;
                }
            """)
        else:
            uploadReceiverInput.setStyleSheet("""
                QLineEdit {
                    border: 1px solid green;
                    border-radius: 4px;
                    padding: 4px;
                }
            """) 


    #Step 1 Upload variables
    uploadOpenOcdButton = QPushButton("Browse")
    uploadBootloaderButton = QPushButton("Browse")
    uploadReceiverButton = QPushButton("Browse")
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
        print(f"Updated bootloader.hex path to {src.config.bootloaderpath}")
        updateBootloaderBorder()
    def uploadReceiverInput_changed():
        global receiverpath
        receiverpath = uploadReceiverInput.text()
        print(f"Updated receiver.hex path to {src.config.bootloaderpath}")
        updateReceiverBorder()
    uploadOpenOcdInput.textChanged.connect(uploadOpenOcdInput_changed)
    uploadBootloaderInput.textChanged.connect(uploadBootloaderInput_changed)
    uploadReceiverInput.textChanged.connect(uploadReceiverInput_changed)


    # Step 1 Layout

    updateOpenocdBorder()
    updateBootloaderBorder()
    updateReceiverBorder()

    step1title= QLabel("Step 1: Gather Required Files")
    step1title.setStyleSheet("font-size:20px; font-weight:bold;")
    layout.addWidget(step1title)

    layout.addWidget(uploadOpenOcdInput)
    layout.addWidget(uploadOpenOcdButton)

    layout.addWidget(probeTypeDropdown)
    layout.addSpacing(40)

    layout.addWidget(bootloaderlink)
    layout.addWidget(uploadBootloaderInput)
    layout.addWidget(uploadBootloaderButton)

    layout.addWidget(receiverlink)
    layout.addWidget(uploadReceiverInput)
    layout.addWidget(uploadReceiverButton)

    layout.addSpacing(40)

    layout.addWidget(nextButton)

    # Proceed to step2 if button is pressed
    def go_to_step2():
        while layout.count():
            clearEach = layout.takeAt(0)
            if clearEach.widget():
                clearEach.widget().deleteLater()
        
        step2(layout)
    nextButton.clicked.connect(go_to_step2)