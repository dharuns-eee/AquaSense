# AquaSense

**A Low-Power, Real-Time Adaptive Software-Defined SONAR Transmitter Payload for AUVs**

AquaSense is an adaptive SONAR transmitter payload/subsystem concept for autonomous underwater vehicles (AUVs). The system is designed to adapt its transmitted waveform according to target state and changing underwater operating conditions.

> **Prototype status:** The current implementation is a **basic digital prototype built with an ESP32 and Python** for demonstrating the adaptive waveform-generation and signal-processing workflow. The **final hardware demonstration will be implemented using an STM32G4** with the intended high-speed DAC, filtering, MOSFET/power stage, amplifier and oscilloscope verification.

## Current Basic Prototype

The ESP32-based prototype demonstrates the core software-defined SONAR transmission concept:

- ESP32 waveform generation.
- Software-commanded target-state selection.
- Stationary target sequence: `LFM → PCP`.
- Non-stationary target sequence: `HFM → LFM → PCP`.
- Serial transfer from ESP32 to Python at 115200 baud.
- Hann-windowed FFT processing.
- Combined time-domain and frequency-domain visualization.
- 0–500 kHz presentation display.

The current prototype is intentionally a reduced demonstration of the broader system architecture. A physical SONAR receiver/transducer chain is not connected in the ESP32 demonstration, so target state is software-commanded/simulated.

## Planned Final STM32G4 Hardware Demonstration

The final hardware demonstration is planned around an **STM32G4**, which will provide the embedded real-time control and waveform-generation platform for the physical transmitter subsystem.

The intended final hardware chain is:

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

The oscilloscope will be used to verify the electrical waveform at appropriate points in the physical transmitter chain. The ESP32 is **not** the final hardware platform.

## Adaptive Waveform Concept

AquaSense uses different waveform families for different operating conditions and target states:

- **LFM** — Linear Frequency Modulation.
- **HFM** — Hyperbolic Frequency Modulation, selected for Doppler-aware transmission scenarios.
- **PCP** — Phase-Coded Pulse, using an 8-chip phase code.
- **Geometric** — retained as part of the broader waveform library.

The current basic demonstration uses:

| Target state | Transmission sequence |
|---|---|
| Stationary | `LFM → PCP` |
| Non-stationary | `HFM → LFM → PCP` |

Environmental variables such as depth, temperature, salinity and turbidity remain part of the broader adaptive-system concept. The current ESP32 basic menu does not depend on physical potentiometer inputs.

## Current Basic Prototype Parameters

| Parameter | Value |
|---|---|
| Controller | ESP32 |
| Sampling rate | 1 MHz |
| Samples per waveform | 1000 |
| Waveform duration | 1 ms |
| Demonstration frequency band | 250–270 kHz |
| PCP carrier | 260 kHz |
| PCP code | `+ + + - - + - +` |
| Serial communication | 115200 baud |
| FFT processing | Hann window → FFT |
| Display range | 0–500 kHz |

The frequency-domain presentation includes controlled visualization data for the basic demonstration. It is **not a measured underwater acoustic spectrum**.

## Broader System Architecture

The complete AquaSense concept includes:

```text
Environmental Inputs + Target Information
                 ↓
        Adaptive Decision Logic
                 ↓
        Waveform Selection / Scheduling
                 ↓
              STM32G4
                 ↓
           High-Speed DAC
                 ↓
          Analog Filtering
                 ↓
       MOSFET / Amplifier Stage
                 ↓
          SONAR Transducer
                 ↓
       Underwater Acoustic Path
                 ↓
          Receiver / Analysis
                 ↓
             Oscilloscope
```

MATLAB/Simulink is used to represent and study the broader system-level concept, while the ESP32 + Python implementation provides the current basic prototype.

## Repository Structure

```text
AquaSense/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── competition-notes.md
│   ├── basic-demo.md
│   ├── hackathon-basic-demo.md
│   ├── testing-plan.md
│   └── waveform-selection.md
├── firmware/
│   ├── AquaSense_ESP32.ino
│   └── README.md
├── hardware/
│   └── README.md
├── signal-processing/
│   ├── AquaSense_Demo.py
│   └── README.md
└── results/
    ├── README.md
    ├── Figure_1.png
    ├── Figure_2.png
    └── AquaSense_Final_Demo.mp4
```

## Evidence and Technical Scope

AquaSense distinguishes between:

1. **Design/system concept** — intended final architecture and algorithms.
2. **Simulation/model** — MATLAB/Simulink and representative software behaviour.
3. **Basic prototype demonstration** — ESP32 + Python implementation.
4. **Final physical prototype / validation** — planned STM32G4-based hardware, physical transmitter chain and oscilloscope measurements.

Simulation values and controlled presentation data are not presented as physical measurements. Quantitative claims about acoustic output, power consumption, receiver performance or underwater operation require physical validation.

## Project Direction

The ESP32 prototype establishes and demonstrates the core adaptive software workflow. The next hardware stage is the **STM32G4-based final hardware demonstration**, integrating the waveform generator with the intended DAC, analog and power stages and verifying the electrical waveform with an oscilloscope.