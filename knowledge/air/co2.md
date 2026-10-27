<!-- Source: https://docs.smartcitizen.me/knowledge/air/co2/ -->

# CO2 Measurements

**Carbon dioxide (CO2)** is a colorless gas produced by the combustion of all carbon-based fuels, such as methane (natural gas), petroleum distillates (gasoline, diesel, kerosene, propane), coal, wood and generic organic matter. Carbon dioxide is the most significant long-lived greenhouse gas in Earth's atmosphere. Although not a pollutant *per se*, CO2 can also be considered an indicator of ventilation, and several international norms indicate levels of CO2 that are recommended depending on different indoor space categories (EN 16798-1 and EN 16798-3, which replaced EN 15251 and EN 13779, and ASHRAE 62.1). See the [reference levels](#reference-levels) below.

## Reference levels

CO2 is not considered a pollutant at the concentrations normally found indoors, but it is a very good **indicator of ventilation**: people exhale CO2, so in an occupied space with poor ventilation, CO2 accumulates together with other pollutants, odours and airborne particles (including viruses). For reference:

- **Outdoor air** has around 420 - 430 ppm of CO2 (and it increases by ~2-3 ppm every year with human activity emissions). In cities, close to traffic, it can be somewhat higher
- **Indoor air** is always above the outdoor level when there are people inside. The difference with the outdoor level tells how well the space is ventilated

The European standard EN 16798-1 defines indoor environment categories based on the CO2 concentration **above the outdoor level** [^1]. The table also shows the approximate absolute values, assuming 420 ppm outdoors:

| Category | Expectation | CO2 above outdoors | Approx. absolute CO2 |
|:- |:- |:-: |:-: |
| I | High | ≤ 550 ppm | ≤ 970 ppm |
| II | Normal (new buildings and renovations) | ≤ 800 ppm | ≤ 1220 ppm |
| III | Moderate (acceptable) | ≤ 1350 ppm | ≤ 1770 ppm |
| IV | Low | > 1350 ppm | > 1770 ppm |

In practice, a simple classification is often used in schools, offices and homes, based on these standards:

| CO2 (ppm) | Ventilation |
|:-: |:- |
| < 800 | Good |
| 800 – 1000 | Acceptable, consider ventilating |
| 1000 – 1500 | Poor: ventilate |
| > 1500 | Very poor: ventilate as soon as possible |

High CO2 levels are related to drowsiness, headaches and lower concentration, mostly because of the poor ventilation they indicate. Direct health effects of CO2 itself appear at much higher concentrations: the occupational exposure limit in the EU is 5000 ppm (8 hours average) [^2].

!!! info "Equivalent CO2"
    Some MOx sensors, like the [CCS811](https://docs.smartcitizen.me/knowledge/air/chemical/AMS_CCS811.md), provide an _equivalent CO2_ (eCO2) value. This value is estimated from VOCs, not measured, so the levels above should **not** be used to interpret it.

## Supported sensors

Most CO2 sensors in the _low cost range_ are [NDIR (NonDispersive InfraRed sensors)](https://en.wikipedia.org/wiki/Nondispersive_infrared_sensor), a type of _sensor_ that emits light and uses _infrared absorption_ to measure CO2. This is the principle that the [SCD30](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD30.md) uses, which you can directly plug into the [Auxiliary port](https://docs.smartcitizen.me/hardware/kit/features.md#auxiliary-connector) of the Smart Citizen Kit (2.1 and above). There are some other types of sensor, for instance the [SCD4X](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD4X.md), a smaller _photoacoustic_ NDIR sensor, which is supported from firmware **V0.9.12** onwards and enabled by default in the `sck23_air` firmware build.

- [Sensirion SCD30](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD30.md) (Field | air; Metric | co2; Connection | external): The SCD30 is a NDIR CO2 sensor by Sensirion. You can use it to measure CO2 in indoor spaces or for experiments where you need to know an accurate CO2 level.
- [Sensirion SCD4X](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD4X.md) (Field | air; Metric | co2; Connection | external): The SCD4X (SCD40 and SCD41) is a miniature photoacoustic NDIR CO2 sensor by Sensirion. You can use it to measure CO2 in indoor spaces, in mobile setups, or for experiments where you need to know an accurate CO2 level.


## References

[^1]:
    CEN. “EN 16798-1:2019 Energy performance of buildings - Ventilation for buildings - Part 1: Indoor environmental input parameters for design and assessment of energy performance of buildings addressing indoor air quality, thermal environment, lighting and acoustics.” 2019.
[^2]:
    Commission Directive 2006/15/EC of 7 February 2006 establishing a second list of indicative occupational exposure limit values. https://eur-lex.europa.eu/eli/dir/2006/15/oj.