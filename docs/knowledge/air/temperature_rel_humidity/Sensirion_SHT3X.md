---
card: true
name: Sensirion SHT3X
field:
  - air
type:
  - onboard
target:
  - temperature
feature_img: /assets/images/sensirion-sht3x.jpg
feature_img_credit: "Sensirion"
excerpt: "A temperature and humidity sensor that we love! Available in SCK2.X."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! info "Version"
    This sensor (an SHT31) is available on the [Urban Board](/hardware/boards/urban-board/) of all SCK2.X versions. The same sensor is also available as an external, weatherproof probe: check the [SHT3X Weatherproof](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X-weatherproof/) page.

## Working principle

The SHT3X is a digital temperature and relative humidity sensor by Sensirion. Both sensors are integrated in the same small chip, together with the electronics that convert the signals into calibrated digital values [^1]:

- **Relative humidity** is measured with a **capacitive** sensor: a thin polymer layer between two electrodes absorbs water from the air, which changes its dielectric properties and thus the capacitance of the sensor
- **Temperature** is measured with a band-gap temperature sensor, which is also used to compensate the humidity readings

Each sensor is individually calibrated in the factory. The SHT3X family includes the SHT30, SHT31 and SHT35, which only differ in their accuracy, with the SHT31 being the one used in the SCK.

## Usage and considerations

The sensor is on the Urban Board, and its readings are available as:

| Metric | Shell name | Units |
|:- |:- |:-: |
| Air temperature | `Temperature` | ºC |
| Relative humidity | `Humidity` | % |

You can check the readings with the `read` and `monitor` commands:

```
read temp
read hum
```

The firmware takes a single high repeatability measurement every time a reading is needed.

!!! warning "Sensor placement"
    The sensor measures the temperature and humidity of the air that surrounds it. Inside the kit, the electronics (and specially the battery while it's charging) heat up the air around the sensor, and direct sunlight on the enclosure will also increase the readings. Make sure the kit is in a ventilated place, in the shade, and check the [enclosure options](/hardware/kit/features/) for outdoor deployments.

### Default offsets

To compensate for the heat build-up inside the kit, the firmware applies a default offset to the readings, which has been determined with internal tests on each hardware version:

| Version | Temperature offset | Humidity offset | Additional offset while charging (T / RH) |
|:- |:-: |:-: |:-: |
| SCK2.1 | -1.3 ºC | +5 %rh | -0.2 ºC / 0 %rh |
| SCK2.2 | -1.0 ºC | +3.5 %rh | -0.2 ºC / +0.5 %rh |
| SCK2.3 | -1.0 ºC | +3.5 %rh | -0.25 ºC / +0.5 %rh |

The additional offset is applied only when the kit is powered via USB, since the battery charging heats up the board. These offsets might not be valid for every situation (for instance, if you use a different enclosure), so they can be modified as described below.


## Modify temperature and relative humidity offset

This offset can be used to compensate for heat build-up on the device. Note that this offset is the same for [wi-fi / online](/hardware/kit/features/#wi-fi-mode) or [sd-card / offline](/hardware/kit/features/#sd-card-mode) modes. In addition, a small adjustment is *hardcoded* to compensate for battery charging additional heat up **only on the urban board**. 

To check available commands (note that you can change `temp` or `hum` for the urban board):

```
SCK > control temp
Temperature: 
Available commands:
* cal: [float - clear] Sets temperature offset with respect to current offset or clears it
```

To check the offset currently implemented:

```
SCK > control temp cal
Current temperature offset: -1.00 (degC)
```

```
SCK > control hum cal
Current humidity offset: 3.50 (rh)
```

!!! info "Default offsets"
    These offsets are calibrated based on internal tests on each hardware version. You can always modify them to suit your needs, or revert back to the default with `control temp cal clear` or `control hum cal clear`

To modify, you can issue the `control temp cal` command followed by a the offset to add in float notation (for instance `-10.0`):

Check the calibration and read the current value:

```
SCK > control temp cal
Temperature: cal
Current temperature offset: -1.00 (degC)
SCK > read temp
Temperature: 25.95 C
```

Set the temperature offset to -10.0 degC. Note that for the previous reading, there was already an offset of `-1.00 degC`, so now the offset will be -11.0 degC:

```
SCK > control temp cal -10.00
Temperature: cal -10.00
SCK > control temp cal
Current temperature offset: -11.00 (degC)
SCK > read temp
Temperature: 15.96 C
```

To revert to the previous value:

```
SCK > control temp cal clear
Set default offset: -1.00 (degC)
SCK > control temp cal
Current temperature offset: -1.00 (degC)
SCK > read temp
Temperature: 26.09 C
```

As an example, other sensors can be also modified. For instance, for humidity:

```
control hum cal
Current humidity offset: 3.50 (rh)
SCK > read hum
Humidity: 63.06 %
```

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |Capacitive humidity and band-gap temperature sensor with digital interface (I2C) |
|Temperature range      |-40 ºC – 125 ºC                                                                |
|Temperature accuracy   |±0.2 ºC (typical, 0 – 90 ºC)                                                   |
|Humidity range         |0 – 100 %rh                                                                    |
|Humidity accuracy      |±1.5 %rh (typical)                                                             |

!!! info "Check the latest datasheet"
    The specifications above are for the SHT31, taken from the manufacturer's datasheet at the time of writing. Note that these refer to the sensor itself: the accuracy of the readings of the kit also depends on the placement and on the heat of the electronics, as explained above.

### Limitations

- Heat from the electronics, the battery charging and solar radiation are the main sources of error, and they are not constant (they depend on the activity of the kit and on the environment)
- Exposure to very high humidity (condensation) or to certain chemicals (solvents, for instance) for long periods can produce an offset in the humidity readings, which generally recovers over time in normal conditions
- Relative humidity depends on temperature: if the temperature reading is affected by heat, the relative humidity reading will be lower than the real one

## Resources

- [Official product page and datasheet](https://sensirion.com/products/catalog/SHT31-DIS-B)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    Sensirion. “SHT3x-DIS Humidity and Temperature Sensor - Datasheet.” https://sensirion.com/products/catalog/SHT31-DIS-B.
