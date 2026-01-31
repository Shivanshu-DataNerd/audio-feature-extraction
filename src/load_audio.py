"""
load_audio.py

Robust, format-agnostic audio loader for speech research.
Handles all common audio formats and normalizes paths safely.
"""

import librosa
import os
from typing import Tuple

SUPPORTED_EXTENSIONS = (".wav", ".ogg", ".flac", ".mp3", ".m4a", ".aac")

def load_audio(path: str) -> Tuple[list, int]:
    """
    Load an audio file in a robust, execution-independent way.

    Accepted inputs:
    - "sample.wav"
    - "data/sample.wav"
    - "../data/sample.wav"

    Parameters
    ----------
    path : str
        Audio file path (relative or filename only)

    Returns
    -------
    signal : np.ndarray
        Audio signal
    sr : int
        Sampling rate
    """

    # Project root = one level above src/
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Normalize input path
    path = path.replace("\\", "/").lstrip("./")

    # If only filename is given → assume data/
    if "/" not in path:
        path = f"data/{path}"

    # Remove accidental leading ../
    if path.startswith("../"):
        path = path[3:]

    full_path = os.path.abspath(os.path.join(project_root, path))

    if not full_path.lower().endswith(SUPPORTED_EXTENSIONS):
        raise ValueError(
            f"Unsupported audio format. Supported formats: {SUPPORTED_EXTENSIONS}"
        )

    if not os.path.exists(full_path):
        raise FileNotFoundError(f"Audio file not found: {full_path}")

    signal, sr = librosa.load(full_path, sr=None)
    return signal, sr
