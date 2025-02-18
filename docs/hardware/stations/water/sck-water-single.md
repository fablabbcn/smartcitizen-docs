---
card: true
type: unit
name: One-Sensor Water Station
field:
  - water
grade: intermediate
feature_img: https://live.staticflickr.com/65535/54319269815_af3d4149b4_o.jpg
feature_img_description: "One-Sensor pH Water Station"
excerpt: "The One-Sensor Water Station is meant to measure one physico-chemical parameter at a time. Choose from pH, Temperature, Dissolved Oxygen, Conductivity or ORP."
---

# {{ name }}

**Grade**: _{{ grade }}_

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}
{%if feature_img_description %}***{{ feature_img_description }}***{.image-credit-banner-box}{%endif%}

## Measurements

Measurements on the water stations can be 1 of the ones below:

| Measurement      | Units    | Sensor                        |
| :-:              | :-:      | :-:                           |
| Temperature      | ºC       | Atlas PT-1000, PT-100 probes  |
| pH               | -        | Atlas pH probes               |
| Conductivity     | uS/cm    | Atlas Conductivity probes     |
| Dissolved Oxygen | mg/l     | Atlas DO probes               |
| ORP              | mV       | Atlas ORP probes              |

In the image at the top of the page you can see an example of a One-Sensor Water Station that measures pH, and below you can see another that measures temperature.

![](https://live.staticflickr.com/65535/54319083519_b7f37ebb01_o.jpg){.black-box}
***One-Sensor Temperature Water Station***

## Technical specifications

### Dimensions and weight

| Version                   | Dimensions | Weight |
| :-:                       | :-         | :-     |
| Main Box                  |            |        |
| Probe support             |            |        |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository]({{ extra.urls.enclosures.link }}).

{{ get_snippet_rel("docs/includes/stations.md") }}

{{ get_snippet_rel("docs/includes/water-sensors.md") }}