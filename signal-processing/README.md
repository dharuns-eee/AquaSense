# Signal Processing

AquaSense uses signal analysis to verify transmitted waveforms and provide feedback for the adaptive system.

## Analysis Methods

- FFT
- Spectrum analysis
- Spectrogram
- Performance metrics
- Closed-loop feedback

## Signal Model

A general transmitted signal can be represented as:

$$s(t)=A(t)\cos\left(2\pi\int_0^t f(\tau)\,d\tau+\phi\right)$$

For Linear Frequency Modulation (LFM):

$$f(t)=f_0+kt$$

where $f_0$ is the starting frequency and $k$ is the frequency-sweep rate.

Validated measured plots and datasets will be added here as testing progresses.
