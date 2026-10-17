"""
Air Quality Level Classification using Gas Sensor, ESP32 and MicroPython

IMPORTANT:
- This starter code reads an analog gas sensor output and classifies it using
  example thresholds. It is NOT a trained TinyML model yet.
- Calibrate the thresholds for your exact sensor and environment.
- Many MQ sensors need a warm-up period and a suitable analog interface.
- Check your ESP32 board's ADC pin range and voltage limits before connecting.
"""

from machine import ADC, Pin
from time import sleep

# Change this to the ADC pin you actually connected your sensor's analog output to.
# GPIO34 is an ADC input on many classic ESP32 boards, but pin availability varies.
GAS_SENSOR_PIN = 34

# Example thresholds only. Replace after collecting calibration data.
# The reading range depends on board, sensor, wiring, and ADC configuration.
MODERATE_THRESHOLD = 1400
HIGH_THRESHOLD = 2500

SAMPLES = 10
SAMPLE_DELAY_SECONDS = 0.1

sensor = ADC(Pin(GAS_SENSOR_PIN))

# Configure ADC where supported by the ESP32 MicroPython firmware.
try:
    sensor.atten(ADC.ATTN_11DB)
except AttributeError:
    pass

try:
    sensor.width(ADC.WIDTH_12BIT)
except AttributeError:
    pass


def read_gas_sensor():
    """Return the average raw ADC reading from the gas sensor."""
    readings = []
    for _ in range(SAMPLES):
        readings.append(sensor.read())
        sleep(SAMPLE_DELAY_SECONDS)
    return sum(readings) // len(readings)


def classify_air_quality(reading):
    """Classify using placeholder thresholds, not a trained ML model."""
    if reading < MODERATE_THRESHOLD:
        return "LOW RELATIVE SENSOR READING"
    elif reading < HIGH_THRESHOLD:
        return "MODERATE RELATIVE SENSOR READING"
    return "HIGH RELATIVE SENSOR READING"


while True:
    try:
        value = read_gas_sensor()
        label = classify_air_quality(value)

        print("Gas sensor ADC reading:", value)
        print("Classification:", label)
        print("-" * 35)

    except Exception as error:
        print("Sensor read error:", error)

    sleep(2)
