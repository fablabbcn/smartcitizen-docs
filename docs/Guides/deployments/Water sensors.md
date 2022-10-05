# Water sensors

<img src="https://live.staticflickr.com/65535/51126012000_ef69edea6b_k.jpg" alt="Water Station - Patí Científic">

## Getting around the box

Here is a first overview of the box:

![](/assets/images/water-annotated.jpeg)

## Setup

!!! danger "Only if you bought them separately"
    This guide describes the setup procedure of the Atlas Scientific probes in case you bought them separately. If you have a [Water Station](/Components/Soil and water/#water-station), you don't need to do this.

### Manually switching circuits to I2C mode

If the drivers are new normally they come configured in UART mode so we need to change them to I2C mode.

1. Remove circuit from Tentacle shield.
2. Put the circuit into a breadboard.
3. For **PH**, **DO**, **ORP** and **EC**: Short the `PGND` pin to the `TX` pin using a jumper wire.
4. For **RTD** (temperature): Short the `PRB` pin to the `TX` pin using a jumper wire.
5. Power the device (connecting `GND` and `VCC`)
6. Wait for LED to change from green to blue (UART→I2C) or from blue to green (I2C→>UART).
7. Remove the jumper wire from the `PGND` (or `PRB` respectively) pin to the `TX` pin (Do this **before removing power!**).
8. Remove power (`VCC`).
9. Apply power (`VCC`).
10. The device is now in the new mode (repeat all steps to switch back to previous mode).

!!! warning "Official documentation"
    [Atlas Doc](https://www.whiteboxes.ch/tentacle/#tentacle-t3)

### Connection to Smartcitizen Kit

![](https://i.imgur.com/Dc6Us2F.png)

After connecting the [Tentacle 3](https://atlas-scientific.com/carrier-boards/whitebox-labs-tentacle-t3/) to the SCK power your kit and if youre connected to the shell the autodetecition message should look similar to this (depending on the connected drivers and probes):

```
Urban board detected
Enable Atlas Temperature
Enable Atlas PH
Enable Atlas Conductivity
Enable Atlas Specific gravity
...
```

!!! warning "Sensor calibration"
    Make sure to follow our sensor calibration guide for the [water sensors](/Guides/calibration/Water sensors/).

## Preparing the probes

[Atlas Scientific](https://atlas-scientific.com) has great documents on how to use their probes, and maintain them (all the images below are theirs). Many other probes by other manufacturers will have the same issues, as they are based on the similar working principles. Below we compile some guidelines specific to the sensors. Make sure you also follow the instructions on [how to calibrate them](/Guides/calibration/Water sensors/).

### All probes

Most of the probes will generate potassium chloride (KCl) crystals that are fully harmless. Make sure you clean them with distilled water before use.

![](/assets/images/kcl-creep.png)

!!! warning ""
    Once you are done using them, the probes that have a protective electrolyte solution (pH and ORP) will need to be put back in.

### Dissolved Oxygen

The dissolved oxygen probe needs to be actively maintained. The [datasheet](https://files.atlas-scientific.com/Mini_DO_probe.pdf) has a good information on how to maintain and clean the probe. Here is a small brief:

* When you open the probe the first time, make sure you only open the rubber cap, and **not any sensor component such as the membrane cap**

![](/assets/images/open-precautions.png)

* The sensor has an electrolyte solution inside to support the chemical reaction in the electrodes. **This solution depletes over time, as the sensor is used** and it will generate a solid residue that needs to be cleaned periodically (roughly every 6 months for the Mini DO probe, but better to check)

![](/assets/images/unscrew-precautions.png)

![](/assets/images/probe-refill.png)

* You can recondition the sensor with a small file and remove all Zinc Oxyde. Make sure that the probe membrane is cleaned with a **very soft** brush both inside and outside. The membrane can be replaced if damaged. Make sure it is in good conditions because it will otherwise leak the electrolyte solution and the sensor will work erratically.

![](/assets/images/probe-recondition.png)

![](/assets/images/membrane-cleaning.png)

!!! warning "First time use? Do it"
    Even it the sensor is brand new, we recommend you follow this process to avoid issues.

### pH and ORP

No particular consideration for these probes, other than they are very delicate:

![](/assets/images/education/es/atlas_ph_cuidado.png)

## Maintenance

Make sure that the sensors are cleaned frequently, specially if deployed on the field.
In some cases, sensors will be affected by [biofouling](https://en.wikipedia.org/wiki/Biofouling) and they will need more or less often cleanup - **in some cases weekly!**

<p><a href="https://commons.wikimedia.org/wiki/File:Zebra_mussel_GLERL_4.jpg#/media/File:Zebra_mussel_GLERL_4.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/3/3d/Zebra_mussel_GLERL_4.jpg" alt="Zebra mussel GLERL 4.jpg"></a><br>Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=2143950">Link</a></p>



