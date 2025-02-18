---
card: true
name: Sensirion SCD30
field:
  - air
type:
  - external
target:
  - co2
feature_img: /assets/images/sensirion-scd30.png
feature_img_credit: "Seeed Studio"
excerpt: The SCD30 is a NDIR CO2 sensor by Sensirion. You can use it to measure CO2 in indoor spaces or for experiments where you need to know an accurate CO2 level.
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

## Usage

The easiest way to connect to the SCD30 to the SCK is by using the [SEEED Studio breakout](https://www.seeedstudio.com/Grove-CO2-Temperature-Humidity-Sensor-SCD30-p-2911.html), the sensor can be directly connected to the [Auxiliary connector](/hardware/boards/data-board#auxiliary-connector) on the data board, using a [4-wire grove cable](https://www.seeedstudio.com/cables-c-949.html).

If you have the SCD30 _rugged_ board by Sensirion: you can connect it using [4-wire grove to female header cables](https://www.seeedstudio.com/Grove-4-pin-Female-Jumper-to-Grove-4-pin-Conversion-Cable-5-PCs-per-PAck.html) as below:

## Working principle

Being a NDIR CO2 sensor, the SCD30 has a non dispersive element which is used to filter the light produced by an emitter with a _band-pass_ filter, allowing the infra-red (IR) wavelengths around 4.2μm to pass through [^22].

![](https://files.seeedstudio.com/products/101020634/3.png)
_Image credit: Seeed Studio_

CO2 molecules strongly absorb IR light in these wavelengths, so shining these through a gas sample, the CO2 concentration can be calculated from the proportion of light that is absorbed. Transmissive NDIR sensors typically feature an **IR emitter and an optical detector**, such as a photodiode, at opposite ends of a specially designed optical cavity. The optical detector measures the amount of IR light energy that is not absorbed by (i.e., transmitted through) the gas sample. The higher the CO2 concentration, the lower the light detected. A comparison between the measurement and a reference intensity at known CO2 concentration provides a direct way to calculate the CO2 concentration. This technique, though, requires **careful alignment of the emitter and detector**, and the **mechanical stresses** on the device can provoke wrong readings [^37].

## Usage and considerations

Sensirion provides a lot of information in their [applications note website](https://www.sensirion.com/en/download-center/carbon-dioxide-sensors-co2/co2-sensor-scd30/) for the SCD30 CO2. The datasheet can be found [here](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf).

If you are using the [SEEED Studio breakout](https://www.seeedstudio.com/Grove-CO2-Temperature-Humidity-Sensor-SCD30-p-2911.html), the sensor can be directly connected to the [Auxiliary connector](/hardware/boards/data-board#auxiliary-connector) on the data board, using a [4-wire grove cable](https://www.seeedstudio.com/cables-c-949.html).

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

!!! danger "Mechanical stress"
    Mechanical stress can lead to output deviations. Make sure to check [the assembly guidelines](https://sensirion.com/media/documents/6E0DB3D9/616534F2/Sensirion_CO2_Sensors_SCD30_Assembly_Guideline.pdf).

#### Operation modes

The sensor can operate in two modes for finding it's reference value. For both of these modes have customizable reading intervals that affect power consumption and response time. Finally, a temperature correction can be applied for electronics temperature build-up.

All the commands below are accessed by:

```
SCD30 CO2:
Options:
interval [2-1000 (seconds)]
autocal [on/off]
calfactor [400-2000 (ppm)]
caltemp [newTemp/off]
pressure
```

The procedure for setting up the sensor goes as follows (more information in [Low power mode AN](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Low_Power_Mode.pdf)):

![](/assets/images/sensirion-scd30-calibration-process.png)

#### Reading interval

The SCD30 can have different internal reading intervals, **independent from the SCK's interval**. A larger reading interval will reduce power consumption, but it will increase response time. By default, the reading interval is 2s. A good reading interval for reducing substantially power consumption is 15s. Below there is a table derived from the manufacturer's application notes that can guide in the reading interval setup process:

|Interval (s) |Consumption (mA) |Response time (t63 - s)|
|:- |:-:|:-:|
|2|19|20|
|15|6.5|72|
|30|6.5|145|

More information can be found in the [low power mode application note](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Low_Power_Mode.pdf).

To control this, and set it up to 15s:

```
control scd30 interval 15
```

To check the current interval:

```
control scd30 interval
```

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Probe type  			|NDIR with digital interface. Not waterproof without enclosure                  |
|Measurement range 	    |400 ppm – 10.000 ppm                                                           |
|Accuracy 			    |±(30 ppm + 3%)                                                                 |
|Reaction Time     		|63% in 20s                                                                     |
|Life expectancy     	|15 years                                                                       |
|Deployment type 		|indoor/outdoor (mostly indoor). Sensor provides auto compensation for drift.   |

### Calibration

The SCD30 can work in two main modes: ASC (automatic self-calibration) or FRC (forced re-calibration). They are both described in the [Field calibration for SCD30 AN](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Field_Calibration.pdf). Both modes shift the sensor baseline, only that FRC requires an external value, while ASC will adapt over time looking for "clean air" readings.

![](/assets/images/sensirion-scd30-calibration-modes.png)
_Image source: Sensirion_

!!! info "Drift"
    A typical SDC30 sensor drift per year is 50ppm and 80ppm maximal.

Additionally, there is a possibility to calibrate the temperature readings with an external sensor for correcting the SCD30 internal temperature corrections.

#### ASC

In SC, the SCD30 sensor by default is set in ASC mode. In this mode, the sensor looks for a clean environment over a 1-3 weeks period of time, for at **least 1h of clean air per day**.

!!! info "Manufacturer information"

    ASC assumes that the lowest CO2 concentration the SCD30 is exposed to corresponds to 400 ppm. The sensor estimates the most likely reading corresponding to this background level and identifies this as 400ppm. Using this reference value, the very same manipulation is triggered when applying FRC with the reference value of 400 ppm. Generating a reference value not corresponding to 400 ppm induces an erroneous update of the calibration and reduces sensor accuracy. To prevent a faulty self-calibration, ASC employs an internal self-consistency check: the algorithm will store the **seven most recent concentration minima** in volatile memory. Recalibration by the ASC algorithm will only be triggered when those seven successive minima of measured CO2 concentration are within ± 50 ppm. Also, minima need to be separated by at least 18 hours. If the seven successive minima span a range larger than ± 50 ppm, the ASC will not update the calibration. The buffer storing the minima has a depth of seven measurements, the most recent found minima will always replace the oldest minima (first-in first-out).

Some additional considerations:

- Do not unplug the sensors during the first week period of ASC
- Place it in a place where you know there is going to be a clean air composition during that period. Indoor environments is not always the best for this purpose
- Do not trust the initial values, as the self-calibration algorithm might have not found proper values yet
- The intention of ASC is manly to correct sensor drift due to aging
- There is no way for us to know wether the self-calibration process has satisfactory values. The only indication of the process being satisfactory or not is that there is a "step" in the readings when ASC kicks in (see [insights](#insights))

To turn it on:

```
control scd30 autocal on
```

Or off:

```
control scd30 autocal off
```

#### FRC

To activate FRC mode, we need to provide an external CO2 concentration in ppm. FRC calibration takes place inmediately, and it can be do multiple times at aribtrary intervals. Before applying it, run the sensor for at least 2 minutes in the desired environment.

!!! warning "Unstable environments"
    Take into account the response time of the sensor (with 2s it's t63=20s). If the environment in which you are taking readings it's too unstable, do not apply the FRC.

First, make sure both reference and SCD30 sensors are stable:

```
monitor scd30 co2
```

To stop the monitor, just press `Enter`.

Secondly, feed the external reading into the sensor. The value **needs to be between 400ppm and 2000ppm**. For instance, for a value of 450ppm:

```
SCK > control scd30 calfactor 450
SCD30 CO2: calfactor 450
Forced Recalibration Factor: 450
```

After applying this value, ASC will be disabled automatically and readings will be inmediately corrected to the new value.

!!! warning "Resetting the sensor"
    Take into account that if you ask for the `calfactor` after setting it up:

    ```
    SCK > control scd30 calfactor
    SCD30 CO2: calfactor
    Forced Recalibration Factor: 450
    ```

    However, **if you reset the sensor**, it will return `400ppm`. The FRC will remain active with the set value, but it will only visible through the `autocal` check:

    ```
    SCK > control scd30 calfactor
    SCD30 CO2: calfactor
    Forced Recalibration Factor: 400
    SCK > control scd30 autocal
    SCD30 CO2: autocal
    Auto Self Calibration: off
    ```

#### Temperature correction

An external temperature sensor can also be used to compensate the self-heating of the SCD30 board. A temperature correction can be supplied with the `caltemp` command.

First, read the temperature from the SCD30, to verify it's lower than the reference sensor.

```
read scd30 temp
```

If it is, then feed the external temperature value (for instance, 15 ºC):

```
control scd30 caltemp 15
```

After this, the sensor will stabilise and converge to the new temperature correction reading after a while.

To turn off the temperature compensation:

```
control scd30 caltemp off
```

### Insights

Here are some insights:

- It is recommended to use FRC after assembly with reference data
- ASC can be used instead of performing FRC after assembly but leaves the user of the device with sensor outputs that might be out of specification for a prolonged time
- FRC after assembly corrects deviations caused by mechanical stress during handling and assembly. ASC will then take care of sensor drift due to aging. Only exception, applications where ASC conditions can’t be met

Here is how to identify ASC has kicked in:

![](/assets/images/sensirion-scd30-asc.png)

### Calibration process

Normally, we perform tests of sensors of larger units (we do not have reference sensor data). This allows us to have significantly large sensor data and be able to correct sensor deviations better. In this circumstances, the process is as follows:

- Place sensors in well ventilated environment for at least 2 weeks and **ASC enabled**
- Identify sensors with ASC performed and valid
- Identify sensor baselines of all sensors
- Determine most likely sensor value of the population in sensor baseline readings. Use a normal distribution of the sensors after performing ASC
- Feed an offset to all the sensors, ASC corrected and not, by introducing a real value via FRC
- Test if new spread is valid with respect to sensor accuracy (± 30 ppm)
- Enable ASC for it to automatically correct drift
- Mark sensor as calibrated

For those cases in which there is not a significant amount of sensors to evaluate, or a refencence unit, **ASC is recommended**, by leaving the sensor in a very well ventilated area (i.e. outdoors). However, **there is a risk for the sensor to never achieve the conditions for ASC to work**. In this case, the recommendation is to post-process the data and extract a baseline, considering this baseline is 400ppm.


### Limitations

NDIR CO2 sensors tend to show drift in the data signal over time, and have interferences by humidity [^14], [^23]. This can lead to invalid data, jumps in the signal, and other artefacts that need to be corrected. In the particular case of the SCD30, these limitations are addressed by including a temperature and humidity sensor that can correct by these effects. The signal drift over time is corrected by an onboard algorithm, known as [automatic-self calibration](#asc). This type of algorithm is commonly used to detect clean instances of air and correct the readings, assuming that baseline levels are constant over time [^24]. After several reviews of sensors, we have seen that this type of technology is currently providing good results and evolving rapidly [^25], [^26].

Finally, **mechanical stress** can make these sensors yield invalid values, due to the misalignment between the emitter and the photodetector. In the case of mobile devices, [photoacoustic NDIR sensors](/knowledge/air/co2/Sensirion_SCD4X/) would be more suitable, with the further advantage of their smaller size.

## Resources

- [Official datasheet](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf)
- [Seeed Studio Guide](https://wiki.seeedstudio.com/Grove-CO2_Temperature_Humidity_Sensor-SCD30/)

### References

[^14]:
    Clements, A., S. Lung, A. Arfire, AND A. Polidori. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition: Evaluation Activities. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition. World Meteorological Organization, Geneva, Switzerland, , NA, (2020).
[^22]:
    Dinh, Trieu-Vuong, In-Young Choi, Youn-Suk Son, and Jo-Chun Kim. “A Review on Non-Dispersive Infrared Gas Sensors: Improvement of Sensor Detection Limit and Interference Correction.” Sensors and Actuators B: Chemical 231 (August 2016): 529–38. https://doi.org/10.1016/j.snb.2016.03.040.
[^23]:
    Müller, Michael, Peter Graf, Jonas Meyer, Anastasia Pentina, Dominik Brunner, Fernando Perez-Cruz, Christoph Hüglin, and Lukas Emmenegger. “Integration and Calibration of Non-Dispersive Infrared (NDIR) CO2 Low-Cost Sensors and Their Operation in a Sensor Network Covering Switzerland.” Atmospheric Measurement Techniques 13, no. 7 (July 15, 2020): 3815–34. https://doi.org/10.5194/amt-13-3815-2020.
[^24]:
    Sensirion SCD30 Field Calibration Application Note (Accessed January 2023) https://sensirion.com/media/documents/33C09C07/620638B8/Sensirion_SCD30_Field_Calibration.pdf
[^25]:
    Demanega, Ingrid, Igor Mujan, Brett C. Singer, Aleksandar S. Anđelković, Francesco Babich, and Dusan Licina. “Performance Assessment of Low-Cost Environmental Monitors and Single Sensors under Variable Indoor Air Quality and Thermal Conditions.” Building and Environment 187 (January 2021): 107415. https://doi.org/10.1016/j.buildenv.2020.107415.
[^26]:
    Zheng, Hailin, Vinayak Krishnan, Shalika Walker, Marcel Loomans, and Wim Zeiler. “Laboratory Evaluation of Low-Cost Air Quality Monitors and Single Sensors for Monitoring Typical Indoor Emission Events in Dutch Daycare Centers.” Environment International 166 (August 2022): 107372. https://doi.org/10.1016/j.envint.2022.107372.
[^37]:
    Popa, Daniel, and Florin Udrea. “Towards Integrated Mid-Infrared Gas Sensors.” Sensors 19, no. 9 (May 4, 2019): 2076. https://doi.org/10.3390/s19092076.