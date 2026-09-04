# AquaSense Architecture

AquaSense is a low-power, real-time adaptive software-defined SONAR transmitter payload for Autonomous Underwater Vehicles (AUVs).

## System Flow

**Sense → Decide → Adapt → Transmit → Analyse**

## Inputs

- Temperature
- Salinity
- Depth
- Turbidity
- Target motion / Doppler conditions

## Processing

Adaptive decision logic evaluates environmental and mission conditions and selects a suitable software-defined waveform and transmission parameters.

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
SONAR Transducer / Oscilloscope
↓
FFT / Spectrogram / Performance Analysis

## Status

This document describes the current prototype/design architecture. Quantitative water-test results and measured power data will be added after validation.
