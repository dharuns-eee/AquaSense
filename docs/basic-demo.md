# AquaSense Basic Prototype Demo Specification

This document describes the **current basic digital prototype demonstration**. It must not be presented as the final hardware demonstration.

## Current Basic Prototype Hardware

- ESP32 development board
- USB connection to laptop
- Python host program for serial reception and visualization

The current ESP32 implementation is a reduced software/serial prototype used to demonstrate waveform generation, adaptive target-state sequencing and signal-processing visualization.

## Planned Final Hardware Demonstration

The **final AquaSense hardware demonstration will be implemented using an STM32G4 and a physical transmitter chain**, with an oscilloscope used to verify the electrical waveform.

The intended final chain is:

```text
STM32G4
   ↓
High-Speed DAC
   ↓
Low-Pass Filter
   ↓
MOSFET Switching / Power Stage
   ↓
Amplifier
   ↓
SONAR Transducer / Test Load
   ↓
Oscilloscope
```

The STM32G4-based stage is the planned final hardware direction. The current ESP32/Python demonstration does not contain this physical chain.

## Current Prototype Firmware

`firmware/AquaSense_ESP32.ino`

| Parameter | Current basic prototype |
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
- Geometric sweep: retained as an additional software-defined generator.

### Target commands

`0` selects the stationary sequence.

`1` selects the non-stationary sequence.

## Basic Prototype Sequences

### Target 0 — Stationary

**LFM → PCP**

### Target 1 — Non-Stationary

**HFM → LFM → PCP**

The target state is software-simulated in the current prototype because no physical SONAR receiver is connected.

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

The Python script calculates an actual Hann-windowed FFT from the received samples. For the dashboard, a controlled presentation spectrum is then generated so that spectral activity is visible across the requested 0–500 kHz display and around the 250–270 kHz demonstration band.

Therefore, the plotted 0–500 kHz presentation spectrum is **not a measured underwater acoustic spectrum**.

## System-Level Context

The broader AquaSense architecture remains:

```text
Environmental Inputs + Target Information
       ↓
Adaptive Decision Logic
       ↓
Waveform Selection
       ↓
STM32G4
       ↓
High-Speed DAC
       ↓
Low-Pass Filter
       ↓
MOSFET / Amplifier Stage
       ↓
SONAR Transducer
       ↓
Oscilloscope / Receiver / FFT
```

The MATLAB/Simulink material represents this broader system concept. The ESP32/Python implementation is only the **current basic prototype**.

## Environmental Inputs

Temperature, salinity, depth and turbidity remain part of the **system-level adaptive concept**. The current ESP32 menu demonstration does not depend on physical potentiometer inputs.

## Technical Honesty

The current prototype should be presented as:

> **A basic software-defined adaptive SONAR transmission demonstration with embedded waveform generation, target-state sequencing and Hann-windowed FFT visualization.**

The **final hardware demonstration** is planned around the STM32G4 transmitter chain and oscilloscope-based electrical verification.

Do not claim physical echo-based target detection, measured underwater acoustic performance or measured power savings unless those stages are subsequently validated.