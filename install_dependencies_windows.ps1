# Ensure the script is running with administrative privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Output "This script needs to run as Administrator. Restarting with admin privileges..."
    Start-Process powershell -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File $($MyInvocation.MyCommand)" -Verb RunAs
    exit
}

# Install Chocolatey if not installed
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Output "Installing Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((Invoke-WebRequest -Uri 'https://chocolatey.org/install.ps1').Content)
}

# Check if Arduino is installed
if (-not (choco list --local-only | Select-String 'arduino')) {
    Write-Output "Installing Arduino..."
    choco install arduino
}

# Check if Python3 is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Output "Installing Python..."
    choco install python
}

# Ensure pip is added to PATH
$env:Path += ";C:\Python39\Scripts\"

# Install necessary Python libraries
pip install librosa matplotlib pyserial torch torchaudio

# Install Demucs
pip install demucs

Write-Output "All necessary components are now installed!"
