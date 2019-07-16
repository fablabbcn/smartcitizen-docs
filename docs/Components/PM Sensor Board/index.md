PM Sensor Board
====================

The PM Sensor Board is based around Plantower PMS 5003[^11] a digital particle concentration sensor that uses the Laser Scattering principle to obtain the number of suspended particles in the air. This includes a custom designed PCB with an MCU to provide I2C connectivity with the Data Board.  

![](https://i.imgur.com/Hqt1dXh.jpg)

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-pm-board" aria-label="Check the source code">Check the source code</a>

## Sensor measurements

| Measurement | Units | Sensor                        |
|-------------|-------|-------------------------------|
| PM 1        | µg/m3 | Plantower PMS5003 Dual System |
| PM 2.5      | µg/m3 | Plantower PMS5003 Dual System |
| PM 10       | µg/m3 | Plantower PMS5003 Dual System |


## Sensors selection


The following characteristics have been considered for the sensor
choice:

* Provides PM 2.5 and PM 10 measurements in ug/m³

* Minimal distinguishable particle diameter of 0.3 am

* No need for external ADC or linearization circuits. The sensor includes an internal MCU capable of dealing with all the light emitting and sensing processing. All the communication is done using the I2C protocol. A dedicated driver has been designed for this.

* Ultra Low Cost when compared to other commercial solutions with similar performance

* Low Power

The selection is based on the academic references selected above. For a complete Low-Cost Sensors Evaluation see recommendations for application and the subsequent publication _(Rai et al. 2017)_.

## Design

The PM Sensor Board runs a dedicated ARM M0+ 32-bits, the same as the [Data Board](/ComponentsData Board) to provide a unified hardware architecture. The board includes an higly efficient step up to provide 5V to drive the PM sensors and a disable/enable circuit to turn off the sensor by software.

!!! info
	Visit the [source files](#source-files) section to download the complete schematics.

## Setup

The board is connected to the [Data Board](/ComponentsData Board) using the AUX connector. Before, the Plantower PMS sensors need to be connected. The board will autodetect the PMS sensors and present them seamlessly to the main [Firmware](/ComponentsFirmware)  running on the Data Board. Multiple sensor board can be daisy-chained as seen on the image.

![](https://i.imgur.com/RRu8MiV.jpg)

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-pm-board/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-pm-board" aria-label="Check the source code">Check the source code</a>


[^11]: PLANTOWER PMS5003 Technical Datasheet [https://aqicn.org/air/view/sensor/spec/pms5003.pdf](https://aqicn.org/air/view/sensor/spec/pms5003.pdf)