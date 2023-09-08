#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew is not installed. Installing it now..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Homebrew is already installed!"
fi

# Update Homebrew
brew update

# Check if Arduino is installed
if ! brew list --cask | grep -q arduino
then
    echo "Arduino is not installed, installing now..."
    brew install --cask arduino
else
    echo "Arduino is already installed!"
fi

# Check if Python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed, installing now..."
    brew install python3
fi

# Install necessary Python libraries
pip3 install librosa matplotlib pyserial torch torchaudio

# Install Demucs
pip3 install demucs

echo "All necessary components are now installed!"
