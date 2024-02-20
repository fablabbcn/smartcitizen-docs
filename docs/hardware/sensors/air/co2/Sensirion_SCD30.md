---
name: Sensirion SCD30
field: air
type: external
target: co2
feature_img: /assets/images/scd30-seeed.png
status: stable
versions:
    hardware: 2.1+
    firmware: 0.9.8+
excerpt: The [SCD30](https://www.sensirion.com/products/catalog/SCD30) is a **NDIR CO2** sensor by [Sensirion](https://sensirion.com/). You can use it to measure CO2 in indoor spaces or for experiments where you need to know an accurate CO2 level.
---

<!-- TODO - Proofread + check on links -->
# Sensirion SCD30

{{ page.meta.excerpt }}

![]({{page.meta.feature_img}})

<!-- TODO - Make this chunk reproducible over other pages -->
!!! info "Version support"
    It is supported in the Smart Citizen Kit `{{ page.meta.versions.hardware }}`, and firmware version `{{ page.meta.versions.firmware }}`. This is an {{ page.meta.type }} sensor, available in various formats. Check the [usage](#usage) section below!

## Usage

<!-- TODO - Insert versions -->

The easiest way to connect to the SCD30 to the SCK is by using the [SEEED Studio breakout](https://www.seeedstudio.com/Grove-CO2-Temperature-Humidity-Sensor-SCD30-p-2911.html), the sensor can be directly connected to the [Auxiliary connector](/hardware/Auxiliary Connector/) on the data board, using a [4-wire grove cable](https://www.seeedstudio.com/cables-c-949.html).

<!-- TODO - Image showing how to connect it to the kit -->

If you have the SCD30 _rugged_ board by Sensirion: you can connect it using [4-wire grove to female header cables](https://www.seeedstudio.com/Grove-4-pin-Female-Jumper-to-Grove-4-pin-Conversion-Cable-5-PCs-per-PAck.html) as below:

<!-- TODO - Image showing how to connect it to the kit -->

!!! warning "Don't miss the advanced usage guide"
    We have prepared an advanced usage and calibration guide for the SCD30. Check it out [here](/guides/calibration/Sensirion SCD30/). More references [below](#references)!

## Working principle

Being a NDIR CO2 sensor, the SCD30 has a non dispersive element which is used to filter the light produced by an emitter with a _band-pass_ filter, allowing the infra-red (IR) wavelengths around 4.2μm to pass through [^22].

![](https://files.seeedstudio.com/products/101020634/3.png)
_Image credit: Seeed Studio_
<!-- TODO: figcaption style -->

CO2 molecules strongly absorb IR light in these wavelengths, so shining these through a gas sample, the CO2 concentration can be calculated from the proportion of light that is absorbed. Transmissive NDIR sensors typically feature an **IR emitter and an optical detector**, such as a photodiode, at opposite ends of a specially designed optical cavity. The optical detector measures the amount of IR light energy that is not absorbed by (i.e., transmitted through) the gas sample. The higher the CO2 concentration, the lower the light detected. A comparison between the measurement and a reference intensity at known CO2 concentration provides a direct way to calculate the CO2 concentration. This technique, though, requires **careful alignment of the emitter and detector**, and the **mechanical stresses** on the device can provoke wrong readings [^37].

<!-- TODO - Add references -->

## Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Probe type  			|NDIR with digital interface. Not waterproof without enclosure                  |
|Measurement range 	    |400 ppm – 10.000 ppm                                                           |
|Accuracy 			    |±(30 ppm + 3%)                                                                 |
|Reaction Time     		|63% in 20s                                                                     |
|Life expectancy     	|15 years                                                                       |
|Deployment type 		|indoor/outdoor (mostly indoor). Sensor provides auto compensation for drift.   |

### Limitations

NDIR CO2 sensors tend to show drift in the data signal over time, and have interferences by humidity [^14], [^23]. This can lead to invalid data, jumps in the signal, and other artefacts that need to be corrected. In the particular case of the SCD30, these limitations are addressed by including a temperature and humidity sensor that can correct by these effects. The signal drift over time is corrected by an onboard algorithm, known as [automatic-shelf calibration](/guides/calibration/Sensirion SCD30/#asc). This type of algorithm is commonly used to detect clean instances of air and correct the readings, assuming that baseline levels are constant over time [^24]. After several reviews of sensors, we have seen that this type of technology is currently providing good results and evolving rapidly [^25], [^26].

Finally, **mechanical stress** can make these sensors yield invalid values, due to the misalignment between the emitter and the photodetector. In the case of mobile devices, [photoacoustic NDIR sensors](/hardware/sensors/air/co2/Sensirion_SCD4X/) would be more suitable, with the further advantage of their smaller size.

## Resources

Make sure to check our [calibration guide](/Guides/calibration/SCD30 CO2 sensor/) for this sensor. There are plenty of advanced settings already available.

### External documents

- [Official datasheet](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf)
- [Seeed Studio Guide](https://wiki.seeedstudio.com/Grove-CO2_Temperature_Humidity_Sensor-SCD30/)

## References


