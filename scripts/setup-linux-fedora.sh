#!/bin/bash
set -e
if [ "$EUID" -ne 0 ]; then
  echo "This script must be run with sudo to access dnf"
  exit 1
fi

# Install fedora packages
dnf update -y
dnf install -y python3.12 python3.12-pip git

# Project deps
python3.12 -m pip install --upgrade pip
python3.12 -m pip install pyqt6 pyinstaller

#Clone repo to desktop
cd ~/Desktop
git clone https://github.com/SL9M/wavephoenix-utility
cd wavephoenix-utility

#Clone and extract openocd
curl -L https://downloads.arduino.cc/tools/openocd-0.12.0-arduino1-static-x86_64-ubuntu16.04-linux-gnu.tar.bz2 -o openocd.tar.bz2 && \
tar -xjf openocd.tar.bz2 && \
mv x86_64-ubuntu16.04-linux-gnu openocd

echo "Setup complete! Run pyinstaller main.spec to build"
