---
internal:
  writing: false
  proofread: false
  links: false
  images: false
---

# Urban Board

The Urban Board is a solution that contains a selection of low-cost sensors for environmental monitoring. The actual [measurements](#measurements) it takes depend on the version, but overall, it is capable of measurements such as:

- Temperature and Relative Humidity
- Barometric Pressure
- Noise Level and Frequency Spectrum
- Light (including UV-index after the 2.2 version)
- Air Quality Indicators (depending on the version)
- PM sensor connector

The Urban Board has undergone several modifications throughout its development, and its current version is the **V2.3**. Below you can see all versions:

=== "SCK2.3"
    <img style="max-height: 450px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281726349_e3353f828b_o.jpg" alt="SCK2.3 Urban Board"/>
=== "SCK2.2"
    <img style="max-height: 450px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281726359_471ec852eb_o.jpg" alt="SCK2.2 Urban Board"/>
=== "SCK2.1"
    <img style="max-height: 450px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281911420_32e26bdd40_o.jpg" alt="SCK2.1 Urban Board"/>

<a class="github-button" data-size="large" href="{{ config.extra.urls.ghhardware.link }}" aria-label="Check the design files">Check the design files</a>

## Assembly

The Urban Board connects to the [Data Board](/hardware/boards/data-board/) with the connector labeled `Sensor Board`:

![](/assets/images/sck-connection.png)

### PM sensor

=== "SCK2.3/2.2"
    ![](/assets/urban-board-sen5x.png)
=== "SCK2.1"
    TODO

## Measurements

=== "SCK 2.3"
    | Measurement                                  | Units                                          | Sensor                |
    |----------------------------------------------|------------------------------------------------|-----------------------|
    | Air temperature                              | ºC                                             | Sensirion SHT-31      |
    | Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
    | Noise level                                  | dBA, dBC or dBZ                                | Invensense ICS-434342 |
    | Ambient light                                | lux                                            | Rohm BH1721FVC        |
    | Barometric pressure                          | kPa                                            | NXP MPL3115A26S       |
    | UV-A, B, C                                   | uW/cm2                                         | AMS AS7311            |
    | PM1, PM2.5, PM4 and PM10                     | µg/m3                                          | Sensirion SEN5X       |
    | NOx Index, VOx Index (Optional)              | -                                              | Sensirion SEN54, 55   |
=== "SCK 2.2"
    | Measurement                                  | Units                                          | Sensor                |
    |----------------------------------------------|------------------------------------------------|-----------------------|
    | Air temperature                              | ºC                                             | Sensirion SHT-31      |
    | Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
    | Noise level                                  | dBA, dBC or dBZ                                | Invensense ICS-434342 |
    | Ambient light                                | lux                                            | Rohm BH1721FVC        |
    | Barometric pressure                          | kPa                                            | ST LPS33K             |
    | UV-A, B, C                                   | uW/cm2                                         | AMS AS7311            |
    | PM1, PM2.5, PM4 and PM10                     | µg/m3                                          | Sensirion SEN5X       |
    | NOx Index, VOx Index (Optional)              | -                                              | Sensirion SEN54, 55   |
=== "SCK 2.1"
    | Measurement                                  | Units                                          | Sensor                |
    |----------------------------------------------|------------------------------------------------|-----------------------|
    | Air Temperature                              | ºC                                             | Sensirion SHT-31      |
    | Relative Humidity                            | % REL                                          | Sensirion SHT-31      |
    | Noise Level and Spectrum                     | dBA, dBC or dBZ                                | Invensense ICS-43432  |
    | Ambient Light                                | Lux                                            | Rohm BH1721FVC        |
    | Barometric pressure and AMSL                 | kPa and Meters                                 | NXP MPL3115A2         |
    | eCO2 and TVOC                                | ppm/ppb                                        | AMS CCS811            |
    | PM1, PM2.5 and PM10                          | µg/m3                                          | Plantower PMS5003     |

## Design files

You can find all the design files for the different versions of the Urban Board in the [hardware repository]({{ extra.urls.ghhardware.link }}).

!!!info "Previous versions"
    Previous versions of the SCK, are in their respective repositories:

    - Smart Citizen Kit 2.0: https://github.com/fablabbcn/smartcitizen-kit-20
    - Smart Citizen Kit 1.5: https://github.com/fablabbcn/smartcitizen-kit-15