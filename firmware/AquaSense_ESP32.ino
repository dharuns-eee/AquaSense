#include <Arduino.h>
#include <math.h>

// ============================================================
// AQUASENSE - BASIC ESP32 PROTOTYPE TRANSMISSION GENERATOR
// This firmware is the current digital demonstration only.
// Planned final hardware platform: STM32G4 + DAC + analog/power
// stages, with oscilloscope verification.
// ============================================================

const float FS = 1000000.0;      // 1 MHz sampling
const float DURATION = 0.001;   // 1 ms
const int N = 1000;              // 1000 samples

// Demonstration frequency band
const float F0 = 250000.0;       // 250 kHz
const float F1 = 270000.0;       // 270 kHz
const float PCP_CARRIER = 260000.0;

// ============================================================
// LFM: 250 kHz -> 270 kHz
// ============================================================

float generateLFM(int n)
{
  float t = (float)n / FS;
  float k = (F1 - F0) / DURATION;

  float phase =
      2.0 * PI *
      (F0 * t + 0.5 * k * t * t);

  return sin(phase);
}

// ============================================================
// HFM: 250 kHz -> 270 kHz
// ============================================================

float generateHFM(int n)
{
  float t = (float)n / FS;
  float a = (F0 - F1) / DURATION;

  float phase =
      2.0 * PI *
      ((F0 * F1 / a) *
      log((F1 + a * t) / F1));

  return sin(phase);
}

// ============================================================
// PCP: 260 kHz carrier with 8-chip phase code
// Code: + + + - - + - +
// ============================================================

float generatePCP(int n)
{
  float t = (float)n / FS;

  const int code[8] =
  {
    1, 1, 1, -1,
    -1, 1, -1, 1
  };

  int samplesPerChip = N / 8;
  int chip = n / samplesPerChip;

  if (chip >= 8)
    chip = 7;

  float carrier =
      sin(2.0 * PI * PCP_CARRIER * t);

  return code[chip] * carrier;
}

// ============================================================
// GEOMETRIC SWEEP
// ============================================================

float generateGeometric(int n)
{
  float t = (float)n / FS;
  float ratio = F1 / F0;

  float phase =
      2.0 * PI *
      (F0 * DURATION / log(ratio)) *
      (pow(ratio, t / DURATION) - 1.0);

  return sin(phase);
}

// ============================================================
// SEND ONE WAVEFORM
// ============================================================

void sendWaveform(const char* name, char type)
{
  Serial.print("WAVEFORM,");
  Serial.println(name);
  Serial.println("DATA");

  for (int n = 0; n < N; n++)
  {
    float sample = 0.0;

    if (type == 'L')
      sample = generateLFM(n);
    else if (type == 'H')
      sample = generateHFM(n);
    else if (type == 'P')
      sample = generatePCP(n);
    else if (type == 'G')
      sample = generateGeometric(n);

    Serial.println(sample, 6);
  }

  Serial.println("END_WAVEFORM");
}

// ============================================================
// TARGET 0 - STATIONARY
// LFM -> PCP
// ============================================================

void sendTarget0()
{
  Serial.println("AQUASENSE_START");
  Serial.println("TARGET,0,STATIONARY");

  sendWaveform("LFM", 'L');
  delay(200);

  sendWaveform("PCP", 'P');

  Serial.println("AQUASENSE_END");
}

// ============================================================
// TARGET 1 - NON-STATIONARY
// HFM -> LFM -> PCP
// ============================================================

void sendTarget1()
{
  Serial.println("AQUASENSE_START");
  Serial.println("TARGET,1,NON_STATIONARY");

  sendWaveform("HFM", 'H');
  delay(200);

  sendWaveform("LFM", 'L');
  delay(200);

  sendWaveform("PCP", 'P');

  Serial.println("AQUASENSE_END");
}

// ============================================================
// SETUP
// ============================================================

void setup()
{
  Serial.begin(115200);
  delay(1000);
  Serial.println("AQUASENSE_READY");
}

// ============================================================
// LOOP
// ============================================================

void loop()
{
  if (Serial.available())
  {
    char command = Serial.read();

    if (command == '0')
      sendTarget0();
    else if (command == '1')
      sendTarget1();
  }
}
