<!-- Source: https://docs.smartcitizen.me/knowledge/soil-water/EC/Atlas_EC/ -->

# Atlas EC

A conductivity meter to measure electrolytes in a liquid!

![](https://docs.smartcitizen.me/assets/images/atlas-scientific-ec.jpg){.banner-box}

_Image Credit: **Atlas Scientific**_{.image-credit-banner-box}

## Working principle

To measure electrical conductivity, we'll use a sensor called a **conductivity meter**. In the case of Smart Citizen, using Atlas Scientific sensors, the conductivity sensor does not have an integrated temperature sensor, so we will need to use an additional temperature sensor to measure the temperature at which we are taking our sample. **This temperature sensor should be submerged at the same time when we take conductivity measurements**.

If there is an active temperature sensor taking simultaneous readings, the reported values from the conductivity meter will be based on the measured temperature, and this process will be automatic. If you do not have a temperature sensor, the reading will based on a temperature of 25ºC, which may represent a source of error. Additionally, it is important to check corrections for extreme pH values (greater than 12 or less than 2), as these can introduce large errors in the results on Smart Citizen (and Atlas Scientific) sensors.

The range of the sensor depends on the probe type (its _K_ constant). The EZO conductivity circuit supports probes from K 0.1 to K 10, with the following accurate reading ranges, according to the manufacturer:

| Probe | Conductivity range | TDS | Salinity (PSU) |
|:- |:-: |:-: |:-: |
| K 0.1 | 0.07 – 50.000 µS/cm | 0 – 25.000 ppm | 0 – 33 |
| K 1.0 | 5 – 200.000 µS/cm | 2 – 100.000 ppm | 0 – 42 |
| K 10 | 10 µS/cm – 1 S/cm | 5 – 500.000 ppm | 0 – 42 |

Check the [EZO EC datasheet](https://files.atlas-scientific.com/EC_EZO_Datasheet.pdf) for more details.

## Usage and considerations

The following metrics are available:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| Electrical conductivity | `Atlas Conductivity` | µS/cm | [45](https://api.smartcitizen.me/v0/sensors/45) |
| Total dissolved solids | `Atlas Total Dissolved Solids` | ppm | [122](https://api.smartcitizen.me/v0/sensors/122) |
| Salinity | `Atlas Salinity` | PSU (ppt) | [123](https://api.smartcitizen.me/v0/sensors/123) |
| Specific gravity | `Atlas Specific gravity` | - | [46](https://api.smartcitizen.me/v0/sensors/46) |

### How to prepare the sensor

**Before and after** measuring, the sensor should be cleaned with deionized water. In case of debris, it can be cleaned with laboratory tissue to avoid dust. If it is very dirty or contains oily residues, it can also be cleaned first with a little detergent and then with distilled water.

!!! info "**Calibration**"

    If the sensor is not calibrated, follow the procedure described below.

### Calibration


!!! warning
    When calibrating **don't use the normal `read sensor` command**, this command applies temperature/salinity compensation, calibration should be done without any compensation. Instead you should use `control sensorName com,r` and that will return the raw metrics that sensor can provide. On the documentation of each sensor calibration procedure we describe the format of this metrics.

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

![](https://docs.smartcitizen.me/assets/images/water/atlas-ec-probe-type.jpg)

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

![](https://docs.smartcitizen.me/assets/images/water/calibration.png)

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

    ![alt_text](https://docs.smartcitizen.me/assets/images/water/atlas-ec-minimum.jpg "At minimum, to here!")

    It also prevents bubbles from accumulating in the sensor covering. Simply shake the sensor a little to remove the bubbles:

    ![alt_text](https://docs.smartcitizen.me/assets/images/water/atlas-ec-bubbles.jpg "Bubbles")


### Factory reset procedure

!!! info "Why is this needed?"
    You may need to do a factory reset for water sensors for different reasons. However, the most common case is a wrong calibration process and it's very much related to a wrongful automatic temperature compensation of the sensor while calibrating the sensor.

    To explain further: EC, DO and pH sensor readings are automatically compensated by temperature readings. If there is an existing temperature correction in the EZO driver, or there is a correction in the middle of the calibration process, the data available for the calibration process will be invalid. Follow the steps below to be make sure there is no correction while you calibrate the probes.

Each EZO driver has it's independent calibration and status. This process needs to be done per **_driver_** (i.e. per EZO metric). To make a factory reset procedure for the EZO drivers follow the steps below:

1. Make sure that the [Smart Citizen Data](https://docs.smartcitizen.me/hardware/boards/data-board.md) board will not take any readings while you follow the calibration process. The best option is to reset the configuration to the defaults. Make sure you [back-up your information](https://docs.smartcitizen.me/guides/firmware/upgrading-the-firmware.md#make-a-back-up-of-your-info) before:

    - The config command will output your current configuration. Copy it and keep it safe:

    ```
    config
    ```

    - Then issue the default configuration:

    ```
    config -defaults
    ```

    - The LED should be red now (the Data Board is in [Setup mode](https://docs.smartcitizen.me/hardware/kit/features.md#setup-mode))

2. Issue the factory reset command to the _driver_ in question. For instance, for the _conductivity_ one:

    ```
    control cond com factory
    0
    ```

3. Now you can check what the status of the device is:

    ```
    control cond com cal,?
    ?CAL,0
    ```

4. Reset the kit

5. Follow the calibration process as you would normally would.

6. Reconfigure the kit using the `config` command, by putting back the information you backed-up before:

    ```
    config -mode ...
    ```

!!! danger
    After finishing the calibration process **restart your SCK** to start from a clean state.

## Resources

!!! tip "Additional resources"

    On the importance of salinity for physical oceanography, as well as its application to the identification of fronts between different bodies of water:

    - [Ocean Science In Your Kitchen | Salinity & Density (_Royal Museums Greenwich_)](https://www.youtube.com/watch?v=-B5PDNmSidY)

    - [Ocean Science In Your Kitchen | Salinity & the Sea (_Royal Museums Greenwich_)](https://www.youtube.com/watch?v=AsLJLt70Zo4)

    - [Ocean Science in Your Kitchen | Salinity & Temperature (_Royal Museums Greenwich_)](https://www.youtube.com/watch?v=oxAwn8nunGo)

    In case you want to delve deeper into conductivity measurements, you can review the references at [USGS: _Science for a Changing World: Specific Conductance_](https://pubs.usgs.gov/tm/09/a6.3/tm9-a6_3.pdf).