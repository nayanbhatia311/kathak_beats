import os
import subprocess as sp
import librosa
import serial
from flask import Flask, render_template, request
from flask_dropzone import Dropzone

# Add your own separate() and find_files() functions here, or import them if they are in a separate module.

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE_SIZE=1024,
    DROPZONE_TIMEOUT=5 * 60 * 1000
)

dropzone = Dropzone(app)

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
        f.save(path)
        
        # Call your separate function to separate vocals
        separate(inp=path, outp=os.path.join(basedir, 'output'))
        
        # Load the separated vocal track (adjust path as needed)
        audio_file_path = os.path.join(basedir, f'output/htdemucs/{f.filename}/vocals.mp3')
        audio, sr = librosa.load(audio_file_path)
        
        # Onset detection
        onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
        onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
        onset_times = librosa.frames_to_time(onset_frames, sr=sr)
        
        # Open COM port 3
        try:
            ser = serial.Serial('COM3', 9600, timeout=1)
        except Exception as e:
            return f"Failed to open COM port: {e}"

        # Write onset timestamps to COM port 3
        for time in onset_times:
            ser.write(f"{time}\n".encode())
        
        # Close the COM port
        ser.close()

        return str(onset_times)
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
