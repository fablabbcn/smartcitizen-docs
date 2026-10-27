---
card: true
name: AMS AS7331
field:
  - air
type:
  - onboard
target:
  - light
feature_img: /assets/images/ams-as7331.jpg
feature_img_credit: "ams OSRAM"
excerpt: "A sensor for measuring UV-A, UV-B and UV-C light! Available in SCK2.2 and above."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! info "Version"
    This sensor is available on the [Urban Board](/hardware/boards/urban-board/) from SCK2.2 onwards.

## Working principle

The AS7331 is an ultraviolet (UV) light sensor with three independent channels, each one with its own photodiode and interference filter, that measure the three bands of the UV spectrum [^1]:

| Channel | Band | Wavelength range |
|:- |:- |:-: |
| UVA | UV-A | 315 - 410 nm |
| UVB | UV-B | 280 - 315 nm |
| UVC | UV-C | 200 - 280 nm |

Each photodiode is connected to a converter that integrates the current produced by the light during a certain time, and transforms it into a digital value. The sensor also measures the conversion time, which allows to convert the readings into **irradiance** (power per unit area).

UV radiation is relevant for health: UV-A and specially UV-B radiation are responsible for sunburns and skin damage. Most UV-C radiation from the sun is absorbed by the atmosphere, so UV-C measurements outdoors should be very close to zero. However, UV-C is used in germicidal lamps, where the sensor can be useful.

## Usage and considerations

The sensor is on the Urban Board, and its readings are available as:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| UV-A | `AS7331 UVA` | µW/cm2 | [214](https://api.smartcitizen.me/v0/sensors/214) |
| UV-B | `AS7331 UVB` | µW/cm2 | [215](https://api.smartcitizen.me/v0/sensors/215) |
| UV-C | `AS7331 UVC` | µW/cm2 | [216](https://api.smartcitizen.me/v0/sensors/216) |

You can check the readings with the `read` and `monitor` commands, for instance:

```
read as7331 uva
```

The firmware operates the sensor in _command mode_: every time a reading is needed, the sensor makes a single measurement, and then goes back to standby to save power. The measurement is done with a gain of 8x and an integration time of 512 ms, and the result is converted to µW/cm2 using the sensitivities from the datasheet.

!!! warning "Sensor exposure"
    UV light is filtered by most plastics and glass. If you place the kit inside an enclosure, make sure the sensor is exposed, or behind a UV-transparent material. Also, the readings will be very different if the kit is placed in the shade, or indoors.

!!! info "UV index"
    The [UV index](https://en.wikipedia.org/wiki/Ultraviolet_index) is calculated by weighting the solar spectrum with the _erythemal action spectrum_ (how much each wavelength affects the skin). The SCK reports the **irradiance** of each band, not the UV index directly. The UV index can be estimated from the UV-A and UV-B readings, but this requires a calibration of the sensor against a reference instrument, and it is only valid for solar radiation.

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |UV sensor with three channels and digital interface (I2C)                      |
|Channels               |UV-A, UV-B, UV-C                                                               |
|Gain (SCK)             |8x                                                                             |
|Integration time (SCK) |512 ms                                                                         |
|Full scale (SCK)       |~5000 µW/cm2 (UV-A), ~6500 µW/cm2 (UV-B), ~3100 µW/cm2 (UV-C)                 |
|Resolution (SCK)       |~0.08 µW/cm2 (UV-A), ~0.1 µW/cm2 (UV-B), ~0.05 µW/cm2 (UV-C)                   |
|Units                  |µW/cm2                                                                         |

The full scale and resolution above are calculated from the 16-bit output and the conversion factors used in the firmware for the SCK settings (8x gain and 512 ms). The sensor itself can measure from below 1 µW/cm2 up to ~3.5x10^5 µW/cm2 with other gain and integration time settings [^1].

!!! warning "Saturation in direct sunlight"
    Midday sun in summer can reach values close to the UV-A full scale with the SCK settings, so readings at the top of the range might be saturated.

### Limitations

- The readings depend a lot on the placement of the sensor and on the material of the enclosure window
- The filters are not perfect, and there might be some _crosstalk_ between channels (for instance, some UV-A light measured in the UV-B channel), which is relevant when one band is much stronger than the others (like in solar radiation)
- The readings are not calibrated against a reference instrument, so they should be considered as indicative

## Resources

- [Official product page and datasheet](https://ams-osram.com/products/sensor-solutions/ambient-light-color-spectral-proximity-sensors/ams-as7331-spectral-uv-sensor)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckUrban.cpp)

### References

[^1]:
    ams OSRAM. “AS7331 Spectral UVA/B/C Sensor - Datasheet.” https://ams-osram.com/products/sensor-solutions/ambient-light-color-spectral-proximity-sensors/ams-as7331-spectral-uv-sensor.
