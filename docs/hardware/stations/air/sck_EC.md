---
card: true
type: unit
name: SCK + 1xCHEM
field:
  - air
versions:
    hardware: 2.x
    firmware:  sck22_air
grade: intermediate
feature_img: https://live.staticflickr.com/65535/53909712132_b46cae1a7e_k.jpg
excerpt: Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor!
---

# {{ name }}

**Grade**: _{{ grade }}_

![]({{ feature_img }})

## Measurements

SCK2.1 Based

| Measurement                           | Units | Sensor                |
|:-                                     |:-:    |:-:                    |
| Air temperature                       | ºC    | Sensirion SHT-31      |
| Relative Humidity                     | % REL | Sensirion SHT-31      |
| Noise level                           | dBA   | Invensense ICS-434342 |
| Ambient light                         | lux   | Rohm BH1721FVC        |
| Barometric pressure                   | kPa   | NXP MPL3115A26        |
| Equivalent Carbon Dioxide             | ppm   | AMS CCS811            |
| Volatile Organic Compounds            | ppb   | AMS CCS811            |
| Particulate Matter PM1, PM2.5, PM10   | µg/m3 | Plantower PMS 5003    |


## Technical specifications

### Power

Currently, the Smart Citizen Air Quality Stations have only been tested with an [external power supply](/hardware/power/Power Supply) (230VAC to 5VDC), with a small battery for backup during power brownouts. Due to the number of sensors, and depending on the configuration the solution is normally not meant for long term deployment with just battery power. For detailed specifications of the power supply, visit the [power supply section](/hardware/power/Power Supply/).

| Power        |                                                                  |
| :-:          | :-                                                               |
| DC Voltage   | 5V                                                               |
| DC Current   | 2A _recommended_                                                 |
| AC Voltage   | 230V  _into the [Power Supply](/hardware/power/Power Supply/)_   |
| AC Current   | <0.16A _into the [Power Supply](/hardware/power/Power Supply/)_  |

!!! warning "Battery or solar operation?"
    The Station currently supports battery operation only for short periods of time (<2d days). Depending on the location, [solar power](/hardware/power/Solar Panel/) might be available, but we do not recommend it unless you are willing to _experiment_.

### Dimensions and weight

<!-- TODO - Add table with size -->

| Version       | Dimensions | Weight |
| :-:           | :-         | :-     |
| Indoor         | | |
| Outdoor (with umbrella)         | | |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository]({{ extra.urls.enclosures.link }}).

![TODO](TODO)

### Connectivity

Similar to the [Smart Citizen Kit](/hardware/Smart Citizen Kit/) if you want to have your data online, the Smart Citizen Air Quality Station requires a Wi-Fi connection to report data to the [platform](/Data/Sensor Platform). If not, the unit can also store data locally on its onboard sd-card. Read more about the [operation modes](/hardware/Smart%20Citizen%20Kit/#operation-modes) and the [supported networks](/_FAQ/#what-networks-does-it-support).

## Enclosure

## Guides

- CO2 sensor calibration