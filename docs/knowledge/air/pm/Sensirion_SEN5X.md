---
card: true
name: Sensirion SEN5X
field:
  - air
type:
  - onboard
target:
  - pm
feature_img: /assets/images/sensirion-sen5x.jpg
feature_img_credit: "Fab Lab Barcelona (Smart Citizen Team)"
excerpt: "The Sensirion SEN5X is a newer PM sensor with a very good performance for such low cost. Available in SCK2.2 and above!"
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! info "Version"
    This sensor is connected to the [Urban Board](/hardware/boards/urban-board/#pm-sensor-connection) from SCK2.2 onwards, replacing the [Plantower PMS5003](/knowledge/air/pm/Plantower_PMS5003/).

## Working principle

The SEN5X is an **environmental sensor node** by Sensirion. All the models of the family include an optical particulate matter sensor, and some of them include additional sensors [^1]:

| Model | PM | Temperature and humidity | VOC Index | NOx Index |
|:- |:-: |:-: |:-: |:-: |
| SEN50 | ✓ | | | |
| SEN54 | ✓ | ✓ | ✓ | |
| SEN55 | ✓ | ✓ | ✓ | ✓ |

The PM sensor uses the same principle as the [PMS5003](/knowledge/air/pm/Plantower_PMS5003/) (_laser scattering_): a fan pulls air through a chamber where a laser beam is scattered by the particles, and a photodetector measures the scattered light. From this signal, the sensor **counts** the particles of different sizes, and **estimates** their mass, assuming certain properties of the particles (shape, density, refractive index...). The sensor reports mass concentrations (PM1, PM2.5, PM4 and PM10), number concentrations, and the typical particle size.

The VOC and NOx sensors are **metal oxide (MOx)** sensors, which change their resistance when exposed to oxidising or reducing gases. Since the raw resistance is not an absolute measurement, Sensirion provides an algorithm that converts it into an **index**: the VOC index compares the current reading with the average conditions of the last 24 hours (100 being the average), while the NOx index shows the deviation from a baseline of clean air (1 being the baseline). Check the [chemical composition page](/knowledge/air/chemical/) for more information on MOx sensors and their limitations.

## Usage and considerations

The sensor is connected to the Urban Board with a custom cable, and the firmware automatically detects which model is connected. Depending on the model, the following metrics are available:

| Metric | Shell name | Units | Models | API |
|:- |:- |:-: |:- |:- |
| PM1, PM2.5, PM4, PM10 | `SEN5X PM 1.0`, `SEN5X PM 2.5`... | µg/m3 | All | [193](https://api.smartcitizen.me/v0/sensors/193), [194](https://api.smartcitizen.me/v0/sensors/194), [195](https://api.smartcitizen.me/v0/sensors/195), [196](https://api.smartcitizen.me/v0/sensors/196) |
| PN0.5, PN1, PN2.5, PN4, PN10 | `SEN5X PN 0.5`, `SEN5X PN 1.0`... | #/0.1l | All | [197](https://api.smartcitizen.me/v0/sensors/197), [198](https://api.smartcitizen.me/v0/sensors/198), [199](https://api.smartcitizen.me/v0/sensors/199), [200](https://api.smartcitizen.me/v0/sensors/200), [201](https://api.smartcitizen.me/v0/sensors/201) |
| Typical particle size | `SEN5X Typical Particle Size` | µm | All | [202](https://api.smartcitizen.me/v0/sensors/202) |
| Temperature | `SEN5X Temperature` | ºC | SEN54, SEN55 | [204](https://api.smartcitizen.me/v0/sensors/204) |
| Humidity | `SEN5X Humidity` | % | SEN54, SEN55 | [203](https://api.smartcitizen.me/v0/sensors/203) |
| VOC Index | `SEN5X Vocs Index` | - | SEN54, SEN55 | [205](https://api.smartcitizen.me/v0/sensors/205) |
| NOx Index | `SEN5X NOx Index` | - | SEN55 | [206](https://api.smartcitizen.me/v0/sensors/206) |

Raw values for temperature, humidity, VOCs and NOx are also available, but disabled by default.

!!! info "Grouped metrics"
    The SEN5X metrics are grouped (PM, PN, temperature and humidity, VOCs and NOx). When you enable or disable one metric with the `sensor` command, all the metrics in its group are enabled or disabled at the same time.

### Sensor operation

To save power, the PM sensor (fan and laser) is not running all the time. By default, PM readings are taken **every 5 reading intervals** (every 5 minutes with the default 1 minute interval). When a reading is needed, the sensor is started and the firmware waits for a **warm-up period** of 16 seconds, as recommended by the manufacturer. If the number of particles is low (below 100 #/cm3), the firmware waits until 30 seconds to get a more stable reading.

When the VOC or NOx metrics are enabled (SEN54 and SEN55), the gas sensors need to keep measuring continuously for the index algorithms to work. In this case, the firmware keeps the sensor in a mode where only the gas, temperature and humidity sensors are running (with the fan and laser off) between PM readings. The firmware also stores the state of the VOC algorithm, so that the learned baseline is not lost when the sensor is restarted.

!!! warning "Powering the sensor"
    The sensor needs a high current when it starts. If the SCK is powered only via USB, without a battery, it might not be able to start the sensor, and it can even enter a reset loop. Make sure the kit has a battery connected, and use a good USB cable and adaptor (at least 1A).

### Fan cleaning

Over time, dust accumulates inside the sensor. To avoid this, the fan can run at maximum speed for 10 seconds to blow the dust out. The firmware does this **automatically once a week**. You can also trigger a cleaning, or check when the last one happened:

```
SCK > control sen5x help
Available commands:
* debug: [0-1] Sets debug messages
* doclean: Starts a cleaning
* lastClean
* info
```

```
control sen5x doclean
control sen5x lastclean
```

The `info` command shows the firmware and hardware versions of the sensor, and the measurement mode:

```
control sen5x info
```

!!! info "Sensor firmware"
    The SCK firmware requires a SEN5X with firmware version 2 or higher. If the sensor has an older firmware, it will not be started.

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |Laser scattering PM sensor (and MOx gas sensors in SEN54/SEN55)                |
|Mass concentration range |0 – 1000 µg/m3                                                               |
|PM1 and PM2.5 precision |±(5 µg/m3 + 5% m.v.) from 0 to 100 µg/m3, ±10% m.v. from 100 to 1000 µg/m3     |
|PM4 and PM10 precision |±25 µg/m3 from 0 to 100 µg/m3, ±25% m.v. from 100 to 1000 µg/m3                |
|VOC and NOx index range |1 – 500                                                                       |

!!! info "Check the latest datasheet"
    The specifications above are taken from the manufacturer's datasheet at the time of writing. Check the [product page](https://sensirion.com/products/catalog/SEN55) for the latest values.

### Limitations

As all optical PM sensors, the SEN5X is affected by **relative humidity**, since particles can absorb water and grow in size, and by the **type of particles**, since the mass is estimated assuming certain properties. These sensors are good at detecting fine particles (PM1 and PM2.5), but their PM4 and PM10 values are mostly _estimated_ from the smaller particles, so they should be used with care [^2].

The VOC and NOx indices are **relative** values that adapt to the environment of the sensor. They are useful to detect events (like cooking, cleaning products, or traffic), but they cannot be converted to concentrations, and they cannot be compared between different locations.

## Resources

- [Official product page and datasheet](https://sensirion.com/products/catalog/SEN55)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    Sensirion. “SEN5x Environmental Sensor Node - Datasheet.” https://sensirion.com/products/catalog/SEN55.
[^2]:
    Vogt, Matthias, Philipp Schneider, Nuria Castell, and Paul Hamer. “Assessment of Low-Cost Particulate Matter Sensor Systems against Optical and Gravimetric Methods in a Field Co-Location in Norway.” Atmosphere 12, no. 8 (July 27, 2021): 961. https://doi.org/10.3390/atmos12080961.
