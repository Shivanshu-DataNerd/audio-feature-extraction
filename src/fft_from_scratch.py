"""
fft_from_scratch.py

Purpose:
--------
Convert a time-domain signal into frequency domain using FFT.

Key idea:
---------
Speech is a mixture of many frequencies.
FFT helps us see which frequencies are present.
"""

import numpy as np

def compute_fft(signal):
    """
    Compute the Fast Fourier Transform of an audio signal.

    Parameters
    ----------
    signal : np.ndarray
        Time-domain audio signal

    Returns
    -------
    magnitude : np.ndarray
        Magnitude spectrum of the signal
    """
    fft = np.fft.fft(signal)
    magnitude = np.abs(fft)
    return magnitude
