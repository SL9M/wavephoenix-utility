# WavePhoenix Utility

A GUI based program written to help users unfamiliar with commandline tools flash their WavePhoenix receivers. Ideal for DIYers, bulk WavePhoenix flashing, and people who dislike memorizing or hunting down commands for each flash.

Built with Python & Qt6.

## Current Features
1. Prompt user to download all essential files
2. File upload fields that should work with future updates
3. Step by step on screen instructions
4. Extracts OpenOCD tar files to reduce friction
5. Seperate window with console output for debugging
6. Support for Windows

## Planned Features
1. Continuous bulk flashing
2. Optional Pico probe uf2 flashing - for users who've never flashed a pico
3. Support for macOS and Linux

## Build Instructions
For macOS and Linux users, you can simply run nix-shell in the project directory. then run "pyinstaller main.spec" 

For windows, use winget or similar to obtain all of the project dependencies then run the same command.