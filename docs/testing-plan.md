# AquaSense Testing and Validation Plan

AquaSense uses staged validation so that the **current basic digital prototype demonstration** is clearly separated from the **planned final STM32G4 hardware demonstration and physical validation**.

## 1. Current Basic Digital Prototype — Completed

The current ESP32 + Python prototype verifies the embedded waveform-generation, serial communication and digital signal-processing path.

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

These checks validate the **basic software prototype**, not the final physical SONAR transmitter.

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

Verify the mathematical generator separately when required. It is retained in firmware as an additional waveform option.

## 3. Python Signal Processing

The current Python analysis performs:

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

The dashboard is intended for clear basic-prototype demonstration. Its controlled 0–500 kHz presentation spectrum must not be interpreted as a measured underwater acoustic spectrum.

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

The physical pots/environmental inputs are **not required for the current ESP32 basic demo**.

Future testing should verify:

- Sensor acquisition.
- Input normalization.
- Decision-state calculation.
- Waveform selection under known conditions.
- Repeatability across input changes.

## 6. Final STM32G4 Hardware Demonstration — Planned

The final hardware demonstration will replace the ESP32 digital prototype with an **STM32G4-based transmitter chain**.

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

The oscilloscope will be used to verify the physical electrical waveform at appropriate points in the transmitter chain.

Planned checks include:

- STM32G4 peripheral configuration.
- Deterministic waveform generation.
- DAC output waveform.
- Filtered waveform.
- MOSFET/power-stage operation.
- Amplifier output.
- Transducer/test-load interface.
- Oscilloscope waveform measurements.
- Measured frequency characteristics.
- Timing and repeatability.
- Power measurements where instrumentation is available.

## 7. Receiver and Target-Motion Validation — Planned

A receiver-enabled system should eventually evaluate:

- Echo acquisition.
- Real target observation.
- Target-motion estimation.
- Doppler-related behaviour.
- Adaptive waveform selection based on measured acoustic information.

The current ESP32 prototype does not perform these functions.

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
- **Basic digital prototype** — ESP32 waveform generation and Python analysis.
- **Final physical prototype / measurement** — STM32G4, DAC, analog/power chain and oscilloscope observations.
- **Underwater validation** — controlled acoustic tests.

Only the evidence appropriate to each category should be claimed.

## Current Status

The **ESP32 + Python basic digital prototype is completed for demonstration purposes**. The **final hardware demonstration is planned around the STM32G4 and oscilloscope-verified physical transmitter chain**. Receiver-based target detection, measured underwater performance and controlled underwater testing remain future validation stages.