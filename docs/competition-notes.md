# Competition Notes

## Project

**AquaSense — Adaptive SONAR Transmission for AUVs**

## One-Line Positioning

AquaSense is a **software-defined SONAR transmitter payload** that adapts its waveform strategy to changing underwater conditions and target scenarios.

## What We Are Building

AquaSense is a **SONAR subsystem/payload**, not a complete AUV. The project focuses on adaptive transmission: selecting and generating different waveform families through software.

## Core Story

```text
Underwater / Mission Conditions
            ↓
      Adaptive Decision
            ↓
      Waveform Selection
            ↓
   Software Waveform Generation
            ↓
       SONAR Transmission
            ↓
      Signal Analysis / FFT
```

## System-Level Inputs

The broader architecture uses representative:

- Temperature
- Salinity
- Depth
- Turbidity
- Target motion / Doppler conditions

The MATLAB/Simulink figures demonstrate these changing inputs and the system-level adaptive architecture. They should be described as representative/modelled inputs unless backed by a physical measurement.

## Waveform Set

AquaSense includes:

- **LFM** — Linear Frequency Modulation.
- **HFM** — Hyperbolic Frequency Modulation; used as the Doppler-aware/resilient option in the moving-target demo.
- **PCP** — Phase-Coded Pulses.
- **Geometric Sweep** — additional software-defined sweep mode.

## Final Competition Demonstration

The final embedded demonstration uses an **ESP32** with a 1 MHz sampling configuration and a 250–270 kHz demonstration band.

```text
Target 0 — Stationary
LFM → PCP

Target 1 — Non-Stationary
HFM → LFM → PCP
```

The Python program receives the waveform samples over serial at 115200 baud and produces the combined time-domain and Hann-windowed FFT dashboard.

The target state is **software-commanded/simulated** because the current prototype has no SONAR receiver. It demonstrates adaptive transmission sequencing rather than physical target-motion detection.

## Demonstration Strengths

The strongest competition points are:

1. **Software-defined transmitter:** waveform behaviour is changed in firmware rather than by redesigning the transmitter for every waveform.
2. **Multiple waveform families:** LFM, HFM, PCP and geometric sweep are implemented.
3. **Target-state adaptation:** stationary and non-stationary cases use different sequences.
4. **Embedded + PC workflow:** ESP32 generation is connected to Python analysis through a simple serial protocol.
5. **Signal-processing verification:** the Python side explicitly demonstrates Hann-window processing followed by FFT.
6. **System-level scalability:** the same concept can progress toward DAC, filtering, amplification, transducer and receiver hardware.

## What Not to Claim

For technical accuracy:

- Do not claim that the current ESP32 prototype performs physical SONAR target detection.
- Do not claim that the pots/environmental sensors are driving the final ESP32 menu demo.
- Do not call the 250–270 kHz Python presentation spectrum a measured underwater spectrum.
- Do not claim HFM eliminates Doppler; describe it as a Doppler-aware/resilient waveform option.
- Do not claim quantitative low-power improvement without measurement.

## Presentation Sequence

A clean live demonstration is:

1. Show the ESP32/prototype hardware.
2. Connect the ESP32 to the laptop.
3. Run `AquaSense_Demo.py`.
4. Select **1. Target 0 — Stationary** and show `LFM → PCP`.
5. Show the combined waveform and `Hann Window → FFT` dashboard.
6. Select **2. Target 1 — Non-Stationary** and show `HFM → LFM → PCP`.
7. Explain that the target state is currently software-simulated and that the receiver/transducer stage is future work.

## Scope Boundary

The full system architecture may include ADC/environmental inputs, adaptive decision logic, waveform scheduling, DAC, low-pass filtering, amplifier/MOSFET stage, transducer, receiver and analysis. The final competition prototype demonstrates the digital waveform-generation, sequencing and visualization portion of that architecture.
