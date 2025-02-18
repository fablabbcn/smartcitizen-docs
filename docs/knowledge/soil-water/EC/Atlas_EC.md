---
card: true
name: Atlas EC
field:
  - water
  - soil
type:
  - external
target:
  - electrical conductivity
feature_img: /assets/images/atlas-scientific-ec.jpg
feature_img_credit: "Atlas Scientific"
excerpt: "A conductivity meter to measure electrolytes in a liquid!"
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

To measure electrical conductivity, we'll use a sensor called a **conductivity meter**. In the case of Smart Citizen, using Atlas Scientific sensors, the conductivity sensor does not have an integrated temperature sensor, so we will need to use an additional temperature sensor to measure the temperature at which we are taking our sample. **This temperature sensor should be submerged at the same time when we take conductivity measurements**.

If there is an active temperature sensor taking simultaneous readings, the reported values from the conductivity meter will be based on the measured temperature, and this process will be automatic. If you do not have a temperature sensor, the reading will based on a temperature of 25ºC, which may represent a source of error. Additionally, it is important to check corrections for extreme pH values (greater than 12 or less than 2), as these can introduce large errors in the results on Smart Citizen (and Atlas Scientific) sensors.

## Usage and considerations

### How to prepare the sensor

**Before and after** measuring, the sensor should be cleaned with deionized water. In case of debris, it can be cleaned with laboratory tissue to avoid dust. If it is very dirty or contains oily residues, it can also be cleaned first with a little detergent and then with distilled water.

!!! info "**Calibration**"

    If the sensor is not calibrated, follow the procedure described below.

### Calibration

{{ get_snippet_rel('docs/includes/pre-calibration-water-stations.md')}}

You need to perform a 3 step calibration with a dry point and a 2-point calibration with the calibration solutions.

!!! info "Datasheet"
    Here you can find the [datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/EC_EZO_Datasheet.pdf):

    - Calibration info on page 12
    - Calibration commands on page 55

    **Example commands**

    ```
    control conductivity com,r
    control conductivity com,K,[probeType]
    control conductivity com,K,?
    control conductivity com,cal,[dry,clear,84]
    control conductivity com,cal,low,1413
    control conductivity com,cal,high,12,880
    control conductivity com,cal,?
    ```

#### 2-point calibration

This is the order of the calibration:

1. set probe type
1. dry point
2. two-point calibration

##### Set probe type

Depending on which probe you have (check drawing for reference) you should set the probe type to K 0.1, 1.0 or 10 (new drivers have K1.0 as default):

![](/assets/images/water/atlas-ec-probe-type.jpg)

To set the correct probe type:

```
control conductivity com,K,1.0
```

and check which type is set:

```
control conductivity com,K,?
?K,1.0
```

!!! info "About the sensor"
    The **Electrical Conductivity** sensor provides four different metrics:

    * Electrical Conductivity → EC
    * Total Dissolved Solids → TDS
    * Salinity → S
    * Specific Gravity → SG

    The data is presented in order and comma separated **EC,TDS,S,SG**, for instance **0.00,0,0.00,1.000**

!!! warning "Readings are 0?"
    It is normal that if the probe type has been changed (for instance, you are using a K10 probe), that the readings are 0 after setting the probe type.

##### Dry calibration

Follow the steps below with the dry sensor before introducing it to the calibration solutions. You need to do this step even if the readings in dry state are 0.

* Read the sensor multiple times until the reading is stable:

    ```
    control conductivity com,r
    0.00,0,0.00,1.000
    control conductivity com,r
    0.00,0,0.00,1.000
    ...
    ```

* Issue the dry calibration command:

    ```
    control conductivity com,cal,dry
    ```

##### Low point calibration

You can check the recommended calibration solutions for each probe on the _Probetypes_ drawing (for instance, for K1.0 probe, _12,880uS_ and _80,000uS_ are recomended)

![](/assets/images/water/calibration.png)

* Read the sensor multiple times until the reading is stable:

    ```
    control conductivity com,r
    13470,7278,7.76,1.0
    control conductivity com,r
    13230,7144,7.61,1.0
    ...
    ```

* Issue the low point calibration command. **The value to input is the one of the calibration solution**, for example _128800_:

    ```
    control conductivity com,cal,low,12880
    ```

After this command readings will **not change**.

##### High point calibration

Repeat this steps with **high point** calibration solution and when the readings stabilize issue the command. Again, **remember that the value to input here is the one from the calibration solution**, for instance _80000_:

```
control conductivity com,cal,high,80000
```

After this steps the **two point calibration is complete** and the readings **will change**.

### How to measure

If you aren't familiar with the site where you are taking samples, measure at several points at different depths and sections. In case there is little water movement, take several samples at different depths.

1. Take the measurement at the desired depth, letting the sensor stabilize for at least 60 seconds. To find out if it is stabilized, wait for variations of ±5 μS/cm for measurements ≤100 μS/cm or ±3% for measurements >100 μS/cm. Do not immerse the probe too deeply, ensuring it does not reach sediment areas.
2. Takes temperature and conductivity measurements, without moving the water probes (take both at the same time).
3. When finished, clean the probe with deionized water.

!!! warning

    The conductivity sensor needs to be immersed to cover the active element:

    ![alt_text](/assets/images/water/atlas-ec-minimum.jpg "At minimum, to here!")

    It also prevents bubbles from accumulating in the sensor covering. Simply shake the sensor a little to remove the bubbles:

    ![alt_text](/assets/images/water/atlas-ec-bubbles.jpg "Bubbles")

{{ get_snippet_rel("docs/includes/water-probes-reset.md") }}

## Resources

!!! tip "Additional resources"

    On the importance of salinity for physical oceanography, as well as its application to the identification of fronts between different bodies of water:

    - [Ocean Science In Your Kitchen | Salinity & Density (_Royal Museums Greenwich_)](https://www.youtube.com/watch?v=-B5PDNmSidY)

    - [Ocean Science In Your Kitchen | Salinity & the Sea (_Royal Museums Greenwich_)](https://www.youtube.com/watch?v=AsLJLt70Zo4)

    - [Ocean Science in Your Kitchen | Salinity & Temperature (_Royal Museums Greenwich_)](https://www.youtube.com/watch?v=oxAwn8nunGo)

    In case you want to delve deeper into conductivity measurements, you can review the references at [USGS: _Science for a Changing World: Specific Conductance_](https://pubs.usgs.gov/tm/09/a6.3/tm9-a6_3.pdf).
