<!-- Source: https://docs.smartcitizen.me/knowledge/air/light/ -->

# Light Measurements

Light measurements supported in the SCK can be either for visible light (ambient light sensors or ALS), ultraviolet light sensors (UV), or spectral sensors. Ambient light can be an indicator of light pollution, while UV-index can help people determine if they live in an area where they are exposed to high levels of UV radiation. In some areas of the world, this is an important issue, given the ozone-layer depletion and the increased levels of UV-radiation because of it. Additionally, spectral sensors can measure the color composition of light, from violet to near infrared, and detect the flicker of artificial lighting.

## Reference levels

### Ambient light (lux)

There are no _good_ or _bad_ light levels in absolute terms, as it depends on the activity and on the time of the day. These are some typical values, for orientation:

| Illuminance (lux) | Example |
|:-: |:- |
| < 0.01 | Moonless night sky, far from cities |
| 0.1 – 0.3 | Full moon |
| 5 – 50 | Street lighting |
| 100 | Corridors, stairs |
| 300 – 500 | Offices, classrooms (500 lux is the usual requirement for desk work [^1]) |
| 1000 – 10.000 | Overcast day, outdoors |
| 30.000 – 100.000 | Direct sunlight |

Light also has an effect on our **sleep and circadian rhythm**. Recent recommendations suggest at least 250 lux during the day, below 10 lux in the three hours before going to sleep, and below 1 lux in the bedroom at night [^2]. Note that these recommendations are given in _melanopic_ units, which are more sensitive to blue light, so photopic lux (as measured by ambient light sensors) are only an approximation. At night, ambient light measurements can also be used to study **light pollution**: in a natural dark environment, the light level should be well below 1 lux.

### UV radiation

The usual reference for UV radiation is the **UV index** (UVI), defined by the WHO [^3]:

| UV index | Category | Recommended protection |
|:-: |:- |:- |
| 0 – 2 | Low | No protection needed |
| 3 – 5 | Moderate | Protection needed: shade around midday, shirt, sunscreen and hat |
| 6 – 7 | High | Protection needed |
| 8 – 10 | Very high | Extra protection: avoid being outside around midday |
| 11+ | Extreme | Extra protection |

The UV index is calculated from the UV irradiance **weighted by the sensitivity of the skin** (_erythemal_ weighting), which is much higher for UV-B than for UV-A. Each unit of UV index corresponds to 25 mW/m2 (2.5 µW/cm2) of erythemally weighted irradiance. The [AS7331](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7331.md) measures the UV-A, UV-B and UV-C bands **without** this weighting, so its readings can't be directly converted to UV index without a calibration against a reference instrument.

### Flicker

Light flicker (measured by the [AS7341](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7341.md)) is not visible above ~80 Hz, but it can cause discomfort, headaches, and in extreme cases, seizures. The IEEE 1789-2015 recommendation defines a **low risk** zone depending on the frequency and the percent of modulation of the light (the difference between maximum and minimum light, relative to the sum of both) [^4]:

| Flicker frequency | Low risk | No observable effect |
|:- |:-: |:-: |
| Below 90 Hz | Modulation < 0.025 x frequency (%) | Modulation < 0.01 x frequency (%) |
| 90 – 1250 Hz | Modulation < 0.08 x frequency (%) | Modulation < 0.0333 x frequency (%) |
| Above 1250 Hz | No restriction | No restriction above 3000 Hz |

For instance, a lamp flickering at 100 Hz is in the low risk zone if its modulation is below 8 %. The SCK reports the flicker amplitude as a peak to peak value in counts, so it is useful to compare light sources, but the percent of modulation needs to be estimated with the average light level.

## Supported sensors

- [AMS AS7331](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7331.md) (Field | air; Metric | light; Connection | onboard): A sensor for measuring UV-A, UV-B and UV-C light! Available in SCK2.2 and above.
- [AMS AS7341](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7341.md) (Field | air; Metric | light; Connection | external): The AS7341 is an 11-channel spectral sensor by ams OSRAM. You can use it to measure the color composition of light, from violet to near infrared, and to detect light flicker.
- [Rohm BH1730FVC](https://docs.smartcitizen.me/knowledge/air/light/Rohm_BH1730FVC.md) (Field | air; Metric | light; Connection | onboard): A digital ambient light sensor, that measures light as perceived by the human eye. Available in all SCK2.X versions.


## References

[^1]:
    CEN. “EN 12464-1:2021 Light and lighting - Lighting of work places - Part 1: Indoor work places.” 2021.
[^2]:
    Brown, Timothy M., George C. Brainard, Christian Cajochen, Charles A. Czeisler, John P. Hanifin, Steven W. Lockley, Robert J. Lucas, et al. “Recommendations for Daytime, Evening, and Nighttime Indoor Light Exposure to Best Support Physiology, Sleep, and Wakefulness in Healthy Adults.” PLOS Biology 20, no. 3 (March 17, 2022): e3001571. https://doi.org/10.1371/journal.pbio.3001571.
[^3]:
    World Health Organization. “Global Solar UV Index: A Practical Guide.” Geneva: World Health Organization, 2002. https://www.who.int/publications/i/item/9241590076.
[^4]:
    IEEE. “IEEE 1789-2015 - IEEE Recommended Practices for Modulating Current in High-Brightness LEDs for Mitigating Health Risks to Viewers.” 2015. https://doi.org/10.1109/IEEESTD.2015.7118618.