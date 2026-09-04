# Waveform Selection

AquaSense uses software-defined waveform generation so the same transmitter hardware can switch between multiple waveform modes.

## Waveform Modes

| Waveform | Intended operating condition |
|---|---|
| LFM | Stationary / clear and stable conditions |
| HFM | Changing conditions / moving-target Doppler conditions |
| Phase-Coded Pulses (PCP) | High-turbidity conditions |
| Geometric Sweep | Alternative software-defined sweep |

## Decision Approach

The controller evaluates environmental and mission inputs using weighted decision logic:

$$S_i=\sum_{j=1}^{n}w_jx_j$$

The selected waveform can be represented as:

$$W^*=\arg\max_{W_i}S_i$$

The exact thresholds and weights are treated as design parameters and should be validated with controlled experiments before being presented as measured results.

## Real-Time Execution

Precomputed waveform Look-Up Tables (LUTs), DMA and hardware timers reduce repeated CPU work during transmission and enable fast waveform switching.
