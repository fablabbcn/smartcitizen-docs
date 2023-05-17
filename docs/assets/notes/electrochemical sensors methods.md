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

![](/assets/images/qDp2cED.png)
**Background concentrations**. _Source [^3]_

#### Application on 4-electrode sensors

This algorithm can be used to correct temperature effects on the working electrode based on the temperature in 4-electrode sensors. The results are discussed below for tests validation campaigns performed  within the iScape project. These tests are summarized below:

- *University of Bologna*: data collected from 23/January to 13/February. The measured pollutants with reference equipments were CO, NO~2~, NO, NOx and O3. Two prototype Smart Citizen Stations were deployed in two different sites, with two Smart Citizen Kits.
- *University College Dublin*: data collected from 27/March to 17/April. The measured pollutants with reference equipments were NO, NO~2~ and NOX. One prototype Smart Citizen Station was deployed with two Smart Citizen Kits.

The results found with this methodology in the reduction sensors (NO~2~, O3) are significant in a daily basis. Two examples of the variation of the correlation coefficient with respect to the delta used to calculate the baseline are shown below:

![](/assets/images/PhA3UVN.png)

![](/assets/images/XL7OPTx.png)


The algorithm is set to apply the best performing correlation function from either a linear or an exponential fit, basing this decission on the one that yields better correlation coefficient. NO~2~ and O3 at high concentrations yield better results with an exponential fit, whilst lower concentrations reflect a linear trend:

![](/assets/images/yRUrTZJ.jpg)

Furthermore, the study from which this methodology is drawn from states that oxidation sensors do not yield a proper baseline correlation methodology and so is validated. The result is indeed far better correlated with the reference measurement if using the manufacturer's methodology:

![](/assets/images/F4uAY8y.jpg)

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
![](/assets/images/jW7qSaB.jpg)

Both, CO and NO~2~ pollutants, using the best method for each calculation, are shown below:

![](/assets/images/lripMLT.jpg)

Finally, a comparison between the reference measurement results from both methods is detailed below:

||Manufacturer Method|Baseline Method|
|:--|:--:|:--:|
|**Pollutant**|*RMSE / R2*|*RMSE / R2*|
|**CO (ppm)**| **0.2-0.3 / 0.3-0.5**| >2 / <0.01|
|**NO~2~ (ppb)**| 21-24 / 0.3-0.5| **6 - 12 / 0.4 - 0.6**|
|**O3 (ppb)**|20-40 / 0.1-0.3| **4-9 / 0.1 - 0.3**|


As seen above, the NO~2~ correlation with both methods yields significant results for non-corrected signals, whilst the RMSE values are higher in the case of the manufacturer's proposal. Therefore, for this pollutant, the selected methodology will be the baseline method. On the contrary, the CO measurements are highly uncorrelated with the baseline method, whilst the original manufacturer's proposal yields decent results. Finally, the O3 correlation levels are lower than the CO and NO~2~ measurements. This is possibly due to the O3 reference measurement equipment used in the Bologna campaing, since it shows an inverse relationship with NO~2~ which suggests a biased pollutant calculation in the reference equipment:

![](/assets/images/258Gec6.jpg)

As well, the results from UCD that are used as a reference for NO~2~, suggest a poor zero/span calibration of the equipment as it yields negative results that could spoil the NO~2~ correlation/model errors from those tests:

![](/assets/images/DbCuX0g.jpg)

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