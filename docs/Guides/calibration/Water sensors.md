# Water Sensors Calibration

<img src="https://live.staticflickr.com/65535/51230999551_3941affaa5_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

## Calibration on the Smart Citizen Kit

The Smart Citizen firmware has built-in support for the calibration of the sensors. In order to calibrate the sensors you will need to use the [SCK Shell](/Guides/getting started/Using the Shell/).

To enable the sensors you just need to plug you board to the Smart Citizen kit aux port and reboot the Smart Citizen Kit and the sensors will be handled by the board.

!!! warning
    When calibrating **don't use the normal `read sensor` command**, this command applies temperature/salinity compensation, calibration should be done without any compensation. Instead you should use `control sensorName com r` and that will return the raw metrics that sensor can provide. On the documentation of each sensor calibration procedure we describe the format of this metrics.

!!! danger
    After finishing the calibration process **restart your SCK** to start from a clean state.

### Atlas PH

The pH value at current temperature can be found on the reference table on the calibration solution bottle. If the current temperature is not on it, use the closest value.

!!! info "Datasheet"
    [Datasheet](https://www.atlas-scientific.com/files/pH_EZO_Datasheet.pdf) (calibration theory on page 11, and commands on page 52)

**Example commands**

```
control ph com r
control ph com cal,[mid,low,high],value
control ph com cal,clear
control ph com cal,?
```

#### 3-point calibration

First start a serial communication with the Smart Citizen Kit with `screen` or `pio device monitor`or even the serial monitor of the Arduino IDE.

Order of the calibration : 

1. mid point
2. low point
3. high point

!!! warning
    Always calibrate the mid point first because it calibration erase all the previous calibration done.

!!! danger
    **Always clean the probe with distilled water between each calibration**

##### Mid point calibration

Put the sensor in the pH 7 calibration solution. 

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

<span style="text-decoration:underline">example at 30°C:</span> 

```
control atlas ph com cal,mid,6.99 
```

After this command if you take a pH reading the result should be 7.00 (or very close to it)

##### Low Point Calibration

Repeat the procedure with the **Low point** 4.00 solution (the red one).

##### High Point Calibration

The same step with **High point** 10.00 calibration solution (blue).

---

!!! info ""
    *(not tested)* If your calibration solutions are not 4, 7 and 10, you can still use them and replace `[value of pH at current temperature]` by your values.

!!! info ""
    The command `control com cal,?` can be used to check the calibration status as explained on datasheet page 52. The answers can be:

    - **`?CAL,0`** → No calibration done
    - **`?CAL,1`** → One point calibration done
    - **`?CAL,2`** → Two point calibration done
    - **`?CAL,3`** → Three point calibration done

### Atlas EC

!!! info ""
    [Datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/EC_EZO_Datasheet.pdf)
    - Calibration info on page 12.
    - Calibration commands on page 55.

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

Order of the calibration :

1. set probe type
1. dry point
2. two-point calibration

---

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

!!! info ""
    The **Electrical Conductivity** sensor provides four different metrics:

    * Electrical Conductivity → EC
    * Total Dissolved Solids → TDS
    * Salinity → S
    * Specific Gravity → SG

    The data is presented in order and comma separated **EC,TDS,S,SG**, for instance **0.00,0,0.00,1.000**

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

After this command readings will **not change**

##### High point calibration

Repeat this steps with **high point** calibration solution and when the readings stabilize issue the command. Again, **remember that the value to input here is the one from the calibration solution**, for instance _80000_:

```
control conductivity com cal,high,80000
```

After this steps the **two point calibration is complete** and the readings will change.

### Atlas DO

Order of the calibration:

1. dry point
2. 0 mg/L point (optional)

!!! info "Datasheet"
    [Datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/DO_EZO_Datasheet.pdf) (calibration info on page 9, calibration commands on page 52)

```
com dissolved r
com dissolved cal
com dissolved cal,0
com dissolved cal,clear
com dissolved cal,?
```

!!! warning "Pressure compensation"
    If the sensor is going to be used at more than 10 meters deep into the water **Pressure compensation** should be set with:

    ```
    control dissolved com P,kPaValue
    ```
    
    More information on [datasheet](https://www.atlas-scientific.com/_files/_datasheets/_circuit/DO_EZO_Datasheet.pdf), page 57

#### OPTION A: Single point calibration

* Read the sensor multiple times until the reading is stable:

```
control dissolved com r
13.95,50%
control dissolved com r
13.76,49%
...
```

* Issue the calibration command, after this the readings will change. In this case, there is no need to add any value after `cal`. The sensor will take the current reading as the _dry point_.

```
control dissolved com cal
```

#### OPTION B: 2-point calibration 

Two point calibration is recommended if you require accurate readings below 1.0 mg/L. After completing the single point calibration procedure put the probe in the calibration solution.

![](https://i.imgur.com/icxCaOZ.png)

* Read the sensor multiple times until the reading is stable:

```
control dissolved com r
13.95,50%
control dissolved com r
13.76,49%
...
```

* Issue the calibration command. In this case, you have to input the value of the calibration solution too, for example _0_:

```
control dissolved com cal,0
```

Reset your SCK and you are ready.

!!! success "Ready to go?"
    If you want to send the data to the platform, you will need to  [Advanced Kit Selection](/Guides/getting started/Onboarding Sensors/#advanced-kit-selection/). At the moment the closest Kit Blueprint will be `#22 BioPV Kit` or `#31 SCK 2.1 Sea Water` in case you are using a SCK2.1 with GPS. You can request in the [forum](http://forum.smartcitizen.me) for a custom blueprint with the specific sensors you are using. 