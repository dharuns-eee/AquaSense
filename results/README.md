# Results

The `results/` directory separates **demonstration evidence** from future measured experimental results.

## Current Demonstration Evidence

The final digital prototype demonstrates:

- ESP32 waveform generation.
- Stationary sequence: `LFM → PCP`.
- Non-stationary sequence: `HFM → LFM → PCP`.
- Serial transfer to Python at 115200 baud.
- Combined time-domain visualization.
- Hann-windowed FFT calculation.
- 0–500 kHz presentation display.

The Python dashboard also includes a controlled presentation spectrum. This is **visualization data for the competition demo**, not a measured underwater acoustic spectrum.

## System-Level / Simulation Evidence

The MATLAB/Simulink material demonstrates the broader AquaSense architecture, including representative depth, temperature, salinity and turbidity profiles, adaptive parameters, waveform generation/scheduling and output analysis.

These figures should be treated as **model/simulation evidence** unless a figure is explicitly backed by a physical measurement.

## Future Physical Results

The repository can later contain:

- DAC captures.
- Filtered waveform captures.
- Amplifier/MOSFET measurements.
- Transducer measurements.
- Receiver-based target observations.
- FFT and spectrograms from measured signals.
- Processing-time measurements.
- Memory/DMA/timer observations.
- Power measurements.
- Controlled underwater test results.

## Recommended Result Record

| Field | Description |
|---|---|
| Test ID | Unique experiment identifier |
| Date | Measurement date |
| Setup | Hardware/software configuration |
| Inputs | Environmental or representative inputs |
| Target state | Stationary / non-stationary / other |
| Waveform | LFM / HFM / PCP / Geometric |
| Parameters | Frequency, duration, sampling and other settings |
| Instrumentation | Oscilloscope, analyser, power meter, etc. |
| Observation | Measured behaviour |
| Files | Related plots, captures or datasets |
| Status | Validated / requires review |

## Evidence Policy

AquaSense uses four evidence categories:

1. **Design** — intended architecture and algorithms.
2. **Simulation/model** — MATLAB/Simulink or other representative software behaviour.
3. **Prototype demonstration** — ESP32 + Python digital demonstration.
4. **Physical/underwater validation** — measured hardware or acoustic results.

Simulated, representative or presentation-only values must not be reported as physical measurements.

## Current Status

The active competition result is the **digital ESP32/Python demonstration**. Physical acoustic receiver/transducer validation, quantitative power measurements and controlled underwater testing remain future stages.
