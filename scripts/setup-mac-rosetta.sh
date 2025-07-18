#!/bin/bash
set -e

if [[ "$(uname -m)" != "x86_64" ]]; then
  echo "This script must be run under Rosetta 2 on an Intel-based Mac."
  exit 1
fi

if ! command -v brew >/dev/null 2>&1; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

BREW_PREFIX="/usr/local"
ZPROFILE="$HOME/.zprofile"
echo 'eval "$(/usr/local/bin/brew shellenv)"' >> "$ZPROFILE"
eval "$(/usr/local/bin/brew shellenv)"

brew install pyenv

pyenv install 3.12.10 || echo "Python 3.12.10 already installed"
pyenv global 3.12.10

ZSHRC="$HOME/.zshrc"
{
  echo 'export PYENV_ROOT="$HOME/.pyenv"'
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"'
  echo 'eval "$(pyenv init --path)"'
  echo 'eval "$(pyenv init -)"'
  echo 'alias python=python3'
  echo 'alias pip=pip3'
} >> "$ZSHRC"

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

pip3 install --upgrade pip
pip3 install pyinstaller pyqt6

brew install git

git clone https://github.com/SL9M/wavephoenix-utility.git
cd wavephoenix-utility

curl -LO https://downloads.arduino.cc/tools/openocd-0.12.0-arduino1-static-x86_64-apple-darwin19.tar.bz2
tar -xjf openocd-0.12.0-arduino1-static-x86_64-apple-darwin19.tar.bz2
mv x86_64-apple-darwin19 openocd
rm openocd-0.12.0-arduino1-static-x86_64-apple-darwin19.tar.bz2

echo "Setup complete!"