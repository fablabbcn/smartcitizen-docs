Urban Sensor Board
==================

!!! info "We are updating"
    We are currently updating the documentation and many of the figures are from V2.0. We will move them shortly to a more updated version.

## What is it?

The Urban Sensor Board is a solution that contains a selection of low-cost sensors for environmental monitoring. Its main purpose is to serve as a tool for citizen science and awareness activities, and for that reason, metrics such as temperature, pressure, and humidity, as well as noise levels, ambient light, air quality indicators and PM sensors are included. The Urban Sensor Board has undergone several modifications throughout its development, and its **current version is V2.1**:

![](https://i.imgur.com/SGdx1Q2.jpg)

An iteration with a different set of sensors was developed as part of the [iScape Project](https://www.iscapeproject.eu/) and is shown in the image below:

![](https://i.imgur.com/Xk2Gkeo.jpg)

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-20" aria-label="Check the source code">Check the source code</a>

A major effort has been carried out on this design to improve the accuracy of the data provided. The sensors on the board include: Air Temperature, Relative Humidity, Noise Levels and Spectrum, Ambient Light and Barometric Pressure. The board also features a section especially focused on Air Quality including a Particle Matter Sensor, and, in version V2.1, an eCO2 and TVOC sensor. Previously, in version V2.0, a Carbon Monoxide and a Nitrogen Dioxide sensors was included, but due to the high power consumption and the need of important calibration efforts, these were removed. The sensor density of the board design offers more than ten different environmental metrics at a very low cost and differentiates the design from other existing solutions. The following sections describe in detail each of the sensors available.

!!! info "Board assembly"
    The Urban Sensor Board connect to the Data Board connector named **Sensor Board**

    ![](https://i.imgur.com/IqLEbIr.png)

**V2.1 Sensors**

| Measurement                                  | Units                                          | Sensor                |
|----------------------------------------------|------------------------------------------------|-----------------------|
| Air Temperature                              | ºC                                             | Sensirion SHT-31      |
| Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
| Noise Level and Spectrum                           | dBA, dBC, dBZ                                  | Invensense ICS-434342 |
| Ambient Light                                | Lux                                            | Rohm BH1721FVC        |
| Barometric pressure and AMSL                 | Pa and Meters                                  | NXP MPL3115A26        |
| eCO2 and TVOC                             | ppm/ppb | AMS CCS811         |
| Particulate Matter PM1/PM2.5/PM10 | µg/m3                                          | PMS 5003              |


**V2.0 Sensors**

| Measurement                                  | Units                                          | Sensor                |
|----------------------------------------------|------------------------------------------------|-----------------------|
| Air Temperature                              | ºC                                             | Sensirion SHT-31      |
| Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
| Noise Level and Spectrum                           | dBA, dBC, dBZ                                  | Invensense ICS-434342 |
| Ambient Light                                | Lux                                            | Rohm BH1721FVC        |
| Barometric pressure and AMSL                 | Pa and Meters                                  | NXP MPL3115A26        |
| Carbon Monoxide                              | ppm (Periodic Baseline Calibration Required) | SGX MICS-4514         |
| Nitrogen Dioxide                             | ppb (Periodic Baseline Calibration Required) | SGX MICS-4514         |
| Particulate Matter PM2.5 (external - power req) | µg/m3                                          | PMS 5003              |

## Metal Oxyde Sensors (all versions)

The metal oxyde sensors section is so extense, that we decided to dedicate a full section to them. Have a look at it [here](/Components/Urban Sensor Board/Metal Oxide Sensor)!

!!! info "Read more"
    More on the [MICS working principle and field validation](/Components/Urban Sensor Board/Metal Oxide Sensor/MICS/)

!!! info "What are normal values?"
    More on the [AMS CCS811, eCO2 and TVOC](/Components/Urban Sensor Board/Metal Oxide Sensor/CCS811/)

## Noise Level Sensor (V2.0 onwards)

The noise sensor is based on the INVENSENSE ICS-43432[^3] high-performance, low power, digital output, omnidirectional MEMS microphone with a bottom port and I2S interface. The sensors are similar to the one found on some high-end smartphones. It delivers the information directly in a digital format to the MCU where a custom library has been developed to provide noise data in dB scales A, C and Z. The raw FFT is also accessible to support characterization of specific noise frequencies. The sensor has been calibrated specifically for the project on an anechoic chamber using standard microphone calibration procedures.

The following characteristics have been considered for the sensor choice

* High 65 dBA SNR with a −26 dB FS Sensitivity

* Low Sensitivity Tolerance ±1 dB

* Wide Frequency Response from 50Hz to 20kHz

* High Acoustic Overload Point 116 dB SPL

* Low Power

!!! info
    Check the [Noise sensor implementation full documentation](Inside the Noise Sensor)


!!! tip "Sensor integration"
    ![](https://i.imgur.com/KHkyHEX.png)

## Relative Humidity and Air Temperature Sensor (V2.0 onwards)

Relative Humidity and Air Temperature Sensor are provided by a SENSIRION SHT31[^4] module.

!!! info "Sensor upgrade"
    Preliminary tests during the project shown a absolute calibration issues affecting the previously selected sensor, the SENSIRION SHT31. Those we updated the sensor to the newest SHT 31 with a PTFE layer for protection obtaining better results.

The following characteristics have been considered for the sensor choice

* Calibrated, linearized sensor signals in digital, I2C format straight to the MCU where data is provided in degrees Celsius and Relative Humidity.

* Wide measurement range with high resolution. The relative humidity range of 0-100% RH with a 0.03% resolution and a repeatability of 0.1%, together with a temperature operating range from -40 to +125°C with a temperature resolution of 0.01 ºC and a repeatability of 0.1%.

* No need for calibration and long-term stability.

* Low power consumption

* Commonly found in many commercial weather stations as the Davis Vantage Pro.

!!! tip "Sensor integration"
    ![](https://i.imgur.com/xoF233L.png)

## Ambient Light Sensor (V1.5 onwards)

The Ambient Light Sensors is based around the ROHM BH1721FVC[^5] which uses an LDR10 combined with an ADC and the corresponding circuit that allows communicating with the device with the I2C protocol.

The following characteristics have been considered for the sensor choice:

* No need of external ADC or linearization circuits uses the well-known I2C protocol

* Measures ambient light data in a wide range from 1lx to 65528 lx a repeatability of 15% and a resolution of 8 lx.

* Possibility to adjust by an I2C command the kind of light that it should measure (visible or infrared).

* Low power consumption.

* 50Hz/60Hz (electric network frequency) light rejection. Filtering the interference of most artificial light sources.

!!! tip "Sensor integration"
    ![](https://i.imgur.com/vYPNdcC.png)

## Barometric Pressure (V2.0 onwards)

The Barometric Pressure sensor is based around the NXP MPL3115A2[^6] is
a compact, piezoresistive, absolute pressure sensor with an I2C digital
interface.

The following characteristics have been considered for the sensor
choice:

* Wide operating range of 20 kPa to 110 kPa.

* Temperature compensated utilizing an on-chip temperature sensor.

* No need for an external ADC or linearization circuits. The pressure and temperature data is fed into an internal high-resolution ADC to provide fully compensated and digitized outputs for pressure in Pascals and temperature in °C using the well-known I2C protocol

* Barometric pressure is also processed by the MCU as height above mean sea level (AMSL) helping to determine the location of the device.

* Low power consumption.

!!! tip "Sensor integration"
    ![](https://i.imgur.com/5g64P7r.png)

## External PM Sensor (V2.0 onwards)

An external connector on the board supports the connection of a Plantower PMS 5003 or PMS 7003[^11]. The device is a digital particle concentration sensor that uses the Laser Scattering principle to obtain the number of suspended particles in the air. The sensor can be fully enabled or disabled in software to save energy when not in use.

The following characteristics have been considered for the sensor
choice:

* Provides PM 2.5 and PM 10 measurements in ug/m³

* Minimal distinguishable particle diameter of 0.3 um

* No need for external ADC or linearization circuits. The sensor includes an internal MCU capable of dealing with all the light emitting and sensing processing. All the communication is done using the I2C protocol. A dedicated driver has been designed for this.

* Ultra Low Cost when compared to other commercial solutions with similar performance

* Low Power

!!! tip "Sensor integration"
    ![](https://i.imgur.com/vyLMF07.png)

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-20/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-20" aria-label="Check the source code">Check the source code</a>


[^2]: SGX MICS 4514 Technical Datasheet

    [https://sgx.cdistore.com/datasheets/sgx/0278\_Datasheet%20MiCS-4514%20rev%2017.pdf](https://sgx.cdistore.com/datasheets/sgx/0278_Datasheet%20MiCS-4514%20rev%2017.pdf)

[^3]: INVENSENSE 43432 Technical Datasheet

    [https://www.invensense.com/wp-content/uploads/2015/02/ICS-43432-data-sheet-v1.3.pdf](https://www.invensense.com/wp-content/uploads/2015/02/ICS-43432-data-sheet-v1.3.pdf)

[^4]: SENSIRION SHT31 Technical Datasheet

    [https://www.sensirion.com/fileadmin/user\_upload/customers/sensirion/Dokumente/2\_Humidity\_Sensors/](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/)

[^5]: ROHM BH1730 Technical Datasheet

    [http://rohmfs.rohm.com/en/products/databook/datasheet/ic/sensor/light/bh1721fvc-e.pdf](http://rohmfs.rohm.com/en/products/databook/datasheet/ic/sensor/light/bh1721fvc-e.pdf)

[^6]: NXP MPL3115A2 Technical Datasheet

    [http://www.nxp.com/docs/en/data-sheet/MPL3115A2.pdf](http://www.nxp.com/docs/en/data-sheet/MPL3115A2.pdf)

[^7]: MAXIM 30105 Technical Datasheet

    [https://datasheets.maximintegrated.com/en/ds/MAX30105.pdf](https://datasheets.maximintegrated.com/en/ds/MAX30105.pdf)

[^8]: ALPHASENSE NO2-B43F Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO~2~B43F.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO2B43F.pdf)

[^9]: ALPHASENSE OX-B431 Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/OX-B431.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/OX-B431.pdf)

[^10]: ALPHASENSE CO-B4 B Technical Datasheet

    [http://www.alphasense.com/WEB1213/wp-content/uploads/2015/04/COB41.pdf](http://www.alphasense.com/WEB1213/wp-content/uploads/2015/04/COB41.pdf)

[^11]: PLANTOWER PMS5003 Technical Datasheet [https://aqicn.org/air/view/sensor/spec/pms5003.pdf](https://aqicn.org/air/view/sensor/spec/pms5003.pdf)