# Build Instructions 

## Windows

Run ```setup-windows.ps1``` in powershell to obtain all project dependencies.

In the project root folder run ```pyinstaller main.spec``` to compile.

Optionally, you can include OpenOCD extracted in the project root folder named "openocd" and pyinstaller will add that to your build.