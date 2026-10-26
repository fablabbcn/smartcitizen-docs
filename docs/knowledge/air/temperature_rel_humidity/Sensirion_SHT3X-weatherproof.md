---
card: true
name: Sensirion SHT3X Weatherproof
field:
  - air
type:
  - external
target:
  - temperature
feature_img: /assets/images/sensirion-sht3x-weatherproof.jpg
feature_img_credit: "DF-Robot"
excerpt: "A temperature and humidity sensor in a weatherproof capsule"
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! info "Sensor ranges"
    The weatherproof version uses the same sensor as the [SHT3X](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X/#performance) (SHT31 or SHT35), so the measurement ranges are the same: -40 ºC to 125 ºC and 0 to 100 %rh. Check the datasheet of your probe, since the cable and the housing can limit the operating temperature range.

## Assembly

To use this sensor, you'll need a [screw connector to grove adaptor](/guides/getting-started/third-party-sensors/#sensors-with-open-leads):

![](/assets/images/df-robot-screw-connector.jpeg)

## Modify temperature and relative humidity offset

External sensors offsets can be modified via the `control` command.

To check available commands (note that you can change `sht31` or `sht35`):

```
SCK > control ext sht31
Temperature: 
Available commands:
* cal: [float - clear] Sets temperature offset with respect to current offset or clears it
```

To check the offset currently implemented:

```
SCK > control ext sht31 temp cal
Current temperature offset: -1.00 (degC)
```

```
SCK > control ext sht31 hum cal
Current humidity offset: 3.50 (rh)
```

!!! info "Default offsets"
    The default offsets for external sensors are always 0degC and 0%rh. You can always modify them to suit your needs, or revert back to the default with `control temp cal clear` or `control hum cal clear`.

To modify, you can issue the `control ext sht31 temp cal` command followed by a the offset to add in float notation (for instance `-10.0`):

Check the calibration and read the current value:

```
SCK > control ext sht31 temp cal
Temperature: cal
Current temperature offset: -1.00 (degC)
SCK > read ext sht31 temp
Temperature: 25.95 C
```

Set the temperature offset to -10.0 degC. Note that for the previous reading, there was already an offset of `-1.00 degC`, so now the offset will be -11.0 degC:

```
SCK > control ext sht31 temp cal -10.00
Temperature: cal -10.00
SCK > control ext sht31 temp cal
Current temperature offset: -11.00 (degC)
SCK > read ext sht31 temp
Temperature: 15.96 C
```

To revert to the previous value:

```
SCK > control ext sht31 temp cal clear
Set default offset: -1.00 (degC)
SCK > control ext sht31 temp cal
Current temperature offset: -1.00 (degC)
SCK > read ext sht31 temp
Temperature: 26.09 C
```

Additional, for relative humidity:

```
control ext sht31 hum cal
Current humidity offset: 3.50 (rh)
SCK > read ext sht31 hum
Humidity: 63.06 %
```

```
SCK > control ext sht31 temp cal
Ext SHT31 Temperature: cal
Current temperature offset: 0.00 (degC)
```

```
SCK > control ext sht31 temp cal -2.00
Ext SHT31 Temperature: cal -2.00
Temperature offset set to -2.00 degC
```

```
SCK > control ext sht31 temp cal clear
Ext SHT31 Temperature: cal clear
Set default offset: 0.00 (degC)
```
