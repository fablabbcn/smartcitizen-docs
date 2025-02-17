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

Alphasense Ltd. provides the calibration data in laboratory conditions for each of the electrochemical cells used. This data can be used to calculate pollutant concentration and to correct for _known effects_ by temperature deviations.

!!! info "More on this"
    Alphasense Ltd. provides very useful application notes for the sensor usage.

Pollutant calculation based on calibration data in laboratory conditions, can be insightful enough for certain applications, but it might not suffice for some conditions in which the sensors are exposed to other pollutants or in harsh environments. For this reason, two different approaches build on top of the laboratory calibration data:

- Usage of more advanced physical models as detailed in [^1]
- Usage of site-specific calibration models with short-term deployments in co-location with reference measurement equipment and generalised calibration models derived from the junction of these [^4].

### Stabilisation

The electrochemical sensors **need stabilisation time under the testing conditions** they will be at. It is important to set and power the sensors with sufficient time (1-2 days) on the test environment for them to adapt. The newer the sensor, the more stabilisation time it requires. For this deployment, you will be receiving brand new sensors.

Humidity and temperature extremes will require of further sensor adaptation, in order to dry out or absorb the necessary humidity for their proper functioning.

!!! danger
    Do not extract/attach the sensor capsule from the base board while powered, this could irreversibly damage the sensor.

### Limitations

Electrochemical sensors typically show a good sensitivity, however, they can be affected by a series of factors such as temperature, humidity, and the presence of other pollutants. Not only temperature and humidity absolute levels affect the readings, but also the speed at which the changes take place can induce short term instabilities on the readings that provoke noise and some artefacts. These artefacts can provoke two issues: wrong readings, and wrong calibrations, especially if not cleaned and when using machine learning algorithms [^21]. In addition, ageing and drift are known problems, which affect the loss of sensitivity and deviations in the baseline response [^14]. In general, it is a common practice to include temperature and humidity sensors of the target air, as well as the electrochemical cells used for the measurement. This is particularly relevant in the case of indoor environments, as mentioned above, since the absolute values and the changes can be more abrupt in certain times of the day due to human activity, i.e. opening windows, doors, heating and air conditioning activation, etc. Typically, the approach for the deployment of electrochemical sensors is to provide a factory base calibration, in laboratory conditions, and to correct this in the final deployment conditions, by co-locating the sensors with high-end instruments during a pre-assigned period of time [^14]. In most cases, a laboratory evaluation to derive linear models will not be sufficient, but will provide good enough information to kick-off the deployment. Specific on-site calibration is needed if accurate readings and other effects, as explained above, are to be compensated. This is a recommendation for the case of the TwinAIR pilots.

### Open questions

These methods, however, are still open to discussion and more research is necessary to address all use cases. For this reason, the use of these sensors in the Smart Citizen Station is tailored to each use and adapted to the calibration needs of the deployment.

Characterisation techniques based on manufacturer data and physical models (i.e. classical linear regression using sensor sensitivity, span and zero) require a big development effort in order to characterise the sensor behaviour that, in the case of low-cost sensors, is affected by a wide variety of external factors such as temperature, humidity and pollutant cross-sensitivity, each of which imply a larger characterisation effort and that can’t be fully represented in a controlled setting. On the other hand, statistical models are able to generate models that describe the sensor behaviour in a mathematical way, but they need to be properly adjusted with large amounts of test data, preferably in the actual deployment site. This approach can be applied per sensor, or to a batch of sensors, assuming that the inter-sensor variation is low or that they can be normalised.

In the case of deploying the sensors in different locations, the conditions of these sites should be sufficiently similar to those when the model was generated, since many models won’t be able to extrapolate well, or account for effects they have not seen (i.e. temperature gradients, specific pollutants, etc). How much is ​sufficiently similar​, depends on the type of model and it is not easy to determine and, since this is not often assessed easily, researchers suggest ([^5], [^6]) that a co-location prior to and post data acquisition with reference sensors should be carried out. In any case, the development of these models highly depends on the amount and quality of the data obtained from both: sensor data and reference data. In the case of reference data [^6] have pointed out that reference stations can deviate up to 15% from the actual pollutant concentration, but this has not been taken into account in this study.

Since co-location possibilities could be limited, two options are compared for the calibration of these sensors: a specific on-site calibration with sensor co-location, aiming to calibrate the sensors with the data from that period; and a general model approach, in which all the co-location tests from the different sensors deployed are input into a statistical model that aims to describe the global behaviour. Whether these methods are able to generalise or not, it's yet to be answered, and it's probably to be defined for each use case in particular.

## Resources

Below you can find a small selection of publications on these sensors:

[^1]:In search of an optimal in-field calibration method of low-cost gas sensors for ambient air pollutants. Comparison of linear, multilinear and artificial neural network approaches. In Atmospheric Environment (2018): https://doi.org/10.1016/j.atmosenv.2019.06.028
[^2]:The use of electrochemical sensors for monitoring urban air quality in low-cost, high-density networks: https://www.sciencedirect.com/science/article/pii/S1352231012011284?via%3Dihub
[^3]:Development of a baseline-temperature correction methodology for electrochemical sensors and its implications for long-term stability: https://www.sciencedirect.com/science/article/pii/S1352231016308317?via%3Dihub
[^4]:Modelling atmospheric composition in urban street canyons: https://rmets.onlinelibrary.wiley.com/doi/full/10.1002/wea.781
[^5]:ISCAPE D7.8 Sensor monitoring experiences and technological innovations: [link](/assets/publications/iSCAPE_D78.pdf)
[^6]:Node-to-node field calibration of wireless distributed air pollution sensor network. In Environmental pollution (2017): https://doi.org/10.1016/j.envpol.2017.09.042
[^14]:
    Clements, A., S. Lung, A. Arfire, AND A. Polidori. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition: Evaluation Activities. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition. World Meteorological Organization, Geneva, Switzerland, , NA, (2020).
[^21]:
    iSCAPE Project Deliverable 7.8 Sensor monitoring experiences and technological innovations (November 2019). (Accessed January 2023) https://ec.europa.eu/research/participants/documents/downloadPublic?documentIds=080166e5cff9eb33&appId=PPGMS