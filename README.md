# AquaSense

**Adaptive SONAR for Autonomous Underwater Vehicles (AUVs)**

AquaSense is a **real-time, software-defined SONAR transmitter payload** designed to be integrated into an Autonomous Underwater Vehicle (AUV). The core idea is simple: instead of transmitting one fixed waveform for every underwater situation, AquaSense uses environmental and mission-condition inputs to **select a more suitable waveform dynamically**.

> **AquaSense is the SONAR payload/subsystem — not the complete AUV.**

## What Problem Does AquaSense Address?

Underwater acoustic conditions are not constant. Temperature, salinity, depth, turbidity and target motion can change the way an acoustic signal behaves. A fixed SONAR transmission strategy may therefore not be equally suitable across different operating conditions.

AquaSense addresses this by making the **transmit side adaptive**. The embedded controller evaluates available condition inputs, applies configured decision logic and selects one of several software-defined waveform modes.

### Core Concept

**Sense → Decide → Select → Generate → Transmit → Analyse**

The adaptation happens before transmission:

```text
Changing Underwater Conditions
              ↓
      Environmental Inputs
              ↓
      Adaptive Decision Logic
              ↓
       Waveform Selection
              ↓
      Software Waveform Generation
              ↓
       DAC + Analog Front-End
              ↓
       SONAR Transducer / Oscilloscope
```

## Adaptive Solution

AquaSense considers inputs such as:

- **Temperature** — identifies thermal-condition changes that may influence acoustic propagation.
- **Salinity** — represents changes in the underwater medium.
- **Depth** — provides information about the operating environment and mission state.
- **Turbidity** — represents changes in water clarity and operating conditions.
- **Target motion / Doppler conditions** — represents dynamic target scenarios where waveform choice can be important.

The controller maps these inputs to a configured decision state and selects an appropriate waveform.

### Supported Waveform Modes

| Waveform | Role in AquaSense |
|---|---|
| **LFM** | Baseline frequency-swept waveform for stable operating conditions |
| **HFM** | Frequency-swept option considered for changing and Doppler-related conditions |
| **PCP** | Phase-coded pulse option for conditions where coded transmission is desirable |
| **Geometric Sweep** | Alternative software-defined frequency-sweep mode |

The exact thresholds, weights and mode-selection parameters are treated as **design parameters** until validated experimentally.

## Why Software-Defined SONAR?

In a conventional fixed-waveform transmitter, changing the acoustic transmission behaviour can require hardware-level changes or a separate signal-generation path. AquaSense moves waveform selection and generation into embedded firmware.

This means the same transmitter hardware can be configured to generate different waveform families depending on the selected operating state.

```text
Fixed SONAR
     │
     └── One predefined transmission strategy

AquaSense
     │
     ├── Sense conditions
     ├── Decide operating state
     ├── Select waveform
     ├── Generate waveform in firmware
     └── Stream selected waveform through the same hardware
```

## System Architecture

```text
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
```

### Architecture Stages

1. **Input stage** — condition values are obtained from sensors or representative inputs during prototype testing.
2. **Decision stage** — the controller evaluates the configured environmental and mission factors.
3. **Waveform stage** — the selected waveform mode determines the signal-generation parameters.
4. **Generation stage** — waveform samples are produced using software-defined signal-generation methods and precomputed LUTs where appropriate.
5. **Streaming stage** — DMA and hardware timers support deterministic sample delivery to the DAC.
6. **Analog stage** — DAC output passes through filtering and the amplifier/MOSFET stage before reaching the acoustic output path.
7. **Analysis stage** — the physical electrical waveform can be inspected using an oscilloscope and analysed using FFT/spectrogram methods.

## Decision Logic

AquaSense can represent the score of a candidate waveform using a weighted decision model:

$$
S_i = \sum_{j=1}^{n} w_j x_j
$$

where:

- $S_i$ = score associated with waveform option $i$
- $x_j$ = normalized input factor
- $w_j$ = weight assigned to that input factor

The selected waveform can then be represented as:

$$
W^* = \arg\max_{W_i} S_i
$$

This provides a structured way to combine multiple condition inputs instead of relying on a single environmental parameter.

For an initial rule-based implementation, the same concept can also be expressed as condition states:

```text
IF operating conditions are stable
        → select configured baseline waveform

IF turbidity condition changes significantly
        → select configured phase-coded mode

IF temperature/depth conditions shift
        → select configured alternative sweep mode

IF target motion / Doppler condition is detected
        → consider Doppler-resilient waveform configuration
```

These are **design examples**, not claims of experimentally validated performance.

## Embedded Implementation

The embedded controller is responsible for turning the selected waveform decision into a timed stream of digital samples.

### Firmware responsibilities

