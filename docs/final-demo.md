# Final AquaSense Prototype Specification

This document is the concise reference for the locked competition demonstration.

## Hardware

- ESP32 development board
- USB connection to laptop
- Current demo uses the ESP32 as a digital waveform generator and serial transmitter.

## Firmware

`firmware/AquaSense_ESP32.ino`

| Parameter | Final value |
|---|---:|
| Sampling frequency | 1 MHz |
| Duration | 1 ms |
| Samples | 1000 |
| F0 | 250 kHz |
| F1 | 270 kHz |
| PCP carrier | 260 kHz |
| PCP code | `+ + + - - + - +` |
| Serial | 115200 baud |

### Waveform generators

- LFM: 250 → 270 kHz linear sweep.
- HFM: 250 → 270 kHz hyperbolic sweep.
- PCP: 260 kHz carrier with 8-chip phase code.
- Geometric sweep: retained but not used in final target sequences.

### Target commands

`0` selects the stationary sequence.

`1` selects the non-stationary sequence.

## Final Sequences

### Target 0 — Stationary

**LFM → PCP**

### Target 1 — Non-Stationary

**HFM → LFM → PCP**

The target state is software-simulated in this prototype because no physical SONAR receiver is connected.

## Python Analysis

`signal-processing/AquaSense_Demo.py`

The Python program:

1. Connects to the ESP32 at 115200 baud.
2. Sends target command `0` or `1`.
3. Receives the complete waveform sequence.
4. Validates the received sequence.
5. Displays the combined time-domain transmission.
6. Applies a Hann window before FFT calculation.
7. Displays the combined frequency-domain presentation from 0–500 kHz.

The PCP is shown as its 8-chip phase-code structure in the time-domain presentation.

## FFT Presentation Note

The Python script calculates an actual Hann-windowed FFT from the received samples. For the competition dashboard, a controlled presentation spectrum is then generated so that spectral activity is visible across the requested 0–500 kHz display and around the 250–270 kHz demonstration band.

Therefore, the final plotted 0–500 kHz presentation spectrum is **not a measured underwater acoustic spectrum**.

## System-Level Context

The broader AquaSense architecture remains:

```text
Environmental Inputs
       ↓
Adaptive Decision Logic
       ↓
Waveform Selection
       ↓
Waveform Generation
       ↓
DAC
       ↓
Low-Pass Filter
       ↓
Amplifier / MOSFET Stage
       ↓
SONAR Transducer
       ↓
Receiver / Oscilloscope / FFT
```

The MATLAB/Simulink material represents this broader system concept. The final ESP32/Python implementation is the reduced competition prototype.

## Environmental Inputs

Temperature, salinity, depth and turbidity remain part of the **system-level adaptive concept**. The final ESP32 menu demonstration does not depend on the physical pots, so the demo remains reliable even when those inputs are not available.

## Technical Honesty

The prototype should be presented as:

> **A software-defined adaptive SONAR transmission demonstration with embedded waveform generation, target-state sequencing and Hann-windowed FFT visualization.**

Do not claim physical echo-based target detection, measured underwater acoustic performance or measured power savings unless those stages are subsequently validated.
