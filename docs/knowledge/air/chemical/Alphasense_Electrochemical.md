---
card: true
name: Alphasense EC Sensors
field:
  - air
type:
  - external
target:
  - chemical
feature_img: /assets/images/alphasense-electrochemical-sensors.jpg
feature_img_credit: "Alphasense"
excerpt: "Electrochemical sensors for a variety of chemical pollutants"
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

In electrochemical (EC) sensors a gaseous pollutant undergoes a chemical reaction that results in a signal – typically manifested as a current – that is related to the concentration of the target gas in the air [^14]. This type of sensor is called an amperometric gas sensor. Since the interface to this sensor is normally provided as a current reading, dedicated circuitry is necessary to convert such to a voltage reading, for which an Analog to Digital converter (ADC) will suffice on the data-logger side. Signal processing and calculation of the final concentrations can be done in different ways, some of which rely on physically rooted models or, more commonly, on empirical evaluations (e.g., linear models) or even black-box models shaped by sample-based knowledge (e.g., machine learning models).

## Working principle

The electrochemical cells used are toxic gas sensors from Alphasense Ltd. that operate in an amperometric mode. That is, they generate a current that is linearly proportional to the fractional volume of the toxic gas in the environment:

![](/assets/images/alphasense-electrochemical-working-principle.png)

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

Therefore, while the sensor response is exposed to the target gas, it creates a current flowing from the working to the counter electrode or viceversa (depending on the oxidative or reductive nature of the target gas). This current has been found to be nicely responsive to target gas and therefore subject to characterisation and calibration.

### Reduction vs Oxidation Electrochemical Sensor

As mentioned above, the **counter electrode** is meant to balance the reaction of the working electrode. This determines the current direction within the board: whether it _goes from the working electrode to the counter electrode_ or viceversa.

- Oxidation sensors, such as CO, provoke a positive current **out of the working electrode** and the larger the amount of CO present, the larger (positive) is this current.

- Reduction sensors, such as NO~2~, provoke a negative current, i.e: **going into the sensor** and the larger the amount of NO~2~ present, the larger (negative) is this current

## Usage and considerations

