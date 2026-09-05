# Competition Notes

## Project

**AquaSense: Adaptive SONAR for AUVs**

## One-Line Positioning

AquaSense is a **real-time, software-defined SONAR transmitter payload** that dynamically selects suitable acoustic waveforms for changing underwater conditions.

## What We Are Building

AquaSense is a **SONAR subsystem/payload intended to be integrated into an AUV**, not a complete AUV platform.

The project focuses on the transmit side of underwater sensing:

```text
Environmental / Mission Conditions
              ↓
       Adaptive Decision Logic
              ↓
        Waveform Selection
              ↓
      Software-Defined Generation
              ↓
       SONAR Transmitter Payload
```

## Core Loop

**Sense → Decide → Adapt → Transmit → Analyse**

The key idea is to move waveform selection into embedded software so that the transmitter is not limited to a single fixed waveform.

## Main Innovation Areas

### 1. Real-Time Adaptive SONAR

The transmitter considers changing operating conditions and selects a configured waveform mode rather than always using one fixed transmission strategy.

### 2. Software-Defined Waveforms

The same transmitter hardware can support multiple waveform families:

- LFM
- HFM
- Phase-Coded Pulses
- Geometric Sweep

### 3. Environment-Aware Waveform Selection

Temperature, salinity, depth, turbidity and target-motion/Doppler-related conditions can be used as inputs to the configured decision layer.

### 4. Hardware-Assisted Transmission

DMA, hardware timers and LUT-based sample generation are used to support deterministic real-time waveform streaming to the DAC.

### 5. Low-Power Embedded Design

Efficient peripheral usage, LUTs, DSP capabilities and controlled CPU activity support the low-power objective of an AUV-oriented payload.

## What Makes the Approach Different?

A fixed transmitter generally follows a predefined waveform path. AquaSense is designed around the ability to change the waveform mode through firmware:

```text
Conventional approach
→ Fixed waveform
→ Fixed transmission behaviour

AquaSense approach
→ Sense conditions
→ Evaluate decision rules
→ Select waveform
→ Generate selected waveform
→ Transmit through shared hardware
```

## Competition Positioning

For demonstrations and competitions, the strongest story is the **adaptive transmit capability**, with low-power implementation as a supporting engineering advantage.

The project should emphasize:

- The transmitter is adaptive.
- Waveforms are software-defined.
- Multiple environmental/mission factors can influence selection.
- The same hardware supports multiple waveform modes.
- Embedded hardware assists real-time waveform delivery.
- Measurements will be used to validate the design as testing progresses.

## Scope Boundary

AquaSense does not claim to implement the complete AUV. Vehicle navigation, propulsion, mechanical design and full vehicle autonomy are outside the current SONAR payload scope.

## Evidence Policy

Only measured or otherwise validated experimental results should be added as results. Design targets, simulations, representative inputs, planned tests and future work should be clearly labelled.

Avoid presenting an intended waveform-selection rule as proof of acoustic performance until it has been experimentally tested.

## Demonstration Story

A concise project demonstration can follow this sequence:

1. Show the SONAR payload hardware.
2. Provide representative environmental-condition inputs.
3. Show the current decision state.
4. Show the selected waveform mode.
5. Generate the waveform on the embedded controller.
6. Stream the samples through DMA and hardware timing.
7. Inspect the physical waveform with the oscilloscope.
8. Analyse the waveform using FFT or spectrogram tools.

## Current Documentation Status

The repository currently contains architecture, waveform-selection, firmware, hardware, signal-processing and testing documentation. Media and experimental result files will be added separately when the corresponding assets and measurements are available.
