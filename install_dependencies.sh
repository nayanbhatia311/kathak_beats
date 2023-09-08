#!/bin/bash

# Check if Arduino is installed
if ! command -v arduino &> /dev/null
then
    echo "Arduino is not installed, installing now..."
    # Add the Arduino repository
    sudo apt-add-repository ppa:arduino-ubuntu-team/ppa
    sudo apt update
    sudo apt install arduino arduino-core
else
    echo "Arduino is already installed!"
fi

# Install Python3 and pip if they aren't installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed, installing now..."
    sudo apt install python3
fi

if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed, installing now..."
    sudo apt install python3-pip
fi

# Install necessary Python libraries
pip3 install librosa matplotlib pyserial torch torchaudio

# Install Demucs
pip3 install demucs

echo "All necessary components are now installed!"
