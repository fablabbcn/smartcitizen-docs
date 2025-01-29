---
internal:
  writing: false
  proofread: false
  links: false
  images: false
---

# Analog Sensor Board

The SmartCitizen Analog Sensor Board (_ASB_) is an expansion board for the Smart Citizen Kit that provides connectivity to analog sensors with a high precission ADC (Texas ADS1115) via I2C, with four configurable addresses. It also gives the possibility to directly hook up [this ADC by Adafruit](https://www.adafruit.com/product/1085).

<img style="max-height: 350px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/53968621883_5c4f1ab625_k.jpg" alt="Analog-Sensor-Board-front-b"/>

We use it to measure low power sensors such as the Alphasense Ltd. electrochemical sensors, or SPEC sensors. You can use it in different configurations and the different headers:

![](/assets/images/asb-socket-options.png)

Below you see a comparison:

=== "B-series sensors"
    <img src="https://live.staticflickr.com/65535/53968621883_5819b0379c_h.jpg" alt="Analog-Sensor-Board-front-b"/>
=== "A-series sensors"
    <img src="https://live.staticflickr.com/65535/53968379046_ab50fd93bd_h.jpg" alt="Analog-Sensor-Board-front-a"/>
=== "Empty"
    <img src="https://live.staticflickr.com/65535/53968710279_06c66e72e6_h.jpg" alt="Analog-Sensor-Board-front-empty"/>

## Characteristics

![](/assets/images/asb-diagram.png){:style="width: 500px"}

### Operating voltage

Natively operates at 3.3V, but can use also up to 5.5V in EXT-V, and with a selectable jumper. It integrates a level-shifter from the GROVE connector's voltage to EXT-V.

### Connectivity

I2C, from 3.3V up to 5.5V.

### Inputs

<img src="https://live.staticflickr.com/65535/50812573983_30bfb4b35f_k.jpg" width="2000" height="1334" alt="Smart Citizen Station rev3">

- 4 channels in the 4-channel version. Daisy chainable up to 4 boards - with a total of 16 analog channels!
- 8 channels in the 8-channel version.

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-analog-sensor-board" aria-label="Check the source code">Check the source</a>

