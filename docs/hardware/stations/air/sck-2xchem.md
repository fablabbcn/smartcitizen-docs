---
card: true
type: unit
name: SCK + 2xCHEM
field:
  - air
grade: intermediate
feature_img: https://live.staticflickr.com/65535/54318267807_78d5c57497_o.jpg
feature_img_description: "Smart Citizen 2x Chemical Air Quality Station"
excerpt: Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure 2 chemical composition metrics with electrochemical sensors.
---

# {{ name }}

**Grade**: _{{ grade }}_

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}
{%if feature_img_description %}***{{ feature_img_description }}***{.image-credit-banner-box}{%endif%}

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

![](https://live.staticflickr.com/65535/54319161481_b7006df36b_o.jpg)
***Smart Citizen 2x Chemical Air Quality Station***

### Dimensions and weight

| Version                   | Dimensions            | Weight |
| :-:                       | :-                    | :-     |
| Indoor                    | 16.6 x 12.5 x 5.5 cm  | 360g   |
| Outdoor (with umbrella)   | 23.1 x 14.7 x 8.5 cm  | 1080g  |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository]({{ extra.urls.enclosures.link }}).

{{ get_snippet_rel("docs/includes/stations.md") }}