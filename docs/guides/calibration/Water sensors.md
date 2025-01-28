# Atlas Scientific

<img src="https://live.staticflickr.com/65535/51230999551_3941affaa5_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

## Calibration on the Smart Citizen Kit

The Smart Citizen firmware has built-in support for the calibration of some Atlas Scientific sensors. The supported sensors are:

- pH
- Electric Conductivity
- Dissolved Oxygen
- Oxidation reduction potential
- Temperature

In order to calibrate the sensors you will need to use the [SCK Shell](/guides/getting-started/using-the-shell/).

To enable the sensors you just need to plug you board to the Smart Citizen kit aux port and reboot the Smart Citizen Kit and the sensors will be handled by the board.

!!! warning
    When calibrating **don't use the normal `read sensor` command**, this command applies temperature/salinity compensation, calibration should be done without any compensation. Instead you should use `control sensorName com r` and that will return the raw metrics that sensor can provide. On the documentation of each sensor calibration procedure we describe the format of this metrics.

!!! danger
    After finishing the calibration process **restart your SCK** to start from a clean state.

### pH

You need to perform a 3-point calibration with the calibration solutions. The solutions vary their pH with temperature, so make sure to check the temperature prior. **The pH value at current temperature can be found on the reference table on the calibration solution bottle. If the current temperature is not on it, use the closest value or use the calculator [here](https://atlas-scientific.com/ph-temperature-calculator/)**.

!!! info "Datasheet"
    Here you can find the [datasheet](https://www.atlas-scientific.com/files/pH_EZO_Datasheet.pdf):

    - Calibration theory on page 11
    - Commands on page 52

    **Example commands**

    ```
    control ph com r
    control ph com cal,[mid,low,high],value
    control ph com cal,clear
    control ph com cal,?
    ```

#### 3-point calibration

This is the order of the calibration:

1. mid point
2. low point
3. high point

!!! warning
    Always calibrate the mid point first because it calibration erase all the previous calibration done.

!!! danger
    **Always clean the probe with distilled water between each calibration**

##### Mid point calibration

* Put the sensor in the pH 7 calibration solution.

![](https://i.imgur.com/WhpJiN2.png)

* Read the sensor multiple times until the reading is stable:

    ```
    control ph com r
    6.48
    control ph com r
    6.45
    ...
    ```

* Issue the midpoint calibration command:

    ```
    control atlas ph com cal,mid,[value of pH at current temperature]
    ```

!!! info "Example at 30°C"

    ```
    control atlas ph com cal,mid,6.99
    ```

After this command if you take a pH reading the result should be 7.00 (or very close to it)

##### Low Point Calibration

* Repeat the procedure with the **Low point** 4.00 solution (the red one). First, read the sensor multiple times until the reading is stable:

    ```
    control ph com r
    3.98
    control ph com r
    3.98
    ...
    ```

* Issue the midpoint calibration command:

    ```
    control atlas ph com cal,low,[value of pH at current temperature]
    ```

!!! info "Example at 30°C"

    ```
    control atlas ph com cal,low,4.01
    ```

##### High Point Calibration

* The same step with **High point** 10.00 calibration solution (blue). First, read the sensor multiple times until the reading is stable:

    ```
    control ph com r
    9.84
    control ph com r
    9.84
    ...
    ```

* Issue the midpoint calibration command:

    ```
    control atlas ph com cal,high,[value of pH at current temperature]
    ```

!!! info "Example at 30°C"

    ```
    control atlas ph com cal,high,9.96
    ```

!!! info "Extra notes"
    The command `control com cal,?` can be used to check the calibration status as explained on datasheet page 52. The answers can be:

    - **`?CAL,0`** → No calibration done
    - **`?CAL,1`** → One point calibration done
    - **`?CAL,2`** → Two point calibration done
    - **`?CAL,3`** → Three point calibration done

    *(not tested)* If your calibration solutions are not 4, 7 and 10, you can still use them and replace `[value of pH at current temperature]` by your values.

### Electric conductivity

You need to perform a 3 step calibration with a dry point and a 2-point calibration with the calibration solutions.

!!! info "Datasheet"
    Here you can find the [datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/EC_EZO_Datasheet.pdf):

    - Calibration info on page 12
    - Calibration commands on page 55

    **Example commands**

    ```
    control conductivity com r
    control conductivity com K,[probeType]
    control conductivity com K,?
    control conductivity com cal,[dry,clear,84]
    control conductivity com cal,low,1413
    control conductivity com cal,high,12,880
    control conductivity com cal,?
    ```

#### 2-point calibration

This is the order of the calibration:

1. set probe type
1. dry point
2. two-point calibration

##### Set probe type

Depending on which probe you have (check drawing for reference) you should set the probe type to K 0.1, 1.0 or 10 (new drivers have K1.0 as default):

![](https://i.imgur.com/MWFjbYw.png)

To set the correct probe type:

```
control conductivity com K,1.0
```

and check which type is set:

```
control conductivity com K,?
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
    control conductivity com r
    0.00,0,0.00,1.000
    control conductivity com r
    0.00,0,0.00,1.000
    ...
    ```

* Issue the dry calibration command:

    ```
    control conductivity com cal,dry
    ```

##### Low point calibration

You can check the recommended calibration solutions for each probe on the _Probetypes_ drawing (for instance, for K1.0 probe, _12,880uS_ and _80,000uS_ are recomended)

![](https://i.imgur.com/nendSkI.png)

* Read the sensor multiple times until the reading is stable:

    ```
    control conductivity com r
    13470,7278,7.76,1.0
    control conductivity com r
    13230,7144,7.61,1.0
    ...
    ```

* Issue the low point calibration command. **The value to input is the one of the calibration solution**, for example _128800_:

    ```
    control conductivity com cal,low,12880
    ```

After this command readings will **not change**.

##### High point calibration

Repeat this steps with **high point** calibration solution and when the readings stabilize issue the command. Again, **remember that the value to input here is the one from the calibration solution**, for instance _80000_:

```
control conductivity com cal,high,80000
```

After this steps the **two point calibration is complete** and the readings **will change**.

### Dissolved Oxygen

You have two options for this calibration:

1. Single point calibration (dry point)
2. 2-point calibration (dry point and 0 mg/l point) - **only if you need accurate readings below 1mg/l**

**Make sure you have followed the [probe reconditioning](/Guides/deployments/Water sensors/#dissolved-oxygen) before proceeding with this calibration.**

!!! info "Datasheet"
    Here you can find the [datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/DO_EZO_Datasheet.pdf):

    - Calibration info on page 9
    - Calibration commands on page 52

    **Example commands** (you can put `control ox`, `control oxygen` or `control dissolved oxygen` - **however!** do not put `control dissolved` as  it will use TDS)

    ```
    control ox com r
    control ox com cal
    control ox com cal,0
    control ox com cal,clear
    control ox com cal,?
    ```

!!! warning "Pressure compensation"
    If the sensor is going to be used at more than 10 meters deep into the water **Pressure compensation** should be set with:

    ```
    control ox com P,kPaValue
    ```

    More information on [datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/DO_EZO_Datasheet.pdf), page 57

#### OPTION 1: Single point calibration

!!! warning "First calibrate, compensate later"
    Temperature, salinity and pressure compensation values have no effect on calibration.

* Read the sensor multiple times until the reading is stable:

    ```
    control ox com r
    13.95,50%
    control ox com r
    13.76,49%
    ...
    ```

* Issue the calibration command, after this the readings will change. In this case, there is no need to add any value after `cal`. The sensor will take the current reading as the _dry point_.

    ```
    control ox com cal
    ```

!!! danger "Be careful"
    If at any point of the calibration process you see akward readings (for instance, that using a 0mg/l solution for dissolved oxygen you see weirdly high values), it is better to start over. For this, proceed with:

    ```
    control ox com cal,clear
    ```

    And start from the beginning.

#### OPTION 2: 2-point calibration

**Two point calibration is recommended if you require accurate readings below 1.0 mg/l.** After completing the single point calibration procedure put the probe in the calibration solution.

![](https://i.imgur.com/icxCaOZ.png)

* Read the sensor multiple times until the reading is stable:

    ```
    control ox com r
    13.95,50%
    control ox com r
    13.76,49%
    ...
    ```

* Issue the calibration command. In this case, you have to input the value of the calibration solution too, for example _0_:

    ```
    control ox com cal,0
    ```

Reset your SCK and you are ready.

!!! success "Ready to go?"
    If you want to send the data to the platform, you will need to  [Advanced Kit Selection](/Guides/getting started/Onboarding Sensors/#advanced-kit-selection/). At the moment the closest Kit Blueprint will be `#22 BioPV Kit` or `#31 SCK 2.1 Sea Water` in case you are using a SCK2.1 with GPS. You can request on the [forum]({{ extra.urls.forum.link }}) for a custom blueprint with the specific sensors you are using.

### Oxidation-reduction potential

You only need to perform a single point calibration. You can use any calibrated solution, as long as it's within your sensor range. Atlas uses a 225mV calibration.

!!! info "Datasheet"
    Here you can find the [datasheet](https://files.atlas-scientific.com/ORP_EZO_Datasheet.pdf):

    - Calibration info on page 12
    - Calibration commands on page 49

    **Example commands**

    ```
    control redox com r
    control redox com cal
    control redox com cal,[value]
    control redox com cal,clear
    control redox com cal,?
    ```

#### Single point calibration

![](/assets/images/atlas_orp_cal_process.png)

* Read the sensor multiple times until the reading is stable:

    ```
    control redox com r
    225
    control redox com r
    224
    ...
    ```

* Issue calibration command

    ```
    control redox com cal,[value of ORP]
    ```

!!! info "Example at 25°C"

    ```
    control redox com cal,225
    ```

### Temperature

You only need to perform a single point calibration. This process is only necessary if you change the probe cable or the first time you use the sensor.

!!! info "Datasheet"
    Here you can find the [datasheet](https://files.atlas-scientific.com/EZO_RTD_Datasheet.pdf):

    - Calibration info on page 12
    - Calibration commands on page 53

    **Example commands** (you can put `control ox`, `control oxygen` or `control dissolved oxygen` - **however!** do not put `control dissolved` as  it will use TDS)

    ```
    control atlas temp com r
    control atlas temp com cal
    control atlas temp com cal,[value]
    control atlas temp com cal,clear
    control atlas temp com cal,?
    ```

!!! warning
    This is needed because the temperature probe is a resistive sensor – more cable → more resistance!

!!! danger "Reference"
    You will need another temperature probe or something of known temperature (like boiling water, or the triple point of water...) for this. If  you are using a reference sensor, make sure both are stable before issuing calibration commands!

#### Single point calibration

* Read the **reference probe** multiple times until the reading is stable. Write down the value:

    ```
    control atlas temp com r
    22.5
    control atlas temp com r
    22.4
    ...
    ```

* Read the **target probe** multiple times until the reading is stable:

    ```
    control atlas temp com r
    29.5
    control atlas temp com r
    29.4
    ...
    ```

* Issue calibration command:

    ```
    control atlas temp com cal,[value of temperature from reference probe or temperature]
    ```