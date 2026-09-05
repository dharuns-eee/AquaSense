# Waveform Selection

Waveform selection is the central adaptive feature of AquaSense. The transmitter is not restricted to one predefined signal. Instead, the embedded decision layer can select among multiple software-defined waveform modes based on configured environmental and mission conditions.

## Why Multiple Waveforms?

Different underwater operating conditions can create different requirements for acoustic transmission. A single waveform may therefore not be the preferred choice for every scenario.

AquaSense keeps waveform generation in software so that the transmitter hardware can support multiple modes without changing the main DAC, filter and amplifier path.

## Waveform Modes

| Waveform | Intended operating condition | Role |
|---|---|---|
| **LFM** | Stationary / clear and stable conditions | Baseline frequency-swept transmission |
| **HFM** | Changing conditions / moving-target Doppler conditions | Alternative sweep designed for Doppler-related scenarios |
| **Phase-Coded Pulses (PCP)** | High-turbidity conditions | Coded-pulse transmission option |
| **Geometric Sweep** | Alternative software-defined sweep | Additional frequency-sweep mode |

These operating-condition descriptions represent the current design intent. They are not presented as experimentally proven performance claims.

## Input Factors

The decision layer can consider:

- Temperature
- Salinity
- Depth
- Turbidity
- Target motion / Doppler conditions

Inputs can be normalized or converted into configured operating states before waveform selection.

## Decision Approach

A weighted decision model can score each candidate waveform:

$$S_i=\sum_{j=1}^{n}w_jx_j$$

where:

- $S_i$ is the score of waveform $i$.
- $x_j$ is an input factor.
- $w_j$ is the configured weight of that factor.

The selected waveform can then be represented as:

$$W^*=\arg\max_{W_i}S_i$$

This model provides a structured way to combine multiple conditions instead of basing the decision on a single input.

## Rule-Based Prototype Logic

For early embedded validation, deterministic rules can be used alongside or instead of a weighted model:

```text
Stable operating state
        ↓
      LFM

High-turbidity state
        ↓
      PCP

Changing temperature/depth state
        ↓
      HFM / configured sweep

Dynamic target / Doppler state
        ↓
      Doppler-resilient waveform configuration
```

The exact threshold values and priority between competing conditions should be treated as configurable design parameters.

## Waveform Generation

After a waveform is selected, the firmware must generate the corresponding sample sequence. The generation path can use:

- Mathematical waveform generation.
- Precomputed Look-Up Tables (LUTs).
- Configured frequency and timing parameters.
- Amplitude scaling.
- Pulse-duration or sweep-duration parameters.

The generated samples are then prepared for DAC transmission.

## Real-Time Execution

AquaSense uses hardware-assisted transmission so that waveform generation and sample delivery do not require continuous CPU intervention.

```text
Decision
   ↓
Waveform + Parameters
   ↓
LUT / Sample Buffer
   ↓
DMA
   ↓
Hardware Timer
   ↓
DAC
```

The hardware timer establishes the sample/update timing while DMA transfers samples to the DAC. This approach supports repeatable waveform timing and leaves the CPU available for other embedded tasks.

## Switching Between Modes

When the operating state changes, the firmware can load the corresponding waveform configuration and sample source. The transition strategy should ensure that waveform parameters are updated at an appropriate transmission boundary rather than producing an unintended partial waveform.

A prototype mode switch can therefore follow:

```text
Input condition changes
        ↓
Decision state updated
        ↓
New waveform selected
        ↓
New LUT / parameters loaded
        ↓
DMA transmission configured
        ↓
Selected waveform transmitted
```

## Validation Plan

Waveform-selection validation should compare the configured input state with the selected output mode.

Recommended checks include:

1. Apply a known input condition.
2. Record the decision state.
3. Record the selected waveform.
4. Capture the generated waveform.
5. Inspect its time-domain and frequency-domain characteristics.
6. Repeat for other representative conditions.

The results can later be stored in the `results/` directory once measurements are available.

## Current Status

The waveform-selection document describes the design approach and intended operating modes. Exact thresholds, weights and performance comparisons should be added only after the corresponding prototype behaviour has been tested and validated.
