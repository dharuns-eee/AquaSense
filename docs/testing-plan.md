# Testing Plan

AquaSense will be validated progressively from digital waveform checks to controlled underwater experiments.

## 1. Signal validation

- Verify generated waveform shape
- Verify frequency sweep behavior
- Compare time-domain and frequency-domain output
- Inspect FFT and spectrogram results

## 2. Hardware validation

- Verify DAC output
- Verify filtered analog output
- Verify amplifier/transducer drive path
- Capture physical output with an oscilloscope where applicable

## 3. Adaptive behavior

- Apply representative environmental-condition inputs
- Verify decision-state transitions
- Verify selected waveform matches the configured decision rules
- Record mode-switching behavior

## 4. Power evaluation

- Measure MCU activity during transmission
- Measure transmission power where instrumentation is available
- Compare continuous and duty-cycled operation
- Record validated measurements rather than estimated results

## 5. Underwater validation

Planned next step: controlled water testing with real sensors and measured performance data.
