---
card: true
name: ST LPS33K
field:
  - air
type:
  - onboard
target:
  - pressure
feature_img: /assets/images/st-lps33k.jpg
feature_img_credit: "STMicroelectronics"
excerpt: "A compact barometric pressure sensor. Available in SCK2.2."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! info "Version"
    This sensor is available on the [Urban Board](/hardware/boards/urban-board/) of the SCK2.2. The SCK2.1 and SCK2.3 use the [NXP MPL3115A2](/knowledge/air/pressure/NXP_MPL3115A2/) instead.

## Working principle

The LPS33K is a **piezoresistive** MEMS absolute pressure sensor. Like the [MPL3115A2](/knowledge/air/pressure/NXP_MPL3115A2/), it has a thin silicon membrane that bends with the pressure of the air, and piezoresistive elements that change their resistance as it bends. The integrated electronics measure this change, compensate it with an internal temperature sensor, and convert it into a digital pressure value [^1].

## Usage and considerations

The sensor is on the Urban Board, and its readings are available as:

| Metric | Shell name | Units | Enabled by default | API |
|:- |:- |:-: |:-: |:- |
| Barometric pressure | `LPS33 Barometric pressure` | kPa | Yes | [227](https://api.smartcitizen.me/v0/sensors/227) |
| Internal temperature | `LPS33 internal temperature` | ºC | No | - |

Metrics with `-` in the API column are not published to the platform.

You can check the readings with the `read` and `monitor` commands:

```
read lps33 barometric pressure
```

The firmware operates the sensor in _one-shot_ mode: the sensor only takes a measurement when the SCK needs a reading, and stays in power down mode the rest of the time to save power.

Barometric pressure is used in meteorology: decreasing pressure generally indicates bad weather coming, while increasing pressure indicates good weather. It is also used to compensate other sensors that are affected by pressure.

!!! info "Internal temperature"
    The internal temperature is the temperature of the sensor itself, which is affected by the heat of the electronics, so it is not a good measurement of the air temperature. For that, use the [SHT3X](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X/).

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |Piezoresistive MEMS pressure sensor with digital interface (I2C)               |
|Measurement range      |30 kPa – 120 kPa (300 – 1200 hPa)                                              |

## Resources

- [Official product page and datasheet](https://www.st.com/en/mems-and-sensors/lps33k.html)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    STMicroelectronics. “LPS33K MEMS pressure sensor - Datasheet.” https://www.st.com/en/mems-and-sensors/lps33k.html.
