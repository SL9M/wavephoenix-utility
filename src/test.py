from PyQt6.QtWidgets import  QLabel, QPushButton, QSizePolicy
import src.config
import subprocess

def testPhoenix(window,layout):

    # Test phoenix variables
    testphoenixtitle= QLabel("Test Your Device")
    testphoenixtitle.setStyleSheet("font-size:20px; font-weight:bold;")
    testphoenixinstructions = QLabel('Unplug and plug back in your WavePhoenix. Click "Test Device" sending this command will allow it to function while connected to the probe.')
    testphoenixinstructions.setWordWrap(True)
    testphoenixinstructions.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
    

    readmemoryButton = QPushButton("Test Device")
    #Back button
    backGatherButton = QPushButton("Back Home")


    def read_memory():
        try:
            memoryReadCommand = [
                src.config.openocdpath,
                "-f", "interface\\cmsis-dap.cfg",
                "-c", "transport select swd",
                "-f", "target\\efm32s2.cfg",
                "-c", "init; reset init; exit"
            ]
            print(memoryReadCommand)
            memoryReadResult = subprocess.run(memoryReadCommand, capture_output=True, text=True, check=True)
            print("Testing device, you should now be able to click the button to pair. If you have a blinking light, your device can pair to a WaveBird with X+Y\n",memoryReadResult.stdout)
        except subprocess.CalledProcessError as memoryReadError:
            print("Testing device, you should now be able to click the button to pair. If you have a blinking light, your device can pair to a WaveBird with X+Y\n", memoryReadError.stderr)

    # Create layout
    layout.addWidget(testphoenixtitle)
    layout.addWidget(testphoenixinstructions)
    layout.addWidget (readmemoryButton)
    readmemoryButton.setFixedHeight(35)
    readmemoryButton.clicked.connect(read_memory)
    layout.addSpacing(40)


    window.setFixedWidth(300)
    window.setMinimumHeight(300)
    window.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)    
    layout.invalidate()
    layout.activate()
    window.adjustSize()
    window.repaint()

    # Back to step1 if button is pressed
    def go_to_step1():
        from src.step1 import step1
        while layout.count():
            clearEach = layout.takeAt(0)
            if clearEach.widget():
                clearEach.widget().deleteLater()
        
        step1(window,layout)
    layout.addWidget(backGatherButton)
    backGatherButton.setFixedHeight(35)
    backGatherButton.clicked.connect(go_to_step1)