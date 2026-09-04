# AquaSense

**Adaptive SONAR for Autonomous Underwater Vehicles (AUVs)**

AquaSense is a low-power, real-time, software-defined SONAR transmitter payload designed for Autonomous Underwater Vehicles (AUVs). The system is designed to sense changing underwater conditions, select an appropriate transmit waveform, generate it on an embedded controller, and adapt transmission while considering available battery power.

## Core Idea

**Sense → Decide → Adapt → Transmit → Analyse & Feedback**

AquaSense considers mission factors such as:

- Temperature
- Salinity
- Depth
- Turbidity
- Target motion / Doppler conditions
- Battery level

The adaptive decision system can select among software-defined waveforms such as:

- **LFM** — Linear Frequency Modulation
- **HFM** — Hyperbolic Frequency Modulation
- **PCP** — Phase-Coded Pulses
- **Geometric Sweep**

## System Architecture

```text
Environmental / Mission Inputs
          ↓
   Adaptive Decision Logic
          ↓
    Waveform Selection
          ↓
  LUT + DMA + Hardware Timer
          ↓
          DAC
          ↓
    Low-Pass Filtering
          ↓
   Class-D + MOSFET Stage
          ↓
   SONAR Transducer / Payload
          ↓
 FFT / Spectrogram / Performance Analysis
          ↓
      Closed-Loop Feedback
```

## Hardware

- STM32G4-series MCU
- SAR ADC
- 12-bit high-speed DAC
- Low-pass filter
- Class-D amplifier + MOSFET
- Underwater acoustic transducer

## Software & Signal Processing

- Embedded C
- Adaptive waveform-selection logic
- LFM, HFM, PCP and geometric-sweep generation
- DMA and hardware timers for waveform transmission
- Look-Up Tables (LUTs) for fast waveform switching
- NVIC priority interrupts
- CMSIS-DSP / FPU-based processing
- WFI-based CPU duty-cycling
- FFT and spectrogram analysis

## Adaptive Decision Concept

A weighted decision model can be represented as:

$$
S_i = \sum_{j=1}^{n} w_j x_j
$$

where $x_j$ represents an input factor and $w_j$ represents its decision weight.

The selected waveform can be represented as:

$$
W^* = \arg\max_{W_i} S_i
$$

These equations describe the design approach; parameter values and experimental performance are documented separately as testing progresses.

## Power-Aware Operation

The design focuses on reducing unnecessary transmit and processing activity in an AUV-constrained power environment.

For a transmit interval:

$$
E_{\text{tx}} = P_{\text{tx}} \times T_{\text{tx}}
$$

For duty-cycled transmission:

$$
P_{\text{avg}} \approx D\,P_{\text{tx}}
$$

where $D$ is the fraction of time spent transmitting.

## Current Prototype Direction

The prototype uses embedded waveform generation and hardware-assisted transmission, with sensor-condition inputs available for adaptive decision testing. Oscilloscope-based inspection is used for physical waveform verification.

Real-water testing, quantitative power measurements, and AUV integration are planned next steps.

## Project Status

This repository documents the AquaSense design, embedded implementation, signal-processing approach, and ongoing prototype work. Experimental results are added as they are validated.

## Team

**Team WAVELET**  
Chennai Institute of Technology

## License

This project is intended for academic, prototype, and hackathon development. Add an appropriate open-source license before external reuse if required.
