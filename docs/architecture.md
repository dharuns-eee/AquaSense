# AquaSense Architecture

AquaSense is a **real-time, software-defined SONAR transmitter payload** intended for integration into an Autonomous Underwater Vehicle (AUV). The architecture separates environmental-condition assessment from waveform generation so that the transmitter can adapt its acoustic output through embedded software.

> AquaSense is a SONAR payload/subsystem, not a complete AUV platform.

## System Flow

**Sense → Decide → Adapt → Transmit → Analyse**

The adaptation is performed on the transmit side. Environmental and mission inputs are interpreted by the controller, which selects a configured waveform mode before the signal is generated and transmitted.

## Input Layer

AquaSense considers representative environmental and mission inputs:

- Temperature
- Salinity
- Depth
- Turbidity
- Target motion / Doppler conditions

During early prototype validation, representative sensor-condition inputs may be used to exercise the decision logic before controlled underwater testing.

## Adaptive Decision Layer

The decision layer converts multiple input conditions into an operating state. A weighted model can be represented as:

$$S_i=\sum_{j=1}^{n}w_jx_j$$

where $x_j$ represents an input factor and $w_j$ represents its decision weight.

The waveform with the highest configured score can be represented as:

$$W^*=\arg\max_{W_i}S_i$$

A rule-based implementation can also be used for deterministic prototype testing. Exact thresholds and weights remain design parameters until validated experimentally.

## Waveform Layer

The selected state determines the waveform mode and associated parameters. The current design considers:

- **LFM** — Linear Frequency Modulation
- **HFM** — Hyperbolic Frequency Modulation
- **PCP** — Phase-Coded Pulses
- **Geometric Sweep**

The important architectural feature is that these modes are generated through the same software-defined transmitter path rather than requiring a separate fixed waveform transmitter for each mode.

## Digital Generation Layer

Once a waveform is selected, the embedded system prepares its digital samples. Precomputed Look-Up Tables (LUTs) can store frequently used waveform samples or parameterized tables.

DMA and hardware timers are then used to move samples to the DAC at a controlled update rate. This separates sample-transfer activity from repeated CPU intervention and supports deterministic waveform timing.

## Analog Transmission Layer

The digital samples are converted by the DAC and passed through the analog signal chain:

```text
DAC
 ↓
Low-Pass Filter
 ↓
Class-D Amplifier
 ↓
MOSFET Stage
 ↓
Underwater Acoustic Transducer
```

The electrical waveform can be inspected using an **oscilloscope** during prototype validation.

## Complete Signal Path

```text
Environmental / Mission Inputs
          ↓
   Adaptive Decision Logic
          ↓
    Waveform Selection
          ↓
 Software Waveform Generation
          ↓
        LUT / Buffer
          ↓
  DMA + Hardware Timer
          ↓
          DAC
          ↓
    Low-Pass Filtering
          ↓
   Class-D + MOSFET Stage
          ↓
   SONAR Transducer / Oscilloscope
          ↓
 FFT / Spectrogram / Performance Analysis
```

## Real-Time Execution

The architecture is designed so that time-sensitive waveform transmission is handled primarily by hardware peripherals:

1. The controller determines the waveform state.
2. Waveform samples are prepared or selected from a LUT.
3. A hardware timer establishes the sample/update timing.
4. DMA transfers samples to the DAC.
5. The analog chain conditions and amplifies the signal.
6. The acoustic transducer provides the underwater output.
7. Oscilloscope and digital analysis tools are used for verification and characterization.

## Low-Power Considerations

Low power is a supporting architectural objective. The design considers:

- DMA-based sample transfer instead of CPU-driven per-sample handling.
- LUTs to avoid unnecessary repeated waveform calculations.
- Hardware timers for deterministic timing.
- Efficient DSP operations where required.
- WFI-based CPU inactivity during periods where active processing is unnecessary.
- Controlled transmit activity through configured waveform timing and duty cycling.

## Architecture Boundaries

AquaSense focuses specifically on the **SONAR transmitter payload**. It does not claim to implement the complete AUV navigation, propulsion, mechanical structure or vehicle-level autonomy stack.

The payload interface is conceptually divided into:

- **Inputs:** environmental / mission condition information.
- **Processing:** adaptive waveform-selection and signal-generation logic.
- **Output:** acoustic transmission through the SONAR transducer.
- **Measurement:** oscilloscope and signal-analysis tools used during development.

## Current Status

This document describes the current prototype/design architecture. Hardware implementation, quantitative power measurements and controlled underwater measurements will be documented separately as validation progresses.
