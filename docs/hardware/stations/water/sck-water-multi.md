---
card: true
type: unit
name: Multi-Sensor Water Station
field:
  - water
grade: advanced
feature_img: https://live.staticflickr.com/65535/53909712132_b46cae1a7e_k.jpg
feature_img_description: "Multi-Sensor Water Station"
excerpt: The Water Station is a multiparametric water unit, capable of measuring pH, Temperature, Dissolved Oxygen, Conductivity and ORP.
---

# {{ name }}

**Grade**: _{{ grade }}_

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}
{%if feature_img_description %}***{{ feature_img_description }}***{.image-credit-banner-box}{%endif%}

## Measurements

Measurements on the water stations can be from 2, to all 5 from below:

| Measurement      | Units    | Sensor                        |
| :-:              | :-:      | :-:                           |
| Temperature      | ºC       | Atlas PT-1000, PT-100 probes  |
| pH               | -        | Atlas pH probes               |
| Conductivity     | uS/cm    | Atlas Conductivity probes     |
| Dissolved Oxygen | mg/l     | Atlas DO probes               |
| ORP              | mV       | Atlas ORP probes              |

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