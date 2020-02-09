Gases Pro Sensor Board
======================

The Gases Sensor Board is a custom, ultra-low noise, high-performance, low power, digital output driver for 3 Alphasense Ltd. Electrochemical Series B Gas Sensors specifically designed for the project from the ground up.

![](https://i.imgur.com/4tNzsdR.jpg)

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-gases-pro-board" aria-label="Check the source code">Check the source code</a>

## Sensor measurements

| Measurement      | Units | Sensor              |
|------------------|-------|---------------------|
| Carbon Monoxide  | ppm   | Alphasense CO-B4    |
| Nitrogen Dioxide | ppb   | Alphasense NO2-B43F |
| Ozone            | ppb   | Alphasense OX-B431  |

## Sensors selection

The following characteristics have been considered for the sensor choice

-   The driver's board designed includes a temperature and humidity sensor for calibrating the temperature dependence of the sensing subsystem.

-   Same technology as the A4 series but more robust when exposed to outdoor environments 24/7.  

-   Designed for fixed site air quality networks which demand longer term reliability.

-   Manufacturers provide the baseline resistance calibration values per sensor allowing corrections to be easily applied.

-   Low power consumption

The Alphasense EC Sensors were selected to provide a higher linearity, repeatability and resolution than the SGX MICS MO Gas Sensors found on the Urban Sensor Board.

The selection of the sensors was based on the wide variety of literature available on them. Both Penza and EuNetAir Consortium (2014) and Mead et al. (2013) test the NO2A1-A3 against reference instruments, in the laboratory as well as in the field, with well-correlated results. The former concluded that the Data Quality Objective for "indicative measurements" (European Parliament and Council of the European Union, 2008) is fulfilled, and the latter report sensitivity in the low ppb region with high linearity. Spinelle et al. tested the Alphasense NO2B4 and O3B4 in a field experiment, with various calibration approaches. Performance evaluation of the same sensors was performed later including a test on a wide range of performance parameters (e.g. response time, calibration function, repeatability, drift, hysteresis effect, and matrix effect) (Spinelle et al. 2017). The experiment found a strong correlation with reference instruments (R^2^ > 0.9) and identified some cases with significant hysteresis effect related to humidity. In chamber conditions, the performances of the Alphasense CO-B4 was found to be excellent, with the R^2^ values being greater than 0.9 (Castell et al. 2017) (Mead et al. 2013) (Sun et al. 2016). Two field studies reported moderate to excellent R^2^  values (0.53--0.97) for the CO-B4 sensor (Castell et al. 2017) (Mead et al. 2013). Finally, some calibration approaches as detailed in Popoola et al. (2016) and Hagan et al. (2018) are used in the post-processing stage as a basis for pollution concentration calculations.

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

[^8]: ALPHASENSE NO2-B43F Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO~2~B43F.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO~2~B43F.pdf)

[^9]: ALPHASENSE OX-B431 Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/OX-B431.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/OX-B431.pdf)

[^10]: ALPHASENSE CO-B4 B Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2015/04/COB41.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2015/04/COB41.pdf)