<!-- Source: https://docs.smartcitizen.me/hardware/stations/air/sck-co2/ -->

# SCK + CO2

**Grade**: _intermediate_

Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor!

![](https://docs.smartcitizen.me/assets/images/sck-co2-feature.jpg){.banner-box}
***Smart Citizen CO2 Air Quality Station***{.image-credit-banner-box}

## Measurements

=== "SCK2.3 based"
    | Measurement                           | Units | Sensor                |
    |:-                                     |:-:    |:-:                    |
    | Air temperature                       | ºC    | Sensirion SHT-31      |
    | Relative Humidity                     | % REL | Sensirion SHT-31      |
    | Noise level                           | dBA   | Invensense ICS-43432 |
    | Ambient light                         | lux   | Rohm BH1730FVC        |
    | Barometric pressure                   | kPa   | NXP MPL3115A2        |
    | Equivalent Carbon Dioxide             | ppm   | AMS CCS811            |
    | Volatile Organic Compounds            | ppb   | AMS CCS811            |
    | Particulate Matter PM1, PM2.5, PM4.0 PM10   | µg/m3 | Sensirion SEN5X    |
    | CO2                                   | ppm | Sensirion SCD30     |
=== "SCK2.1 based (deprecated)"
    | Measurement                           | Units | Sensor                |
    |:-                                     |:-:    |:-:                    |
    | Air temperature                       | ºC    | Sensirion SHT-31      |
    | Relative Humidity                     | % REL | Sensirion SHT-31      |
    | Noise level                           | dBA   | Invensense ICS-43432 |
    | Ambient light                         | lux   | Rohm BH1730FVC        |
    | Barometric pressure                   | kPa   | NXP MPL3115A2        |
    | Equivalent Carbon Dioxide             | ppm   | AMS CCS811            |
    | Volatile Organic Compounds            | ppb   | AMS CCS811            |
    | PM1, PM2.5 and PM10                   | µg/m3 | Plantower PMS5003     |
    | CO2                                   | ppm   | Sensirion SCD30       |

## Technical specifications

![](https://docs.smartcitizen.me/assets/images/sck-co2.jpg)
***Smart Citizen CO2 Air Quality Station***


### Dimensions and weight

| Version                   | Dimensions            | Weight |
| :-:                       | :-                    | :-     |
| Indoor                    | 16.6 x 12.5 x 5.5 cm  | 330g   |
| Outdoor (with umbrella)   | 23.1 x 14.7 x 8.5 cm  | 1050g  |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository](https://enclosures.smartcitizen.me).


### Power

Currently, the Smart Citizen Air Quality Stations have only been tested with an [external power supply](https://docs.smartcitizen.me/hardware/addons/power-supply.md) (230VAC to 5VDC), with a small battery for backup during power brownouts. Due to the number of sensors, and depending on the configuration the solution is normally not meant for long term deployment with just battery power. For detailed specifications of the power supply, visit the [power supply section](https://docs.smartcitizen.me/hardware/addons/power-supply.md).

| Power        |                                                                  |
| :-:          | :-                                                               |
| DC Voltage   | 5V                                                               |
| DC Current   | 2A _recommended_                                                 |
| AC Voltage   | 230V  _into the [Power Supply](https://docs.smartcitizen.me/hardware/addons/power-supply.md)_   |
| AC Current   | <0.16A _into the [Power Supply](https://docs.smartcitizen.me/hardware/addons/power-supply.md)_  |

!!! warning "Battery or solar operation?"
    The Station currently supports battery operation only for short periods of time (<2d days). Depending on the location, [solar power](https://docs.smartcitizen.me/hardware/addons/solar-panel.md) might be available, but we do not recommend it unless you are willing to _experiment_.

### Connectivity

Similar to the [Smart Citizen Kit](https://docs.smartcitizen.me/hardware/kit.md) if you want to have your data online, the Smart Citizen Air Quality Station requires a Wi-Fi connection to report data to the [platform](https://docs.smartcitizen.me/data/data-platform.md). If not, the unit can also store data locally on its onboard sd-card. Read more about the [operation modes](https://docs.smartcitizen.me/hardware/kit.md#operation-modes) and the [supported networks](https://docs.smartcitizen.me/_FAQ.md#what-networks-does-it-support).


## Hardware design

!!! warning "A note about versions"
    Some of the diagrams below are from older designs, but you they haven't changed much! Hopefully they are still understandable!

The Stations should come assembled and ready to use. They consist of various parts:

- [Enclosure and mounting system](#enclosure-and-mounting-system): for protection and support.
- Sensors module: contains the electronics and sensors, it can be accessed without having to uninstall the rain cover.
- [Power supply](#power): is separated from the main module, so that intervention in the sensors' area can be performed safely with a tangible desconection of the mains power.

![](https://docs.smartcitizen.me/assets/images/station-small-exploded.png)

### Enclosure and mounting system

The enclosure holds the sensors in place and protects them against weather. A rain and sun radiation **cover** for additional protection can be used, which carries out the structural support of the station and protects the unit against rain, wind or heat.

![](https://docs.smartcitizen.me/assets/images/station-v3-mounting.png)

!!! tip "Flexible attachment"
    This mounting is thought to work on a lampost, fence or wall. We recommend a somewhat flexible join (i.e. zip-ties) in case of windy locations.

The enclosure can be installed using the _mounting holes_ seen below. There is sufficient space to pass zip ties. If you want to use drills, we recommend at least 6mm screws (or 8mm) and to dissasemble the plastic cover from the sandwich pannel for safer installation.

## Deployment tips

Below are some general guidelines for the installation of the device:

- Avoid areas with moist accumulation when possible
- Avoid temperature and humidity transients
- Avoid covering the sensors in front of the sensors, specially the PM sensor
- Avoid covering the microphone and particles to go in the microphone port
- Avoid direct flow towards the sensors. If exposed under flow conditions, have the flow go parallel to the sensors' surface
- Despite the umbrella cover, sun radiation and transients are better to be avoided
- A good height for installing the sensors is somewhere between 2-3m, but it all depends on the case study and available support structures.

### Sensor placement

!!! danger ""
    The device should never be placed horizontally (wide side flat on a surface). This placement would cover completely the sensor inlets, or leave them exposed to dust accumulation. Likewise, the sensors, do not work properly on this configuration.

For indoor placement, check the placement below:

![](https://docs.smartcitizen.me/assets/images/sensor-placement-horizontal.png)

![](https://docs.smartcitizen.me/assets/images/sensor-placement-vertical.png)

For outdoow placement, if you are using the umbrella, check the image below. **Sensors should be facing down**:

![](https://docs.smartcitizen.me/assets/images/mini-station-field.jpg)

## Handling calibration data

Some components of the Station have individual calibrations such as the Alphasense Electrochemical Sensors. For this reason, it's necessary to store the physical ID (hardware ID) of the Station alonside to the virtual device in the Smart Citizen Platform. The harwdware ID should normally be in a sticker to the enclosure **both inside and outside** and looks like this:

```
SCAS2100XX
```

This number is important to relate to the actual calibration values of the sensors, stored in the [data repository](https://github.com/fablabbcn/smartcitizen-data/tree/master/hardware). In order to postprocess the data and calculate pollutants, make sure that the `Hardware ID` is safely stored in the platform's device, by posting this data to `postprocessing_info` field of the device. You can follow [these instructions](https://docs.smartcitizen.me/guides/data/handling-calibration-data.md) to store the `postprocessing_info` of your device.

All the data is sent in raw to the Smart Citizen Platform and it's then processed outside of the sensors themselves. Both raw, and processed data are kept on the platform and can be accessed at any time. Data can be published to other APIs or to [Zenodo](https://zenodo.org) as well, in case of research projects that seek contribution to Open Science Datasets.

!!! tip "More on the processing of the data"
    Check [this guide](https://docs.smartcitizen.me/guides/data/custom-data-processing.md) to learn more about how to postprocess the data of the sensors your own way.