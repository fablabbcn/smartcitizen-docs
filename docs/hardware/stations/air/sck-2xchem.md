---
card: true
type: unit
name: SCK + 2xCHEM
field:
  - air
grade: intermediate
feature_img: /assets/images/station-2xchem.jpg
excerpt: Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure 2 chemical composition metrics with electrochemical sensors.
---

# {{ name }}

**Grade**: _{{ grade }}_

![]({{ feature_img }})

## Measurements

=== "SCK2.3 based"
    | Measurement                           | Units | Sensor                |
    |:-                                     |:-:    |:-:                    |
    | Air temperature                       | ºC    | Sensirion SHT-31      |
    | Relative Humidity                     | % REL | Sensirion SHT-31      |
    | Noise level                           | dBA   | Invensense ICS-434342 |
    | Ambient light                         | lux   | Rohm BH1721FVC        |
    | Barometric pressure                   | kPa   | NXP MPL3115A26        |
    | Equivalent Carbon Dioxide             | ppm   | AMS CCS811            |
    | Volatile Organic Compounds            | ppb   | AMS CCS811            |
    | Particulate Matter PM1, PM2.5, PM4.0 PM10   | µg/m3 | Sensirion SEN5X    |
    | 2 Chemical metrics (NO2, CO, NO, O3, SO2 or H2S) | ppb/ppm | Alphasense A-series    |
=== "SCK2.1 based (deprecated)"
    | Measurement                           | Units | Sensor                |
    |:-                                     |:-:    |:-:                    |
    | Air temperature                       | ºC    | Sensirion SHT-31      |
    | Relative Humidity                     | % REL | Sensirion SHT-31      |
    | Noise level                           | dBA   | Invensense ICS-434342 |
    | Ambient light                         | lux   | Rohm BH1721FVC        |
    | Barometric pressure                   | kPa   | NXP MPL3115A26        |
    | Equivalent Carbon Dioxide             | ppm   | AMS CCS811            |
    | Volatile Organic Compounds            | ppb   | AMS CCS811            |
    | PM1, PM2.5 and PM10                   | µg/m3 | Plantower PMS5003     |
    | 2 Chemical metrics (NO2, CO, NO, O3, SO2 or H2S) | ppb/ppm | Alphasense A-series    |

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