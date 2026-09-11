# AquaSense

## Adaptive SONAR Transmission for AUVs

AquaSense is a **software-defined SONAR transmitter payload/subsystem** intended for integration into an Autonomous Underwater Vehicle (AUV). The project explores how waveform selection can adapt to changing underwater conditions and target scenarios instead of relying on one fixed transmission strategy.

> **Scope:** AquaSense is the SONAR payload/subsystem, not a complete AUV.

## Core Idea

```text
Changing Underwater Conditions / Mission State
                    ↓
          Adaptive Decision Logic
                    ↓
             Waveform Selection
                    ↓
        Software-Defined Generation
                    ↓
             Transmission
                    ↓
          Signal Processing / FFT
```

At system level, AquaSense considers representative **temperature, salinity, depth, turbidity and target-motion/Doppler conditions**. The MATLAB/Simulink material models these inputs and the broader adaptive transmitter architecture.

The final competition prototype intentionally focuses on the **software-defined waveform-generation and analysis path**.

## Final Prototype

The final demonstration uses an **ESP32** connected to a computer over USB serial.

### Final firmware parameters

| Parameter | Value |
|---|---:|
| Sampling frequency | **1 MHz** |
| Waveform duration | **1 ms** |
| Samples per waveform | **1000** |
| Demonstration band | **250–270 kHz** |
| PCP carrier | **260 kHz** |
| Serial baud rate | **115200** |

### Final target sequences

**Target 0 — Stationary**

```text
LFM → PCP
```

**Target 1 — Non-Stationary**

```text
HFM → LFM → PCP
```

The target state is **software-commanded/simulated** in this prototype. The ESP32 does not have a physical SONAR receiver, so target motion is not being detected from a measured echo. A complete SONAR implementation would use received acoustic information to infer target motion and Doppler-related behaviour.

## Waveforms

The firmware contains four waveform generators:

- **LFM — Linear Frequency Modulation:** 250 kHz → 270 kHz linear sweep.
- **HFM — Hyperbolic Frequency Modulation:** sweep across the 250–270 kHz demonstration band; used in the non-stationary sequence as the Doppler-aware/resilient option.
- **PCP — Phase-Coded Pulse:** 260 kHz carrier with 8-chip code `+ + + - - + - +`.
- **Geometric Sweep:** additional non-linear sweep generator retained in firmware but not used in the two final target sequences.

The waveform equations are implemented directly in the ESP32 firmware.

## Python Demonstration

`signal-processing/AquaSense_Demo.py` receives the ESP32 transmission and displays one dashboard containing:

1. Combined time-domain transmission.
2. Waveform labels and sequence information.
3. PCP as an 8-chip phase-code display.
4. **Hann Window → FFT** processing flow.
5. Combined FFT presentation from **0–500 kHz**.
6. Highlighted **250–270 kHz demonstration band**.
7. Different presentation patterns for stationary and non-stationary modes.

The FFT processing applies a Hann window before calculating the real FFT magnitude.

### Important demonstration note

The Python dashboard includes a **controlled presentation spectrum** to make the 0–500 kHz demonstration visually clear. It is not a measured underwater acoustic spectrum and must not be reported as physical acoustic measurement data.

## System-Level Architecture

The broader intended transmitter chain is:

```text
Environmental / Mission Inputs
          ↓
   Adaptive Decision Logic
          ↓
    Waveform Selection
          ↓
 Software Waveform Generation
          ↓
     LUT / Sample Buffer
          ↓
   DMA + Hardware Timer
          ↓
          DAC
          ↓
    Low-Pass Filter
          ↓
 Class-D + MOSFET Stage
          ↓
 SONAR Acoustic Transducer
          ↓
 Oscilloscope / FFT / Spectrogram
```

The MATLAB/Simulink material represents this broader system architecture. The ESP32/Python implementation is the **final reduced competition demonstration**.

## Adaptive Selection Concept

The system-level design can combine normalized condition factors with a weighted model:

$$S_i=\sum_{j=1}^{n}w_jx_j$$

and select:

$$W^*=\arg\max_{W_i}S_i$$

For the final demo, the environmental-input portion is not used to drive the ESP32 menu. Instead, the demonstration directly exercises the two target-state sequences so that the adaptive transmission concept can be shown reliably.

Environmental thresholds and waveform-selection performance remain design/validation items rather than experimentally proven claims.

## Running the Final Demo

Install the required Python packages:

```bash
pip install pyserial numpy matplotlib
```

Connect the ESP32 and make sure the Arduino Serial Monitor is closed. The current Python configuration uses **COM9**.

Run:

```bash
python signal-processing/AquaSense_Demo.py
```

Menu:

```text
1. Target 0 - Stationary
2. Target 1 - Non-Stationary
3. Quit
```

## Hardware Direction

The complete payload architecture is intended to progress toward:

```text
Embedded Controller → DAC → Low-Pass Filter
→ Amplifier / MOSFET Stage → Transducer
→ Measurement / Receiver
```

The present ESP32 prototype demonstrates digital waveform generation and serial analysis; it does **not** claim completed physical acoustic transmission or receiver-based target detection.

## Low-Power Design Intent

Low power is a supporting AUV-oriented objective. The broader architecture considers LUTs, DMA, hardware timers, efficient DSP and controlled CPU activity. No quantitative power advantage is claimed without measurement.

## Validation Philosophy

AquaSense separates:

- **Design:** intended system architecture and adaptive strategy.
- **Simulation:** MATLAB/Simulink representative system behaviour.
- **Prototype demonstration:** ESP32 waveform generation and Python visualization.
- **Physical validation:** future DAC/transducer/receiver and controlled underwater measurements.

Simulated or presentation-only values are not presented as measured underwater results.

## Repository Structure

```text
AquaSense/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── competition-notes.md
│   ├── final-demo.md
│   ├── hackathon-demo.md
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
├── media/
│   ├── README.md
│   └── captions.md
└── results/
    └── README.md
```

## Team

**Team WAVELET**  
Chennai Institute of Technology

## License

Academic, prototype and hackathon project. Add an appropriate open-source license before external reuse if required.
