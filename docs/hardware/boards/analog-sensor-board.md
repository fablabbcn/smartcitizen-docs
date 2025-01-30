---
internal:
  writing: true
  proofread: false
  links: false
  images: false
---

# Analog Sensor Board

The SmartCitizen Analog Sensor Board (_ASB_) is an expansion board for the Smart Citizen Kit that provides connectivity to analog sensors with a high precission ADC (Texas ADS1115) via I2C, with four configurable addresses. It also gives the possibility to directly hook up [this ADC by Adafruit](https://www.adafruit.com/product/1085).

<img style="max-height: 350px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/53968621883_5c4f1ab625_k.jpg" alt="Analog-Sensor-Board-front-b"/>

We use it to measure analog voltages from low power sensors such as the [Alphasense Ltd.](https://www.alphasense.com/) [electrochemical](/docs/knowledge/air/chemical/Alphasense_Electrochemical/) sensors, or [SPEC](https://www.spec-sensors.com/) sensors. You can use it in different configurations and the different headers:

![](/assets/images/asb-socket-options.png)

Below you see a comparison:

=== "B-series sensors"
    <img src="https://live.staticflickr.com/65535/53968621883_5819b0379c_h.jpg" style="max-height: 350px; width: 100%; object-fit: cover;" alt="Analog-Sensor-Board-front-b"/>
=== "A-series sensors"
    <img src="https://live.staticflickr.com/65535/53968379046_ab50fd93bd_h.jpg" style="max-height: 350px; width: 100%; object-fit: cover;" alt="Analog-Sensor-Board-front-a"/>
=== "Empty"
    <img src="https://live.staticflickr.com/65535/53968710279_06c66e72e6_h.jpg" style="max-height: 350px; width: 100%; object-fit: cover;" alt="Analog-Sensor-Board-front-empty"/>

## Features

The **Analog Sensor Board** features two [TI ADS1115](https://www.ti.com/product/ADS1115) 16bit 4-channel ADCs, and can read 8 analog channels in total. It has a potential to read up to 16 channels by daisy chainning two boards (by changing the address with the selectable jumper), or many more if you use a multiplexer.

!!! info "Previous version"
    A previous version could interface 4 channels, daisy chainable up to 4 boards - with a total of 16 analog channels, by using [Adafruit ADS1115 Breakout board](https://www.adafruit.com/product/1085).

Below you have a functional diagram:

![](/assets/images/asb-diagram.png){:style="width: 450px"}

The **Analog Sensor Board** natively operates at 3.3V, but can work up to 5.5V with a selectable jumper through a step-up converter (RECOM 0309S), making the digital voltage consistent with the sensor measurement voltage. To make everything consistent, it integrates a level-shifter from the GROVE connector's voltage to the internal voltage. Digital communications, via the Grove port, is done via I2C, from 3.3V up to 5.5V.

## Design files

You can find all the design files for the different versions of the **Analog Sensor Board** in the [hardware repository](https://github.com/fablabbcn/smartcitizen-analog-sensor-board).

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-analog-sensor-board" aria-label="Check the design files">Check the design files</a>

