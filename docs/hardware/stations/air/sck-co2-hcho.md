---
card: true
type: unit
name: SCK + CO2 + HCHO
field:
  - air
grade: intermediate
feature_img: https://live.staticflickr.com/65535/54323282033_4e809d48ee_o.jpg
feature_img_description: "Smart Citizen CO2+HCHO Air Quality Station"
excerpt: Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 and Formaldehyde!
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
    | PM1, PM2.5, PM4.0 and PM10            | µg/m3 | Sensirion SEN5X       |
    | CO2                                   | ppm   | Sensirion SCD30       |
    | HCHO                                  | ppb   | Sensirion SFA30       |
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
    | CO2                                   | ppm   | Sensirion SCD30       |
    | HCHO                                  | ppb   | Sensirion SFA30       |

## Technical specifications


![](https://live.staticflickr.com/65535/54323454845_af966626b4_o.jpg)
***Smart Citizen CO2+HCHO Air Quality Station***

### Dimensions and weight

| Version                   | Dimensions          | Weight |
| :-:                       | :-                  | :-     |
| Indoor                    | 19 x 12.3 x 5.5 cm  | 400g   |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository]({{ extra.urls.enclosures.link }}).

{{ get_snippet_rel("docs/includes/stations.md") }}

{{ get_snippet_rel("docs/includes/aq-stations.md") }}