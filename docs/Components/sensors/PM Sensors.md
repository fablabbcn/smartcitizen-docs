PM Sensors
==============

## Working principle

<a data-flickr-embed="true"  title="SCK 2.1 Particle Sensor"><img src="https://live.staticflickr.com/65535/47950939936_8942068512_h.jpg" alt="SCK 2.1 Particle Sensor"></a>

The PM sensors available in the Smart Citizen Kit (one sensor per Kit) and the Smart Citizen Station (two sensors per Station), are the Plantower PMS5003 sensor. The PMS5003 is a [nephelometer](https://en.wikipedia.org/wiki/Nephelometer), and this type of measures suspended particulates by employing a light beam and a light detector set to one side (often 90°) of the source beam. Particle density is then a function of the light reflected into the detector and the particle mass is a calculation derived from this density, assuming certain properties of the particles, such as shape, color and reflectivity, among others. 

<div style="text-align: center;">
<img src="https://i.imgur.com/aNlzRba.png">
</div>

What the sensor does, is to analyse the readings from the sensing element and count how many particles are there, for different particles sizes, or bins. This means that the sensor will group, for instance, the particles that have a diameter between 1um and 2.5um in one bucket, and count them. Once it has the **particle number** calculated for all the buckets, it **estimates** the **Particle Mass** for PM1 (particles with a diameter below 1um), PM2.5 (particles with a diameter below 2.5um) and PM10 (particles with a diameter below 10um). For estimating this, it makes quite a few assumptions (the internal calculations are unknown to us), such as:

- Particle shape (normally a sphere, but with some shape factors)
- Particle color, and hence reflectivity index
- Particle composition, and hence density

!!! info "The performance of the sensor"
    We have been part of a study in which we characterised a few low cost sensors. You can check it in [here](https://doi.org/10.5194/amt-2019-422)

## Sensor considerations

!!! info "Sources"
    Have a read to the [Datasheet](https://cdn-shop.adafruit.com/product-files/3686/plantower-pms5003-manual_v2-3.pdf)

These sensors are used in some other projects, such as [Purple Air](https://www2.purpleair.com/) and have been evaluated in [laboratory](https://doi.org/10.5194/amt-2019-422) by the [Finnish Meteorological Institute - FMI](https://en.ilmatieteenlaitos.fi/) and in outdoor conditions the [South Coast AQMD](http://www.aqmd.gov/docs/default-source/aq-spec/field-evaluations/purpleair---field-evaluation.pd) (Air Quality Management District), USA. The study by the FMI did not yield good results for this sensor (specially in PM10), but given the cost we still think is a good citizen awareness sensor and that can be used for certain studies. The AQMD study shows better results for PM10 and PM2.5 with high correlation results with respect to reference equipment (R2 > 0.9 in most cases), although we are not aware of actual testing conditions, or the reference equipment calibration. Other authors also show good results and recommend the usage of these sensors, although in some measurement conditions (like specific types of particles) they perform better, which makes sense given the assumptions mentioned above (read the academic article [here](https://doi.org/10.1016/j.envpol.2018.11.065)). Similar sensors are used in the [Luftdaten project](https://luftdaten.info/en/home-en/) (with a [SDS011](https://inovafitness.de/produkt/sds011/) in this case).

Relative humidity affects this type of sensor, since particles can absorb water and grow in size, hence modifying the fractions and the calculated mass. Additionally, particle's chemistry can affect these assumed properties, and these assumptions may not be usable in every type of environment. However, a relative humidity correction is being tested, correcting size distribution based on particle higroscopicity.

!!! warning "Dusty environments"
    The sensor might get clogged in a very dusty environment (like a workshop) and might need some periodic cleaning. It is safe to use a vaccum cleaner to do so, but be careful not to damage the light sensor, the laser emitter or the fan during the process.

### Sensor operation

The sensor is operated in a _one-shot mode_: turning on for 15s the sensor, everytime a reading is needed. This is done this way in order to save battery. 

!!! info "About one-shot mode"
    An study of this was carried out to validate the measurements and can be found [here](/assets/notes/one-shot-pmsx003-analysis.pdf)

From the long term deployment point of view, the one-shot mode has not been found to have any effect of this in the performance of the sensor, other than normal accumulation of dust in the inner channels of the PMS. This has been seen in continuous mode as well, and it’s probably more due to the construction of the sensor itself.

!!! info "Working in pairs"
    In the Smart Citizen Station, the particle sensors measurements are delivered as averages of the two sensors with periodic validity checks. Please make sure the sensor has reliable energy supply if you will use these sensors permanently.

### Powering the sensor

Make sure that you power the Smart Citizen Kit with a _good enough USB cable_ and with an adaptor that can provide at least 1A. We have found some issues when powering the sensor with a thin cable, or from a weak power source, like a screen.





