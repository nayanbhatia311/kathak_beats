import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt


def detect_peaks_in_song(audio_file):
    # Load the audio file
    y, sr = librosa.load(audio_file, sr=None)

    # Compute the short-time Fourier transform
    D = librosa.stft(y)

    # Compute the onset envelope
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)

    # Detect the onsets
    onsets = librosa.onset.onset_detect(
        onset_envelope=onset_env, sr=sr, backtrack=True)

    # Convert onset frames to time
    onset_times = librosa.frames_to_time(onsets, sr=sr)

    return onset_times


if __name__ == '__main__':

    audio_file = ".wav"
    onset_times = detect_peaks_in_song(audio_file)

    # Display the waveform and onsets
    plt.figure(figsize=(12, 4))
    librosa.display.waveshow(librosa.load(audio_file, sr=None)[0], alpha=0.5)
    plt.vlines(onset_times, -1, 1, color='r', alpha=0.9, label='Onsets')
    plt.legend()
    plt.title('Waveform and Onsets')
    plt.show()
