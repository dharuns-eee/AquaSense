# Firmware

The `firmware/` directory contains the embedded software for the AquaSense SONAR transmitter concept.

## Current Basic Demonstration Firmware

`AquaSense_ESP32.ino` is the current **basic ESP32 prototype**. It streams selected waveform samples over serial to the Python visualization program.

### Demonstration parameters

- Sampling frequency: **1 MHz**
- Demonstration band: **250–270 kHz**
- PCP carrier: **260 kHz**
- Samples per waveform: **1000**
- Serial baud rate: **115200**
- Serial port used by the basic demo: **COM9**

### Current target sequences

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
- **Geometric sweep:** retained in the firmware as an additional software-defined waveform generator.

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

## Run the Basic Python Demo

Use the companion program:

```bash
python signal-processing/AquaSense_Demo.py
```

Make sure the Arduino Serial Monitor is closed while the Python program is using **COM9**.

## Prototype Boundary

This firmware is part of the **current basic digital prototype**. The 250–270 kHz configuration is used to make the software frequency-domain demonstration clear. It should not be presented as a measured underwater acoustic transmission result.

## Planned Final Firmware Platform

The final hardware prototype will move the waveform-generation and adaptive control functions to an **STM32G4** and connect them to the intended high-speed DAC, filtering, MOSFET/power and amplifier stages. The final physical demonstration will use an **oscilloscope** to verify the electrical waveform.
