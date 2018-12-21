Urban Sensor Board
==================

The Urban Sensor Board contains a selection of sensors for the measuring the urban outdoor environment. The sensor selection is based on the recommendations provided by ISCAPE WP1 among the experience acquired from previous Smart Smart Citizen Kit generations.

![](https://i.imgur.com/Xk2Gkeo.jpg)

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-20" aria-label="Check the source code">Check the source code</a>

A major effort has been carried out on this design to improve the accuracy of the data provided. The sensors on the board include: Air Temperature, Relative Humidity, Noise Level, Ambient Light and Barometric Pressure. The board also features a section especially focused on Air Quality including a Particles Matter, a Carbon Monoxide and a Nitrogen Dioxide detectors. The sensor density of the board design offers more than ten different environmental metrics at a cost below 50€ and differentiates the design from other existing solutions. The following sections describe in detail each of the sensors available.

!!! info "Board assembly"
    The Urban Sensor Board connect to the Data Board connector named **Sensor Board**

    ![](https://i.imgur.com/IqLEbIr.png)

| Measurement                                  | Units                                          | Sensor                |
|----------------------------------------------|------------------------------------------------|-----------------------|
| Air Temperature                              | ºC                                             | Sensirion SHT-31      |
| Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
| Noise Level                                  | dBA, dBC, dBZ                                  | Invensense ICS-434342 |
| Ambient Light                                | Lux                                            | Rohm BH1721FVC        |
| Barometric pressure and AMSL                 | Pa and Meters                                  | NXP MPL3115A26        |
| Carbon Monoxide                              | ppm (Periodic Baseline Calibration Required) | SGX MICS-4514         |
| Nitrogen Dioxide                             | ppb (Periodic Baseline Calibration Required) | SGX MICS-4514         |
| Particulate Matter PM2.5 (external - power req) | µg/m3                                          | PMS 5003              |


## Metal Oxide NO~2~ and CO Sensor

The SGX Sensortech (formerly e2v) MICS 4514 [^2]is a dual, robust MEMS sensor for the detection of pollution from automobile exhausts. It integrates on a single SMD package the more well-known SGX MICS 5525 for Carbon Monoxide detection and the SGX MICS 2710 for Nitrogen Dioxide detection. The sensor includes two sensor chips with independent heaters and sensitive layers. One sensor chip detects Oxidizing gases (OX) primarily NO~2~ in a 0.05-10ppm, and the other sensor detects reducing gases (RED) primarily NO~2~ in a 1-1000ppm.

The following characteristics have been considered for the sensor choice:

* Combines in the same package both the CO and NO~2~ sensors in a low-cost unit \<15€

* Low heating current, especially important since the sensor can be battery-powered.

* Wide range gas concentration detection.

* Extensive operational temperature range.

* Robust to vibrations and shocks.

The MICS-4514 Carbon Monoxide detection performance was tested by _(Rai et al. 2017; Spinelle et al. 2017)_ under field conditions. They reported good agreement (R2 = 0.76--0.78) between sensor response and reference measurements when it was calibrated by using simple or multiple linear regression models _(Rai et al. 2017)_

The sensor integration on the Urban Sensor Board features an analog front-end different than those used by other products using the same sensor to achieve more precise and stable readings. That includes a dynamic gaining circuit and an adjustable heating system designed from the ground up for this application.

However, the baseline resistance can vary a lot from sensor to sensor, and according to the measuring conditions, which is why the manufacturer recommends monitoring the sensitivity periodically. That mean re-calibration of the device after a few months might be required because the pairs of metal-oxide on the surface of the captor change their physical properties when exposed to the detectable gases. That is the primary reason the Smart Citizen Station include an extra Gas Sensor Board featuring three pre calibrated EC gas sensors to provide more precise and meaningful air quality data.

!!! tip "Sensor integration"
    **Main Sensor Interface**

    ![](https://i.imgur.com/iH5WUQ6.png)

    **Filters**

    ![](https://i.imgur.com/MU7zFMC.png)

    **Analog to Digital Converter**

    ![](https://i.imgur.com/BQONoBI.png)

    **Digital Potentiometer for heater control**

    ![](https://i.imgur.com/k1db1nl.png)

    !!! info "Heater design"
        Check the [MICS implementation document](MICS Driver Implementation) to learn more about the brand new heating stage.

!!! tip "Field validation"
    The NO~2~ data the sensor post processed with the [Sensor Analysis Framework](Sensor Analysis Framework) compared with the Arpae Emilia-Romagna referenced instrumentation.

    ![](https://i.imgur.com/982qA89.png)

    !!! info "Read more"
        More on the [MICS working principle and field validation](Metal Oxide Sensors)

## Noise Level Sensor

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

## Relative Humidity and Air Temperature Sensor

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

## Ambient Light Sensor

The Ambient Light Sensors is based around the ROHM BH1721FVC[^5] which uses an LDR10 combined with an ADC and the corresponding circuit that allows communicating with the device with the I2C protocol.

The following characteristics have been considered for the sensor choice:

* No need of external ADC or linearization circuits uses the well-known I2C protocol

* Measures ambient light data in a wide range from 1lx to 65528 lx a repeatability of 15% and a resolution of 8 lx.

* Possibility to adjust by an I2C command the kind of light that it should measure (visible or infrared). The infrared channel is not used in the current version, but it could be considered in future versions.

* Low power consumption.

* 50Hz/60Hz (electric network frequency) light rejection. Filtering the interference of most artificial light sources.

!!! tip "Sensor integration"
    ![](https://i.imgur.com/vYPNdcC.png)

## Barometric Pressure

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

## Dust Particles Sensor

!!! warning
    The following sensor might be replaced in future iterations as it gets replaced by the **External PM Sensor connector** supporting a Plantowe PMS5003 or PMS7003

The MAXIM MAX30105[^7] is an integrated particle-sensing module. Is a high Sensitivity Optical Reflective Solution for detection of wide a variety of particle sizes. This sensor is aimed at measuring relative air dust levels. However, an algorithm is being developed to support PM 2.5 or PM 10 measurements. At the time the document is being written no data on the sensor lab tests can be provided.

The following characteristics have been considered for the sensor
choice:

* No need for external ADC or linearization circuits. The sensor includes an internal MCU capable of dealing with all the light emitting and sensing processing. All the communication is done using the I2C protocol.

* Robust Motion Artifact Resilience and -40°C to +85°C Operating Temperature

* Capable of Operating at High Ambient Levels with Excellent Ambient Rejection Capability

* Includes a temperature sensor for calibrating the temperature dependence of the particle sensing subsystem.

* Low power consumption

!!! tip "Sensor integration"
    ![](https://i.imgur.com/E4FhioM.png)

## External PM Sensor

An external connector on the board supports the connection of a Plantower PMS 5003 or PMS 7003[^11]. The device is a digital particle concentration sensor that uses the Laser Scattering principle to obtain the number of suspended particles in the air. The sensor can be fully enable or disable in software to save energy when not in use.

The following characteristics have been considered for the sensor
choice:

* Provides PM 2.5 and PM 10 measurements in ug/m³

* Minimal distinguishable particle diameter of 0.3 am

* No need for external ADC or linearization circuits. The sensor includes an internal MCU capable of dealing with all the light emitting and sensing processing. All the communication is done using the I2C protocol. A dedicated driver has been designed for this.

* Ultra Low Cost when compared to other commercial solutions with similar performance

* Low Power

The selection is based on the academic references selected above. For a complete Low-Cost Sensors Evaluation see ISCAPE D1.5 Summary of air quality sensors and recommendations for application and the subsequent publication _(Rai et al. 2017)_.

Compliance with the NAAQS (US National Ambient Air Quality Standards) is based on 24-h PM mass concentrations \[\...\] Both of the FEM instruments correlate with the 24-h PM2.5 mass measurements with an R2 \> 0.99. The PMS PM2.5 concentrations are also well correlated with the 24-h mass average concentration (R2 \> 0.88), which is slightly better than the GRIMM research-grade instrument (R2 1⁄4 0.7.). South Coast Air Quality Management District (SCAQMD) recently published preliminary comparisons of the PM2.5 measurements from three PMS 1003s and two FEMs, with high correlations (R2 \> 0.9) over a 2-month period. This study demonstrated that the PMS 1003/3003 correlates well with FRMs, FEMs, and research-grade instrumentation under ambient conditions during a series of cold-air pools and in a wind-tunnel environment. Under ambient conditions, this sensor correlates better with an FRM than other low-cost sensors in similar studies. \[\...\] these sensors are a promising tool for identifying relative increases or decreases in PM concentration, complementing sparsely distributed monitoring stations and for assessing and minimizing exposure to PM _(Kelly et al. 2017)_.

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