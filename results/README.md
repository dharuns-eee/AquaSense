# Results

The `results/` directory is reserved for **validated AquaSense measurements, experiment records and analysis outputs**. It is intentionally kept separate from design documentation so that measured evidence can be distinguished from planned behaviour and design assumptions.

## Why This Folder Matters

AquaSense contains adaptive waveform-selection logic, embedded waveform generation and a physical transmitter chain. The results directory will eventually provide evidence for how these parts behave when tested.

The repository should not claim experimental performance before the corresponding measurement has been completed.

## Planned Result Categories

### 1. Waveform Generation

Results may include captures and data for:

- LFM generation.
- HFM generation.
- Phase-Coded Pulse generation.
- Geometric-sweep generation.

Possible checks include waveform shape, timing, frequency progression and sample-generation accuracy.

### 2. Adaptive Waveform Selection

The adaptive logic can be evaluated using representative input conditions.

A future result record may contain:

```text
Input Conditions
      ↓
Expected Decision State
      ↓
Actual Decision State
      ↓
Selected Waveform
      ↓
Observed Output
```

This will help demonstrate whether the implemented decision rules produce the intended waveform-selection behaviour.

### 3. Oscilloscope Measurements

Physical waveform captures may be added for the transmitter chain, including:

- DAC output.
- Filtered analog output.
- Amplifier-stage output where measurable.
- SONAR transducer / oscilloscope test setup.
- Waveform-mode comparisons.

Each measurement should identify the relevant test condition and measurement point.

### 4. FFT and Spectrum Results

Frequency-domain results may include:

- FFT plots.
- Spectrum analysis.
- Dominant-frequency observations.
- Frequency-sweep verification.
- Comparison between expected and measured spectral behaviour.

### 5. Spectrogram Results

Spectrograms can be used to visualize time-varying frequency content, particularly for LFM, HFM and geometric-sweep signals.

Potential records may compare the configured sweep with the measured output.

### 6. Embedded Performance

Once the firmware is measured on hardware, this directory may contain observations related to:

- Processing time.
- DMA activity.
- Timer-driven waveform transmission.
- CPU activity during transmission.
- Memory usage where relevant.

### 7. Power Measurements

Low-power operation is part of the project objective. Validated measurements may include:

- MCU activity during waveform generation.
- Transmission-stage power.
- Average transmission power.
- Continuous versus duty-cycled operation.

Power values should always include the measurement conditions and instrumentation used.

### 8. Controlled Underwater Tests

Future underwater experiments may record:

- Test environment.
- Sensor/input conditions.
- Selected waveform.
- Transmission configuration.
- Measurement setup.
- Observed waveform characteristics.
- Repeatability across test runs.

## Recommended Result Format

Each experiment should ideally record:

| Field | Description |
|---|---|
| Test ID | Unique experiment identifier |
| Date | Date of measurement |
| Setup | Hardware/software configuration |
| Inputs | Environmental or representative input conditions |
| Waveform | Selected waveform mode |
| Parameters | Relevant waveform parameters |
| Instrumentation | Measurement equipment used |
| Observation | Main measured behaviour |
| Files | Associated plots, captures or datasets |
| Status | Validated / requires review |

## Suggested Directory Structure

```text
results/
├── README.md
├── waveform-generation/
├── adaptive-selection/
├── oscilloscope/
├── fft/
├── spectrogram/
├── embedded-performance/
├── power/
└── underwater-tests/
```

The subdirectories can be created when actual result files become available.

## Evidence Policy

The following distinction should be maintained:

- **Design** — what the system is intended to do.
- **Simulation** — behaviour observed in software or a model.
- **Prototype measurement** — behaviour observed on the physical hardware.
- **Underwater validation** — behaviour observed during controlled water testing.

Do not use simulated or expected values as substitutes for measured experimental results.

## Current Status

No experimental result files are being added at this stage. The folder is prepared for future validated waveform captures, signal-analysis plots, embedded measurements, power measurements and controlled underwater test results.
