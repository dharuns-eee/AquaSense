# AquaSense Architecture

AquaSense is a low-power, real-time adaptive software-defined SONAR transmitter payload for Autonomous Underwater Vehicles (AUVs).

## System Flow

Sense → Decide → Adapt → Transmit → Analyse & Feedback

## Inputs

- Temperature
- Salinity
- Depth
- Turbidity
- Target motion / Doppler conditions
- Battery level

## Processing

Adaptive decision logic selects suitable waveform and transmission parameters based on mission and environmental conditions.

## Signal Path

Environmental / Mission Inputs
↓
Adaptive Decision Logic
↓
Waveform Selection
↓
LUT + DMA + Hardware Timer
↓
DAC
↓
Low-Pass Filtering
↓
Class-D + MOSFET Stage
↓
SONAR Transducer / Payload
↓
FFT / Spectrogram / Performance Analysis
↓
Closed-Loop Feedback

## Status

This document describes the current prototype/design architecture. Quantitative water-test results and measured power data will be added after validation.
