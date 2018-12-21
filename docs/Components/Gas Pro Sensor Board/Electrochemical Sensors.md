Inside the Electrochemical Sensors
==================================

## Sensor working principle

The electrochemical cells used are toxic gas sensors from alphasense that operate in an amperometric mode. That is, they generate a current that is linearly proportional to the fractional volume of the toxic gas in the environment:

![](https://i.imgur.com/K0yeMN0.png)

_Image Source: Alphasense Ltd._

These electrochemical sensors are comprised of four electrodes:

- Working electrode
- Auxiliary electrode
- Counter electrode
- Reference electrode

The **working electrode** is where the oxidation (CO, H2S, NO, SO2) or reduction (NO~2~, Cl2) of the toxic gas to be measured takes place. This electrode is exposed to the outside air and  directly exposed to all gases in the air including the gas to be measured. This electrode may as well be **poisoned** if it is exposed to certain gases that either adsorb onto the catalyst (such as acetylene onto CO sensors), or react, creating by-products which inhibit the catalyst (NO~2~ or aromatics onto H2S sensors).

The **auxiliary electrode** is an electrode of the same characteristics to those of the working electrode, but it is buried inside an electrolite and, hence, it is not in contact with the target gas. Since it is isolated from external conditions that could affect the **working electrode**, it serves as a reference to the measurements provided by the latter.

The **counter electrode** balances the reaction of the working electrode – if the working electrode oxidises the gas, then the counter electrode must reduce some other molecule to generate an equivalent current, in the opposite sense. For example, where carbon monoxide will be oxidised on the working electrode, oxygen will be reduced on the counter electrode.

The **reference electrode** anchors the working electrode potential to ensure that it is always working in the right conditions. It is important that the reference electrode has a stable potential, keeping the working electrode at the right electrochemical potential to maintain a constant sensitivity, good linearity and minimum sensitivity to interfering gases.

Therefore, while the sensor response is exposed to the target gas, it creates a current flowing from the working to the counter electrode or viceversa (depending on the oxidative or reductive nature of the target gas). This relationship can be characterised and follows a curve such as:

![](https://i.imgur.com/nIgeTRr.png)
_Image source: Alphasense Ltd._

When operating in the so called *transport limited current plateau* the measured current (IL) should be linearly dependent on the concentration or fractional volume of the toxic gas (CT) in the external environment:

$$
I_L = k C_T
$$

where k is a proportionality constant. This constant is provided by the manufacturer as Sensitivity and is explained below.

!!! warning "Electronics design considerations"
	A potentiostat circuit is built in order to ensure that the counter electrode is provided with as much current as it needs, also maintaining the working electrode at a fixed potential, irrespective of how hard it is working.


### Manufacturer data

The manufacturer provides the calibration data in laboratory conditions for each of the electrochemical cells used. This data is listed below:
- **Sensor sensitivity**: the sensor response in nA per each ppm of target pollutant in _nominal_ conditions
- **Electrode zero current**: the electrode reading in nA to zero air (pure air at 25degC). This is provided for both, working and auxiliary electrodes, in the case of 4-electrode sensors
- **Sensor response** ($t_{90}$)
- **Sensor range**

The manufacturer suggests using the following equation in order to determine the sensor's corrected reading in the presence of target gas:

$$
Concentration \ [ppm] = {I_{WE}-n(I_{AE}) \ [nA] \over Sensitivity \ [nA/ ppm]}
$$

Where:

$$
I_{WE} (nA) = K (nA/mV) V_{WE} (mV)
$$

$$
I_{AE} (nA) = K (nA/mV) V_{AE} (mV)
$$

Where:
* $I_{PCBWE}$ and $I_{PCBAE}$ are the electronic offsets for each electrode
* $n  = {I_{0WE} \over I_{0AE}}$, the ratio between alphasense's zero currents
* k is a **constant convertion factor** (*~ 6.36* in the case of the SCK Gas Pro Board electronics)

With regards to **sensor ranges**, the following are available from the manufacture:

- [**NO~2~**](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/NO~2~B43F.pdf): 20ppm
- [**O3 + NO~2~**](http://www.alphasense.com/WEB1213/wp-content/uploads/2017/07/OX-B431.pdf): 20ppm both
- [**CO**](http://www.alphasense.com/WEB1213/wp-content/uploads/2015/04/COB41.pdf): 1000ppm

Finally, toxic gas sensors' sensitivity will **drift downwards with time, typically 0.5% to 2% per month**, depending on the sensor type, relative humidity and gas concentration/temperature conditions.

### Reduction vs Oxidation Electrochemical Sensor

As mentioned above, the **counter electrode** is meant to balance the reaction of the working electrode. This determines the current direction within the board: whether it _goes from the working electrode to the counter electrode_ or viceversa.

- Oxidation sensors, such as CO, provoke a positive current **out of the working electrode** and the larger the amount of CO present, the larger (positive) is this current.

- Reduction sensors, such as NO~2~, provoke a negative current, i.e: **going into the sensor** and the larger the amount of NO~2~ present, the larger (negative) is this current

As an example, this is reflected in the different signs of the sensor sensitivity:

- NO2-B43F Average Batch Sensitivity: -347nA/ppm
- CO-B4F Average Batch Sensitivity: 588nA/ppm

Although this is in principle directly related with the sensor itself, there are further signal transformations to be taken into account.  For instance, the currents seen in the electrodes, if comparing between CO and NO~2~, should be different in sign, however, for both, CO and NO~2~ sensors, we see positive currents which grow positively with higher CO and NO~2~ concentrations:

![](https://i.imgur.com/DSpt0p4.png)

Hence, the sensor senstivity provided by the manufacturer should be considered in absolute terms ($abs(Sensitvity)$) for the calculations to yield always positive results in pollutant fractional volumes.

## Sensor Calibration

The model described in the following section is based on the findings of [^1]. This study uses alphasense's 3-electrode sensors, and here it is further extended to the case of 4-electrode sensors, taking into account the auxiliary electrode.

### Baseline correction based on temperature

The mentioned work described the  correction method based on temperature using a baseline correction algorithm which is described in [^2]. This is summarised below:

1. For each day of gas working electrode readings, and for each point in the time series (i), the minimum value of the working electrode value that is contained within the interval (i-$\delta$ < i < i+$\delta$) is determined, where $\delta$ is an interval ranging from 0 to a day length. The outcome of this procedure is an array where each column is a vector of minimum working electrode values calculated for each $\delta_i$ value (this is, from now on, $baseline_{\delta_i}$).
2. The correlation between each $baseline_{\delta_i}$ and the temperature is calculated. Relative humidity is not considered in this study since it's generaly inversely correlated with the temperature.
3. The correlation coefficients for each correlation ($R^2_{\delta_i}$) are calculated. The maximum $R^2$ whith this array is obtained.
4. For the equation at which the maximum $R^2_{\delta_i}$ is found, the temperature reading is used to calculate the corrected baseline.
5. The corrected baseline is substracted from the actual working electrode reading
6. The final pollutant concentration is calculated based on the corrected working electrode reading and the manufacturer's data.

The readings are treated in a day-to-day basis in order to avoid non-stationary temperature trends over several days, but still to account for temperature variations within each day.

Finally, a background pollutant concentration is assumed from [^3] which is also summarised below for each pollutant. This background concentration is added to the final result.

![](https://i.imgur.com/qDp2cED.png)
**Background concentrations**. _Source [^3]_

#### Application on 4-electrode sensors

This algorithm can be used to correct temperature effects on the working electrode based on the temperature in 4-electrode sensors. The results are discussed below for tests validation campaigns performed  within the iScape project. These tests are summarized below:

- *University of Bologna*: data collected from 23/January to 13/February. The measured pollutants with reference equipments were CO, NO~2~, NO, NOx and O3. Two prototype Smart Citizen Stations were deployed in two different sites, with two Smart Citizen Kits.
- *University College Dublin*: data collected from 27/March to 17/April. The measured pollutants with reference equipments were NO, NO~2~ and NOX. One prototype Smart Citizen Station was deployed with two Smart Citizen Kits.

The results found with this methodology in the reduction sensors (NO~2~, O3) are significant in a daily basis. Two examples of the variation of the correlation coefficient with respect to the delta used to calculate the baseline are shown below:

![](https://i.imgur.com/PhA3UVN.png)

![](https://i.imgur.com/XL7OPTx.png)


The algorithm is set to apply the best performing correlation function from either a linear or an exponential fit, basing this decission on the one that yields better correlation coefficient. NO~2~ and O3 at high concentrations yield better results with an exponential fit, whilst lower concentrations reflect a linear trend:

![](https://i.imgur.com/yRUrTZJ.jpg)

Furthermore, the study from which this methodology is drawn from states that oxidation sensors do not yield a proper baseline correlation methodology and so is validated. The result is indeed far better correlated with the reference measurement if using the manufacturer's methodology:

![](https://i.imgur.com/F4uAY8y.jpg)

This methodology reads as follows:

$$
Concentration \ [ppm] = {I_{WE}-n(I_{AE}) \ [nA] \over Sensitivity \ [nA/ ppm]}
$$

Where:

$$
I_{WE} (nA) = K (nA/mV) V_{WE} (mV)
$$

$$
I_{AE} (nA) = K (nA/mV) V_{AE} (mV)
$$

Where:
* $I_{PCBWE}$ and $I_{PCBAE}$ are the electronic offsets for each electrode
* $n  = {I_{0WE} \over I_{0AE}}$, the ratio between alphasense's zero currents
* k is a **constant convertion factor** (*~ 6.36* in the case of the SCK Gas Pro Board electronics)

In the case of NO~2~, the results provided by this baseline correction algorithm yield better results:
![](https://i.imgur.com/jW7qSaB.jpg)

Both, CO and NO~2~ pollutants, using the best method for each calculation, are shown below:

![](https://i.imgur.com/lripMLT.jpg)

Finally, a comparison between the reference measurement results from both methods is detailed below:

||Manufacturer Method|Baseline Method|
|:--|:--:|:--:|
|**Pollutant**|*RMSE / R2*|*RMSE / R2*|
|**CO (ppm)**| **0.2-0.3 / 0.3-0.5**| >2 / <0.01|
|**NO~2~ (ppb)**| 21-24 / 0.3-0.5| **6 - 12 / 0.4 - 0.6**|
|**O3 (ppb)**|20-40 / 0.1-0.3| **4-9 / 0.1 - 0.3**|


As seen above, the NO~2~ correlation with both methods yields significant results for non-corrected signals, whilst the RMSE values are higher in the case of the manufacturer's proposal. Therefore, for this pollutant, the selected methodology will be the baseline method. On the contrary, the CO measurements are highly uncorrelated with the baseline method, whilst the original manufacturer's proposal yields decent results. Finally, the O3 correlation levels are lower than the CO and NO~2~ measurements. This is possibly due to the O3 reference measurement equipment used in the Bologna campaing, since it shows an inverse relationship with NO~2~ which suggests a biased pollutant calculation in the reference equipment:

![](https://i.imgur.com/258Gec6.jpg)

As well, the results from UCD that are used as a reference for NO~2~, suggest a poor zero/span calibration of the equipment as it yields negative results that could spoil the NO~2~ correlation/model errors from those tests:

![](https://i.imgur.com/DbCuX0g.jpg)

### Baseline correction based on auxiliary electrode

As seen above, the results from applying this methodology to a low concentration, urban environment measurement with 4-electrode sensors yield significantly correlated results in the case of the reductive sensors. It was also seen that oxidation measurements are significantly correlated with the reference measurements while using the manufacturer's suggested method.

However, as detailed in the following section, the use of the auxiliary electrode as the source of the correction yields better results due to:

- The auxiliary electrode is accounting for both, temperature and absolute humidity. The latter could be discarded if the relative humidity is not considered.
- Since data is treated in a day to day basis, variations of mean temperatures during different days could provoke significant correlations to be found at different timelapses. This provokes gaps in the prediction during night hours that are reduced by the use of the auxiliary electrode.
- Finally, it is preferrably to use data contained in a single sensor (such as the auxiliary electrode for the EC sensor) rather than including additional sensors in the algorithm.

A comparison between the results using this proposed method and the reference measurement from both test campaigns is seen below:

||Manufacturer Method|Baseline Method With Temperature|Baseline Method With Auxiliary Electrode|
|:--|:--:|:--:|:--:|
|**Pollutant**|*RMSE / R2*|*RMSE / R2*|*RMSE / R2*|
|**CO (ppm)**| **0.2-0.3 / 0.3-0.5**| >2 / <0.1| >2 / <0.01|
|**NO~2~ (ppb)**| 21-24 / 0.3-0.5|6-12/0.1-0.4| **6 - 12 / 0.4 - 0.6**|
|**O3 (ppb)**|20-40 / 0.1-0.3|4-12 / <0.2| **4-9 / 0.1 - 0.3**|

## References

[^1]: [The use of electrochemical sensors for monitoring urban air quality
in low-cost, high-density networks - _M.I. Mead, O.A.M. Popoola, G.B. Stewart, P. Landshoff, M. Calleja, M. Hayesb, J.J. Baldovi, M.W. McLeod, T.F. Hodgson, J. Dicks, A. Lewis J. Cohen, R. Baron, J.R. Saffell, R.L. Jones_](https://www.sciencedirect.com/science/article/pii/S1352231012011284?via%3Dihub)

[^2]: [Development of a baseline-temperature correction methodology for
electrochemical sensors and its implications for long-term stability - _Olalekan A.M. Popoola*, Gregor B. Stewart, Mohammed I. Mead, Roderic L. Jones_](https://www.sciencedirect.com/science/article/pii/S1352231016308317?via%3Dihub)

[^3]: [Modelling atmospheric composition
in urban street canyons - _Vivien Bright, William Bloss and Xiaoming Cai_](https://rmets.onlinelibrary.wiley.com/doi/full/10.1002/wea.781)
