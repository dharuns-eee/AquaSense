# Testing Plan

AquaSense uses staged validation so that the final competition demonstration can be separated from future physical SONAR validation.

## 1. Final Digital Demonstration — Completed Target

The current prototype verifies the embedded waveform-generation and serial path.

### Checks

- ESP32 starts correctly.
- Python connects at the configured serial port and 115200 baud.
- Target command `0` produces `LFM → PCP`.
- Target command `1` produces `HFM → LFM → PCP`.
- Each waveform contains 1000 samples.
- Waveform names and sequence boundaries are parsed correctly.
- Python applies a Hann window before its FFT calculation.
- Dashboard displays the combined time-domain sequence.
- Dashboard provides the 0–500 kHz presentation axis.

## 2. Waveform Checks

### LFM

Verify the generated linear sweep across the configured 250–270 kHz demonstration band.

### HFM

Verify the generated hyperbolic sweep across the same demonstration band.

### PCP

Verify the 260 kHz carrier and the 8-chip code:

```text
+ + + - - + - +
```

### Geometric Sweep

Verify the mathematical generator separately when required. It is retained in firmware but is not part of the two final target sequences.

## 3. Python Signal Processing

The Python analysis performs:

```text
Received signal
      ↓
Hann window
      ↓
rFFT
      ↓
Magnitude
      ↓
Frequency-domain presentation
```

The dashboard is intended for clear competition demonstration. Its controlled 0–500 kHz presentation spectrum must not be interpreted as a measured underwater acoustic spectrum.

## 4. Target-State Demonstration

The current target state is software-commanded rather than physically detected.

```text
Menu choice
   ↓
0 or 1 command
   ↓
ESP32 selects sequence
   ↓
Waveforms generated
   ↓
Serial transfer
   ↓
Python validation + display
```

A future receiver-enabled implementation can replace the command with target-motion information derived from received acoustic data.

## 5. Environmental Adaptation — System-Level Validation

Temperature, salinity, depth and turbidity are part of the broader AquaSense architecture and MATLAB/Simulink model. Their thresholds/weights are design parameters until experimentally validated.

The physical pots/environmental inputs are **not required for the final ESP32 competition demo**.

Future testing should verify:

- Sensor acquisition.
- Input normalization.
- Decision-state calculation.
- Waveform selection under known conditions.
- Repeatability across input changes.

## 6. Physical Hardware Validation — Future

The intended physical transmitter chain remains:

```text
Embedded Controller
      ↓
DAC
      ↓
Low-Pass Filter
      ↓
Amplifier / MOSFET Stage
      ↓
Transducer
      ↓
Oscilloscope / Receiver
```

Future tests should measure the electrical output at each appropriate stage before making acoustic-performance claims.

## 7. Power Evaluation — Future

Low power is a supporting design objective. Actual measurements should use suitable instrumentation and report the test conditions.

Do not claim a quantitative power saving from the current software demonstration alone.

## 8. Underwater Validation — Future

A controlled underwater test should eventually evaluate:

- Real environmental inputs.
- Adaptive waveform selection.
- Physical acoustic transmission.
- Receiver-based target observation.
- Doppler-related behaviour.
- Repeatability.
- Power consumption.

## Evidence Rules

AquaSense distinguishes:

- **Design** — intended architecture and decision strategy.
- **Simulation/model** — MATLAB/Simulink behaviour using representative inputs.
- **Digital prototype** — ESP32 waveform generation and Python analysis.
- **Physical measurement** — oscilloscope/DAC/amplifier/transducer observations.
- **Underwater validation** — controlled acoustic tests.

Only the evidence appropriate to each category should be claimed.

## Current Status

The final digital demonstration is the active competition prototype. Physical receiver/transducer validation, measured power data and controlled underwater testing remain future validation stages.
