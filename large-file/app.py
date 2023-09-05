import os
import subprocess as sp
import librosa
import serial
from model import separate
from flask import Flask, render_template, request
from flask_dropzone import Dropzone

# Initialize your Flask application and Dropzone
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE_SIZE=999999999,
    DROPZONE_TIMEOUT=5 * 60 * 1000
)

dropzone = Dropzone(app)

if not os.path.exists(os.path.join(basedir, 'uploads')):
    os.makedirs(os.path.join(basedir, 'uploads'))

@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        
        print(f"Received file named {f.filename}")
        
        path = os.path.join(app.config['UPLOADED_PATH'], f.filename)

        print(f"Saving file to {path}")

        try:
            f.save(path)
        # Call the separate function from model.py
        separate(filename=f.filename,inp=path)
        except Exception as e:
            return f"Could not save file: {e}"


        # Load the separated vocal track (adjust path as needed)
        audio_file_path = os.path.join(basedir, f'output/htdemucs/{f.filename}/vocals.mp3')
        
        # Debugging: Print the audio file path
        print(f"Looking for file at {audio_file_path}")

        try:
            audio, sr = librosa.load(audio_file_path)
        except Exception as e:
            return f"Could not load audio file: {e}"


        # COM port operations here (assuming you have one)

        return str("Replace this with your onset times or other return values")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
