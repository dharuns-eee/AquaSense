# Hardware

AquaSense is a **SONAR transmitter payload/subsystem for an AUV**. The repository distinguishes the broader intended transmitter hardware from the current ESP32 competition prototype.

## Current Competition Prototype

The final live demonstration uses:

- ESP32 development board
- USB connection to a laptop
- Python host application for serial reception and visualization

The ESP32 prototype is a **digital waveform-generation and serial-streaming demonstration**. It does not currently include a SONAR receiver or a complete acoustic transmit chain.

## Broader Intended Hardware Chain

```text
Environmental / Mission Inputs
          ↓
   Embedded Controller
          ↓
      High-Speed DAC
          ↓
     Low-Pass Filter
          ↓
 Class-D Amplifier / MOSFET Stage
          ↓
 SONAR Acoustic Transducer
          ↓
 Receiver / Oscilloscope
```

The system-level architecture and MATLAB/Simulink model use the STM32G4/SAR-ADC/DAC-oriented transmitter concept. That architecture is the planned full payload direction, not a claim that every block is present in the final ESP32 demonstration.

## System-Level Components

### Embedded controller

The broader design uses an MCU to coordinate input acquisition, adaptive decisions, waveform generation and deterministic sample delivery.

### Environmental input interface

Temperature, salinity, depth and turbidity are representative inputs to the system-level adaptive architecture. They are not required for the final ESP32 menu demonstration.

### DAC

The intended physical chain converts digital waveform samples into an analog signal before filtering and amplification.

### Low-Pass Filter

The filter conditions the reconstructed analog waveform and suppresses unwanted components before the power stage.

### Amplifier / MOSFET Stage

The amplifier and switching stage provide the drive path toward the acoustic transducer.

### SONAR Transducer and Receiver

These blocks form the future physical acoustic interface. A receiver would provide the echo information needed for real target observation and motion/Doppler analysis.

### Oscilloscope

An oscilloscope can be used to inspect the physical electrical waveform at appropriate points in the transmitter chain.

## Hardware-to-Software Relationship

```text
System-level inputs
      ↓
Adaptive decision
      ↓
Waveform selection
      ↓
Digital waveform generation
      ↓
DAC / analog chain
      ↓
Acoustic output
```

For the current competition prototype, the last physical transmission stages are represented by the digital/serial demonstration and Python visualization.

## Future Validation

Future hardware validation should proceed stage by stage:

1. Verify controller peripherals.
2. Verify environmental-input acquisition.
3. Verify waveform samples.
4. Verify DAC output.
5. Verify filtering.
6. Verify amplifier/MOSFET operation.
7. Verify transducer interface.
8. Add receiver-based target observation.
9. Measure waveform characteristics and power.
10. Perform controlled underwater testing.

No physical acoustic-performance claim should be made until the corresponding hardware stage has been measured.
