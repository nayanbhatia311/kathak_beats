# kathak_beats
This is a Flask application designed to detect peaks in songs. Users can upload song files, which are then processed to identify peaks in the audio data.  

# Installation Instructions

This guide provides steps to set up the necessary dependencies for running the provided code on different operating systems: Linux (Ubuntu), macOS, and Windows.

## Prerequisites
pip install -r requirements.txt 
Before beginning the installation, ensure you have:

- A stable internet connection.
- Administrative or sudo privileges to install software on your machine.

## Linux (Ubuntu)

### Automatic Installation

1. Download the `install_dependencies.sh` script.
2. Open the Terminal.
3. Navigate to the directory containing the script.
4. Make the script executable:
   ```bash
   chmod +x install_dependencies.sh
   ```
5. Run the script:
   ```bash
   ./install_dependencies.sh
   ```

### Manual Installation

1. Install Arduino:
   ```bash
   sudo apt-add-repository ppa:arduino-ubuntu-team/ppa
   sudo apt update
   sudo apt install arduino arduino-core
   ```
2. Install Python3 and pip:
   ```bash
   sudo apt install python3 python3-pip
   ```
3. Install necessary Python libraries:
   ```bash
   pip3 install -r requirements.txt
   ```

## macOS

### Automatic Installation

1. Download the `install_dependencies_mac.sh` script.
2. Open the Terminal.
3. Navigate to the directory containing the script.
4. Make the script executable:
   ```bash
   chmod +x install_dependencies_mac.sh
   ```
5. Run the script:
   ```bash
   ./install_dependencies_mac.sh
   ```

### Manual Installation

1. Install Homebrew if not already installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install Arduino and Python3:
   ```bash
   brew install --cask arduino
   brew install python3
   ```
3. Install necessary Python libraries:
   ```bash
   pip3 install -r requirements.txt
   ```

## Windows

### Automatic Installation

1. Download the `install_dependencies_windows.ps1` script.
2. Open PowerShell as an administrator.
3. Navigate to the directory containing the script.
4. Run the script:
   ```
   powershell -ExecutionPolicy Bypass -File .\install_dependencies_windows.ps1
   ```

### Manual Installation

1. Install [Chocolatey](https://chocolatey.org/install).
2. Install Arduino and Python3 using Chocolatey:
   ```powershell
   choco install arduino python
   ```
3. Install necessary Python libraries:
   ```powershell
   pip install -r requirements.txt
   ```

---

After following these steps, you should have all the necessary dependencies installed to run the provided code on your operating system.

## Setup
git clone <repository_url>
cd <repository_folder>/large-files/

python3 -m venv venv  
source venv/bin/activate (mac or linux)  
venv\Scripts\activate (on windows)  
pip3 install -r requirements.txt 
python3 app.py

