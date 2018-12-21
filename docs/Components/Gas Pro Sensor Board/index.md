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

The final EC sensors selected were Alphasense Ltd. NO~2~B4[^8] (Nitrogen Dioxide Sensor), O3B4[^9] (Oxidising Gas Sensor Ozone + Nitrogen Dioxide) and COB4[^10] (Carbon Monoxide). This selection was based on the academic references selected above. For a complete Low-Cost Sensors Evaluation see ISCAPE D1.5 Summary of air quality sensors and recommendations for application and the subsequent publication _(Rai et al. 2017_. Both _(Penza and EuNetAir Consortium 2014)_ and _(Mead et al. 2013)_ test the Alphasense Ltd (UK) NO~2~A1-A3 against reference instruments, both in the laboratory and in the field, with well-correlated results. The former concluded that the Data Quality Objective for "indicative measurements" (European Parliament and Council of the European Union, 2008) are fulfilled, and the latter report sensitivity in the low ppb region with high linearity. _(Jensen 2016)_ _(Spinelle et al. 2015)_ tested the Alphasense NO~2~B4 and O3B4 in a field experiment, with various calibration approaches. The correlation with reference measurements was poor (R2 \< 0.1 and R2 \< 0.5 for NO~2~ and O~3~, respectively) when using linear and multivariate linear calibration, and good (R2 around 0.9 and 0.6 for NO~2~ and O~3~, respectively) when using artificial neural networks. The poor results for NO~2~ are likely due to the experiments being in a rural setting with quite low NO~2~ concentrations. _(Jensen 2016)_.  A performance evaluation of the same sensors was performed later including a test on a wide range of performance parameters (e.g. response time, calibration function, repeatability, drift, hysteresis effect and matrix effect) _(Spinelle et al. 2015)_. The experiment gave very good correlation with reference instruments (R2 \> 0.99) and identifies some cases with major hysteresis effect related to humidity. _(Spinelle et al. 2014)_ did a detailed laboratory and field study of the Alphasense Ltd (UK) O3B4 O~3~ sensor, reporting good linearity, while uncertainty is adequately low to meet the requirements for \"indicative measurements\" by the Data Quality Objective (European Parliament and Council of the European Union, 2008). _(Jensen 2016)_. In chamber conditions, the performances of the Alphasense CO-B4 was found to be excellent, with the R2 values being greater than 0.99 _(Castell et al. 2017; Mead et al. 2013; Sun et al. 2016_. However, the field investigations report significant deterioration and variations in sensor performances as given in Table 6. Two field studies reported moderate to excellent R2 values (0.53--0.97) for the CO-B4 sensor _(Borrego et al. 2016)_; _(Castell et al. 2017; Mead et al. 2013; Sun et al. 2016)_. However, two other field studies have reported significantly lower R2 values (0.17--0.45) for the CO-B4, when calibrating them with reference measurements  _Castell et al. 2017; Mead et al. 2013; Sun et al. 2016)_ _(Spinelle et al. 2017)_ _(Rai et al. 2017)_ _(Spinelle et al. 2017)_.

## Design

Each of the three drivers for Alphasense Ltd. Series B Sensors is built around the same design. They include a three stage adjustable amplifier design for the working electrode and and another simetrical design for the auxiliary electrode. Both signals are then feed to a high accuracy delta-sigma A/D converter with differential inputs 18 bits of resolution. All the parameters are digitally adjustable via I2C from the **Data Board**. Each board also include a unique identifier chip allowing the firmware on the **Data Board** to identify the board and apply the corresponding calibration values and a humidity and temperature sensor. 

!!! info
	Visit the [source files](#source-files) section to download the complete schematics.

![](https://i.imgur.com/b9tGVmH.png)

## Setup

The board is connected to the [Data Board](/ComponentsData Board) using the AUX connector. Before, the Alphasense sensors need to be in place and properly registered using the board id. The board will be autodetected by the main [Firmware](/ComponentsFirmware) running on the Data Board. Multiple sensor board can be daisy-chained as seen on the image.

![](https://i.imgur.com/RRu8MiV.jpg)


## Field validation

!!! warning
	The following section is work in progress and the sensors are being test by different partners.

A comparaison of the NO~2~ measurements taken by the Gas Pro Board Alphasense NO2-B43F and a [Teledyne TML-41](http://www.teledyne-ml.com/pdf/TML41MHmanual.pdf) used by [UCD](https://www.ucd.ie/) as the reference equipment.

![](https://i.imgur.com/DbCuX0g.jpg)

## Design

Each of the three drivers for Alphasense Ltd. Series B Sensors is built around the same design. They include a three stage adjustable amplifier design for the working electrode and and another simetrical design for the auxiliary electrode. Both signals are then feed to a high accuracy delta-sigma A/D converter with differential inputs 18 bits of resolution. All the parameters are digitally adjustable via I2C from the **Data Board**. Each board also include a unique identifier chip allowing the firmware on the **Data Board** to identify the board and apply the corresponding calibration values and a humidity and temperature sensor. 

!!! info
	Visit the [source files](#source-files) section to download the complete schematics.

![](https://i.imgur.com/b9tGVmH.png)

## Setup

The board is connected to the [Data Board](/ComponentsData Board) using the AUX connector. Before, the Alphasense sensors need to be in place and properly registered using the board id. The board will be autodetected by the main [Firmware](/ComponentsFirmware) running on the Data Board. Multiple sensor board can be daisy-chained as seen on the image.

![](https://i.imgur.com/RRu8MiV.jpg)


## Field validation

!!! warning
	The following section is work in progress and the sensors are being test by different partners.

A comparaison of the NO2 measurements taken by the Gas Pro Board Alphasense NO2-B43F and a [Teledyne TML-41](http://www.teledyne-ml.com/pdf/TML41MHmanual.pdf) used by [UCD](https://www.ucd.ie/) as the reference equipment.

![](https://i.imgur.com/DbCuX0g.jpg)

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-gases-pro-board/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-gases-pro-board" aria-label="Check the source code">Check the source code</a>

[^8]: ALPHASENSE NO2-B43F Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO~2~B43F.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO~2~B43F.pdf)

[^9]: ALPHASENSE OX-B431 Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/OX-B431.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/OX-B431.pdf)

[^10]: ALPHASENSE CO-B4 B Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2015/04/COB41.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2015/04/COB41.pdf)