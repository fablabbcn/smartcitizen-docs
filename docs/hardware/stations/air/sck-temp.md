---
card: true
type: unit
name: SCK + T / RH
field:
  - air
grade: basic
feature_img: https://live.staticflickr.com/65535/54325253435_f9b2859671_o.jpg
feature_img_description: "Smart Citizen Temperature/RH Air Quality Station"
excerpt: Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor!
---

# {{ name }}

**Grade**: _{{ grade }}_

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}
{%if feature_img_description %}***{{ feature_img_description }}***{.image-credit-banner-box}{%endif%}

## Measurements

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
    | Particulate Matter PM1, PM2.5, PM10   | µg/m3 | Plantower PMS 5003    |
    | External air temperature              | ºC    | DF Robot Module Sensirion SHT-31 Weatherproof    |
    | External relative Humidity            | % REL | DF Robot Module Sensirion SHT-31 Weatherproof    |

=== "SCK2.3 based"
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

![](https://live.staticflickr.com/65535/54324846296_fc5f1bf887_o.jpg)
***Smart Citizen Temperature/RH Air Quality Station***

### Dimensions and weight

| Version                   | Dimensions            | Weight |
| :-:                       | :-                    | :-     |
| Indoor                    | 11.7 x 11.5 x 5.5 cm  | 350g   |
| Outdoor (with umbrella)   | 18.2 x 14.7 x 8.5 cm  | 1010g  |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository]({{ extra.urls.enclosures.link }}).

{{ get_snippet_rel("docs/includes/stations.md") }}
