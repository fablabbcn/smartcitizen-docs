Gases Pro Sensor Board
======================

The Gases Sensor Board is a custom, ultra-low noise, high-performance, low power, digital output driver for 3 Alphasense Ltd. Electrochemical Series B Gas Sensors specifically designed for the project from the ground up.

![](https://i.imgur.com/4tNzsdR.jpg)

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-gases-pro-board" aria-label="Check the source code">Check the source code</a>

## Sensor measurements

The Gases Pro Board is capable of interfacing with Alphasense Ltd. B4 series sensors without offset voltage compensarion, i.e. it can't interface with NO, NO2 or OX sensors, but it can be used for CO, SO2 and H2S. For measuring NO, NO2 or OX, please refer to the [Analog Sensor Board](/Components/Analog Sensor Board.md)

## Design

Each of the three drivers for Alphasense Ltd. Series B Sensors is built around the same design. They include a three stage adjustable amplifier design for the working electrode and and another simetrical design for the auxiliary electrode. Both signals are then feed to a high accuracy delta-sigma A/D converter with differential inputs 18 bits of resolution. All the parameters are digitally adjustable via I2C from the **Data Board**. Each board also include a unique identifier chip allowing the firmware on the **Data Board** to identify the board and apply the corresponding calibration values and a humidity and temperature sensor. 

!!! info
	Visit the [source files](#source-files) section to download the complete schematics.

![](https://i.imgur.com/b9tGVmH.png)

## Setup

The board is connected to the [Data Board](/ComponentsData Board) using the AUX connector. Before, the Alphasense sensors need to be in place and properly registered using the board id. The board will be autodetected by the main [Firmware](/ComponentsFirmware) running on the Data Board. Multiple sensor board can be daisy-chained as seen on the image.

![](https://i.imgur.com/RRu8MiV.jpg)

!!! info "Validation"
    This board is currently being evaluated under the iScape Project and the results will be public soon!

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-gases-pro-board/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-gases-pro-board" aria-label="Check the source code">Check the source code</a>