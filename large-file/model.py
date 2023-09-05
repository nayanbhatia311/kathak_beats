import subprocess as sp
from pathlib import Path
import librosa
import librosa.display
import matplotlib.pyplot as plt
import serial  


def separate(filename=None, inp=None, outp=None, model="htdemucs", mp3=True, mp3_rate=320, float32=False, int24=False, two_stems=None):
    print(f"Debug: separate(filename={filename}, inp={inp}, outp={outp}) called")

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
        print(f"Debug: No valid audio files in {inp}")
        return

    print("Debug: Going to separate the files:")
    print('\n'.join(files))
    print("Debug: With command:", " ".join(cmd))

    p = sp.Popen(cmd + files, stdout=sp.PIPE, stderr=sp.PIPE)
    stdout, stderr = p.communicate()

    print(f"Debug: stdout: {stdout}")
    print(f"Debug: stderr: {stderr}")

    if p.returncode != 0:
        print("Debug: Command failed, something went wrong.")

    audio_file_path = f'output/htdemucs/{filename}/vocals.mp3'
    audio, sr = librosa.load(audio_file_path)
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
    onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    print("Debug: Onset Timestamps:", onset_times)

    # Plotting code here ...

    try:
        ser = serial.Serial('COM3', 9600, timeout=1)
    except Exception as e:
        print(f"Debug: Failed to open COM port: {e}")
        exit(1)

    for time in onset_times:
        ser.write(f"{time}\n".encode())

    ser.close()


def find_files(in_path, extensions=["wav", "mp3", "m4a", "flac"]):
    print(f"Debug: find_files called with in_path={in_path} and extensions={extensions}")
    return [file for file in Path(in_path).iterdir() if file.suffix.lower().lstrip(".") in extensions]


if __name__ == "__main__":
    print("Debug: __main__ called")
    separate()
