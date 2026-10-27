---
card: true
name: Sensirion SPS30
field:
  - air
type:
  - external
target:
  - pm
feature_img: /assets/images/sensirion-sps30.jpg
feature_img_credit: "Sensirion"
excerpt: "The Sensirion SPS30 is PM sensor with a very good performance for such low cost. Only supported for experimental setups!"
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! warning "Experimental support"
    The SPS30 is not enabled in any of the default firmware builds. To use it, you need to compile the firmware with the `SCK_WITH_SPS30` flag. Check the guide on [enabling additional features](/guides/firmware/enabling-additional-features/). For most uses, we recommend the [SEN5X](/knowledge/air/pm/Sensirion_SEN5X/), which is based on the same technology and is supported by default from SCK2.2 onwards.

## Working principle

The SPS30 is an optical particulate matter sensor by Sensirion, based on **laser scattering**. A fan pulls air through a chamber where a laser beam is scattered by the particles, and a photodetector measures the scattered light. From this signal, the sensor **counts** the particles of different sizes, and **estimates** their mass, assuming certain properties of the particles (shape, density, refractive index...) [^1]. Check the [PMS5003](/knowledge/air/pm/Plantower_PMS5003/) page for a more detailed explanation of this principle.

The sensor reports mass concentrations (PM1, PM2.5, PM4 and PM10), number concentrations (PN0.5, PN1, PN2.5, PN4 and PN10) and the typical particle size. Sensirion's PM sensors have a fan speed control and a contamination resistant design, which gives them a good long-term stability.

## Usage and considerations

The SPS30 is implemented in the firmware as an I2C sensor on the same bus as the Urban Board PM connector (address `0x69`). It needs a 5V supply. When enabled, the following metrics are available:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| PM1, PM2.5, PM4, PM10 | `SPS30 PM 1.0`, `SPS30 PM 2.5`... | µg/m3 | [182](https://api.smartcitizen.me/v0/sensors/182), [183](https://api.smartcitizen.me/v0/sensors/183), [184](https://api.smartcitizen.me/v0/sensors/184), [185](https://api.smartcitizen.me/v0/sensors/185) |
| PN0.5, PN1, PN2.5, PN4, PN10 | `SPS30 PN 0.5`, `SPS30 PN 1.0`... | #/0.1l | [186](https://api.smartcitizen.me/v0/sensors/186), [187](https://api.smartcitizen.me/v0/sensors/187), [188](https://api.smartcitizen.me/v0/sensors/188), [189](https://api.smartcitizen.me/v0/sensors/189), [190](https://api.smartcitizen.me/v0/sensors/190) |
| Typical particle size | `SPS30 Typical Particle Size` | µm | [191](https://api.smartcitizen.me/v0/sensors/191) |

### Sensor operation

As with the other PM sensors, the SPS30 is not running all the time, to save power. By default, PM readings are taken **every 5 reading intervals**. When a reading is needed, the sensor is woken up, and the firmware waits for a **warm-up period** of 16 seconds. If the number of particles is low, it waits until 30 seconds to get a more stable reading, as recommended by the manufacturer.

The sensor needs a periodic **fan cleaning** to blow out the dust accumulated inside. The firmware does this automatically once a week. You can also control it with the following commands:

```
SCK > control sps30 help
Available commands:
* debug: [0-1] Sets debug messages
* doclean: Starts a cleaning
* lastClean
```

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |Laser scattering PM sensor                                                     |
|Mass concentration range |0 – 1000 µg/m3                                                               |
|PM1 and PM2.5 precision |±(5 µg/m3 + 5% m.v.) from 0 to 100 µg/m3, ±10% m.v. from 100 to 1000 µg/m3     |
|PM4 and PM10 precision |±25 µg/m3 from 0 to 100 µg/m3, ±25% m.v. from 100 to 1000 µg/m3                |
|Number concentration range |0 – 3000 #/cm3                                                             |
|Particle size range    |0.3 – 10 µm                                                                    |
|Interface (SCK)        |I2C                                                                            |

!!! info "Check the latest datasheet"
    The specifications above are taken from the manufacturer's datasheet at the time of writing. Check the [product page](https://sensirion.com/products/catalog/SPS30) for the latest values.

### Limitations

As all optical PM sensors, the SPS30 is affected by **relative humidity** and by the **type of particles**. Its PM4 and PM10 values are mostly estimated from the smaller particles, so they should be used with care [^2].

## Resources

- [Official product page and datasheet](https://sensirion.com/products/catalog/SPS30)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    Sensirion. “SPS30 Particulate Matter Sensor - Datasheet.” https://sensirion.com/products/catalog/SPS30.
[^2]:
    Vogt, Matthias, Philipp Schneider, Nuria Castell, and Paul Hamer. “Assessment of Low-Cost Particulate Matter Sensor Systems against Optical and Gravimetric Methods in a Field Co-Location in Norway.” Atmosphere 12, no. 8 (July 27, 2021): 961. https://doi.org/10.3390/atmos12080961.
