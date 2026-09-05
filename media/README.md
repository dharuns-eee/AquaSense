# Media

The `media/` directory is reserved for visual and presentation material related to AquaSense. It will eventually provide the visual evidence needed to understand the hardware, waveform-generation process and prototype demonstrations without placing large media files directly inside the main documentation.

## Planned Media Categories

### 1. Architecture Diagrams

Visual representations of the AquaSense signal and control architecture, including:

- Environmental / mission inputs.
- Adaptive decision logic.
- Waveform selection.
- LUT, DMA and hardware-timer path.
- DAC and analog signal chain.
- SONAR transducer / oscilloscope measurement path.

### 2. Hardware Photographs

Project photographs may include:

- STM32G4 development hardware.
- DAC and ADC interfaces.
- Filter and amplifier stages.
- MOSFET stage.
- Underwater acoustic transducer.
- Complete SONAR payload prototype.
- Test-bench setup.

### 3. Oscilloscope Captures

Oscilloscope images can be used to show physical waveform output during validation.

Useful captures may include:

- LFM waveform.
- HFM waveform.
- Phase-coded pulse waveform.
- Geometric sweep waveform.
- Different waveform modes under different input conditions.
- DAC or filtered analog output.

### 4. FFT and Spectrogram Figures

Signal-analysis visuals can show how each generated waveform appears in the frequency domain.

Potential figures include:

- FFT plots.
- Spectrum plots.
- Time-frequency spectrograms.
- Digital-versus-measured waveform comparisons.

### 5. Adaptive Decision Demonstrations

Visuals can document the adaptive process:

```text
Input Condition
      ↓
Decision State
      ↓
Selected Waveform
      ↓
Generated Signal
```

Screenshots, diagrams or short recordings can be added when the corresponding implementation is ready.

### 6. Demo Videos

Future demonstration videos may show:

- Hardware startup.
- Waveform generation.
- Adaptive waveform selection.
- DAC output.
- Oscilloscope observation.
- Prototype testing.

### 7. Competition and Presentation Visuals

Presentation-ready graphics may include:

- Project overview diagrams.
- System architecture visuals.
- Adaptive decision flowcharts.
- Hardware signal-chain diagrams.
- Waveform comparison graphics.
- Prototype photographs.

## Suggested Naming Convention

Use descriptive names so that media can be identified directly from the repository:

```text
architecture-overview.png
hardware-prototype.jpg
oscilloscope-lfm.png
oscilloscope-hfm.png
fft-lfm.png
spectrogram-lfm.png
adaptive-selection-demo.png
prototype-demo.mp4
```

## Media Guidelines

- Use project-relevant visuals.
- Prefer clear, high-resolution captures.
- Include enough context to understand what is being shown.
- Do not present simulated graphics as physical prototype evidence.
- Label simulations, diagrams and measured captures clearly.
- Keep filenames descriptive and consistent.

## Current Status

The media directory currently contains documentation only. Actual photographs, oscilloscope captures, FFT/spectrogram figures and demonstration videos will be added later as the prototype and testing work progresses.
