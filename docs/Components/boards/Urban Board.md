Urban Sensor Board
==================

## What is it?

The Urban Sensor Board is a solution that contains a selection of low-cost sensors for environmental monitoring. Its main purpose is to serve as a tool for citizen science and awareness activities, and for that reason, metrics such as temperature, pressure, and humidity, as well as noise levels, ambient light, air quality indicators and PM sensors are included. The Urban Sensor Board has undergone several modifications throughout its development, and its **current version is V2.1**:

![](/assets/images/SGdx1Q2.jpg)

An iteration with a different set of sensors was developed as part of the [iScape Project](https://www.iscapeproject.eu/) and is shown in the image below:

![](/assets/images/Xk2Gkeo.jpg)

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-21" aria-label="Check the source code">Check the source code</a>

A major effort has been carried out on this design to improve the accuracy of the data provided. The sensors on the board include: Air Temperature, Relative Humidity, Noise Levels and Spectrum, Ambient Light and Barometric Pressure. The board also features a section especially focused on Air Quality including a Particle Matter Sensor, and, in version V2.1, an eCO2 and TVOC sensor. Previously, in version V2.0, a Carbon Monoxide and a Nitrogen Dioxide sensors was included, but due to the high power consumption and the need of important calibration efforts, these were removed. The sensor density of the board design offers more than ten different environmental metrics at a very low cost and differentiates the design from other existing solutions. The following sections describe in detail each of the sensors available.

!!! info "Board assembly"
    The Urban Sensor Board connect to the Data Board connector named **Sensor Board**

    ![](/assets/images/IqLEbIr.png)

**V2.1 Sensors**

| Measurement                                  | Units                                          | Sensor                |
|----------------------------------------------|------------------------------------------------|-----------------------|
| Air Temperature                              | ºC                                             | Sensirion SHT-31      |
| Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
| Noise Level and Spectrum                           | dBA, dBC, dBZ                                  | Invensense ICS-43432 |
| Ambient Light                                | Lux                                            | Rohm BH1721FVC        |
| Barometric pressure and AMSL                 | Pa and Meters                                  | NXP MPL3115A2        |
| eCO2 and TVOC                             | ppm/ppb | AMS CCS811         |
| Particulate Matter PM1/PM2.5/PM10 | µg/m3                                          | PMS 5003              |


**V2.0 Sensors**

| Measurement                                  | Units                                          | Sensor                |
|----------------------------------------------|------------------------------------------------|-----------------------|
| Air Temperature                              | ºC                                             | Sensirion SHT-31      |
| Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
| Noise Level and Spectrum                           | dBA, dBC, dBZ                                  | Invensense ICS-43432 |
| Ambient Light                                | Lux                                            | Rohm BH1721FVC        |
| Barometric pressure and AMSL                 | Pa and Meters                                  | NXP MPL3115A2        |
| Carbon Monoxide                              | ppm (Periodic Baseline Calibration Required) | SGX MICS-4514         |
| Nitrogen Dioxide                             | ppb (Periodic Baseline Calibration Required) | SGX MICS-4514         |
| Particulate Matter PM2.5 (external - power req) | µg/m3                                          | PMS 5003              |

!!! info "Sensor performance"
    Make sure you visit the [sensor performance page](/Components/sensors/performance/) for further information about the sensors.