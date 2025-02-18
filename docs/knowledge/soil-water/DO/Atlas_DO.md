---
card: true
name: Atlas DO
field:
  - water
type:
  - external
target:
  - dissolved oxygen
feature_img: /assets/images/atlas-scientific-do.jpg
feature_img_credit: "Atlas Scientific"
excerpt: "A galvanic probe that can measure dissolved oxygen in water."
internal:
  proofread: false
  links: false
  images: false
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

## Working principle

This Atlas Scientific dissolved oxygen probe consists of a teflon membrane and two electrodes, one of them in an electrolyte solution. Oxygen passes through the Teflon membrane, and as it shrinks in the cathode, a voltage difference is created between them, which we can measure. This type of probe is referred to as galvanic, and consumes some oxygen when you take readings. Therefore, it is necessary to move the probe or water around a little (without aerating it).

The sensor can be completely submerged, and has the **following features** (a selection is listed here, but you can find a complete description in the datasheet):

- Range: 1-50mg/l
- Maximum water depth: 70m
- Response rate: ~0.5 mg/l/per second

!!! danger "Taking care of your sensor"

    Since the electrolyte is part of the reaction with the oxygen inside the probe, it is consumed over time. Normally, it takes about 6 months for the electrolyte to be depleted. Therefore, it is recommended that the electrolyte solution and Teflon membrane be replaced every 6-12 months.

!!! warning "Before doing anything, review the datasheet:"

    [https://files.atlas-scientific.com/Mini_DO_probe.pdf](https://files.atlas-scientific.com/Mini_DO_probe.pdf)

## Usage and considerations

### How to prepare the sensor

This sensor comes in several sizes, depending on how much electrolyte solution it has. **Check the sensor for electrolyte before use.**

You may see Potassium Chloride (KCl) formation on the probe. Clean it with distilled water, without scrubbing harshly, and use it normally.

![alt_text](/assets/images/water/atlas-do-mini-kcl-creep.png "SOURCE: ThermoScientific - KCl Creep")

_SOURCE: **ThermoScientific - KCl Creep**_

!!! info "**Calibration**"

    If the sensor is not calibrated, follow the procedure described below.

### Calibration

You have two options for this calibration:

1. Single point calibration (dry point)
2. 2-point calibration (dry point and 0 mg/l point) - **only if you need accurate readings below 1mg/l**

**Make sure you have followed the [probe preparation](#how-to-prepare-the-sensor) above before proceeding with this calibration.**

!!! info "Datasheet"
    Here you can find the [datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/DO_EZO_Datasheet.pdf):

    - Calibration info on page 9
    - Calibration commands on page 52

    **Example commands** (you can put `control ox`, `control oxygen` or `control dissolved oxygen` - **however!** do not put `control dissolved` as  it will use TDS)

    ```
    control ox com,r
    control ox com,cal
    control ox com,cal,0
    control ox com,cal,clear
    control ox com,cal,?
    ```

!!! warning "Pressure compensation"
    If the sensor is going to be used at more than 10 meters deep into the water **Pressure compensation** should be set with:

    ```
    control ox com,P,kPaValue
    ```

    More information on [datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/DO_EZO_Datasheet.pdf), page 57

#### OPTION 1: Single point calibration

!!! warning "First calibrate, compensate later"
    Temperature, salinity and pressure compensation values have no effect on calibration.

* Read the sensor multiple times until the reading is stable:

    ```
    control ox com,r
    13.95,50%
    control ox com,r
    13.76,49%
    ...
    ```

* Issue the calibration command, after this the readings will change. In this case, there is no need to add any value after `cal`. The sensor will take the current reading as the _dry point_.

    ```
    control ox com,cal
    ```

!!! danger "Be careful"
    If at any point of the calibration process you see akward readings (for instance, that using a 0mg/l solution for dissolved oxygen you see weirdly high values), it is better to start over. For this, proceed with:

    ```
    control ox com,cal,clear
    ```

    And start from the beginning.

#### OPTION 2: 2-point calibration

**Two point calibration is recommended if you require accurate readings below 1.0 mg/l.** After completing the single point calibration procedure put the probe in the calibration solution.

![](https://i.imgur.com/icxCaOZ.png)

* Read the sensor multiple times until the reading is stable:

    ```
    control ox com,r
    13.95,50%
    control ox com,r
    13.76,49%
    ...
    ```

* Issue the calibration command. In this case, you have to input the value of the calibration solution too, for example _0_:

    ```
    control ox com,cal,0
    ```

Reset your SCK and you are ready.

### How to take measurements

Choose, depending on whether you're going to [take a sample](#taking-a-sample) and then measure it in the lab, or if you're going to [submerge the sensor directly](#submerging-the-sensor-directly).

#### Taking a sample

1. Insert a bottle about halfway into the desired sample area, letting the water enter the bottle very slowly. If there's a lot of movement, allow the water to overflow for a couple of minutes, or at least until the water has been renewed two or three times in the bottle.
2. Check that there are no water bubbles before removing the bottle from the water - if there are any near the neck of the bottle, which is where they usually accumulate, tilt the bottle and let them out.
3. Fill the bottle as much as possible to avoid bubbles. If when turning the bottle there are bubbles, throw the sample and start again.
4. Do not use funnels or intermediate containers, or pour water from one container to another, because doing so will inevitably aerate the sample. Use a rubber tube and transfer the water from one container to another, with the end of the tube that is in the container you want to fill at the bottom of it.

#### Submerging the sensor directly

1. It is necessary to calibrate the probe beforehand, as indicated in the previous section.
2. If you take a sample, do so by avoiding aerating it, as indicated above.
3. Insert the probe into the sample and take several readings. **If it takes a long time to stabilize, gently remove the probe, but don't shake it, as this could cause changes in the reading!**
4. When the readings are stable, take that value as valid and write it down.

!!! info "A double-check never hurts"

    If you can, check the measurement with calibration solution after each reading.

    ![alt_text](/assets/images/education/es/do_method.png "How to measure in turbulent waters")
