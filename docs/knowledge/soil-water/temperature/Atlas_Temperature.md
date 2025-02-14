---
card: true
name: Atlas Temperature
field:
 - water
 - soil
type:
  - external
target:
  - temperature
feature_img: /assets/images/atlas-scientific-temperature.jpg
feature_img_credit: "Atlas Scientific"
excerpt: ""
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

### The sensor

To measure temperature, we will use a resistance temperature detector (RTD) of the PT1000 type (made of platinum, and with a resistance at 0ºC of 1000Ω). This sensor is encapsulated within a stainless steel tip, to conduct heat very efficiently. To be able to use it at more extreme temperatures, or fix it in a pipe, we will use a _thermowell_:

!!! danger "WATCH OUT!"

    Check the sensor specifications in the following section, because it has a "long" stabilization time of about 13 seconds.


![alt_text](/assets/images/water/atlas_thermo.png "Thermowell")

The sensor can be completely submerged, and has the **following features** (we list some of them here, but you can find a complete description in the datasheet):

- Range: -200 to 850ºC (without thermowell -55ºC to 125ºC)
- Accuracy: +/- (0.15 + (0.002\*t))
- Maximum depth in water: 70m
- Response speed: 90% in 13s

This type of sensor does not require maintenance or recalibration, only periodic cleaning to remove fouling. Using a normal brush is enough.

!!! warning "Before doing anything, review the datasheet:"

    [https://files.atlas-scientific.com/PT-1000-probe.pdf](https://files.atlas-scientific.com/PT-1000-probe.pdf)

## Usage and considerations

### Calibration

You only need to perform a single point calibration. This process is only necessary if you change the probe cable or the first time you use the sensor.

!!! info "Datasheet"
    Here you can find the [datasheet](https://files.atlas-scientific.com/EZO_RTD_Datasheet.pdf):

    - Calibration info on page 12
    - Calibration commands on page 53

    **Example commands** (you can put `control ox`, `control oxygen` or `control dissolved oxygen` - **however!** do not put `control dissolved` as  it will use TDS)

    ```
    control atlas temp com,r
    control atlas temp com,cal
    control atlas temp com,cal,[value]
    control atlas temp com,cal,clear
    control atlas temp com,cal,?
    ```

!!! warning
    This is needed because the temperature probe is a resistive sensor – more cable → more resistance!

!!! danger "Reference"
    You will need another temperature probe or something of known temperature (like boiling water, or the triple point of water...) for this. If  you are using a reference sensor, make sure both are stable before issuing calibration commands!

#### Single point calibration

* Read the **reference probe** multiple times until the reading is stable. Write down the value:

    ```
    control atlas temp com,r
    22.5
    control atlas temp com,r
    22.4
    ...
    ```

* Read the **target probe** multiple times until the reading is stable:

    ```
    control atlas temp com,r
    29.5
    control atlas temp com,r
    29.4
    ...
    ```

* Issue calibration command:

    ```
    control atlas temp com,cal,[value of temperature from reference probe or temperature]
    ```
