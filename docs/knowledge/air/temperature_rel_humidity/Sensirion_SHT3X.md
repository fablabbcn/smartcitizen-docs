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

!!! warning "Under Construction"

    More details on working principles, usage, considerations, and resources are coming soon.

!!! info "Version"
    This sensor is supported from V2.0 onwards


## Modify temperature and relative humidity offset

Starting in firmware `0.9.11`, we have included a command to `control` temperature and relative humidity offsets for [Sensirion SHT3X](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X/) sensors, present in the [Urban Board](/hardware/boards/urban-board/) or as [an external probe](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X-weatherproof/), for both the `SHT31` and the `SHT35` type. This feature allows introducing an offset to both variables: temperature and relative humidity. This offset can be used to compensate for heat build-up on the device. Note that this offset is the same for [wi-fi / online](/hardware/kit/features/#wi-fi-mode) or [sd-card / offline](/hardware/kit/features/#sd-card-mode) modes. In addition, a small adjustment is *hardcoded* to compensate for battery charging additional heat up **only on the urban board**. 

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
