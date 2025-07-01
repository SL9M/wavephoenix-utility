# Build Instructions 

## Windows

Run ```Set-ExecutionPolicy Unrestricted``` 
This allows third party scripts to execute. I recommend doing this in a VM to keep your host system tidy and unmodified.

Run ```setup-windows.ps1``` in powershell to obtain all project dependencies via winget & pip.

In the project root folder run ```pyinstaller main.spec``` to compile.

Optionally, you can include OpenOCD extracted in the project root folder named "openocd" and pyinstaller will add that to your build.