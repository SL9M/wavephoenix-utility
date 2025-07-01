# WavePhoenix Utility

GUI WavePhoenix flashing software written to help users unfamiliar with commandline tools. Ideal for DIYers, bulk WavePhoenix flashing, and people who dislike memorizing or hunting down commands for each flash.

## Usage
1. Download [latest release](https://github.com/SL9M/wavephoenix-utility/releases/latest)
 from Github releases page. - Chrome may flag it as suspicious, this is expected behavior due to the way it's packaging and executing command line tools. 
2. Extract all contents in the zip file
3. Launch the executable
4. Accept any SmartScreen/Security prompts
5. Upload your bootloader and firmware files to the GUI
6. Follow the step by step guide and enjoy!

## Current Features
1. Erase & flash WavePhoenix devices easily
2. Links user to bootloader & firmware downloads
3. Github release bundles include Loopj's OpenOCD fork - no extra software needed!
4. Step by step on screen guide
5. Seperate window with logs & console output for debugging and transparency

## Planned Features
1. "Pro" layout - for bulk flashing & time savings
3. Support for macOS and Linux 
4. Robust error handling with troubleshooting steps included
5. Optional Rpi Pico flashing

## Credits
Credit largely goes to loopj for creating the core WavePhoenix project. Without Loopj's hard work, this tool would have no reason to exist.

Special thanks to members of the GameCube modding community for inspiring me to solve this issue.

Built with Python & Qt6, packaged using PyInstaller.
