Low Cost Sensors Calibration
============================

Low cost sensor calibration and assessment pose a great challenge for data quality objectives. We follow this **sensor calibration procedure**, which can be split into three stages:

<div style="text-align:center">
<image src="https://i.imgur.com/6BZqNrR.png" width="500px"/>
</div>

1. **Behaviour assesment**: in laboratory conditions, serving as base testing for assessing general sensor behaviour.

2. **Characterisation**: also in laboratory conditions, assess generic sensor parameters as sensitivity, zero and span.

3. **Modelisation with real world deployment**: including other variables such as environmental factors and sensor cross-sensitivity.

Each of these stages apply differently depending on the type of sensor. For instance the electrochemical sensors present in the *Station* are already characterised by the manufacturer, while the old SGX MICS4514 Metal Oxyde Sensors in the *Urban Board* of the *Smart Citizen Kit* are not. The different characteristics of these sensors make different calibration approaches to be carried out.

**Base calibration parameters** need to be determined in controlled conditions. In this stage, the aim would be to find parameters such as:

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

These needs make **machine learning** methods great canditates for modeling the data. These methods are implemented in the Sensor Analysis Framework, as well as other _more traditional_ linear methods. The combination of these algorithms with large amounts of data gathered during, for instance, the iScape project, offers a great opportunity to demonstrate the use of low cost sensors for air quality monitoring.

### Smart Citizen Kits

Due to their construction, low-cost metal oxyde sensors suffer from high levels of spread in their baseline resistance and sensitivity. As well, these sensors are generally reactive to other pollutants in the atmosphere, with a low selectivity of the actual target pollutant and drifts in their behaviour can be seen after some weeks of exposure. As well, metal oxyde sensors show short and long term drifts in their calibrations. 

<div style="text-align:center">
<image src="https://i.imgur.com/JfujXTA.png" width="500px"/>
</div>

Ideally, a **sensor characterisation** in laboratory conditions is needed to assess sensitiviy, baseline resistances sensor-to-sensor spread, aiming to obtain normalising factors for each sensor or group of sensors. Even if possible, the variability of the sensor behaviour during the deployment stage, makes the individual characterisation and calibration of the Metal Oxyde sensors unrealistic. For this reason, indicative measurements are to be expected from this type of low cost sensors. More information about the sensors present in the urban board of the SCK can be found in [this section](/Components/Urban Sensor Board/#a-word-about-metal-oxide-sensors).

### Smart Citizen Stations

**Electrochemical sensors** 

These sensors can achieve significant accuracy, but they require a particular data post-processing that combines the measurement at the sensor electrodes with the sensor characterisation on the factory as well as other environmental parameters as air temperature and relative humidity (i.e. absolute humidity). Luckily the manufacturer of these sensors, Alphasense, provides us with that reference data. However, the complexity of the operations performed can not be done inside the sensing device as it uses advanced operations as well as historical data from the same device. For that reason, the data needs to be post processed using the Sensors Analysis Framework. The algorithm is **in a beta stage** and later it will be applied automatically on the data once it arrives at the platform. More details can be found in the [*Electrochemical sensor baseline methodology* Section](https://docs.iscape.smartcitizen.me/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors/#sensor-calibration).

![](https://i.imgur.com/Mi896Jh.png)

This process doesn't require any on-site reference data but requires the data to be processed using the manufacturer calibration reference per sensor as well as other environmental values as temperature and humidity.

**PM sensor**

The selected PM sensor is internally characterised by the manufacturer and, it's readings are currently being evaluated. Preliminarily, the measurements can be as well improved when reference data is available, as some have noted that the PM sensors can be affected by relative humidity. 

!!! info "Plantower PMS 5003"
	Read more on the Plantower PMS 5003 implementation on the [**PM Sensor Board**](/Components/PM%20Sensor%20Board/).