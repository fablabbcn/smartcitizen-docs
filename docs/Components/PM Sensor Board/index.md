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

The selection is based on the academic references selected above. For a complete Low-Cost Sensors Evaluation see ISCAPE D1.5 Summary of air quality sensors and recommendations for application and the subsequent publication _(Rai et al. 2017)_.

Compliance with the NAAQS (US National Ambient Air Quality Standards) is based on 24-h PM mass concentrations \[\...\] Both of the FEM instruments correlate with the 24-h PM2.5 mass measurements with an R2 \> 0.99. The PMS PM2.5 concentrations are also well correlated with the 24-h mass average concentration (R2 \> 0.88), which is slightly better than the GRIMM research-grade instrument (R2 1⁄4 0.7.). South Coast Air Quality Management District (SCAQMD) recently published preliminary comparisons of the PM2.5 measurements from three PMS 1003s and two FEMs, with high correlations (R2 \> 0.9) over a 2-month period. This study demonstrated that the PMS 1003/3003 correlates well with FRMs, FEMs, and research-grade instrumentation under ambient conditions during a series of cold-air pools and in a wind-tunnel environment. Under ambient conditions, this sensor correlates better with an FRM than other low-cost sensors in similar studies. \[\...\] these sensors are a promising tool for identifying relative increases or decreases in PM concentration, complementing sparsely distributed monitoring stations and for assessing and minimizing exposure to PM _(Kelly et al. 2017)_.

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