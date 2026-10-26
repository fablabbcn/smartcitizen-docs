# Temperature and Relative Humidty Measurements

## Reference levels

Temperature and humidity have a big impact on **comfort and health**, and on how other pollutants behave (mould, dust mites, or the emission of VOCs from materials increase with temperature and humidity). The values below refer to **indoor** environments. Outdoors, what is _good_ or _bad_ depends a lot on the local climate, and heat warnings are generally based on local thresholds.

| Parameter | Reference | Value |
|:- |:- |:- |
| Temperature | WHO Housing and Health Guidelines [^1] | At least **18 ºC** indoors during the cold season (higher for older people, children and people with chronic illness) |
| Temperature | EN 16798-1, category II, offices and homes [^2] | **20 – 24 ºC** in winter (heating), **23 – 26 ºC** in summer (cooling) |
| Relative humidity | EN 16798-1, design values [^2] | **25 – 60 %rh** (category II), **30 – 50 %rh** (category I) |

As a general orientation for relative humidity indoors:

| Relative humidity | Interpretation |
|:-: |:- |
| < 30 % | Too dry: irritation of eyes and airways, static electricity |
| 30 – 60 % | Comfortable range |
| > 60 % | Too humid: higher risk of mould and dust mites, specially if it stays high for long periods or there is condensation on walls and windows |

!!! info "Sensor placement"
    The heat of the electronics can make the readings of the kit's internal sensors higher than the real air temperature (and the humidity lower). Check the [SHT3X page](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X/) for the default offsets and how to correct them before comparing the readings with these values.

## Supported Sensors

There are plenty of different temperature (and relative humidity sensors). In general, these do not necessarily go together, but many manufacturers have combined them in digital sensors.

{{ insert_cards(type="sensor", filter="target", value=["temperature"])}}

## References

[^1]:
    World Health Organization. “WHO Housing and Health Guidelines.” Geneva: World Health Organization, 2018. https://www.who.int/publications/i/item/9789241550376.
[^2]:
    CEN. “EN 16798-1:2019 Energy performance of buildings - Ventilation for buildings - Part 1: Indoor environmental input parameters for design and assessment of energy performance of buildings addressing indoor air quality, thermal environment, lighting and acoustics.” 2019.
