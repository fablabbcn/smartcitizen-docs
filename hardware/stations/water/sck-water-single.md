<!-- Source: https://docs.smartcitizen.me/hardware/stations/water/sck-water-single/ -->

# One-Sensor Water Station

**Grade**: _intermediate_

The One-Sensor Water Station is meant to measure one physico-chemical parameter at a time. Choose from pH, Temperature, Dissolved Oxygen, Conductivity or ORP.

![](https://docs.smartcitizen.me/assets/images/sck-water-single-feature.jpg){.banner-box}
***One-Sensor pH Water Station***{.image-credit-banner-box}

## Measurements

Measurements on the water stations can be 1 of the ones below:

| Measurement      | Units    | Sensor                        |
| :-:              | :-:      | :-:                           |
| Temperature      | ºC       | Atlas PT-1000, PT-100 probes  |
| pH               | -        | Atlas pH probes               |
| Conductivity     | uS/cm    | Atlas Conductivity probes     |
| Dissolved Oxygen | mg/l     | Atlas DO probes               |
| ORP              | mV       | Atlas ORP probes              |

In the image at the top of the page you can see an example of a One-Sensor Water Station that measures pH, and below you can see another that measures temperature.

![](https://docs.smartcitizen.me/assets/images/sck-water-single.jpg){.black-box}
***One-Sensor Temperature Water Station***

## Technical specifications

### Dimensions and weight

| Version                   | Dimensions | Weight |
| :-:                       | :-         | :-     |
| Main Box                  |            |        |
| Probe support             |            |        |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository](https://enclosures.smartcitizen.me).


### Power

Currently, the Smart Citizen Air Quality Stations have only been tested with an [external power supply](https://docs.smartcitizen.me/hardware/addons/power-supply.md) (230VAC to 5VDC), with a small battery for backup during power brownouts. Due to the number of sensors, and depending on the configuration the solution is normally not meant for long term deployment with just battery power. For detailed specifications of the power supply, visit the [power supply section](https://docs.smartcitizen.me/hardware/addons/power-supply.md).

| Power        |                                                                  |
| :-:          | :-                                                               |
| DC Voltage   | 5V                                                               |
| DC Current   | 2A _recommended_                                                 |
| AC Voltage   | 230V  _into the [Power Supply](https://docs.smartcitizen.me/hardware/addons/power-supply.md)_   |
| AC Current   | <0.16A _into the [Power Supply](https://docs.smartcitizen.me/hardware/addons/power-supply.md)_  |

!!! warning "Battery or solar operation?"
    The Station currently supports battery operation only for short periods of time (<2d days). Depending on the location, [solar power](https://docs.smartcitizen.me/hardware/addons/solar-panel.md) might be available, but we do not recommend it unless you are willing to _experiment_.

### Connectivity

Similar to the [Smart Citizen Kit](https://docs.smartcitizen.me/hardware/kit.md) if you want to have your data online, the Smart Citizen Air Quality Station requires a Wi-Fi connection to report data to the [platform](https://docs.smartcitizen.me/data/data-platform.md). If not, the unit can also store data locally on its onboard sd-card. Read more about the [operation modes](https://docs.smartcitizen.me/hardware/kit.md#operation-modes) and the [supported networks](https://docs.smartcitizen.me/_FAQ.md#what-networks-does-it-support).


## Preparing the probes

[Atlas Scientific](https://atlas-scientific.com) has great documents on how to use their probes, and maintain them (all the images below are theirs). Many other probes by other manufacturers will have the same issues, as they are based on the similar working principles. Below we compile some guidelines specific to the sensors. Make sure you also follow the instructions on [how to calibrate them as specified for each probe](https://docs.smartcitizen.me/knowledge/soil-water.md).

### All probes

Most of the probes will generate potassium chloride (KCl) crystals that are fully harmless. Make sure you clean them with distilled water before use.

![](https://docs.smartcitizen.me/assets/images/water/kcl-creep.png)
_Image Credit: **Atlas Scientific**

!!! warning ""
    Once you are done using them, the probes that have a protective electrolyte solution (pH and ORP) will need to be put back in.

### Dissolved Oxygen

The dissolved oxygen probe needs to be actively maintained. The [datasheet](https://files.atlas-scientific.com/Mini_DO_probe.pdf) has a good information on how to maintain and clean the probe. Here is a small brief:

* When you open the probe the first time, make sure you only open the rubber cap, and **not any sensor component such as the membrane cap**

![](https://docs.smartcitizen.me/assets/images/water/atlas-do-mini-unscrew-precautions.png)
_Image Credit: **Atlas Scientific**

* The sensor has an electrolyte solution inside to support the chemical reaction in the electrodes. **This solution depletes over time, as the sensor is used** and it will generate a solid residue that needs to be cleaned periodically (roughly every 6 months for the Mini DO probe, but better to check)

![](https://docs.smartcitizen.me/assets/images/water/atlas-do-mini-probe-refill.png)
_Image Credit: **Atlas Scientific**


* You can recondition the sensor with a small file and remove all Zinc Oxyde. Make sure that the probe membrane is cleaned with a **very soft** brush both inside and outside. The membrane can be replaced if damaged. Make sure it is in good conditions because it will otherwise leak the electrolyte solution and the sensor will work erratically.

![](https://docs.smartcitizen.me/assets/images/water/atlas-do-mini-probe-recondition.png)
_Image Credit: **Atlas Scientific**

![](https://docs.smartcitizen.me/assets/images/water/atlas-do-mini-membrane-cleaning.png)
_Image Credit: **Atlas Scientific**

!!! warning "First time use? Do it"
    Even it the sensor is brand new, we recommend you follow this process to avoid issues.

### pH and ORP

No particular consideration for these probes, other than they are very delicate:

![](https://docs.smartcitizen.me/assets/images/water/atlas-ph-warning.png)
_Image Credit: **Atlas Scientific**

!!! danger "Storage solution"
    Both probes need storage solution in a small soaker bottle to prevent it from drying out.

    If the probe is not being used you need to put the soaker bottle back on.

## Maintenance

Make sure that the sensors are cleaned frequently, specially if deployed on the field.
In some cases, sensors will be affected by [biofouling](https://en.wikipedia.org/wiki/Biofouling) and they will need more or less often cleanup - **in some cases weekly!**

<p><a href="https://commons.wikimedia.org/wiki/File:Zebra_mussel_GLERL_4.jpg#/media/File:Zebra_mussel_GLERL_4.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/3/3d/Zebra_mussel_GLERL_4.jpg" alt="Zebra mussel GLERL 4.jpg"></a><br>Public Domain, <a href="https://commons.wikimedia.org/w/index.php?curid=2143950">Link</a></p>