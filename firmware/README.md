# Firmware

The `firmware/` directory contains the embedded demonstration firmware for the AquaSense SONAR transmitter payload.

## Current Demonstration Firmware

`AquaSense_ESP32.ino` is the current ESP32 demonstration transmitter. It streams selected waveform samples over serial to the Python visualization program.

### Demonstration parameters

- Sampling frequency: **1 MHz**
- Demonstration band: **250–270 kHz**
- PCP carrier: **260 kHz**
- Samples per waveform: **1000**
- Serial baud rate: **115200**
- Serial port used by the demo: **COM9**

### Target sequences

```text
Target 0 — Stationary
LFM → PCP

Target 1 — Non-Stationary
HFM → LFM → PCP
```

### Waveforms

- **LFM:** linear frequency sweep from 250 kHz to 270 kHz.
- **HFM:** hyperbolic frequency sweep across the demonstration band.
- **PCP:** 260 kHz carrier with the 8-chip phase code `+ + + - - + - +`.
- **Geometric sweep:** retained in the firmware as an additional software-defined waveform generator, but not used in the two final demo sequences.

## Serial Protocol

The firmware sends a simple text protocol:

```text
AQUASENSE_START
TARGET,<id>,<state>
WAVEFORM,<name>
DATA
<1000 samples>
END_WAVEFORM
...
AQUASENSE_END
```

Python sends a single character command:

```text
0 → Target 0 / Stationary
1 → Target 1 / Non-Stationary
```

## Run with Python Demo

Use the companion program:

```bash
python signal-processing/AquaSense_Demo.py
```

Make sure the Arduino Serial Monitor is closed while the Python program is using **COM9**.

## Prototype Note

This firmware is part of a **demonstration prototype**. The 250–270 kHz configuration is used to make the frequency-domain demonstration clear. It should not be presented as a measured underwater acoustic transmission result. Physical DAC, amplifier, transducer and underwater validation are separate hardware stages.
