# Firmware

The `firmware/` directory contains the embedded-software design for the AquaSense SONAR transmitter payload. The firmware is responsible for interpreting condition inputs, selecting the waveform mode and producing a deterministic stream of samples for the DAC.

## Firmware Role

The embedded controller forms the bridge between the adaptive decision layer and the physical SONAR transmitter.

```text
Condition Inputs
      ↓
Adaptive Decision Logic
      ↓
Waveform + Parameters
      ↓
Sample Generation / LUT
      ↓
DMA + Timer
      ↓
DAC Output
```

## Planned / Prototype Modules

### 1. Input handling

- Read representative environmental-condition inputs.
- Convert raw ADC values into usable condition variables.
- Apply basic scaling or normalization where required.
- Provide the decision layer with stable input values.

### 2. Adaptive decision logic

- Evaluate configured environmental and mission conditions.
- Determine the current operating state.
- Select the appropriate waveform mode.
- Load the associated waveform parameters.
- Keep decision rules configurable for experimentation.

### 3. Waveform generation

The firmware is intended to support:

- LFM generation.
- HFM generation.
- Phase-Coded Pulse generation.
- Geometric frequency sweeps.
- Configurable amplitude and timing parameters.
- Precomputed waveform sample tables.

### 4. Look-Up Tables (LUTs)

LUTs can store precomputed waveform samples so that the controller does not need to repeatedly evaluate the complete waveform equation during every transmission sample.

A LUT-based path is conceptually:

```text
Waveform Selection
       ↓
Select LUT / Parameters
       ↓
Sample Buffer
       ↓
DMA
       ↓
DAC
```

### 5. DAC output control

The firmware configures the DAC interface and prepares digital waveform samples for conversion into the analog signal used by the transmitter chain.

### 6. DMA-driven waveform streaming

DMA is used to transfer waveform samples from memory to the DAC with limited CPU intervention. This is important for maintaining regular sample delivery during real-time transmission.

### 7. Hardware timer control

A hardware timer establishes the waveform sample/update timing. The relationship between timer configuration, DAC update rate and waveform samples determines the generated output frequency and sweep behaviour.

### 8. Interrupt management

NVIC priority configuration can be used to organize time-critical embedded events and ensure that important peripheral operations receive appropriate interrupt priority.

### 9. CMSIS-DSP / FPU processing

Where signal-processing calculations are required, CMSIS-DSP functions and the MCU floating-point capability can be used to reduce computational overhead and improve execution efficiency.

### 10. CPU duty-cycling

WFI-based CPU inactivity can be used during periods where the processor is waiting for an interrupt or peripheral event. This supports the project's low-power embedded design objective.

## Real-Time Transmission Sequence

A typical firmware execution sequence is:

1. Initialize peripherals.
2. Acquire or receive condition inputs.
3. Evaluate the adaptive decision rules.
4. Select the waveform mode.
5. Load waveform parameters or LUT data.
6. Configure the DAC, DMA and hardware timer.
7. Start waveform transmission.
8. Maintain deterministic sample delivery through DMA/timer hardware.
9. Stop or update transmission at the configured boundary.
10. Make the next decision when new operating-condition information is available.

## Firmware Design Principles

- Keep waveform selection separate from waveform generation.
- Keep hardware-specific transmission functions separate from decision logic.
- Prefer deterministic peripheral timing for waveform output.
- Use configurable parameters rather than hard-coding experimental thresholds wherever practical.
- Keep prototype measurements separate from unvalidated assumptions.
- Avoid claiming performance improvements until they are experimentally demonstrated.

## Current Status

The repository currently documents the firmware architecture and planned/prototype modules. Source files will be added and expanded as the embedded implementation is organized and validated on the target hardware.
