#!/bin/bash

echo "================================"
echo " Audio Feature Extraction Runner "
echo "================================"

# Exit on first error
set -e

# Move to project root (script-safe)
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

echo "[1/5] Creating virtual environment..."
python -m venv venv

echo "[2/5] Activating virtual environment..."
source venv/Scripts/activate

echo "[3/5] Installing dependencies..."
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "[4/5] Ensuring graphs directory exists..."
mkdir -p graphs

echo "[5/5] Executing notebooks (graphs only)..."

cd notebooks

NOTEBOOKS=(
  "01_waveform.ipynb"
  "02_fft.ipynb"
  "03_spectrogram.ipynb"
  "04_mel_spectrogram.ipynb"
  "05_mfcc.ipynb"
)

for nb in "${NOTEBOOKS[@]}"; do
  echo "Running $nb ..."
  jupyter nbconvert \
    --execute \
    --to notebook \
    --inplace \
    "$nb"
done

cd ..

echo "================================"
echo " DONE — Graphs saved in /graphs "
echo "================================"
