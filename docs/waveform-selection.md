# Waveform Selection

Waveform selection is the central AquaSense concept: the transmitter can change its signal strategy through software rather than being locked to one fixed waveform.

## Waveform Modes

| Mode | Current role |
|---|---|
| **LFM** | Baseline frequency sweep; used in the stationary sequence and after HFM in the non-stationary sequence. |
| **HFM** | Doppler-aware/resilient sweep option used at the start of the non-stationary target demonstration. |
| **PCP** | Phase-coded pulse used as the final waveform in both demonstration sequences. |
| **Geometric Sweep** | Additional non-linear sweep generator retained in the ESP32 firmware but not used in the final target sequences. |

## Final ESP32 Parameters

- Sampling frequency: **1 MHz**
- Duration: **1 ms**
- Samples: **1000 per waveform**
- Frequency band: **250–270 kHz**
- PCP carrier: **260 kHz**
- PCP code: `+ + + - - + - +`

## Final Target Sequences

### Target 0 — Stationary

```text
LFM → PCP
```

### Target 1 — Non-Stationary

```text
HFM → LFM → PCP
```

These sequences are the locked final competition-demo behaviour.

## Target-State Representation

The current prototype does **not** contain a SONAR receiver. Therefore the target state is supplied to the ESP32 by the demo command rather than inferred from a measured acoustic echo.

In the final demo:

```text
Python menu choice
      ↓
ESP32 command: 0 or 1
      ↓
Target sequence selected
      ↓
Waveforms generated
      ↓
Samples streamed over serial
```

A future receiver-enabled system could replace this software target-state input with a target-motion decision derived from received acoustic data.

## Environmental Adaptation

At the system level, AquaSense is designed around representative environmental inputs such as temperature, salinity, depth and turbidity. The MATLAB/Simulink model demonstrates these changing conditions and an adaptive decision architecture.

The final ESP32 competition code intentionally does **not** use the physical pots/environmental inputs to drive the two live menu sequences. This keeps the final demonstration reliable and focuses it on the adaptive waveform-transmission concept.

Any threshold, weight or mapping from environmental conditions to waveform choice should be treated as a configurable design rule until experimentally validated.

## Waveform Generation

### LFM

The firmware implements a linear sweep using:

$$f(t)=f_0+kt$$

with the final demonstration band set to 250–270 kHz.

### HFM

The firmware uses the hyperbolic phase formulation to generate the HFM sweep across the demonstration band. In competition language, it should be described as **Doppler-aware/resilient**, not as a waveform that removes Doppler effects.

### PCP

PCP uses a 260 kHz carrier multiplied by the 8-chip bipolar phase code:

```text
+ + + - - + - +
```

### Geometric Sweep

The geometric generator uses an exponential frequency progression. It remains available in firmware for future waveform experiments but is not part of the two final target sequences.

## System-Level Decision Model

The broader adaptive architecture can be represented by:

$$S_i=\sum_{j=1}^{n}w_jx_j$$

followed by:

$$W^*=\arg\max_{W_i}S_i$$

This is a **system-level design model**, not the logic executed by the final ESP32 menu demo.

## Validation

The final digital demonstration validates:

- Waveform generation.
- Target-sequence ordering.
- Serial transmission protocol.
- Time-domain visualization.
- Hann-windowed FFT processing.
- 0–500 kHz presentation display.

Physical acoustic validation, receiver-based target detection and underwater performance remain future stages.
