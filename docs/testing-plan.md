# Testing Plan

AquaSense will be validated progressively, starting with digital waveform generation and moving toward hardware and controlled underwater experiments.

The testing approach is intentionally staged so that waveform-generation errors, adaptive-decision errors and hardware-path errors can be isolated instead of evaluating the complete system as one block.

## 1. Digital Signal Validation

The first stage verifies the waveform-generation logic before connecting the signal to the physical transmission chain.

### Checks

- Verify generated waveform shape.
- Verify configured frequency range.
- Verify frequency-sweep behaviour.
- Verify pulse duration and timing where applicable.
- Compare generated samples with expected mathematical models.
- Inspect time-domain output.
- Inspect FFT output.
- Inspect spectrograms for frequency-swept signals.

## 2. Waveform-Mode Validation

Each supported waveform should be tested independently before adaptive switching is evaluated.

### LFM

Verify the intended linear frequency progression and configured sweep duration.

### HFM

Verify the intended non-linear frequency progression and time-frequency representation.

### Phase-Coded Pulses

Verify pulse timing, phase-code structure and sample generation.

### Geometric Sweep

Verify the configured non-linear sweep progression and timing.

## 3. Adaptive Decision Validation

The adaptive layer should be tested independently from the analog hardware.

### Procedure

1. Provide a known set of representative condition inputs.
2. Record the normalized or processed input values.
3. Run the configured decision logic.
4. Record the selected operating state.
5. Record the selected waveform.
6. Compare the result with the expected decision rule.
7. Repeat for different input combinations.

### Important checks

- Stable-condition input produces the configured baseline state.
- Turbidity-related input changes are handled according to the configured rules.
- Temperature/depth changes are handled according to the configured rules.
- Target-motion/Doppler-related conditions select the intended configured mode.
- Competing conditions follow the configured priority or weighting.

Thresholds and weights should be treated as design parameters until validated.

## 4. Hardware Validation

The physical transmitter path should be tested stage by stage.

### Digital and analog checks

- Verify MCU peripheral configuration.
- Verify ADC/input readings.
- Verify DAC output.
- Verify filtered analog output.
- Verify amplifier output behaviour.
- Verify MOSFET stage operation.
- Verify the acoustic transducer connection.
- Capture the physical electrical waveform using an oscilloscope.

## 5. DMA and Timer Validation

The real-time waveform path should be checked for deterministic sample delivery.

- Verify DMA transfer configuration.
- Verify hardware timer frequency.
- Verify DAC update timing.
- Check for missing or repeated samples.
- Check waveform continuity during repeated transmission.
- Confirm that the CPU is not required to handle every individual sample transfer.

## 6. Adaptive Waveform Switching Test

Once individual modes and the decision logic are validated, the complete adaptive digital path can be exercised.

```text
Input Condition A
      ↓
Decision State A
      ↓
Waveform A

Input Condition B
      ↓
Decision State B
      ↓
Waveform B
```

The test should confirm that a change in the configured input conditions causes the expected waveform selection without introducing unintended transmission behaviour.

## 7. Power Evaluation

Low-power operation remains a supporting project objective. Power measurements should be made only with suitable instrumentation.

Possible measurements include:

- MCU activity during waveform generation.
- MCU activity during DMA-based transmission.
- Transmission-stage power.
- Average transmission power.
- Continuous versus duty-cycled operation.
- Processing overhead for different waveform-generation approaches.

Estimated values should be clearly separated from measured values.

## 8. Oscilloscope Verification

The oscilloscope is used to inspect the physical electrical waveform produced by the transmitter chain.

Useful observations include:

- Waveform shape.
- Peak-to-peak amplitude.
- Period or sweep behaviour.
- Pulse duration.
- Timing consistency.
- Distortion or unexpected signal components.

Oscilloscope captures can later be stored in the `media/` directory and referenced from validated experiment records in `results/`.

## 9. Underwater Validation

The final validation stage is planned as controlled water testing using real environmental sensors and the complete transmitter payload.

The testing should evaluate:

- Environmental-condition acquisition.
- Adaptive waveform selection.
- Physical acoustic transmission.
- Waveform characteristics under controlled conditions.
- Repeatability across test runs.
- Measured power behaviour.

The exact underwater test procedure will be documented after the laboratory setup is finalized.

## 10. Evidence and Reporting Rules

AquaSense follows a simple evidence policy:

- Design parameters are labelled as design parameters.
- Planned tests are labelled as planned.
- Simulated or representative data is not presented as measured hardware data.
- Experimental measurements are recorded with the test conditions and instrumentation used.
- Results are added to the repository only after they have been checked.

## Current Status

The testing plan defines the validation sequence and measurement categories. Actual measured results, oscilloscope captures, datasets and underwater test observations will be added as the corresponding experiments are completed.
