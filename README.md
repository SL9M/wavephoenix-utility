# WavePhoenix Utility

GUI WavePhoenix flashing software written to help users unfamiliar with commandline tools. Ideal for DIY, and bulk WavePhoenix flashing.

![Step 1 Screenshot](/resources/step1screenshot.png "Step 1 Screenshot")

## Usage
1. Download [latest release](https://github.com/SL9M/wavephoenix-utility/releases/latest)
 from Github releases page. - Chrome may flag it as suspicious, this is expected behavior due to the way it's packaging and executing command line tools.
2. Download [bootloader and receiver hex files](https://github.com/loopj/wavephoenix/releases/latest) from loopj 
3. Extract all contents in the zip file
4. Launch the executable
5. Accept SmartScreen/Security prompts
6. Upload your bootloader and firmware files to the GUI
7. Follow the step by step guide and enjoy!

## Current Features
1. Erase & flash WavePhoenix devices easily
2. Links user to bootloader & firmware downloads
3. Github release bundles include OpenOCD with efm32s2 support - no extra software needed!
4. Step by step on screen guide
5. Seperate window with logs & console output for debugging and transparency
6. Support for macOS & Linux
7. Robust error handling with troubleshooting steps included

## Planned Features
1. "Pro" layout - all features in one window. Ideal for creating batches
5. Support for J-Link, and ST-Link

## Credits
Credit largely goes to loopj for the core [WavePhoenix project](https://github.com/loopj/wavephoenix/tree/main/hardware/mini-receiver). Without Loopj's hard work, this tool would have no reason to exist.

Special thanks to members of the GameCube modding community for inspiring me to make this.

Built with Python3, PyQt6, OpenOCD, and bundled using PyInstaller.
