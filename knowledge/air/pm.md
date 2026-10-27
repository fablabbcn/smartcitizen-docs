<!-- Source: https://docs.smartcitizen.me/knowledge/air/pm/ -->

# Particulate Matter Measurements

Particulate Matter (or PM for short) refers to mixture of solid particles and liquid droplets that we can find in the air. Some particles, such as dust, dirt, soot, or smoke, are large or dark enough to be seen with the naked eye, but others can reach far inside our respiratory system.

## Light scattering sensors

Generally, the type of sensor that are used to measure suspended particles in air employ a light beam in the form of laser beams or infrared (IR) leds and a light detector. When using laser beams, it is most commonly set to one side (often 90°) of the source beam, to avoid reflections of the light source itself which could induce noise in the readings [^7]. The amount of particles per unit of volume is then a function of the light reflected into the detector and the mass is a calculation derived from this density, assuming certain properties of the particles, such as shape, colour and reflectivity, among others [^7].

An onboard microcontroller is in charge of taking readings from the sensing element and counts how many particles are passing in front of the light detector. The sensor element can differentiate between different particle sizes, and group them in size bins according to the results of an onboard, proprietary algorithm. In other words, this algorithm will group, for instance, the particles that have a diameter between 1 μm and 2.5 μm in one size bin, and provide a particle count for them. Once it has the particle number estimation for all the bins, it will then estimate the mass for each relevant metric. For instance, it will use all the size bins counts below 2.5 μm for estimating PM2.5. The number of size bins is normally higher than the number of actual mass sizes, and the discrimination capacity of the sensor will result in a better quality. For the final conversion, the algorithm has to make some assumptions (and normally the internal calculations are not disclosed), including but not limited to (see [^7] for further details):

* Particle shape (normally a sphere, but with some shape factors)
* Particle colour, and hence reflectivity index
* Particle chemical composition (and density), biological composition

### Limitations

Most of the low cost PM sensors that are currently on the market follow the same principle, and in fact, all of them are in one way or another aggregators of different types of suspended particles due to their inability to distinguish them because of the above mentioned assumptions. Hence data quality comes down to the following factors:

Number of particle sizes and differentiability between them: depending on the particle selectivity of the sensors, when compared to real monodisperse or polydisperse aerosols, the device will or will not be suitable for corrections [^6], [^7], as there might be bins that are falling in ambiguous size distributions.

Theoretical assumptions made by the algorithm designers: this is a consequence of the devices measurement principle, and that the particle count to mass calculations need to assume physical parameters of the particles in question. This leads to over or underestimations of the PM values and will need calibration in the field in almost all cases, since these assumptions are unknown to the end users.

Quality of the hardware, production deviations: due to their low cost, the manufacturer might not be able to test in house every unit, and inter-device deviations might lead to expensive individual calibrations in the field.

In addition, most sensors tend to only perform well on the low-mid range of the particle size spectrum (approximately 1 to 2um) due to technological limitations [7, 13], which are derived from the principle of measurement based on Mie’s Theory, and the relationship of the wavelength of the light source used with respect to the particle’s size [^7]. This is relevant for two reasons:

* The inability to capture ultrafine particles, since most sensors can count particles which size is larger than 0.3 μm.
* The underestimation/lack of correlation of coarse particles by almost all the devices [^11].

These are well known limitations that some manufacturers are tackling at the moment providing new solutions to the market [^12]. It is important to consider the impact of relative humidity on the readings, which leads to hygroscopic growth of the particles by absorption [^19]. It is generally accepted that this is not the case for temperature, which has been shown to have no effect on the readings [^20]. For the purposes of this deliverable, and the TwinAIR project, it is recommended to include a relative humidity sensor that can compensate for the effects on particle sizes. Following the recommendations of [6], the final sensor selection should not only provide particle numbers, in size distribution bins, but also show a proper distinction between different sizes in order to apply these corrections.

Finally, it is very important to remember that low cost particulate matter sensors are particle counters, which in case of polydisperse aerosols of unknown composition, the conversion between particle number to mass is not always attained properly, especially without other measurement methods in place [^7]. No matter which final selected sensor is used, there will always be an assumption made by the manufacturer that will never be fulfilled in every deployment scenario. If not only precision, but also accuracy is needed, then using the particle counts directly can provide one of the necessary pieces to derive the final mass, which will only be determined if the particle composition and density are known by other means (i.e. laboratory analysis of collected samples).

## Reference levels

