<!-- Source: https://docs.smartcitizen.me/knowledge/air/pressure/ -->

# Barometric Pressure Measurements

**Barometric pressure** (or atmospheric pressure) is the pressure exerted by the weight of the air above us. At sea level, it is around 101.3 kPa, and it decreases with altitude. It also changes with the weather: low pressure systems are generally related to clouds and rain, while high pressure systems are related to clear skies. Barometric pressure is also used to estimate altitude, and to compensate other sensors that are affected by pressure, such as some gas sensors.

All the versions of the SCK measure barometric pressure with a MEMS sensor in the [Urban Board](https://docs.smartcitizen.me/hardware/boards/urban-board.md).

## Reference levels

Barometric pressure has no _good_ or _bad_ levels from a health point of view, but these values help to interpret the readings:

| Condition | Pressure |
|:- |:-: |
| Standard atmosphere at sea level | 101.325 kPa (1013.25 hPa) |
| Typical range at sea level | ~98 – 104 kPa |
| Low pressure system (clouds, rain, storms) | Below ~100 kPa at sea level |
| High pressure system (stable weather, clear skies) | Above ~102 kPa at sea level |
| Change with altitude, close to sea level | ~ -1.2 kPa every 100 m |

The SCK reports the **absolute** (station) pressure, in kPa. Weather services report pressure _reduced to sea level_, so to compare both, the altitude of the kit needs to be taken into account (for instance, a kit at 500 m will read around 6 kPa less than the values reported by the weather service). Instead of the absolute value, the **trend** is often more useful: a fast drop in pressure (several hPa in a few hours) is generally a sign of an approaching storm.

## Supported Sensors

- [NXP MPL3115A2](https://docs.smartcitizen.me/knowledge/air/pressure/NXP_MPL3115A2.md) (Field | air; Metric | pressure; Connection | onboard): A barometric pressure sensor, that can also estimate altitude. Available in SCK2.1 and SCK2.3.
- [ST LPS33K](https://docs.smartcitizen.me/knowledge/air/pressure/ST_LPS33K.md) (Field | air; Metric | pressure; Connection | onboard): A compact barometric pressure sensor. Available in SCK2.2.
