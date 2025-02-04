---
card: true
type: unit
name: SCK + T / RH
field:
  - air
grade: basic
feature_img: https://live.staticflickr.com/65535/53909712132_b46cae1a7e_k.jpg
excerpt: Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor!
---

# {{ name }}

**Grade**: _{{ grade }}_

![]({{ feature_img }})

## Measurements

=="SCK2.1 based (deprecated)"
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
    | External air temperature              | ºC    | DF Robot Module Sensirion SHT-31 Weatherproof    |
    | External relative Humidity            | % REL | DF Robot Module Sensirion SHT-31 Weatherproof    |
=="SCK2.3 based"
    | Measurement                           | Units | Sensor                |
    |:-                                     |:-:    |:-:                    |
    | Air temperature                       | ºC    | Sensirion SHT-31      |
    | Relative Humidity                     | % REL | Sensirion SHT-31      |
    | Noise level                           | dBA   | Invensense ICS-434342 |
    | Ambient light                         | lux   | Rohm BH1721FVC        |
    | Barometric pressure                   | kPa   | NXP MPL3115A26        |
    | Particulate Matter PM1, PM2.5, PM4.0 PM10   | µg/m3 | Sensirion SEN5X    |
    | External air temperature              | ºC    | DF Robot Module Sensirion SHT-31 Weatherproof    |
    | External relative Humidity            | % REL | DF Robot Module Sensirion SHT-31 Weatherproof    |

## Technical specifications

### Dimensions and weight

| Version                   | Dimensions | Weight |
| :-:                       | :-         | :-     |
| Indoor                    |            |        |
| Outdoor (with umbrella)   |            |        |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository]({{ extra.urls.enclosures.link }}).

{{ get_snippet_rel("docs/includes/stations.md") }}

## Guides

{{ insert_guides() }}