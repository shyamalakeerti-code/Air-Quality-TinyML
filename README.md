# Air Quality Level Classification using Gas Sensor and TinyML

## Project overview
This project uses an ESP32 and a gas sensor to read an analog sensor signal and display a simple air-quality-related category over the serial console. The code is written for MicroPython.

## Current status
The included `main.py` is a **starter prototype**. It uses example threshold rules to classify relative sensor readings. It does **not** contain a trained TinyML model yet, and the output is not a certified measurement of air quality or a direct measurement of AQI.

To make this a genuine TinyML project, collect labelled sensor data, train and evaluate a small model, then deploy a compatible model/runtime to the ESP32.

## Hardware
- ESP32 development board
- Analog-output gas sensor module (for example, an MQ-series module compatible with your setup)
- Jumper wires
- USB cable for programming and serial output

## Wiring
Connect:
- Sensor VCC to the voltage recommended by the sensor module
- Sensor GND to ESP32 GND
- Sensor analog output (AO) to the selected ESP32 ADC input

**Safety and compatibility:** Do not connect a sensor output that can exceed the ESP32 pin's permitted voltage. Some sensor modules powered at 5 V can produce analog outputs above the ESP32's safe input range; use a suitable level shifter or voltage divider when required. Check the documentation for your exact ESP32 board and sensor. Sensor heaters may become hot and require warm-up.

## Software
- MicroPython firmware installed on the ESP32
- Thonny IDE or another tool that can copy files to the ESP32

## Files
- `main.py` — reads averaged ADC values and prints a threshold-based category.
- `README.md` — project description and setup notes.

## How to run
1. Confirm the sensor model and wiring.
2. Install MicroPython on your ESP32.
3. Open `main.py` in Thonny.
4. Change `GAS_SENSOR_PIN` to your actual ADC pin.
5. Calibrate `MODERATE_THRESHOLD` and `HIGH_THRESHOLD` using readings from your sensor.
6. Save/copy `main.py` to the ESP32 as `/main.py`.
7. Reset the board and view output in the serial console.

## Calibration
The example thresholds are placeholders. Record readings in known test conditions and choose thresholds based on your own data. Gas sensor readings vary with sensor model, temperature, humidity, warm-up, and the substances present.

## TinyML next steps
1. Collect sensor readings with meaningful labels.
2. Split data into training and test sets.
3. Train a small classification model.
4. Evaluate it using held-out data.
5. Convert/deploy the model using a runtime supported by your ESP32/MicroPython setup.
6. Replace the placeholder threshold logic with model inference and document the model, dataset, and accuracy.

## Limitations
This prototype is for learning and demonstration only. It is not a safety device and must not be used to detect dangerous gas concentrations or certify indoor air quality.
