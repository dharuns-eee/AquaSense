# AquaSense Results

This folder contains the **basic digital prototype demonstration outputs** for the AquaSense adaptive SONAR transmission concept. These results are not the final physical hardware demonstration.

## Basic Prototype Demonstration Outputs

### 1. Stationary Target — LFM → PCP

The stationary-target basic demonstration uses the sequence:

`LFM → PCP`

![Stationary target — LFM to PCP](Figure_1.png)

The figure shows the generated LFM waveform, Hann-windowed FFT, PCP phase-code waveform, PCP FFT, and the combined transmission time-domain and frequency-domain views.

### 2. Non-Stationary Target — HFM → LFM → PCP

The non-stationary-target basic demonstration uses the sequence:

`HFM → LFM → PCP`

![Non-stationary target — HFM to LFM to PCP](Figure_2.png)

The figure shows the generated HFM and LFM waveforms, Hann-windowed FFT results, PCP phase-code waveform, PCP FFT, and the combined transmission views.

## Prototype Configuration

| Parameter | Current basic prototype |
|---|---|
| Controller | ESP32 |
| Sampling rate | 1 MHz |
| Samples per waveform | 1000 |
| Waveform duration | 1 ms |
| Frequency band | 250–270 kHz |
| PCP carrier | 260 kHz |
| PCP code | `+ + + - - + - +` |
| Serial communication | 115200 baud |
| Signal processing | Hann window → FFT |
| Display range | 0–500 kHz |

## Demonstration Sequences

| Target state | Transmission sequence |
|---|---|
| Stationary | `LFM → PCP` |
| Non-stationary | `HFM → LFM → PCP` |

The target state in this prototype is **software-commanded/simulated** because a physical SONAR receiver is not connected. In a complete SONAR system, target motion would be inferred from received echo behaviour.

## Important Note on the FFT Display

The Python dashboard includes a controlled presentation spectrum so that the basic prototype demonstration clearly shows the intended frequency-domain behaviour. It is **not a measured underwater acoustic spectrum** and should not be presented as a physical measurement.

## Evidence Classification

The files in this folder are **basic prototype demonstration evidence**. They document the current ESP32 + Python implementation and its software-generated waveform/FFT visualizations.

They should not be interpreted as:

- measured underwater acoustic data,
- receiver-based target detection results,
- transducer performance measurements, or
- quantitative power measurements.

## Planned Final Hardware Demonstration

The final AquaSense hardware demonstration will use an **STM32G4-based physical transmitter chain**, with an **oscilloscope** used to verify the electrical waveform.

```text
STM32G4
   ↓
High-Speed DAC
   ↓
Low-Pass Filter
   ↓
MOSFET Switching / Power Stage
   ↓
Amplifier
   ↓
SONAR Transducer / Test Load
   ↓
Oscilloscope
```

Future final-hardware results may include DAC output captures, filtered/amplified waveform measurements, oscilloscope captures, measured FFT/spectrograms, processing-time measurements and power measurements.
