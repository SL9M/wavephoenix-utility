$ErrorActionPreference = "Stop"

winget install --id=Python.Python.3.12 -e --accept-source-agreements --accept-package-agreements

$env:Path += ";$env:LOCALAPPDATA\Programs\Python\Python312\Scripts;$env:LOCALAPPDATA\Programs\Python\Python312"

python -m pip install --upgrade pip
python -m pip install pyinstaller pyqt6

winget install --id=Git.Git -e --accept-source-agreements --accept-package-agreements

git clone https://github.com/SL9M/wavephoenix-utility

Set-Location -Path ".\wavephoenix-utility"

$tarUrl = "https://downloads.arduino.cc/tools/openocd-0.12.0-arduino1-static-i686-w64-mingw32.tar.bz2"
$tarFile = "openocd-0.12.0-arduino1-static-i686-w64-mingw32.tar.bz2"
Invoke-WebRequest -Uri $tarUrl -OutFile $tarFile

tar -xjf $tarFile

Rename-Item -Path "openocd-0.12.0-arduino1-static-i686-w64-mingw32" -NewName "openocd"

Remove-Item -Path $tarFile

Write-Host "Setup complete."
