#!/bin/bash

if ! sudo -v; then
  echo "This script requires sudo access for package installation." >&2
  exit 1
fi

sudo dnf install -y python3.12 git
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.12
export PATH="/usr/bin:$PATH"

python3.12 --version
python3.12 -m pip install pyinstaller pyqt6

git clone https://github.com/SL9M/wavephoenix-utility
cd wavephoenix-utility || exit 1

wget https://downloads.arduino.cc/tools/openocd-0.12.0-arduino1-static-x86_64-ubuntu16.04-linux-gnu.tar.bz2
tar -xf openocd-0.12.0-arduino1-static-x86_64-ubuntu16.04-linux-gnu.tar.bz2
mv x86_64-ubuntu16.04-linux-gnu openocd
rm openocd-0.12.0-arduino1-static-x86_64-ubuntu16.04-linux-gnu.tar.bz2

echo "Success!"
