import os
from model import detect_peaks_in_song
from flask import Flask, render_template, request
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
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
        array_of_peaks = detect_peaks_in_song(path)
        return array_of_peaks
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