- Read and process condition inputs.
- Maintain the current operating state.
- Evaluate waveform-selection rules.
- Select waveform parameters.
- Generate or access waveform samples.
- Transfer samples to the DAC.
- Maintain deterministic sample timing.
- Support signal-analysis data where required.

### Hardware-assisted waveform transmission

AquaSense uses a combination of:

- **Look-Up Tables (LUTs)** for precomputed waveform samples.
- **DMA** to transfer samples without requiring the CPU to handle every sample individually.
- **Hardware timers** to establish the waveform sample/update rate.
- **NVIC priority interrupts** for time-critical embedded events.
- **CMSIS-DSP / FPU capabilities** for efficient signal-processing operations where required.
- **WFI-based CPU duty-cycling** to avoid unnecessary active processing.

## Hardware Stack

The transmitter payload is organized around the following signal path:

```text
STM32G4 MCU
    ↓
SAR ADC / Input Interface
    ↓
Adaptive Decision Logic
    ↓
Waveform LUT / Generation
    ↓
12-bit High-Speed DAC
    ↓
Low-Pass Filter
    ↓
Class-D Amplifier + MOSFET Stage
    ↓
Underwater Acoustic Transducer
    ↓
Oscilloscope / Measurement Setup
```

### Main components

- STM32G4-series microcontroller
- SAR ADC
- 12-bit high-speed DAC
- Low-pass filter
- Class-D amplifier
- MOSFET power stage
- Underwater acoustic transducer
- Oscilloscope for physical waveform inspection

## Signal Processing & Analysis

The signal-processing side of AquaSense is used to verify and characterize the generated transmission waveform.

Important analysis views include:

- **Time-domain waveform** — checks amplitude and waveform shape.
- **Frequency spectrum** — checks frequency content and occupied components.
- **FFT** — provides a computational frequency-domain representation.
- **Spectrogram** — shows how frequency content changes over time.
- **Performance metrics** — provide a structured way to compare configured waveform modes during testing.

For a general transmitted signal:

$$
s(t)=A(t)\cos\left(2\pi\int_0^t f(\tau)\,d\tau+\phi\right)
$$

For Linear Frequency Modulation:

$$
f(t)=f_0+kt
$$

where $f_0$ is the starting frequency and $k$ is the frequency-sweep rate.

## Low-Power Design

Low power remains an important supporting objective because the payload is intended for an AUV environment. AquaSense therefore emphasizes efficient embedded execution rather than treating power as a separate feature.

The design uses hardware-assisted waveform streaming, LUT-based generation, efficient signal processing and controlled CPU activity to reduce unnecessary processing overhead.

For a transmit interval:

$$
E_{\text{tx}} = P_{\text{tx}} \times T_{\text{tx}}
$$

For duty-cycled transmission:

$$
P_{\text{avg}} \approx D\,P_{\text{tx}}
$$

where $D$ represents the fraction of time spent transmitting.

These equations describe the design approach; measured power values will only be reported after instrumentation and validation.

## Prototype & Validation Direction

The prototype development is being organized progressively:

### Stage 1 — Digital waveform generation

Generate and inspect LFM, HFM, PCP and geometric-sweep samples in software.

### Stage 2 — Embedded waveform output

Move selected waveform generation onto the STM32-based embedded platform and establish deterministic DAC sample streaming.

### Stage 3 — Analog signal path

Verify DAC output, filtering and amplifier/MOSFET stages before the acoustic transducer.

### Stage 4 — Adaptive selection

Apply representative environmental-condition inputs and verify that the configured decision logic selects the intended waveform mode.

### Stage 5 — Physical waveform verification

Use the oscilloscope measurement setup to inspect the transmitted electrical waveform and compare it against the expected digital waveform.

### Stage 6 — Controlled underwater testing

Validate the complete payload under controlled water conditions and document measured results.

## Testing Philosophy

AquaSense separates **design intent** from **validated experimental evidence**.

The repository can contain:

- Architecture and design documentation.
- Waveform-generation logic.
- Decision-rule definitions.
- Test procedures.
- Prototype implementation notes.
- Validated measurements once experiments are completed.

Unmeasured performance should not be presented as a measured result.

## Current Status

The repository currently documents the AquaSense architecture, adaptive waveform-selection concept, embedded implementation approach, hardware signal path and planned validation process.

Media assets and experimental result files will be added as the prototype and testing work progresses.

## Repository Structure

```text
AquaSense/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── competition-notes.md
│   ├── testing-plan.md
│   └── waveform-selection.md
├── firmware/
│   └── README.md
├── hardware/
│   └── README.md
├── signal-processing/
│   └── README.md
├── media/
│   └── README.md
└── results/
    └── README.md
```

## Team

**Team WAVELET**  
Chennai Institute of Technology

## License

This project is intended for academic, prototype and hackathon development. Add an appropriate open-source license before external reuse if required.