!!! info "How to use these values"
    The values below are guidelines for **health protection**, defined as averages over a certain period (24 hours, a year). Short peaks above them are common (for instance, while cooking or near traffic), and what matters for health is the long-term exposure. Also keep in mind that low-cost PM sensors are indicative: they can over or underestimate the concentrations, specially with high relative humidity (see the [limitations](#limitations) above). The World Health Organization (WHO) highlights that there is **no level of PM without health effects**: the lower, the better.

The table below shows the WHO air quality guidelines [^21] and the European Union limit values that apply from 2030 [^22]:

| Pollutant | Averaging period | WHO guideline (2021) | EU limit value (2030) |
|:- |:- |:-: |:-: |
| PM2.5 | 24 hours | 15 µg/m3 | 25 µg/m3 (max. 18 days per year) |
| PM2.5 | Year | 5 µg/m3 | 10 µg/m3 |
| PM10 | 24 hours | 45 µg/m3 | 45 µg/m3 (max. 18 days per year) |
| PM10 | Year | 15 µg/m3 | 20 µg/m3 |

There are no guidelines for PM1 or PM4, although PM1 is included in PM2.5, and PM2.5 in PM10.

To classify the readings in levels, a common reference is the US EPA **Air Quality Index** (AQI) [^23], which uses 24-hour averages:

| Category | PM2.5 (µg/m3, 24h) | PM10 (µg/m3, 24h) | Meaning |
|:- |:-: |:-: |:- |
| Good | 0 – 9.0 | 0 – 54 | Little or no risk |
| Moderate | 9.1 – 35.4 | 55 – 154 | Acceptable. Some risk for unusually sensitive people |
| Unhealthy for sensitive groups | 35.5 – 55.4 | 155 – 254 | Children, older adults and people with heart or lung disease may be affected |
| Unhealthy | 55.5 – 125.4 | 255 – 354 | Some of the general public may experience health effects |
| Very unhealthy | 125.5 – 225.4 | 355 – 424 | Health alert: increased risk for everyone |
| Hazardous | > 225.5 | > 425 | Emergency conditions |

Europe also has its own [European Air Quality Index](https://airindex.eea.europa.eu/), which uses different bands, and many countries have their own national indices.

## Supported Sensors

Low cost PM sensors are normally built around the [light scattering](#light-scattering-sensors) principle. These sensors are an evolution of the Optical Particle Counters (OPCs), but with a lower cost, ranging from approximately USD 10 to USD 500 in some cases. Check the sensors supported on the Smart Citizen Kit below!

- [Plantower PMS5003](https://docs.smartcitizen.me/knowledge/air/pm/Plantower_PMS5003.md) (Field | air; Metric | pm; Connection | onboard): The PMS5003 is an Optical PM sensor by Plantower at a very low cost!
- [Sensirion SEN5X](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SEN5X.md) (Field | air; Metric | pm; Connection | onboard): The Sensirion SEN5X is a newer PM sensor with a very good performance for such low cost. Available in SCK2.2 and above!
- [Sensirion SPS30](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SPS30.md) (Field | air; Metric | pm; Connection | external): The Sensirion SPS30 is PM sensor with a very good performance for such low cost. Only supported for experimental setups!


## References

[^6]:
    Kuula, Joel, Timo Mäkelä, Minna Aurela, Kimmo Teinilä, Samu Varjonen, Óscar González, and Hilkka Timonen. “Laboratory Evaluation of Particle-Size Selectivity of Optical Low-Cost Particulate Matter Sensors.” Atmospheric Measurement Techniques 13, no. 5 (May 15, 2020): 2413–23. https://doi.org/10.5194/amt-13-2413-2020.
[^7]:
    Alfano, Brigida, Luigi Barretta, Antonio Del Giudice, Saverio De Vito, Girolamo Di Francia, Elena Esposito, Fabrizio Formisano, Ettore Massera, Maria Lucia Miglietta, and Tiziana Polichetti. “A Review of Low-Cost Particulate Matter Sensors from the Developers’ Perspectives.” Sensors 20, no. 23 (November 29, 2020): 6819. https://doi.org/10.3390/s20236819.
[^11]:
    Airparif Site (Accessed January 2023) https://airparif.asso.fr/en/node/110
[^12]:
    Piera Systems Intelligent Particle Sensors (Accessed January 2023): https://pierasystems.com/intelligent-particle-sensors/
[^19]:
    Di Antonio, Andrea, Olalekan Popoola, Bin Ouyang, John Saffell, and Roderic Jones. “Developing a Relative Humidity Correction for Low-Cost Sensors Measuring Ambient Particulate Matter.” Sensors 18, no. 9 (August 24, 2018): 2790. https://doi.org/10.3390/s18092790.
[^20]:
    Wang, Yang, Jiayu Li, He Jing, Qiang Zhang, Jingkun Jiang, and Pratim Biswas. “Laboratory Evaluation and Calibration of Three Low-Cost Particle Sensors for Particulate Matter Measurement.” Aerosol Science and Technology 49, no. 11 (November 2, 2015): 1063–77. https://doi.org/10.1080/02786826.2015.1100710.

[^21]:
    World Health Organization. “WHO Global Air Quality Guidelines: Particulate Matter (PM2.5 and PM10), Ozone, Nitrogen Dioxide, Sulfur Dioxide and Carbon Monoxide.” Geneva: World Health Organization, 2021. https://www.who.int/publications/i/item/9789240034228.
[^22]:
    Directive (EU) 2024/2881 of the European Parliament and of the Council of 23 October 2024 on ambient air quality and cleaner air for Europe. https://eur-lex.europa.eu/eli/dir/2024/2881/oj/eng.
[^23]:
    US Environmental Protection Agency. “AQI Basics” (PM breakpoints revised in 2024). https://www.airnow.gov/aqi/aqi-basics/.