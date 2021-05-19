# Sensirion SCD30 CO2 sensor

!!! warning "WIP"
    This guide is a WIP.

This guide will show the calibration process and particularities for using the Sensirion SCD30 CO2 sensor with the Smart Citizen Kit.

## Manufacturer information

Sensirion provides a lot of information in their [applications note website](https://www.sensirion.com/en/download-center/carbon-dioxide-sensors-co2/co2-sensor-scd30/) for the SCD30 CO2. The datasheet can be found [here](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf).

## Setup

If you are using the [SEEED Studio breakout](https://www.seeedstudio.com/Grove-CO2-Temperature-Humidity-Sensor-SCD30-p-2911.html), the sensor can be directly connected to the [Auxiliary connector](/Components/Auxiliary Connector) on the data board, using a [4-wire grove cable](https://www.seeedstudio.com/cables-c-949.html). 

![](/assets/images/scd30_seeed.png)

Sensor can operate in two modes for finding it's reference value. For both of these modes have customizable reading intervals that affect power consumption and response time. Finally, a temperature correction can be applied for electronics temperature build-up.

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

### Reading interval

The SCD30 can have different internal reading intervals, **independent from the SCK's interval**. A larger reading interval will reduce power consumption, but it will increase response time. By default, the reading interval is 2s. A good reading interval for reducing substantially power consumption is 15s.

To control this, and set it up to 15s:

```
control scd30 interval 15
```

To check the current interval:

```
control scd30 interval
```

### Calibration

The SCD30 can work in two main modes: ASC (automatic self-calibration) or FRC (forced re-calibration). They are both described in the [Field calibration for SCD30 AN](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/9.5_CO2/Sensirion_CO2_Sensors_SCD30_Field_Calibration.pdf).

![](/assets/images/scd30_calibration_modes.png)
_Image source: Sensirion_

Additionally, there is a possibility to calibrate the temperature readings with an external sensor for correcting the SCD30 internal temperature corrections.

#### ASC

Sensor by default is set in ASC mode. In this mode, the sensor looks for a clean environment over a 1-3 weeks period of time. Considerations:

- Do not unplug the sensors during this period
- Place it in a place where you know there is going to be a clean air composition during that period. Indoor environments is not always the best for this purpose
- Do not trust the initial values, as the self-calibration algorithm might have not found proper values yet
- There is no way for us to know wether the self-calibration process has satisfactory values. Our understanding is that the internal SCD30 algorithm converges after a period of time, but there is no indication whatsoever of the quality of the readings (see [insights section](#Insights) for more information)

To turn it on:

```
control scd30 autocal on
```

Or off:

```
control scd30 autocal off
```

#### FRC

To activate FRC mode, we need to provide an external CO2 concentration in ppm. 

First, make sure both reference and SCD30 sensors are stable:

```
monitor scd30 co2
```

To stop the monitor, just press `Enter`.

Secondly, feed the external reading into the sensor. For instance, for a value of 450ppm:

```
control scd30 calfactor 450
```

!!! warning "Reference value range"
    The reference value needs to be between 400ppm and 2000ppm

After applying this value, ASC will be disabled automatically. The readings will take a bit of time to scale to the new offset.

#### Temperature correction

An external temperature sensor can also be used to compensate the self-heating of the SCD30 board. A temperature correction can be supplied with the `caltemp` command.

To feed an external temperature value (for instance, 15 ºC):

```
control scd30 caltemp 15
```

After this, the sensor will stabilise and converge to the new temperature correction reading after a while.

To turn off the temperature compensation:

```
control scd30 caltemp off
```

## Insights

This section is WIP.
