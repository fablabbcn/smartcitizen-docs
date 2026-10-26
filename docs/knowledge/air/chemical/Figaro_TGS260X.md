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
excerpt: "Low cost Metal Oxide sensors for VOCs"
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

## Working principle

Metal oxide sensors (MOx) have an exposed surface film that changes its electrical properties (typically resistance) when exposed to the target gas. Small changes in conductivity/resistance are measured and are proportional to the concentration of the adsorbed gas [^14]. In very simple terms, chemical reactions take place between the target gas and the exposed surface film, which for oxidising gases such as O3 or NO2 will make the resistance increase; whereas for reducing gases such as CO or VOCs will make the resistance decrease. In general, these reactions occur at elevated temperatures and hence the sensing layer needs to be heated up. There are various sizes and formats for these sensors, sometimes in separate replaceable units, whereas other times are integrated in MEMS solutions.

## Usage and considerations

The TGS260X family includes several sensors with different target gases, for instance the TGS2600 (general air contaminants, such as hydrogen and carbon monoxide), or the TGS2602 (VOCs and odorous gases, such as ammonia and hydrogen sulfide). Check the [manufacturer's website](https://www.figaro.co.jp/en/product/sensor/) for the datasheets of each model.

These sensors have an **analog output**: the sensing element is a resistor that changes with the gas concentration, and it is generally read by placing it in series with a load resistor, and measuring the voltage across it. The sensor also needs a **heater** powered at 5V, which consumes a significant amount of current compared to digital sensors.

!!! info "Connecting to the SCK"
    There is no dedicated firmware support for these sensors. They can be connected to the SCK as analog sensors through the [Analog Sensor Board](/hardware/boards/analog-sensor-board/), which reads the voltage with a [TI ADS1115](/knowledge/other/TI_ADS1X15/) ADC, and can work at 5V with a selectable jumper. The SCK will log the **voltage**, which needs to be converted to sensor resistance (RS) and normalised in post-processing.

!!! warning "Warm-up"
    MOx sensors need a warm-up period after they are powered (from minutes to several days for a new sensor, depending on the model) before their readings are stable. Check the datasheet of each model.

### Detection range

The typical detection range of the most common models, according to the manufacturer, is:

| Model | Target gases | Typical detection range |
|:- |:- |:-: |
| TGS2600 | General air contaminants (hydrogen, ethanol...) | 1 – 30 ppm of H2 |
| TGS2602 | VOCs and odorous gases (ammonia, H2S...) | 1 – 30 ppm of ethanol |

Note that these ranges refer to the gas used to characterise the sensor. The sensor responds to many other gases, so the readings cannot be directly converted to concentration of a specific gas.

## Limitations

The value of the resistance of the MOx layer cannot be considered as an absolute measurement of the target pollutant concentration, since the resistance varies from sensor to sensor, and it's affected by several conditions, such as temperature, humidity and other non-target pollutant affectations.

To mitigate this problem, the output of the sensor (RS) is normalised using the baseline resistance (RA): RS is divided by RA. This baseline resistance is the resistance that the sensor sees in clean air. Unfortunately, since RA varies with the deployment conditions, RA cannot be determined by a one-time calibration, and depending on the manufacturer and type, is maintained on-the-fly in software. This process is known as baseline correction.

Depending on the sensor type, and specially for MEMS formats, the results are often not valid without careful data analysis. It is then considered that these sensors are best employed for detecting instances or trends of gas presence rather than highly accurate readings.

## Resources

- [Figaro product page](https://www.figaro.co.jp/en/product/sensor/)

## References

[^14]:
    Clements, A., S. Lung, A. Arfire, AND A. Polidori. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition: Evaluation Activities. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition. World Meteorological Organization, Geneva, Switzerland, , NA, (2020).
