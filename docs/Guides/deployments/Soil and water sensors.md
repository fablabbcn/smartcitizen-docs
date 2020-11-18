# Water and soil sensors

## Setup

The Smart Citizen firmware has the support for the monitoring board built-in. To enable the sensors you just need to plug you board to the Smart Citizen kit aux port and reboot the Smart Citizen Kit and the sensors will be handled by the board. However, you will need to register your device again using the [Advanced Kit Selection](/Guides/getting started/Onboarding Sensors#Advanced Kit Selection). At the moment the closest Kit Blueprint will be `#22 BioPV Kit` or `#31 SCK 2.1 Sea Water` in case you are using a SCK2.1 with GPS. You can request in the [forum](http://forum.smartcitizen.me) for a custom blueprint with the specific sensors you are using.

## Sensor calibration

In order to calibrate the sensors you will need to use the [SCK Shell](/Guides/getting started/Using the Shell).

![](https://i.imgur.com/wRIfhks.jpg)

### pH sensor

Open the SCK Shell as [specified above](#sensor calibration) and type:

```
control atlas ph com,[point],[pH value at current temperature]
```

The pH value at current temperature can be found on the reference table on the calibration solution bottle. If the current temperature is not on it, use the closest value.

#### 3-point calibration

First start a serial communication with the Smart Citizen Kit with `screen` or `pio device monitor`or even the serial monitor of the Arduino IDE.

Order of the calibration : 

1. mid point
2. low point
3. high point

!!! warning
    Always calibrate the mid point first because it calibration erase all the previous calibration done.

**Always clean the probe with distilled water between each calibration**

* **The mid point calibration :** Put the sensor in the pH 7 calibration solution and run the command below :

```
control atlas ph com cal,mid,[value of pH at current temperature]
```

<span style="text-decoration:underline">example at 30°C :</span> 

```
control atlas ph com cal,mid,6.99 
```

* **The low point calibration :** Put the sensor in the pH 4 calibration solution and run the command below :

```
control atlas ph com cal,low,[value of pH at current temperature]
```

* **The high point calibration :** Put the sensor in the pH 10 calibration solution and run the command below :

```
control atlas ph com cal,high,[value of pH at current temperature]
```

!!! info
    *(not tested)* If your calibration solutions are not 4, 7 and 10, you can still use them and replace `[value of pH at current temperature]` by your values.

### EC Sensor

#### 2-point calibration

Order of the calibration :

1. dry point
2. high point

* **The dry point calibration :** Check that the sensor is dry and run the command below :

```
control atlas ec com cal,dry
```

* **The high point calibration :** Put the sensor in the high point calibration solution (12,880 µS/cm) and run the command below:

```
control atlas ec com cal,high,[value of EC at current temperature]
```

<span style="text-decoration:underline">example at 30°C :</span> 

```
control atlas ec set cal,high,14,120 
```

!!! warning
    Do not forget the `,` between the hundreds and the thousands or else the calibration will not occur !

!!! info
    *(not tested)* If your calibration solution is not 12880 µS/cm, you can use another one and replace `[value of pH at current temperature]` by your value of electroconducivity.

### DO Sensor

#### 2-point calibration

Order of the calibration 

1. dry point
2. 0 mg/L point (optional)

* **The dry point calibration :** Check that the sensor is dry and run the command below :

```
control atlas do com cal
```

* **The 0mg/L point calibration :** Put the sensor in the 0mg/L calibration solution and run the command below :

```
control atlas do com cal,0
```

## Deployment

![](https://i.imgur.com/2EwPJJc.jpg)
![](https://i.imgur.com/2IHsDWq.jpg)
![](https://i.imgur.com/6w2y12F.jpg)
