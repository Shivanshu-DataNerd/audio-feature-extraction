"""
mfcc.py

Purpose:
--------
Extract Mel-Frequency Cepstral Coefficients (MFCCs).

Why MFCCs?
----------
MFCCs capture the spectral envelope of speech,
which is closely related to phonetic content.
"""

import librosa

def compute_mfcc(signal, sr, n_mfcc=13):
    """
    Compute MFCC features.

    Parameters
    ----------
    signal : np.ndarray
    sr : int
    n_mfcc : int
        Number of MFCC coefficients

    Returns
    -------
    mfcc : np.ndarray
        MFCC feature matrix
    """
    mfcc = librosa.feature.mfcc(
        y=signal,
        sr=sr,
        n_mfcc=n_mfcc
    )
    return mfcc
