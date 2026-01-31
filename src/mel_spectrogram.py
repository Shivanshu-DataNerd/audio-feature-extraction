"""
mel_spectrogram.py

Purpose:
--------
Convert spectrogram into Mel-scale representation.

Why Mel scale?
--------------
Human hearing is nonlinear.
Mel scale approximates human auditory perception.
"""

import librosa
import numpy as np

def compute_mel_spectrogram(signal, sr, n_mels=128):
    """
    Compute Mel Spectrogram.

    Parameters
    ----------
    signal : np.ndarray
    sr : int
    n_mels : int
        Number of Mel filter banks

    Returns
    -------
    mel_db : np.ndarray
        Log-scaled Mel spectrogram
    """
    mel = librosa.feature.melspectrogram(
        y=signal,
        sr=sr,
        n_mels=n_mels
    )
    mel_db = librosa.power_to_db(mel)
    return mel_db
