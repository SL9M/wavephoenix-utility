from src.mainWindow import mainWindow
from PyQt6.QtWidgets import  QLabel, QFileDialog, QPushButton, QLineEdit
from src.config import openocdpath

def step1(layout):

    #Next step button logic
    nextButton = QPushButton("Next Step")
    nextButton.setEnabled(False)

    #Download variables
    openocdlink = QLabel('<a href="https://github.com/loopj/openocd-efm32s2/releases/download/latest/openocd-c9fd9f6a2-i686-w64-mingw32.tar.gz">OpenOCD tar file from GitHub (loopj/openocd-efm32s2)</a>')
    bootloaderlink = QLabel('<a href="https://github.com/loopj/wavephoenix/releases">bootloader.hex</a>')
    receiverlink = QLabel('<a href="https://github.com/loopj/wavephoenix/releases">receiver.hex')
    openocdlink.setOpenExternalLinks(True)
    bootloaderlink.setOpenExternalLinks(True)
    receiverlink.setOpenExternalLinks(True)

    bootloaderpath = ""
    receiverpath = ""

    #Upload Dialogs and path storage
    def file_dialog_openocd():
        openocdpath, _ = QFileDialog.getOpenFileName(None, "Open File", "", "Gzipped Tar Files (*.tar.gz *.tgz);;Tar Files (*.tar);;All Files (*)")
        if openocdpath:
            print(f"Selected file: {openocdpath}")
            uploadOpenOcdInput.setText(openocdpath)
            return openocdpath
    def file_dialog_bootloader():
        bootloaderpath, _ = QFileDialog.getOpenFileName(None, "Open Hex File", "", "Hex Files (*.hex);;All Files (*)")
        if bootloaderpath:
            print(f"Selected file: {bootloaderpath}")
            uploadBootloaderInput.setText(bootloaderpath)
            return bootloaderpath
    def file_dialog_receiver():
        receiverpath, _ = QFileDialog.getOpenFileName(None, "Open Hex File", "", "Hex Files (*.hex);;All Files (*)")
        if receiverpath:
            print(f"Selected file: {receiverpath}")
            uploadReceiverInput.setText(receiverpath)
            return receiverpath
        


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
    uploadOpenOcdInput.setText(openocdpath)
    uploadBootloaderInput = QLineEdit()
    uploadReceiverInput = QLineEdit()

    #Handle manual text entry variable updating
    def uploadOpenOcdInput_changed():
        global openocdpath
        openocdpath = uploadOpenOcdInput.text()
        print(f"Updated OpenOCD path: {openocdpath}")
    def uploadBootloaderInput_changed():
        global bootloaderpath
        bootloaderpath = uploadBootloaderInput.text()
        print(f"Updated bootloader.hex path: {bootloaderpath}")
    def uploadReceiverInput_changed():
        global receiverpath
        receiverpath = uploadReceiverInput.text()
        print(f"Updated receiver.hex path: {receiverpath}")

    uploadOpenOcdInput.textChanged.connect(uploadOpenOcdInput_changed)
    uploadBootloaderInput.textChanged.connect(uploadBootloaderInput_changed)
    uploadReceiverInput.textChanged.connect(uploadReceiverInput_changed)


    # Step 1 Instructions
    step1title= QLabel("Step 1: Gather Required Files")
    step1title.setStyleSheet("font-size:20px; font-weight:bold;")
    layout.addWidget(step1title)

    layout.addWidget(openocdlink)
    layout.addWidget(uploadOpenOcdInput)
    layout.addWidget(uploadOpenOcdButton)

    layout.addWidget(bootloaderlink)
    layout.addWidget(uploadBootloaderInput)
    layout.addWidget(uploadBootloaderButton)

    layout.addWidget(receiverlink)
    layout.addWidget(uploadReceiverInput)
    layout.addWidget(uploadReceiverButton)

    layout.addSpacing(40)

    layout.addWidget(nextButton)