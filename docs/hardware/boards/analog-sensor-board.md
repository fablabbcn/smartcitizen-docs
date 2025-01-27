---
type: core
feature_img: None
status: stable
versions: None
interface: None
---

# Analog Sensor Board

The SmartCitizen Analog Sensor Board (_ASB_) is an expansion board for the Smart Citizen Kit that provides connectivity to analog sensors with a high precission ADC (Texas ADS1115) via I2C, with four configurable addresses. It also gives the possibility to directly hook up [this ADC by Adafruit](https://www.adafruit.com/product/1085).

![](/assets/images/asb4ch.jpg)

We use it to measure low power sensors such as the Alphasense Ltd. electrochemical sensors.

## Characteristics

### Operating voltage

Natively operates at 3.3V, but can use also up to 5.5V in EXT-V, and with a selectable jumper. It integrates a level-shifter from the GROVE connector's voltage to EXT-V.

### Connectivity

I2C, from 3.3V up to 5.5V.

### Inputs

<img src="https://live.staticflickr.com/65535/50812573983_30bfb4b35f_k.jpg" width="2000" height="1334" alt="Smart Citizen Station rev3">

- 4 channels in the 4-channel version. Daisy chainable up to 4 boards - with a total of 16 analog channels!
- 8 channels in the 8-channel version.

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-analog-sensor-board" aria-label="Check the source code">Check the source</a>