The electrochemical sensors are connected to the SCK through the [Analog Sensor Board](/hardware/boards/analog-sensor-board/) (ASB), which reads the working (`W`) and auxiliary (`A`) electrodes of each sensor with two [TI ADS1115](/knowledge/other/TI_ADS1X15/) ADCs. The firmware does not know which sensor is connected to each channel: it reports the raw voltage of each ADC channel, named after the ADC address and the channel number:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| ADC `0x48`, channels 0 to 3 | `ADS1x15 ADC 0x48 Ch0` to `ADS1x15 ADC 0x48 Ch3` | V | [133](https://api.smartcitizen.me/v0/sensors/133), [134](https://api.smartcitizen.me/v0/sensors/134), [135](https://api.smartcitizen.me/v0/sensors/135), [136](https://api.smartcitizen.me/v0/sensors/136) |
| ADC `0x49`, channels 0 to 3 | `ADS1x15 ADC 0x49 Ch0` to `ADS1x15 ADC 0x49 Ch3` | V | [138](https://api.smartcitizen.me/v0/sensors/138), [139](https://api.smartcitizen.me/v0/sensors/139), [140](https://api.smartcitizen.me/v0/sensors/140), [141](https://api.smartcitizen.me/v0/sensors/141) |

Check the [ADS1115 knowledge page](/knowledge/other/TI_ADS1X15/) for the other addresses. Which channels belong to which sensor and electrode is stored with the [calibration data](/guides/data/handling-calibration-data/) of the device (e.g. `AS_48_01` is an Alphasense sensor with its working electrode on channel 0 and its auxiliary electrode on channel 1 of the ADC `0x48`).

!!! warning "Gases Board"
    Older units, such as the ones of the iSCAPE project, used the [Gases Pro Board](/hardware/boards/gases-pro-board/) (`SCK_WITH_GASES_BOARD` firmware flag), which reported the electrodes of each slot as `Gases Board 1W`, `Gases Board 1A`, etc. This board is discontinued and no longer sold: new units use the Analog Sensor Board.

Pollutant concentrations are not calculated by the firmware: they are derived in post-processing (see [Data processing](#data-processing) below) and published on the platform as:

| Metric | Units | API |
|:- |:-: |:- |
| CO | ppb | [152](https://api.smartcitizen.me/v0/sensors/152) |
| NO2 | ppb | [153](https://api.smartcitizen.me/v0/sensors/153) |
| NO | ppb | [154](https://api.smartcitizen.me/v0/sensors/154) |
| SO2 | ppb | [155](https://api.smartcitizen.me/v0/sensors/155) |
| H2S | ppb | [156](https://api.smartcitizen.me/v0/sensors/156) |
| O3 | ppb | [157](https://api.smartcitizen.me/v0/sensors/157) |

### Measurement range

The range of each sensor depends on its target gas. These are the ranges of the B4 series sensors, according to the manufacturer (the A4 series have similar targets, check their datasheets):

| Sensor | Target gas | Measurement range |
|:- |:- |:-: |
| CO-B4 | Carbon monoxide | 0 – 1000 ppm |
| NO2-B43F | Nitrogen dioxide | 0 – 20 ppm |
| NO-B4 | Nitric oxide | 0 – 20 ppm |
| OX-B431 | Ozone + Nitrogen dioxide | 0 – 20 ppm |
| SO2-B4 | Sulphur dioxide | 0 – 100 ppm |
| H2S-B4 | Hydrogen sulphide | 0 – 100 ppm |

Note that ambient concentrations are generally in the ppb range, so the useful part of the range is the very low end, where the noise and the baseline (zero) of the sensors are very important. Check the [Alphasense website](https://www.alphasense.com/products/) for the latest datasheets of each sensor.

### Stabilisation

The electrochemical sensors **need stabilisation time under the testing conditions** they will be at. It is important to set and power the sensors with sufficient time (1-2 days) on the test environment for them to adapt. The newer the sensor, the more stabilisation time it requires. In general, you will be receiving brand new sensors.

Humidity and temperature extremes will require of further sensor adaptation, in order to dry out or absorb the necessary humidity for their proper functioning.

!!! danger
    Do not extract/attach the sensor capsule from the base board while powered, this could irreversibly damage the sensor.

### Limitations

Electrochemical sensors have a good sensitivity, but their readings are affected by a series of factors:

- **Temperature and humidity**: both their absolute levels and the speed at which they change. Fast changes can induce short-term instabilities that show up as noise and artefacts in the readings. If not cleaned, these artefacts lead to wrong readings and to wrong calibration models, especially when using machine learning algorithms [^21]. Indoors, these changes can be more abrupt due to human activity (opening windows and doors, heating or air conditioning, etc.). For this reason, the temperature and humidity of the air around the sensors are always measured along with the electrodes.
- **Cross-sensitivity** to other pollutants. For instance, the OX-B431 responds to both O~3~ and NO~2~, and needs an NO~2~ sensor to derive O~3~.
- **Ageing and drift**, which cause a loss of sensitivity and a deviation of the baseline over time [^14].

The laboratory calibration provided by Alphasense does not account for all these effects in the deployment conditions. It provides good enough information to start a deployment and follow trends, but accurate readings need further calibration in the field (see [Data processing](#data-processing)).

## Data processing

The raw electrode voltages are converted to pollutant concentrations outside of the units. There are different ways of doing so, such as:

- physically rooted models
- empirical (e.g. linear) models
- to black-box models trained with data (e.g. machine learning).

### Default processing

The default data processing workflow is the **direct calculation of the pollutants based on the laboratory calibration provided by Alphasense**, following the [Alphasense Application Note 803-04](/assets/notes/alphasense-an-803-04-zero-offset.pdf). Alphasense provides the calibration data (electronic zero, sensitivity, and cross-sensitivity to NO~2~ where applicable) for each individual sensor. With it, the processing:

1. Subtracts the electronic zero of each electrode.
2. Corrects the working electrode with the auxiliary electrode, using the temperature-dependent factors given in the application note.
3. Removes the NO~2~ cross-sensitivity (for the OX sensor).
4. Converts the result to ppb with the sensor sensitivity.

This processing runs periodically in [Smart Citizen Flows](https://flows.smartcitizen.me), using the algorithms in [scdata](https://github.com/fablabbcn/smartcitizen-data/), and the results are published on the platform with the metrics listed [above](#usage-and-considerations). Check the [data processing guide](/guides/data/custom-data-processing/) to know how to set it up, or how to try other algorithms yourself.

### Long processing

In addition, [smartcitizen-flows](https://github.com/fablabbcn/smartcitizen-flows) can run a longer batch processing on a window of several months of data (90 days by default) of each device. Instead of relying only on the zero from the laboratory calibration, it estimates the baseline of the working electrode from the data itself, with an asymmetric least squares (ALS) algorithm, and corrects the auxiliary electrode against it, in a similar way as in [^3]. These results are not published on the platform. This processing is used in research projects and is **not offered commercially**.

### Calibration with reference stations

The processing above is based on the laboratory calibration, and it might not suffice when the sensors are exposed to other pollutants or to harsh environments. For this reason, many groups do a finer calibration by **co-locating the units near a reference grade station** for a period of time, and deriving additional calibration factors, from linear and multilinear corrections to machine learning models [^1] [^7] [^8] [^9] [^14]. These models can be specific to each site and sensor, or general models derived from several co-locations [^6]. Since a model can only be trusted in conditions similar to the ones it was trained with, a co-location before and after the deployment is recommended [^5] [^6]. Keep in mind as well that the quality of the reference data matters: reference stations can deviate up to 15% from the actual concentration [^6].

Check the [calibration section](/knowledge/calibration/) for more information.

## Resources

Below you can find a small selection of publications on these sensors:

[^1]:In search of an optimal in-field calibration method of low-cost gas sensors for ambient air pollutants. Comparison of linear, multilinear and artificial neural network approaches. In Atmospheric Environment (2018): https://doi.org/10.1016/j.atmosenv.2019.06.028
[^2]:The use of electrochemical sensors for monitoring urban air quality in low-cost, high-density networks: https://www.sciencedirect.com/science/article/pii/S1352231012011284?via%3Dihub
[^3]:Development of a baseline-temperature correction methodology for electrochemical sensors and its implications for long-term stability: https://www.sciencedirect.com/science/article/pii/S1352231016308317?via%3Dihub
[^4]:Modelling atmospheric composition in urban street canyons: https://rmets.onlinelibrary.wiley.com/doi/full/10.1002/wea.781
[^5]:ISCAPE D7.8 Sensor monitoring experiences and technological innovations: [link](/assets/publications/iSCAPE_D78.pdf)
[^6]:Node-to-node field calibration of wireless distributed air pollution sensor network. In Environmental pollution (2017): https://doi.org/10.1016/j.envpol.2017.09.042
[^7]:Spinelle, L., M. Gerboles, M. G. Villani, M. Aleixandre, and F. Bonavitacola. Field calibration of a cluster of low-cost available sensors for air quality monitoring. Part A: Ozone and nitrogen dioxide. In Sensors and Actuators B: Chemical (2015): https://doi.org/10.1016/j.snb.2015.03.031
[^8]:Hagan, D. H., G. Isaacman-VanWertz, J. P. Franklin, L. M. M. Wallace, B. D. Kocar, C. L. Heald, and J. H. Kroll. Calibration and assessment of electrochemical air quality sensors by co-location with regulatory-grade instruments. In Atmospheric Measurement Techniques (2018): https://doi.org/10.5194/amt-11-315-2018
[^9]:Zimmerman, N., A. A. Presto, S. P. N. Kumar, J. Gu, A. Hauryliuk, E. S. Robinson, A. L. Robinson, and R. Subramanian. A machine learning calibration model using random forests to improve sensor performance for lower-cost air quality monitoring. In Atmospheric Measurement Techniques (2018): https://doi.org/10.5194/amt-11-291-2018
[^14]:
    Clements, A., S. Lung, A. Arfire, AND A. Polidori. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition: Evaluation Activities. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition. World Meteorological Organization, Geneva, Switzerland, , NA, (2020).
[^21]:
    iSCAPE Project Deliverable 7.8 Sensor monitoring experiences and technological innovations (November 2019). (Accessed January 2023) https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5cff9eb33&appId=PPGMS