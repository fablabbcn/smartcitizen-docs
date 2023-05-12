PM Board
====================

The PM Board is an expansion board which can provide additional measurements, such as two extra Plantower PMS 5003, one wire temperature sensors and extra GPIO and ADC support. This is done with a custom designed PCB with an MCU to provide I2C connectivity with the Data Board.

![](/assets/images/Hqt1dXh.jpg)

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-pm-board" aria-label="Check the source code">Check the source code</a>

## Design

The PM Board runs a dedicated ARM M0+ 32-bits, the same as the [Data Board](/Components/Data Board) to provide a unified hardware architecture. The board includes an higly efficient step up to provide 5V to drive the PM sensors and a disable/enable circuit to turn off the sensor by software.

!!! info
	Visit the [source files](#source-files) section to download the complete schematics.

### Pinout

![](/assets/images/DU0hmvx.png)

![](/assets/images/TEPeK3h.png)

#### SERCOM distribution

![](/assets/images/80ob4cX.png)

## Setup

The board is connected to the [Data Board](/Components/Data Board) using the AUX connector. Before, the Plantower PMS sensors need to be connected. The board will autodetect the PMS sensors and present them seamlessly to the main [Firmware](/Components/Firmware)  running on the Data Board. Multiple sensor board can be daisy-chained as seen on the image.

![](/assets/images/RRu8MiV.jpg)

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-pm-board/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-pm-board" aria-label="Check the source code">Check the source code</a>