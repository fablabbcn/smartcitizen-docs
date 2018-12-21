Plantower PMS
==============

## Pulse mode correlation

The purpose of this test is to determine the time needed to obtain representative readings in a one-shot mode.

For this, two kits V2.0 are used with several PM Boards and **one** PMS5003 connected to each of them:

- KIT1: Named OSCAR + 1xPMS5003
- KIT2: Named TEST7 + 1xPMS5003

One of them is set in a continuous operation mode, while the other operates in on/off mode with different on-times.

**TEST**:
- 2018-07_INT_PMS5003_ON_OFF_LOW_PARTICLE
- 2018-07_INT_PMS5003_ON_OFF_MID_PARTICLE

### Results

**2018-07_INT_PMS5003_ON_OFF_MID_PARTICLE**

- 30min logging with a candle under the sensors. Initial 3min in stabilised conditions:

![](https://i.imgur.com/da1DqDL.png)

**2018-07_INT_PMS5003_ON_OFF_LOW_PARTICLE**

- 30min logging with normal ambient air. Initial 3min in stabilised conditions

![](https://i.imgur.com/we83EWi.png)


#### Target errors

The initial 3min are used to determine target errors on the stabilisation phase. For each dataset, they are below:

| **High PN**  | *Average* | *Std Deviation* |
| -------- | -------- | -------- |
| Relative_error_PM 1.0     | 0.15     | 0.17     |
| Relative_error_PM 2.5     | -0.02     | 0.16     |
| Relative_error_PM 10.0    | -0.10     | 0.20     |
 
![](https://i.imgur.com/3oTiKdA.png)


| **Low PN**  | *Average* | *Std Deviation* |
| -------- | -------- | -------- |
| Relative_error_PM 1.0     | 0.07    | 0.07     |
| Relative_error_PM 2.5     | 0.01     | 0.07     |
| Relative_error_PM 10.0    | 0.04     | 0.08     |

![](https://i.imgur.com/mNH99Sf.png)

#### Measurement iterations

The measurement iterations are plotted below, versus the wake up time:

![](https://i.imgur.com/ghAUiF9.png)
![](https://i.imgur.com/gDETISR.png)

Assuming a confidence interval of 95%, the target value for the measurement mean is $(\mu - \sigma<\mu<\mu + \sigma)$ and the values for each period are extracted from the plots above:

| Target Time | *Low PN* | *High PN* |
| -------- | -------- | -------- |
| PM 1.0     | 15s    | 4s     |
| PM 2.5     | 15s     | 5s     |
| PM 10.0    | 12s     | 5s     |


### Conclusion

1. Although the PMS has a faster response at high PN, the variability and the measurement averages are higher as well. **This can also be due to the measurement method uncertainty**
2. For low PN, the time required for stabilisation is between 12 and 15s, to achieve a level of 95% confidence with respect to that of stabilised levels
3. The target time should be 15s, although lower values could be considered down to 12s if there are battery concerns

## PMS Family correlation tests

Tests were conducted over two weeks in Barcelona in order to compare both, PlanTower PMS7003 and PMS5003. Results are shown before for normal urban environment levels of exposure:

| | Average Level |RMSE | R2 |
| -------- |---| -------- | -------- |
| PM 1.0     | 13.89 | 2.34   | 0.90    |
| PM 2.5     | 19.40 | 3.78     | 0.88     |
| PM 10.0    | 20.49 | 0.85     | 4.43     |

## Power consumption tests

### PMS7003
[Datasheet](http://download.kamami.com/p564008-p564008-PMS7003%20series%20data%20manua_English_V2.5.pdf)

![](https://i.imgur.com/rfQGDPW.jpg =400x)
(Check the adaptor position)

**Power consumption**
![](https://i.imgur.com/79XJFVI.png)

**Power consumption** is around **50mA** in average with peaks of **100mA**

### PMS5003

![](https://i.imgur.com/i0CXOm8.jpg =400x)

**Power consumption**
![](https://i.imgur.com/dxZuaEk.png)

**Power consumption** is around **50mA** in average with peaks of **94mA**
