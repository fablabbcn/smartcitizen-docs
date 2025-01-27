---
hide:
    -toc
---

# Particulate Matter Measurements

<!-- TODO - Proofread + check on links -->

Particulate Matter (or PM for short) refers to mixture of solid particles and liquid droplets that we can find in the air. Some particles, such as dust, dirt, soot, or smoke, are large or dark enough to be seen with the naked eye, but others can reach far inside our respiratory system.

<!-- TODO - Talk about PM sizes -->

Generally, the type of sensor that are used to measure suspended particles in air employ a light beam in the form of laser beams or infrared (IR) leds and a light detector. When using laser beams, it is most commonly set to one side (often 90°) of the source beam, to avoid reflections of the light source itself which could induce noise in the readings [^7]. The amount of particles per unit of volume is then a function of the light reflected into the detector and the mass is a calculation derived from this density, assuming certain properties of the particles, such as shape, colour and reflectivity, among others [^7].

An onboard microcontroller is in charge of taking readings from the sensing element and counts how many particles are passing in front of the light detector. The sensor element can differentiate between different particle sizes, and group them in size bins according to the results of an onboard, proprietary algorithm. In other words, this algorithm will group, for instance, the particles that have a diameter between 1 μm and 2.5 μm in one size bin, and provide a particle count for them. Once it has the particle number estimation for all the bins, it will then estimate the mass for each relevant metric. For instance, it will use all the size bins counts below 2.5 μm for estimating PM2.5. The number of size bins is normally higher than the number of actual mass sizes, and the discrimination capacity of the sensor will result in a better quality. For the final conversion, the algorithm has to make some assumptions (and normally the internal calculations are not disclosed), including but not limited to (see [^7] for further details):

* Particle shape (normally a sphere, but with some shape factors)
* Particle colour, and hence reflectivity index
* Particle chemical composition (and density), biological composition

## Limitations

Most of the low cost PM sensors that are currently on the market follow the same principle, and in fact, all of them are in one way or another aggregators of different types of suspended particles due to their inability to distinguish them because of the above mentioned assumptions. Hence data quality comes down to the following factors:

Number of particle sizes and differentiability between them: depending on the particle selectivity of the sensors, when compared to real monodisperse or polydisperse aerosols, the device will or will not be suitable for corrections [^6], [^7], as there might be bins that are falling in ambiguous size distributions.
Theoretical assumptions made by the algorithm designers: this is a consequence of the devices measurement principle, and that the particle count to mass calculations need to assume physical parameters of the particles in question. This leads to over or underestimations of the PM values and will need calibration in the field in almost all cases, since these assumptions are unknown to the end users.
Quality of the hardware, production deviations: due to their low cost, the manufacturer might not be able to test in house every unit, and inter-device deviations might lead to expensive individual calibrations in the field.
In addition, most sensors tend to only perform well on the low-mid range of the particle size spectrum (approximately 1 to 2um) due to technological limitations [7, 13], which are derived from the principle of measurement based on Mie’s Theory, and the relationship of the wavelength of the light source used with respect to the particle’s size [^7]. This is relevant for two reasons:
The inability to capture ultrafine particles, since most sensors can count particles which size is larger than 0.3 μm.
The underestimation/lack of correlation of coarse particles by almost all the devices [^11].

These are well known limitations that some manufacturers are tackling at the moment providing new solutions to the market [^12]. It is important to consider the impact of relative humidity on the readings, which leads to hygroscopic growth of the particles by absorption [^19]. It is generally accepted that this is not the case for temperature, which has been shown to have no effect on the readings [^20]. For the purposes of this deliverable, and the TwinAIR project, it is recommended to include a relative humidity sensor that can compensate for the effects on particle sizes. Following the recommendations of [6], the final sensor selection should not only provide particle numbers, in size distribution bins, but also show a proper distinction between different sizes in order to apply these corrections.
Finally, it is very important to remember that low cost particulate matter sensors are particle counters, which in case of polydisperse aerosols of unknown composition, the conversion between particle number to mass is not always attained properly, especially without other measurement methods in place [^7]. No matter which final selected sensor is used, there will always be an assumption made by the manufacturer that will never be fulfilled in every deployment scenario. If not only precision, but also accuracy is needed, then using the particle counts directly can provide one of the necessary pieces to derive the final mass, which will only be determined if the particle composition and density are known by other means (i.e. laboratory analysis of collected samples).

## Supported Sensors

Low cost PM sensors are normally built around the [light scattering](#light-scattering-sensors) principle. These sensors are an evolution of the Optical Particle Counters (OPCs), but with a lower cost, ranging from approximately USD 10 to USD 500 in some cases. Check the sensors supported on the Smart Citizen Kit below!

{{ insert_cards(type="sensor", filter="target", value=["pm"])}}

## References

{{ insert_references('docs/includes/references.md')}}