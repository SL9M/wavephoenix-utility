#!/bin/bash

# Exit on error
set -e

# Update package info
echo "Updating package repos"
sudo dnf update -y

# Install required packages
echo "Installing Python 3.13, pip, and Git"
sudo dnf install -y python3.13 python3.13-pip git

# Use pip to install PyQt6 and PyInstaller
echo "Installing Python packages..."
python3.13 -m pip install --upgrade pip
python3.13 -m pip install pyqt6 pyinstaller

# Change to Desktop and clone the repository
echo "Cloning GitHub repository..."
cd ~/Desktop
git clone https://github.com/SL9M/wavephoenix-utility

echo "Setup complete!"
