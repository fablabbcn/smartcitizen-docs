PM Sensors
==============

## Working principle

![](https://i.imgur.com/kDxIl26.png)

The PM sensors available in the Smart Citizen Kit (one sensor per Kit) and the Smart Citizen Station (two sensors per Station), are the Plantower PMS5003 sensor. The PMS5003 is a [nephelometer](https://en.wikipedia.org/wiki/Nephelometer), and this type of measures suspended particulates by employing a light beam and a light detector set to one side (often 90°) of the source beam. Particle density is then a function of the light reflected into the detector and the particle mass is a calculation derived from this density, assuming certain properties of the particles, such as shape, color and reflectivity, among others. 

![](https://i.imgur.com/aNlzRba.png)

What the sensor does, is to analyse the readings from the sensing element and count how many particles are there, for different particles sizes, or bins. This means that the sensor will group, for instance, the particles that have a diameter between 1um and 2.5um in one bucket, and count them. Once it has the **particle number** calculated for all the buckets, it **estimates** the **Particle Mass** for PM1 (particles with a diameter below 1um), PM2.5 (particles with a diameter below 2.5um) and PM10 (particles with a diameter below 10um). For estimating this, it makes quite a few assumptions, such as:

- Particle shape (normally a sphere, but with some shape factors)
- Particle color, and hence reflectivity index
- Particle composition, and hence density

The internal calculations are unknown to us, but we have reverse engineered the readings and double checked the calculations it makes, [assuming some particle characteristics](https://doi.org/10.1016/j.envpol.2018.11.065), and they match quite well. Some more work is currently being done to better understand this, and to try to correct from some humidity effect (see below):

![](https://i.imgur.com/YMohosZ.png)

## Sensor considerations

!!! info "Sources"
    Have a read to the [Datasheet](https://cdn-shop.adafruit.com/product-files/3686/plantower-pms5003-manual_v2-3.pdf)

These sensors are used in some other projects, such as [Purple Air](https://www2.purpleair.com/) and [have been evaluated by the South Coast AQMD](http://www.aqmd.gov/docs/default-source/aq-spec/field-evaluations/purpleair---field-evaluation.pd) (Air Quality Management District), USA, giving results for PM10 and PM2.5 with high correlation results with respect to reference equipment (R2 > 0.9 in most cases). Other authors also show strong results and recommend the usage of these sensors, although in some measurement conditions (like specific types of particles) they perform better than in others (read the academic article [here](https://doi.org/10.1016/j.envpol.2018.11.065)). Similar sensors are used in the [Luftdaten project](https://luftdaten.info/en/home-en/) (with a [SDS011](https://inovafitness.de/produkt/sds011/) in this case).

Relative humidity affects this type of sensor, since particles can absorb water and grow in size, hence modifying the fractions and the calculated mass. Additionally, particle's chemistry can affect these assumed properties, and these assumptions may not be usable in every type of environment. However, a relative humidity correction is being tested, correcting size distribution based on particle higroscopicity.

!!! warning "Dusty environments"
    The sensor might get clogged in a very dusty environment (like a workshop) and might need some periodic cleaning. It is safe to use a vaccum cleaner to do so, but be careful not to damage the light sensor, the laser emitter or the fan during the process. 

### Powering the sensor

Make sure that you power the Smart Citizen Kit with a _good enough USB cable_ and with an adaptor that can provide at least 1A. We have found some issues when powering the sensor with a thin cable, or from a weak power source, like a screen.






