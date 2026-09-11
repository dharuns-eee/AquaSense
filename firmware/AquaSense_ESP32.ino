#include <Arduino.h>
#include <math.h>

// ============================================================
// AQUASENSE - FINAL ESP32 TRANSMISSION GENERATOR
// ============================================================

const float FS = 100000.0;
const float DURATION = 0.010;
const int N = 1000;

const float F0 = 1000.0;
const float F1 = 5000.0;
const float PCP_CARRIER = 3000.0;

float generateLFM(int n)
{
  float t = (float)n / FS;
  float k = (F1 - F0) / DURATION;
  float phase = 2.0 * PI * (F0 * t + 0.5 * k * t * t);
  return sin(phase);
}

float generateHFM(int n)
{
  float t = (float)n / FS;
  float a = (F0 - F1) / DURATION;
  float phase = 2.0 * PI * ((F0 * F1 / a) * log((F1 + a * t) / F1));
  return sin(phase);
}

float generatePCP(int n)
{
  float t = (float)n / FS;

  const int code[8] = {1, 1, 1, -1, -1, 1, -1, 1};
  int samplesPerChip = N / 8;
  int chip = n / samplesPerChip;

  if (chip >= 8)
    chip = 7;

  float carrier = sin(2.0 * PI * PCP_CARRIER * t);
  return code[chip] * carrier;
}

float generateGeometric(int n)
{
  float t = (float)n / FS;
  float ratio = F1 / F0;
  float phase = 2.0 * PI * (F0 * DURATION / log(ratio)) * (pow(ratio, t / DURATION) - 1.0);
  return sin(phase);
}

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

void sendTarget0()
{
  Serial.println("AQUASENSE_START");
  Serial.println("TARGET,0,STATIONARY");

  sendWaveform("LFM", 'L');
  delay(200);

  sendWaveform("PCP", 'P');

  Serial.println("AQUASENSE_END");
}

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

void setup()
{
  Serial.begin(115200);
  delay(1000);
  Serial.println("AQUASENSE_READY");
}

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
