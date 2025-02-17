---
card: true
name: Atlas EZO Drivers
feature_img: https://live.staticflickr.com/65535/54333644981_23a2dcff0e_h.jpg
custom_color: blue
type:
    - addon
excerpt: You can use these drivers to interface with Atlas Scientific Probes!
---


# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

These drivers can be used to interface with Atlas Scientific sensors. Each driver is designed to interface with a different type of probe. You can find probe information in the [knowledge](/knowledge/soil-water/) section.

The drivers can be used with carrier boards. We generally use the [Isolated carrier board](https://atlas-scientific.com/carrier-boards/electrically-isolated-ezo-carrier-board-gen-2/), but you can choose other options. These carrier boards can be found in the [water stations](/docs/hardware/stations/water/).

![](https://live.staticflickr.com/65535/54334059580_c7e9d8c68f_h.jpg)

## Setup

This page describes the setup procedure of the Atlas Scientific probes in case you bought them separately. If you have a [water stations](/docs/hardware/stations/water/), you don't need to do this.

### Manually switching circuits to I2C mode

If the drivers are new normally they come configured in UART mode so we need to change them to I2C mode.

1. Remove circuit from carrier board.
2. Put the circuit into a breadboard.
3. For **PH**, **DO**, **ORP** and **EC**: Short the `PGND` pin to the `TX` pin using a jumper wire.
4. For **RTD** (temperature): Short the `PRB` pin to the `TX` pin using a jumper wire.
5. Power the device (connecting `GND` and `VCC`)
6. Wait for LED to change from green to blue (UART→I2C) or from blue to green (I2C→>UART).
7. Remove the jumper wire from the `PGND` (or `PRB` respectively) pin to the `TX` pin (Do this **before removing power!**).
8. Remove power (`VCC`).
9. Apply power (`VCC`).
10. The device is now in the new mode (repeat all steps to switch back to previous mode).
