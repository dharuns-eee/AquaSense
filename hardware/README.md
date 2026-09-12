# Hardware

AquaSense is a **SONAR transmitter payload/subsystem for an AUV**. The repository distinguishes the broader intended transmitter hardware from the **current basic ESP32/Python prototype** and the **planned final STM32G4 hardware demonstration**.

## Current Basic Prototype

The current basic demonstration uses:

- ESP32 development board
- USB connection to a laptop
- Python host application for serial reception and visualization

The ESP32 prototype is a **digital waveform-generation and serial-streaming demonstration**. It does not currently include a SONAR receiver or the complete physical acoustic transmit chain.

## Planned Final Hardware Demonstration

The final physical demonstration will use an **STM32G4** with a high-speed DAC and analog/power stages. An **oscilloscope** will be used to verify the electrical waveform.

```text
Environmental / Mission Inputs
          ↓
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

The STM32G4 chain above is the planned final hardware direction, not a description of the current ESP32 basic demo.

## System-Level Components

### Embedded controller

The final hardware design uses an STM32G4 to coordinate input acquisition, adaptive decisions, waveform generation and deterministic sample delivery.

### Environmental input interface

Temperature, salinity, depth and turbidity are representative inputs to the system-level adaptive architecture. They are not required for the current ESP32 basic menu demonstration.

### DAC

The intended physical chain converts digital waveform samples into an analog signal before filtering and amplification.

### Low-Pass Filter

The filter conditions the reconstructed analog waveform and suppresses unwanted components before the power stage.

### Amplifier / MOSFET Stage

The amplifier and switching stage provide the drive path toward the acoustic transducer or test load.

### SONAR Transducer and Receiver

These blocks form the physical acoustic interface planned for later validation. A receiver would provide the echo information needed for real target observation and motion/Doppler analysis.

### Oscilloscope

An oscilloscope will be used in the final hardware demonstration to inspect and verify the physical electrical waveform at appropriate points in the transmitter chain.

## Hardware-to-Software Relationship

```text
System-level inputs
      ↓
Adaptive decision
      ↓
Waveform selection
      ↓
STM32G4 waveform generation
      ↓
DAC / analog chain
      ↓
Acoustic output / test load
      ↓
Oscilloscope verification
```

For the current basic prototype, the physical transmission stages are represented by the ESP32 digital/serial demonstration and Python visualization.

## Final Hardware Validation Plan

Validation should proceed stage by stage:

1. Verify STM32G4 peripherals.
2. Verify environmental-input acquisition where implemented.
3. Verify waveform samples.
4. Verify high-speed DAC output.
5. Verify filtering.
6. Verify MOSFET/power-stage operation.
7. Verify amplifier output.
8. Verify transducer/test-load interface.
9. Capture the electrical waveform with the oscilloscope.
10. Add receiver-based target observation.
11. Measure waveform characteristics and power.
12. Perform controlled underwater testing.

No physical acoustic-performance claim should be made until the corresponding hardware stage has been measured.