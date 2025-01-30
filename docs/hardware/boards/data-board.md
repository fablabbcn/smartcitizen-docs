---
internal:
  writing: true
  proofread: false
  links: false
  images: false
---

# Data Board

The **Data Board** is the core of the SCK architecture supporting the data-logging tasks. It's designed to perform the heavylifting and interface with sensors, the user, the SD card, take care of communications, and power management. All SCK2.X versions are practically the same, building upon the SCK2.1 design with minor modifications.

=== "SCK2.3"
    <img style="max-height: 325px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281911435_c1ae473a74_o.jpg" alt="SCK2.3 Data Board"/>
=== "SCK2.2"
    <img style="max-height: 325px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281911450_2edda8b7ed_o.jpg" alt="SCK2.2 Data Board"/>
=== "SCK2.1"
    <img style="max-height: 325px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281911410_5f944402a3_o.jpg" alt="SCK2.1 Data Board"/>

<a class="github-button" data-size="large" href="{{ config.extra.urls.ghhardware.link }}" aria-label="Check the design files">Check the design files</a>

## Microcontrollers

The **Data Board** is powered by an ARM M0+ 32-bits 48Mhz **SAMD21** running the [Smart Citizen Firmware](/docs/hardware/firmware/), combining the low power consumption of the ARM M0 family with the power of a 32-bits processor with 32KB of RAM and 256KB of FLASH memory. This solution offers enough program storage and memory space to support multiple auxiliary sensors. This chip is used by the Arduino Zero and MKR boards, therefore benefiting from the open community built around these boards in particular and the Arduino project in general.

![](/assets/images/data-board-mcus.png){:style="width: 500px;"}

The **Data Board** also includes a Wi-Fi module, a micro SD card slot, an internal Flash and a battery management solution. In addition, it includes 4MB of extra Flash Memory for offline data storage, in case of network brownouts. The Wi-Fi Module is the well-known [**Espressif ESP8266**](https://www.espressif.com/en/products/hardware/esp8266ex/overview) IEEE 802.11 b/g/n Wi-Fi with 4MB Internal Flash for web content storage.

## Connectors

The **Data Board** connects to the [Urban board](/hardware/boards/urban-board/) providing power, analog and digital communications (12 bits ADC, GPIO, I2C, I2S, VCC). The Data Board also includes a Seeed Studio standard Grove connector where off-the-shelf modules from the same manufacturer can be connected. The connector supports an independent I2C bus by default, but by software it can be configured to support other uses (GPIO, I2C and UART). It can supply power up to 750mA, and it can be enabled or disabled by software to save power.

![](/assets/images/data-board-connectors.png){:style="width: 500px;"}

The board includes a power unit, with a battery management system, capable of handling a variety of Lithium polymer cells. The batteries are connected to a standard JST-2 pin battery connector. The Smart Citizen Kit by default uses a 2000mAh battery, but larger capacities can be used.

![](/assets/images/data-board-connectors-power.png){:style="width: 500px;"}

The controller allows the batteries to be easily charged using the boards micro USB connector using any standard USB power adapter like the ones used on Smartphones. It can also be powered via the micro USB connector using a [Solar Panel](/hardware/addons/solar-panel/).

## User interfaces

The **Data board** features feedback LEDs, which behaviour is described on the [features](/hardware/kit/features/#user-interfaces) page.

![](/assets/images/data-board-leds.png){:style="width: 500px;"}

It also supports input via the button (both the [ON/OFF button](/hardware/kit/features/#the-onoff-button) and the [reset button](/hardware/kit/features/#the-reset-button)):

![](/assets/images/data-board-buttons.png){:style="width: 500px;"}

## Buses

Below you have a pinout of the **Data Board** buses:

![](/assets/images/data-board-pinout.png){:style="width: 500px;"}

### Sensor Board connector

The **Data Board** features a modular architecture where sensors can be updated independently by replacing any individual Sensor Board. The Sensor Boards features GPIO, ADC, I2C, UART and I2S connections at 3.3V. Currently, we only offer the Urban Sensor Board, but more boards are on the way, and you can even design and build a custom one.

### Auxiliary connector

The **Data Board** features and independent configurable auxiliary bus at 3.3V with a SEEED Studio Grove connector. The Bus has native support for I2C, but it can also be setup on firmware as a GPIO or UART port. It can supply power up to 750mA, and it can be enabled or disabled by software.

## Power management

The **Data Board** features the possibility of running directly from a USB power source with or without lithium battery (only for SCK2.1; SCK2.2 and SCK2.3 require a battery), using the [BQ24259 USB Charger](/assets/datasheets/components/bq24259.pdf). The charger manages external power regulation, battery fast charging (up to 2Ah) and USB OTG that allow us powering other devices from the **Data Board** (although this is currently not implemented).

Normally the SCK uses a 2000 mAh [Lithium polymer battery](https://en.wikipedia.org/wiki/Lithium_polymer_battery) but it is possible to take advantage of larger batteries. The charging current is regulated with a manually coded limit that can be configured, and also auto adjusted to the connected USB charger capacity.

## Design files

You can find all the design files for the different versions of the **Data Board** in the [hardware repository]({{ extra.urls.ghhardware.link }}).

<a class="github-button" data-size="large" href="{{ config.extra.urls.ghhardware.link }}" aria-label="Check the design files">Check the design files</a>

!!!info "Previous versions"
    Previous versions of the SCK, are in their respective repositories:

    - Smart Citizen Kit 2.0: https://github.com/fablabbcn/smartcitizen-kit-20
    - Smart Citizen Kit 1.5: https://github.com/fablabbcn/smartcitizen-kit-15