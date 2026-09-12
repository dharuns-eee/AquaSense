# Signal Processing

The current AquaSense signal-processing path receives waveform samples from the **ESP32 basic prototype** and provides a clear time-domain and frequency-domain demonstration.

## Current Basic Prototype Workflow

```text
ESP32 waveform samples
        ↓
Serial reception
        ↓
Combined time-domain sequence
        ↓
Hann window
        ↓
Real FFT
        ↓
Magnitude spectrum
        ↓
0–500 kHz presentation
```

## Current Python Program

`AquaSense_Demo.py` uses:

- `pyserial` for ESP32 serial communication.
- `numpy` for numerical processing and FFT.
- `matplotlib` for the dashboard.

Install:

```bash
pip install pyserial numpy matplotlib
```

Run:

```bash
python signal-processing/AquaSense_Demo.py
```

## Serial Interface

The current basic demo configuration is:

```text
Port: COM9
Baud: 115200
```

The Python program sends:

```text
0 → Stationary
1 → Non-Stationary
```

The ESP32 returns a simple structured stream containing the target state, waveform names, samples and transmission boundaries.

## Hann Window + FFT

The program applies a Hann window before the FFT:

```text
signal
  ↓
Hann window
  ↓
windowed signal
  ↓
rFFT
  ↓
|X(f)|
```

The implementation uses NumPy's `np.hanning()` and `np.fft.rfft()` functions.

## Basic Prototype Dashboard

The dashboard shows:

- Combined transmission in the time domain.
- LFM/HFM waveform sections.
- PCP as an 8-chip phase-code display.
- `Hann Window → FFT` processing flow.
- Combined FFT presentation from 0 to 500 kHz.
- 250–270 kHz demonstration band.
- Legends and sequence labels.

The time-domain plot reduces displayed chirp samples for visual readability, while the FFT calculation uses the received signal data.

## Demonstration Spectrum

The Python program calculates the actual Hann-windowed FFT magnitude from the received samples. It then creates a **controlled presentation spectrum** for the basic prototype dashboard so that the requested 0–500 kHz range has visible spectral structure and a clear 250–270 kHz demonstration region.

This presentation spectrum is **not a measured underwater acoustic spectrum** and should not be reported as one.

## Current Target Sequences

```text
Target 0 — Stationary
LFM → PCP

Target 1 — Non-Stationary
HFM → LFM → PCP
```

## Analysis Scope

The current program demonstrates digital waveform generation, serial acquisition, sequence validation and frequency-domain visualization. Physical receiver processing, echo-based target detection, underwater acoustic measurement and measured transducer spectra are future validation stages.

## Planned Final Hardware Measurement

The final physical demonstration will use the **STM32G4-based transmitter chain**, with an oscilloscope used to verify the electrical waveform after the appropriate DAC, filtering and power/amplifier stages.