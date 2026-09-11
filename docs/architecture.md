# AquaSense Architecture

AquaSense is a **real-time, software-defined SONAR transmitter payload** intended for integration into an Autonomous Underwater Vehicle (AUV). The project separates the full system architecture from the current competition prototype so that the repository clearly distinguishes design intent from what is currently demonstrated.

> **AquaSense is a SONAR payload/subsystem, not a complete AUV.**

## System Concept

**Sense → Decide → Select → Generate → Transmit → Analyse**

At system level, environmental and mission information can influence the adaptive decision layer. The selected waveform is then generated and passed through the intended transmitter chain.

```text
Environmental / Mission Inputs
          ↓
   Adaptive Decision Logic
          ↓
    Waveform Selection
          ↓
 Software Waveform Generation
          ↓
   DAC + Analog Front-End
          ↓
 SONAR Transducer / Test Load
          ↓
 FFT / Spectrogram / Analysis
```

## Environmental Inputs

The system-level design considers:

- Temperature
- Salinity
- Depth
- Turbidity
- Target motion / Doppler conditions

The environmental profiles shown in the MATLAB/Simulink material are **representative system-level inputs**. They demonstrate how changing underwater conditions can feed an adaptive architecture; they are not claimed as measured sensor data from the final ESP32 demonstration.

## Adaptive Decision Layer

The system-level decision concept can combine multiple normalized factors using a weighted model:

$$S_i=\sum_{j=1}^{n}w_jx_j$$

and select:

$$W^*=\arg\max_{W_i}S_i$$

For deterministic prototype demonstrations, explicit rule-based states can also be used. Thresholds and weights remain configurable design parameters until experimentally validated.

## Waveform Set

AquaSense supports four software-defined waveform generators:

| Waveform | Description |
|---|---|
| **LFM** | Linear Frequency Modulation; frequency increases linearly across the configured band. |
| **HFM** | Hyperbolic Frequency Modulation; used as the Doppler-aware/resilient sweep option in the moving-target demonstration. |
| **PCP** | Phase-Coded Pulse; 260 kHz carrier with an 8-chip code `+ + + - - + - +` in the final ESP32 demo. |
| **Geometric Sweep** | Non-linear frequency sweep retained as an additional software-defined generator. |

## Final ESP32 Demonstration

The final competition prototype uses an **ESP32** as the waveform-generation and serial-streaming controller.

### Fixed demonstration parameters

- Sampling frequency: **1 MHz**
- Waveform duration: **1 ms**
- Samples per waveform: **1000**
- Demonstration band: **250–270 kHz**
- PCP carrier: **260 kHz**
- Serial interface: **115200 baud**

### Target 0 — Stationary

```text
LFM → PCP
```

### Target 1 — Non-Stationary

```text
HFM → LFM → PCP
```

The target state in this prototype is **software-commanded/simulated**. There is no physical SONAR receiver in the final demo, so the ESP32 does not infer target motion from a measured echo. In a complete SONAR implementation, target motion would be inferred from received acoustic data and Doppler-related changes.

## Digital Waveform Path

The final ESP32 firmware generates floating-point samples mathematically and streams them over USB serial to the Python demonstration.

```text
Python command
      ↓
ESP32 target sequence
      ↓
LFM / HFM / PCP samples
      ↓
USB Serial @ 115200
      ↓
Python receiver
      ↓
Time-domain display
```

The final firmware also contains the geometric-sweep generator, although the two final target sequences do not use it.

## System-Level Hardware Architecture

The broader transmitter design remains:

```text
STM32G4 / Embedded Controller
          ↓
      ADC / Inputs
          ↓
 Adaptive Decision Logic
          ↓
 Waveform LUT / Generation
          ↓
        High-Speed DAC
          ↓
     Low-Pass Filter
          ↓
 Class-D + MOSFET Stage
          ↓
 SONAR Acoustic Transducer
          ↓
 Oscilloscope / Analysis
```

This is the **intended full payload architecture**. The final ESP32 demo is a reduced software/serial prototype used to demonstrate waveform generation, target-state sequencing and signal visualization.

## Signal Processing

The Python demonstration applies a Hann window before the computational FFT:

$$w[n]=0.5\left(1-\cos\frac{2\pi n}{N-1}\right)$$

followed by:

```text
Received samples
      ↓
Hann window
      ↓
FFT
      ↓
Magnitude spectrum
      ↓
Combined visualization
```

The dashboard presents a **0–500 kHz** frequency axis and highlights the 250–270 kHz demonstration band.

The Python program also creates a controlled presentation spectrum so that the dashboard has visible spectral activity across the requested 0–500 kHz range. That presentation spectrum is **not a measured underwater acoustic spectrum**.

## Low-Power Design Intent

Low power remains a system-level design objective. The broader architecture considers LUT-based generation, DMA, hardware timers, efficient DSP and controlled CPU activity. Quantitative power claims should only be added after measurement.

## Architecture Boundary

The repository distinguishes three levels:

1. **System architecture** — environmental sensing, adaptive decision logic, waveform selection, DAC/analog chain and acoustic output.
2. **MATLAB/Simulink system model** — representative environmental inputs, adaptive parameters, waveform scheduling and signal-path simulation.
3. **Final competition prototype** — ESP32 waveform generation + serial streaming + Python Hann/FFT visualization with software-simulated target states.

Keeping these boundaries explicit prevents the prototype from being presented as a completed underwater SONAR receiver/transmitter system.

## Validation Status

The current prototype demonstrates the digital transmission sequence and signal-processing visualization. Physical transducer output, receiver-based target detection, quantitative power measurements and controlled underwater validation remain separate future validation stages.
