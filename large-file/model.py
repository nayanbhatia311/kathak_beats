import subprocess as sp
from pathlib import Path
import librosa
import librosa.display
import matplotlib.pyplot as plt


def separate(filename=None,inp=None, outp=None, model="htdemucs", mp3=True, mp3_rate=320, float32=False, int24=False, two_stems=None):
    inp = inp
    outp = outp
    cmd = ["python", "-m", "demucs.separate", "-o", str(outp), "-n", model]
    if mp3:
        cmd += ["--mp3", f"--mp3-bitrate={mp3_rate}"]
    if float32:
        cmd += ["--float32"]
    if int24:
        cmd += ["--int24"]
    if two_stems is not None:
        cmd += [f"--two-stems={two_stems}"]

    files = [str(f) for f in find_files(inp)]
    if not files:
        print(f"No valid audio files in {in_path}")
        return

    print("Going to separate the files:")
    print('\n'.join(files))
    print("With command: ", " ".join(cmd))
    p = sp.Popen(cmd + files, stdout=sp.PIPE, stderr=sp.PIPE)
    p.communicate()
    if p.returncode != 0:
        print("Command failed, something went wrong.")
    audio_file_path=f'output/htdemucs/{filename}/vocals.mp3'
    audio, sr = librosa.load(audio_file_path)
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    print("Onset Timestamps:", onset_times)
    fig, ax = plt.subplots(figsize=(10, 6))
    librosa.display.waveshow(audio, sr=sr, alpha=0.5)

    for time in onset_times:
        ax.axvline(x=time, color='r', linestyle='--', linewidth=1)
    plt.title('Onset Detection Visualization')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend(['Waveform', 'Detected Onsets'])
    plt.xlim(15, 50)
    plt.tight_layout()
    plt.show()
    
    print("Onset Timestamps:", onset_times)
    try:
        ser = serial.Serial('COM3', 9600, timeout=1)
    except Exception as e:
        print(f"Failed to open COM port: {e}")
        exit(1)
    
    # Write onset timestamps to COM port 3
    for time in onset_times:
        ser.write(f"{time}\n".encode())
    
    # Close the COM port
    ser.close()
def find_files(in_path, extensions=["wav", "mp3", "m4a", "flac"]):
    return [file for file in Path(in_path).iterdir() if file.suffix.lower().lstrip(".") in extensions]

if __name__ == "__main__":
    separate()
    
    # Load the separated vocal track (adjust path as needed)
    audio_file_path = "output/htdemucs/kathak_1/vocals.mp3"
    audio, sr = librosa.load(audio_file_path)
    
    # Onset detection
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)
    
    
    
    
    # Open COM port 3
    try:
        ser = serial.Serial('COM3', 9600, timeout=1)
    except Exception as e:
        print(f"Failed to open COM port: {e}")
        exit(1)
    
    # Write onset timestamps to COM port 3
    for time in onset_times:
        ser.write(f"{time}\n".encode())
    
    # Close the COM port
    ser.close()
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    librosa.display.waveshow(audio, sr=sr, alpha=0.5)
    for time in onset_times:
        ax.axvline(x=time, color='r', linestyle='--', linewidth=1)
    plt.title('Onset Detection Visualization')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.legend(['Waveform', 'Detected Onsets'])
    plt.xlim(15, 50)
    plt.tight_layout()
    plt.show()
    
    print("Onset Timestamps:", onset_times)
