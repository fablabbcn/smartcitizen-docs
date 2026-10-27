---
card: true
name: Rohm BH1730FVC
field:
  - air
type:
  - onboard
target:
  - light
feature_img: /assets/images/rohm-bh1721fvc.jpg
feature_img_credit: "ROHM Semiconductor"
excerpt: "A digital ambient light sensor, that measures light as perceived by the human eye. Available in all SCK2.X versions."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! info "Version"
    This sensor is available on the [Urban Board](/hardware/boards/urban-board/) of all SCK2.X versions.

## Working principle

The BH1730FVC is a digital **ambient light sensor** (ALS). It measures the amount of visible light, in **lux**, which is the unit used to express how bright the light is _as perceived by the human eye_ [^1].

The sensor has two photodiodes: one that is sensitive to visible and infrared light (`DATA0`), and one that is mostly sensitive to infrared light (`DATA1`). Since the human eye does not see infrared light, the sensor combines both readings to remove the infrared contribution, and approximate the response of the human eye (the _photopic_ curve). The formula for this depends on the ratio between both readings (`DATA1/DATA0`), which changes with the type of light source (sunlight, incandescent, fluorescent or LED light have very different amounts of infrared light).

## Usage and considerations

The sensor is on the Urban Board, and its readings are available as:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| Ambient light | `Light` | lux | [14](https://api.smartcitizen.me/v0/sensors/14) |

You can check the readings with the `read` and `monitor` commands:

```
read light
```

The firmware adjusts the **integration time** automatically: it starts with a default integration time, and if the readings are too low (dark environments), it increases it to get a better resolution. Then, the lux value is calculated with the formula from the datasheet.

Ambient light measurements can be used, for instance, to study light pollution at night, the amount of daylight in indoor spaces, or as an indicator of the occupancy of a space (lights on or off).

!!! warning "Sensor exposure"
    The readings depend on how much light reaches the sensor. The position of the kit (pointing up, to a wall, in the shade...), and any enclosure placed on top of it, will greatly affect the readings. Keep this in mind when comparing data from different kits.

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |Ambient light sensor with digital interface (I2C)                              |
|Detection range        |0.001 lux – 100.000 lux                                                        |
|Output                 |16 bit (visible + IR and IR channels)                                          |
|Units                  |lux                                                                            |

The detection range above is taken from the manufacturer's [datasheet](https://fscdn.rohm.com/en/products/databook/datasheet/ic/sensor/light/bh1730fvc-e.pdf), using all the combinations of gain and integration time. Very bright conditions, such as direct sunlight, can be at the top of the range.

### Limitations

- The sensor approximates the response of the human eye, but the approximation is better for some light sources than for others
- The sensor has a field of view, and light coming from the sides will be measured with a lower sensitivity
- The readings are not calibrated against a reference luxmeter, so they should be considered as indicative, specially when comparing different kits
- To measure the **color** of the light, and not only the amount, check the [AS7341 spectral sensor](/knowledge/air/light/AMS_AS7341/)

## Resources

- [Official product page and datasheet](https://www.rohm.com/products/sensors-mems/ambient-light-sensor-ics/bh1730fvc-product)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    ROHM Semiconductor. “BH1730FVC Digital 16bit Serial Output Type Ambient Light Sensor IC - Datasheet.” https://www.rohm.com/products/sensors-mems/ambient-light-sensor-ics/bh1730fvc-product.
