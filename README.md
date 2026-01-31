# Audio Feature Extraction from Scratch

## Overview
This project demonstrates how raw speech audio is transformed into
meaningful features used in Speech and Audio AI systems.

The goal is to understand the signal processing pipeline,
not just to use existing libraries.

---

## Signal Processing Pipeline

1. Raw waveform (time domain)
2. Fast Fourier Transform (frequency domain)
3. Spectrogram (time–frequency representation)
4. Mel Spectrogram (human auditory scale)
5. MFCCs (compact speech representation)

---

## What is FFT?
FFT (Fast Fourier Transform) converts a time-domain signal
into its frequency components.
Speech consists of multiple frequencies produced by vocal cords
and vocal tract resonances.

---

## Why Mel Scale?
Human hearing is nonlinear.
We perceive low frequencies more precisely than high frequencies.
The Mel scale models this perception, making features
more meaningful for speech models.

---

## Why MFCCs are useful for Speech?
MFCCs represent the spectral envelope of speech,
which contains phonetic information.
They are compact, robust to noise,
and widely used in speech recognition and emotion detection.

---

## Applications
- Automatic Speech Recognition (ASR)
- Speech Emotion Recognition
- Speaker Identification
- Healthcare and Assistive Technologies

---

## Author
Shivanshu Pal  
MSc Data Science  
Aspiring PhD Researcher (Speech / Audio AI)
Email: contactshiva7@gmail.com

