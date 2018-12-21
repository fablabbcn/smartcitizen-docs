Low Cost Sensors Calibration
============================

Low cost sensor calibration and assessment pose a great challenge for data quality objectives. We follow this **sensor calibration procedure** for the iScape sensor solution, which can be split into three stages:

<div style="text-align:center">
<image src="https://i.imgur.com/6BZqNrR.png" width="500px"/>
</div>

1. **Behaviour assesment**: in laboratory conditions, serving as base testing for assessing general sensor behaviour.

2. **Characterisation**: also in laboratory conditions, assess generic sensor parameters as sensitivity, zero and span.

3. **Modelisation with real world deployment**: including other variables such as environmental factors and sensor cross-sensitivity.

Each of these stages apply differently depending on the type of sensor. For instance the electrochemical sensors present in the *Station* are already characterised by the manufacturer, while the Metal Oxyde Sensors in the *Urban Board* of the *Smart Citizen Kit* are not. The different characteristics of these sensors make different calibration approaches to be carried out.

An **initial behaviour assessment** is to be carried out in laboratory conditions in order to determine the optimal operational modes. This includes basic parameters such as sensor response, heating time and temperature as well as more advanced ones such as heating pulse mode operation. For this purpose, a portable, open source, reproducible **test cell** has been developed for controlled testing with a web based acquisition interface.

![](https://i.imgur.com/A7HmeqM.jpg)

Secondly, **base calibration parameters** need to be determined in controlled conditions. In this stage, the aim would be to find parameters such as:

<div style="text-align:center">
<image src="https://i.imgur.com/FprLD0n.png" width="300px"/>
</div>

- **Sensor sensitivity**: the sensor response per each ppm of target pollutant in _nominal_ conditions
- **Zero**: the sensor reading in zero air (pure air at 25degC).
- **Sensor response** (t<sub>90</sub>)
- **Sensor range**: maximum and minimum readings for the sensor

Finally, after this initial calibration assessment, it is critical to gather as much data as possible from **long term sensor deployments**. These deployments should aim to cover the widest range of sensor exposure conditions, in order to generate robust models. While dealing with low cost sensors this stage is very important, as it is detailed in the sections below.

These sensor deployments serve for two main purposes: to generate **quantitative classification methods** that can classify the air quality in predefined ranges (i.e. 'poor', 'fair', good'); and to generate **predictive qualitative models** for more accurate values. Either of them need large amounts of data if the models are aimed to be representative. Additionally, by the mere nature of the data and the sensors themselves, these models would need to be:

- Robusts to noise
- Capable of learning non-linear relationships
- Handle multivariate inputs
- Capable of learning temporal dependence

These needs make **machine learning** methods great canditates for modeling the data. These methods are implemented in the Sensor Analysis Framework, as well as other _more traditional_ linear methods. The combination of these algorithms with large amounts of data gathered during the iScape project offers a great opportunity to demonstrate the use of low cost sensors for air quality monitoring.

### Smart Citizen Kits

Due to their construction, low-cost metal oxyde sensors suffer from high levels of spread in their baseline resistance and sensitivity. As well, these sensors are generally reactive to other pollutants in the atmosphere, with a low selectivity of the actual target pollutant and drifts in their behaviour can be seen after some weeks of exposure. As well, metal oxyde sensors show short and long term drifts in their calibrations. Therefore, metal oxyde sensors require a careful characterisation and modelisation in both, laboratory and open air conditions. 

<div style="text-align:center">
<image src="https://i.imgur.com/JfujXTA.png" width="500px"/>
</div>

Initially, a **sensor characterisation** in laboratory conditions is needed to assess sensitiviy, baseline resistances sensor-to-sensor spread, aiming to obtain normalising factors for each sensor or group of sensors.

Once **deployed**, data from the Smart Citizen Kits is ingested in the analysis framework and referenced with other sources, such as a Smart Citizen Station or another reference equipment available. When CO and NO~2~ reference data is available from nearby Living Lab Sation or other sources as EPA stations the iSCAPE Sensor Analysis Framework can be used to estimate the absolute values from the Smart Citizen Kits NO~2~ and CO sensors.

![](https://i.imgur.com/qFexJ8A.png)

After data collection, a **sensor re-assessment can be performed**, either in laboratory conditions or collocation with reference equipment. This stage serves for correction for the model parameters used during the deployment and to assess the sensor reliability and need for replacement.

!!! info "No references available"
	This approach might not always be possible. Then, CO and NO~2~ data should be considered as qualitative air pollutants indicators. We should qualitatively use the data to compare short time intervals (no longer than a week). We can ask questions as _Is pollution higher at night?_

### Smart Citizen Stations

**Electrochemical sensors** can achieve significant accuracy, but they require a particular data post-processing that combines the measurement at the sensor electrodes with the sensor characterisation on the factory as well as other environmental parameters as air temperature and relative humidity (i.e. absolute humidity). Luckily the manufacturer of these sensors, Alphasense, provides us with that reference data. However, the complexity of the operations performed can not be done inside the sensing device as it uses advanced operations as well as historical data from the same device. For that reason, the data needs to be post processed using the Sensors Analysis Framework. The algorithm is **in a beta stage** and later it will be applied automatically on the data once it arrives at the platform. More details can be found in the [*Electrochemical sensor baseline methodology* Section](https://docs.iscape.smartcitizen.me/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors/#sensor-calibration).

![](https://i.imgur.com/Mi896Jh.png)

This process doesn't require any on-site reference data but requires the data to be processed using the manufacturer calibration reference per sensor as well as other environmental values as temperature and humidity.

!!! info "References data is available"
	When referenced data from a nearby referenced source as an EPA station is available, the iSCAPE Sensor Analysis Framework can be used to validate the recorded data as well as performing the standard post-processing.

The selected **PM sensor** is as well, characterised by the manufacturer and it provides an accurate measurement with it's calibration. It's measurements can be as well improved when reference data is available, as some have noted that the PM sensors can be affected by relative humidity. 

!!! info "Plantower PMS 5003"
	Read more on the Plantower PMS 5003 implementation on the [**Gas Pro Sensor Board**](/Components/PM%20Sensor%20Board/).