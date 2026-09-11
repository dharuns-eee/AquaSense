# AquaSense Hackathon Demonstration

## Final Demo

The final competition prototype demonstrates adaptive, software-defined SONAR waveform sequencing using an ESP32 and a Python visualization/analysis program.

### Target 0 — Stationary

```text
LFM → PCP
```

### Target 1 — Non-Stationary

```text
HFM → LFM → PCP
```

## ESP32 Configuration

- Sampling frequency: **1 MHz**
- Duration: **1 ms per waveform**
- Samples: **1000 per waveform**
- Demonstration band: **250–270 kHz**
- PCP carrier: **260 kHz**
- PCP code: `+ + + - - + - +`
- Serial: **115200 baud**

## Python Dashboard

The companion script `signal-processing/AquaSense_Demo.py` connects to the ESP32 on the configured serial port (`COM9`) and receives the complete target sequence.

The single dashboard contains:

1. Combined time-domain transmission.
2. Waveform names and sequence boundaries.
3. PCP as an 8-chip phase-code display.
4. `Hann Window → FFT` processing flow.
5. Combined FFT from **0–500 kHz**.
6. Highlighted **250–270 kHz demonstration band**.
7. Different presentation spectra for stationary and non-stationary modes.

## Run

Install dependencies:

```bash
pip install pyserial numpy matplotlib
```

Run:

```bash
python signal-processing/AquaSense_Demo.py
```

Menu:

```text
1. Target 0 - Stationary
2. Target 1 - Non-Stationary
3. Quit
```

## Demonstration Workflow

```text
Connect ESP32
      ↓
Run Python demo
      ↓
Choose target state
      ↓
ESP32 generates sequence
      ↓
Samples streamed over USB serial
      ↓
Python receives waveform data
      ↓
Combined time-domain display
      ↓
Hann Window → FFT
      ↓
Combined frequency-domain presentation
```

## Important Prototype Boundaries

- The target state is **software-commanded/simulated**; there is no physical SONAR receiver in the current prototype.
- Environmental pots/sensors are part of the broader system concept but are **not used to drive the final live ESP32 menu sequence**.
- The 250–270 kHz spectrum shown by the Python dashboard is a **controlled demonstration visualization**, not a measured underwater acoustic spectrum.
- HFM should be described as **Doppler-aware/resilient**, not as eliminating Doppler.
- Physical DAC, amplifier, transducer, receiver and controlled underwater validation are future stages.

## Demo Recording Order

1. Show the ESP32/prototype hardware.
2. Connect it to the laptop.
3. Start the Python program.
4. Select **1 — Stationary**.
5. Show `LFM → PCP` and the dashboard.
6. Return to the menu.
7. Select **2 — Non-Stationary**.
8. Show `HFM → LFM → PCP` and the dashboard.
9. Explain the software-defined adaptation and prototype boundaries.
