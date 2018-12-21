Advanced development setup
==========================

## How to use it?

**Connect the board**

The alphaDelta board should be connected to the kit auxiliary groove connector and the tester board to the alphaDelta. In this way the kit will have acces to both boards writing values in tester board and reading them in the sensor board.

![](https://i.imgur.com/MqFyvDm.png)

The tester board should be connected between Electrodes **A** and **W** from the slot you want to test.

![](https://i.imgur.com/5hJTQIw.png)

**Get the firmware**

You will need the latest version of SCK 2.0 Firmware. To enable tester board in firmware uncomment `#define deltaTest` in [sckAux.h](https://github.com/fablabbcn/smartcitizen-kit-15/blob/master/sam/src/sckAux.h#L10) file compile and upload the firmware.


### Read the sensors

_read Alphadelta [wichSensor: temperature, humidity, 1A, 2A, 2A, 2W, 3A, 3W]_

```
SCK > read alphadelta 1a
AlphaDelta 1A: 8.22
```

### Control digital potentiometers

_control alphadelta 1A set pot [value: 0-100,000]_

```
SCK > control alphadelta 1a set pot 50000
AlphaDelta 1A: set pot 50000
Setting pot to: 50000 Ohms
Actual value: 49803 Ohms
```

### Run the tests

The tester board is enabled as a _control_ command of Alphasense Delta sensors, so it must be called with the prefix **control** then the name of the sensor **alpha** (fuzzy match is supported) then the **test** keyword followed by the slot number we want to test:

> **control alpha test 1**

To complete the line we should select one of the two test modes:

**set** followed by a nA value between -1400/+1400. This will instruct the tester board to output that current and verify the readings of the sensor.

> **control alpha test <slot> set <value>**

```
SCK > control alpha test 1 set 500
AlphaDelta 1A: test 1 set 500
Setting test current to: 500
Tester Electrode W: 500
Alphadelta 1W: 78.87
Tester Electrode A: 500
Alphadelta 1A: 78.70

Testing finished!
```
or **full** that will ouput a csv formated table with the values for both electrodes of the selected slot from -1400 nA to 1400 nA:

> **control alpha test 1 full**

```
SCK > control alpha test 1 full
AlphaDelta 1A: test 1 full
testW,readW,testA,readA
-1400,-220.94,-1400,-220.58
-1399,-220.92,-1399,-220.52
-1398,-220.78,-1398,-220.37
-1397,-220.62,-1397,-220.25
-1396,-220.48,-1396,-220.09
...
```

## How to run the validation?

For validating the boards, we propose verifying that: **each nA input can only yield a single output in mV in the ADC, at minimum gain (for each electrode).**

This means that for a test such as:

> **control alpha test 1 full**

We should obtain an always positively growing value in the readW, readA channels. For this, we have to check that:

$$
\delta[n] = readX[n]-readX[n-1]>0
$$

If we plot all this results we see that they are normally over 0.1 for all the boards, so we use this value as a minimum threshold, instead of zero:

$$
\delta[n] = readX[n]-readX[n-1]>0.1
$$

Finally, this test is also valid for **too high gains** since once the signal is saturated the $\delta$ value is 0 (saturates in a flat plateau).

<style>.embed-container { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; } .embed-container iframe, .embed-container object, .embed-container embed { position: absolute; top: 0; left: 0; width: 100%; height: 100%; }</style><div class='embed-container'><iframe src='https://www.youtube.com/embed/i89nVDCQdII' frameborder='0' allowfullscreen></iframe></div>
