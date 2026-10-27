<!-- Source: https://docs.smartcitizen.me/knowledge/air/pressure/NXP_MPL3115A2/ -->

# NXP MPL3115A2

A barometric pressure sensor, that can also estimate altitude. Available in SCK2.1 and SCK2.3.

![](https://docs.smartcitizen.me/assets/images/nxp-mpl3115a26.jpg){.banner-box}

_Image Credit: **NXP**_{.image-credit-banner-box}

!!! info "Version"
    This sensor is available on the [Urban Board](https://docs.smartcitizen.me/hardware/boards/urban-board.md) of the SCK2.1 and SCK2.3. The SCK2.2 uses the [ST LPS33K](https://docs.smartcitizen.me/knowledge/air/pressure/ST_LPS33K.md) instead.

## Working principle

The MPL3115A2 is a MEMS pressure sensor. It has a very thin silicon membrane that bends with the pressure of the air. The deflection of the membrane is measured and converted into a digital pressure value by the integrated electronics [^1]. The sensor also includes a temperature sensor, used to compensate the pressure readings.

Since atmospheric pressure decreases with height, the sensor can also **estimate the altitude**, by comparing the measured pressure with a reference pressure at sea level.

## Usage and considerations

The sensor is on the Urban Board, and its readings are available as:

| Metric | Shell name | Units | Enabled by default | API |
|:- |:- |:-: |:-: |:- |
| Barometric pressure | `MPL Barometric pressure` | kPa | Yes | [58](https://api.smartcitizen.me/v0/sensors/58) |
| Altitude | `MPL Altitude` | m | No | [219](https://api.smartcitizen.me/v0/sensors/219) |
| Internal temperature | `MPL internal temperature` | ºC | No | - |

Metrics with `-` in the API column are not published to the platform.

You can check the readings with the `read` and `monitor` commands, and enable the other metrics with the `sensor` command:

```
read mpl barometric pressure
sensor mpl altitude -enable
```

!!! warning "Altitude estimation"
    The altitude is estimated using a standard reference pressure at sea level. Since the atmospheric pressure changes with the weather, the estimated altitude can change by tens of meters during the day, even if the kit doesn't move. Use it for relative changes over short periods of time, rather than as an absolute value.

Barometric pressure is used in meteorology: decreasing pressure generally indicates bad weather coming, while increasing pressure indicates good weather. It is also used to compensate other sensors that are affected by pressure.

!!! info "Internal temperature"
    The internal temperature is the temperature of the sensor itself, which is affected by the heat of the electronics, so it is not a good measurement of the air temperature. For that, use the [SHT3X](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X.md).

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |Piezoresistive MEMS pressure sensor with digital interface (I2C)               |
|Measurement range      |20 kPa – 110 kPa (operational), 50 kPa – 110 kPa (calibrated)                  |
|Absolute accuracy      |±0.4 kPa (50 – 110 kPa, 0 – 50 ºC)                                             |
|Resolution             |1.5 Pa (0.3 m in altitude)                                                     |

## Resources

- [Official product page and datasheet](https://www.nxp.com/part/MPL3115A2)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    NXP Semiconductors. “MPL3115A2 I2C Precision Altimeter - Datasheet.” https://www.nxp.com/part/MPL3115A2.