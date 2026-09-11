# Media

This directory contains the visual evidence and presentation assets for AquaSense.

## Media Set

The project presentation is organized around nine visuals:

1. AquaSense system workflow.
2. Complete MATLAB/Simulink architecture.
3. Dynamic environmental inputs: depth, temperature, salinity and turbidity.
4. Adaptive parameter analysis.
5. Adaptive SONAR waveform generator: LFM, HFM, PCP and geometric sweep.
6. Stationary target mode: `LFM → PCP`.
7. Stationary target demonstration with Hann-windowed FFT analysis.
8. Non-stationary target mode: `HFM → LFM → PCP`.
9. Non-stationary target demonstration with Hann-windowed FFT analysis.

The approved captions for these nine visuals are maintained in `captions.md`.

## Recommended Presentation Order

Use the nine visuals in the order above when building the competition story: system concept → architecture → environmental inputs → adaptive parameters → waveform generation → stationary case → stationary analysis → non-stationary case → non-stationary analysis.

## Labelling Guidance

Clearly distinguish:

- **System architecture / diagrams** — design representation.
- **MATLAB/Simulink figures** — model/simulation evidence.
- **ESP32/Python dashboard** — digital prototype demonstration.
- **Oscilloscope or physical captures** — measured hardware evidence.

Do not present a simulation or controlled presentation visualization as a physical measurement.

## Manual Image Upload

Image files are intentionally kept separate from the repository documentation workflow. Add the nine final image files to this directory manually using the approved captions in `captions.md`.

No image files are modified by the documentation updates in this repository pass.
