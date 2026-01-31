"""
spectrogram.py

Purpose:
--------
Generate a spectrogram using Short-Time Fourier Transform (STFT).

Why STFT?
---------
Speech is non-stationary.
Its frequency content changes over time.
"""

import librosa
import numpy as np

def compute_spectrogram(signal, sr, n_fft=1024, hop_length=512):
    """
    Compute spectrogram from audio signal.

    Parameters
    ----------
    signal : np.ndarray
    sr : int
    n_fft : int
        FFT window size
    hop_length : int
        Step size between windows

    Returns
    -------
    spectrogram_db : np.ndarray
        Log-scaled spectrogram
    """
    stft = librosa.stft(signal, n_fft=n_fft, hop_length=hop_length)
    spectrogram_db = librosa.amplitude_to_db(np.abs(stft))
    return spectrogram_db
