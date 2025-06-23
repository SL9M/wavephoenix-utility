# Install Python 3.13 via winget
Write-Host "Installing Python 3.13..."
winget install --id=Python.Python.3.13 -e

# Verify Python installation
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error "Python is not found in PATH after installation. Please ensure Python 3.13 is installed and added to PATH."
    exit 1
}

# Install pyinstaller and pyqt6 using pip
Write-Host "Installing pyinstaller and pyqt6 via pip..."
python -m pip install --upgrade pip
python -m pip install pyinstaller pyqt6

Write-Host "Installation completed successfully. Run pyinstaller main.spec in the project root."