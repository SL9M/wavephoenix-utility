#!/bin/zsh

#  Homebrew needs installing
if ! command -v brew &>/dev/null; then
  echo "Homebrew not found. Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install python
brew install python@3.13

# May not appear in path right away
# If you get a path error, try closing
# terminal, and re-running this script

# Use pip to install packages
"$PYTHON_BIN/pip3" install pyinstaller PyQt6