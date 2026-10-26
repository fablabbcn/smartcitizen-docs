---
card: true
name: Bosch BME680
field:
  - air
type:
  - external
target:
  - chemical
feature_img: /assets/images/bosch-bme680.jpg
feature_img_credit: "Bosch Sensortec"
excerpt: "A multi-sensor node for environmental metrics and air quality."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! warning "Experimental support"
    The BME680 is not enabled in any of the default firmware builds. To use it, you need to compile the firmware with the `SCK_WITH_BME68X` flag. Check the guide on [enabling additional features](/guides/firmware/enabling-additional-features/), and reach out on the [forum]({{ extra.urls.forum.link }}) if you plan to use it.

## Working principle

The BME680 is a small environmental sensor by Bosch Sensortec that combines four measurements in a single package [^1]:

- **Temperature**, **relative humidity** and **barometric pressure**, measured with MEMS sensors similar to the ones found in other Bosch sensors (like the BME280)
- A **gas sensor**, which is a [metal oxide (MOx)](/knowledge/air/chemical/Figaro_TGS260X/#working-principle) sensor. Its sensing layer is heated up and its resistance changes in the presence of reducing gases, such as VOCs or carbon monoxide

The gas sensor is not selective to any specific gas. Its resistance decreases with higher concentrations of reducing gases, so it is generally used as an indicator of **indoor air quality**: cooking, cleaning products, people breathing, or materials emitting VOCs will produce a drop in the resistance.

## Usage and considerations

When enabled in the firmware, the following metrics are available:

| Metric | Shell name | Units |
|:- |:- |:-: |
| Temperature | `Temperature BME680` | ºC |
| Humidity | `Humidity BME680` | % |
| Barometric pressure | `Barometric pressure BME680` | kPa |
| Gas resistance | `VOC Gas BME680` | Ohms |

The firmware reports the **raw gas resistance** of the sensor, in Ohms. Bosch provides a closed-source library (BSEC) that converts this resistance into an _Indoor Air Quality (IAQ) index_ and other estimated values, but this library is **not** used in the SCK firmware, so the resistance needs to be interpreted in post-processing.

!!! info "Interpreting the gas resistance"
    A **lower** resistance means **more** reducing gases (worse air quality). The absolute value changes from sensor to sensor and with temperature and humidity, so look at relative changes over time, rather than absolute values.

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Temperature range      |-40 ºC – 85 ºC (±0.5 ºC at 25 ºC, ±1.0 ºC from 0 to 65 ºC)                     |
|Humidity range         |0 – 100 %rh (±3 %rh from 20 to 80 %rh, at 25 ºC)                               |
|Pressure range         |300 – 1100 hPa (±0.6 hPa from 0 to 65 ºC)                                      |
|Gas sensor             |Raw resistance (Ohms). Operational range of the gas sensor: 10 – 95 %rh        |

The specifications above are taken from the manufacturer's [datasheet](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/) at the time of writing.

### Limitations

As all MOx sensors, the gas resistance cannot be considered as an absolute measurement of any pollutant concentration. It is affected by temperature, humidity and many different gases, and it drifts over time. Check the [limitations of MOx sensors](/knowledge/air/chemical/Figaro_TGS260X/#limitations) for more information. These sensors are best used for detecting events or trends in indoor air quality.

The temperature readings are affected by the heat of the gas sensor's heater and of the surrounding electronics, so they might be higher than the actual air temperature.

## Resources

- [Official product page and datasheet](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    Bosch Sensortec. “BME680 Low power gas, pressure, temperature & humidity sensor - Datasheet.” https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/.
