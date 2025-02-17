---
card: true
name: Figaro TGS260X
field:
  - air
type:
  - external
target:
  - vocs
feature_img: /assets/images/figaro-tgs260x.jpg
feature_img_credit: "Figaro"
excerpt: ""
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! warning "Under Construction"

    More details on working principles, usage, considerations, and resources are coming soon.

## Working principle

Metal oxide sensors (MOx) have an exposed surface film that changes its electrical properties (typically resistance) when exposed to the target gas. Small changes in conductivity/resistance are measured and are proportional to the concentration of the adsorbed gas [^14]. In very simple terms, chemical reactions take place between the target gas and the exposed surface film, which for oxidising gases such as O3 or NO2 will make the resistance increase; whereas for reducing gases such as CO or VOCs will make the resistance decrease. In general, these reactions occur at elevated temperatures and hence the sensing layer needs to be heated up. There are various sizes and formats for these sensors, sometimes in separate replaceable units, whereas other times are integrated in MEMS solutions.

## Limitations

The value of the resistance of the MOx layer cannot be considered as an absolute measurement of the target pollutant concentration, since the resistance varies from sensor to sensor, and it's affected by several conditions, such as temperature, humidity and other non-target pollutant affectations.

To mitigate this problem, the output of the sensor (RS) is normalised using the baseline resistance (RA): RS is divided by RA. This baseline resistance is the resistance that the sensor sees in clean air. Unfortunately, since RA varies with the deployment conditions, RA cannot be determined by a one-time calibration, and depending on the manufacturer and type, is maintained on-the-fly in software. This process is known as baseline correction.

Depending on the sensor type, and specially for MEMS formats, the results are often not valid without careful data analysis. It is then considered that these sensors are best employed for detecting instances or trends of gas presence rather than highly accurate readings.

## References

[^14]:
    Clements, A., S. Lung, A. Arfire, AND A. Polidori. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition: Evaluation Activities. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition. World Meteorological Organization, Geneva, Switzerland, , NA, (2020).
