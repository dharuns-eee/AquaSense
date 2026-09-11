# AquaSense Hackathon Demonstration

## Final Demo Modes

### Stationary target

`LFM → PCP`

### Non-stationary target

`HFM → LFM → PCP`

## Demonstration Software

The ESP32 streams waveform samples over serial at 115200 baud. The Python demonstration connects to `COM9`, receives the selected transmission sequence, and presents the result in one Matplotlib dashboard.

The dashboard contains:

1. Combined time-domain transmission waveform.
2. PCP represented as an 8-chip phase-code step waveform.
3. A visual `Hann Window → FFT` processing flow.
4. Combined FFT display with a 0–500 kHz presentation axis.
5. Separate visual patterns for stationary and non-stationary demonstration modes.

## Run

Install the Python dependencies:

```bash
pip install pyserial numpy matplotlib
```

Then run:

```bash
python signal-processing/AquaSense_Demo.py
```

Use the menu:

```text
1. Target 0 - Stationary
2. Target 1 - Non-Stationary
3. Quit
```

## Prototype Note

This hackathon demonstration focuses on the software-defined transmission and visualization flow. The displayed FFT presentation is a demonstration visualization rather than a measured underwater acoustic spectrum. Physical SONAR receiver/transducer validation is a separate future stage.
