

### Sensor Evaluation Campaign

Prior to sensor deployment for the intervention monitoring, some of the Living Lab Stations will be evaluated and compared against reference measurement under different conditions. They will be deployed in several cities among the iScape partners in order to *1.* develop models for sensor calibration under different climatic and pollutant exposure conditions and *2.* assess data quality. This campaign intends to evaluate the Living Lab Station before it's deployment, and trying to prevent concerns raised about data quality that other low-cost sensor platforms [^2] [^3] [^4].

This evaluation will focus on the **real-world conditions calibration**, under wide range of exposure and climatic conditions, rather than developing tests in controlled conditions, as prior studies show discrepancies in the accuracy resulting from evaluation in laboratory conditions, versus that of outdoor conditions [^2] [^5] [^6]. The tests will be conducted by co-location of at least two stations per site with high-end sensors under the conditions indicated in [the test section](/Living%20Lab%20Station/#test) below.

The duration of the tests will be of 2,5 months, with two location changes. This is a compromise between the indications given in [^1] for at least 3-months campaign and the availability of high-end sensors for the evaluation. Nevertheless, this campaign intends to cover a range of conditions by the deployment of the Living Lab Station in diverse conditions, not only climatic but also exposure-wise. The location changes will also intend to evaluate how well the sensors are able to adapt to these exposure and climatic changes [^10]. The data will be uploaded to the [SmartCitizen Platform](http://www.smartcitizen.me) and will be analysed using the [Sensor Analysis Framework](/Sensor%20Analysis%20Framework). The results of this evaluation in terms of models will be uploaded to a dedicated [repository](https://github.com/fablabbcn/smartcitizen-iscape-models) and will be implemented on the SmartCitizen Platform for on-the-fly sensor data processing. This processing aims to provide an open platform for sensor analysis using data analysis techniques, need which has been highlighted by [^2] [^5] [^6] [^9].

As well, as stated in [^2] [^10] [^11], it is necessary to perform individual field calibration for low-cost sensors if measurements comparable to those of high-end solutions are targeted. However, this calibration might not always be feasible in a wide range of conditions, leading to non-generalised models which can perform badly out of the training datasets. This test campaign also aims to study this concern, with an evaluation for a cross calibration methodology, in which results from a limited subset of observations are applied to the complete dataset [^7]. If successful, this would be set ground for the development of calibration strategies where the sensors are co-located with a high-end sensor and posteriorly deployed for citizen-science activities, or long term monitoring of the iScape Living Labs interventions, where high end sensors might not be available. This co-location could be performed in a recurrent manner, performing sequences of calibration-deployment-calibration, using merging calibrations as suggested in [^11].

As a summary, this field campaign aims to cover the following points:

- Assess data quality levels and positioning with respect to the DQO set by the European Air Quality Directive
- Stablish match scores for the different range of sensors available in the Living Lab Station
- Validation and assessment of  [EC sensor methodology](/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors/#sensor-calibration) for NO2 and O3 compounds in urban conditions (urban background and traffic) in various sites
- Validation of PMS PM raw data accuracy and effect of climatic conditions
- Calibration of Alphasense’s EC sensors and PMS PM sensors for model quality improvement accounting for climatic conditions
- Feasibility assessment for the calibration of metal oxide sensor models with the use of reference data and/or Living Lab station data
- Validation of climatic sensors of the station itself (temperature, humidity, pressure)
- Drifts and stability:
    - Drifts and possible root causes for EC sensor sensitivities variations over time
    - Calibration stability for SGX MOS sensors
    - Sensor decay and recoverability of PMS sensors due to dust accumulation or others

#### Test

The table below shows a description of the proposed test campaign:

| Stage | Duration | Exposure | Reference equipment | Purpose |
|:---|:---:|:---:|:---:|:---:|
| Pre-test| 2 weeks| Urban Background| No| Stabilise electrochemical sensors to urban background on site.  and verify overall functioning|
| Low Exposure test | 1 month | Urban Background | Yes | Evaluate response in low transient areas and evaluate repeatability of urban background measurements in higher exposure testing phases |
| High Exposure test | 1 month | Urban with traffic (canyon or junction) | Yes | Evaluate response in high transient / high concentration areas and validate current model and post-processing approach. Propose further models with more variables |

The sites at which these calibration deployments are planned are:

| Site | Season | Reference equipment | Duration |
|:---|:---:|:---:|:---:|
|Bologna (Italy) |Summer| YES | 1 month |
|Guildford (England)| Autumn| YES | 2.5 months |
|Dublin (Ireland)| Autumn| YES | 2.5 months |
|Bottrop (Germany)|Autumn| YES | 2.5 months |
|Barcelona (Spain)|Spring| YES | >3 months |

#### Sensor Installation

Guidelines for representativeness of the results are given below:

**Height**

Between 2,5 and 3,5m. Not reachable by hand.

**Reference equipment position**

Within <2m and with similar exposure, air flow (both either on wall, or lamppost) [^7]

**Desirable measurements**

- Chemical compounds (higher priority above):
    - NO2
    - CO, O3
    - NOx, NO
    - NMHC

- Particulate Matter (higher priority above)
    - PM 2.5
    - PM 1.0, PM 10

- Climatic conditions (higher priority above)
    - Temperature and relative humidity
    - Wind speed and direction

!!! warning "Important Guidelines"

    Please, refer to the [sensor considerations section](/Living%20Lab%20Station/#sensor-considerations) for general information about the sensors. As well, take into account the following:

    - Avoid direct exposure to intense sunlight for long periods of time, since this can severely affect the measurements (direct sun or intense transients).

    - Avoid locations where high temperature or humidity transients are present since the sensor response is affected by these rapid changes.

    - Avoid locations with low air flow or with direct exposure to air conditioning exhausts.

### References

[^1]: [**Spinelle L., Aleixandre M., Gerboles M.** - 2013: Protocol of Evaluation and Calibration of Low-cost Gas Sensors for the Monitoring of Air Pollution. Joint Research Centre (Report EUR 26112 EN)](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC83791/eur%20report%20protocol%20evaluation.pdf)

[^2]: [**Nuria Castell, Franck R. Dauge, Philipp Schneider, Matthias  Vogt, Uri Lerner, Barak Fishbain, David Broday, Alena Bartonova** - 2018: Can commercial low-cost sensor platforms contribute to air quality monitoring and exposure estimates?](https://www.sciencedirect.com/science/article/pii/S0160412016309989)

[^3]: [**Snyder E., Watkins T., Solomon P., Thoma E.,Williams R., Hagler G., Shelow D., Hindin D., Kilaru V., Preuss P.** - 2013: The changing paradigm of air pollution monitoring. Environ. Sci. Technol. 47, 11369–11377](https://doi.org/10.1021/es4022602)

[^4]:  [**Lewis A., Edwards P.** - 2016: Validate personal air-pollution sensors](https://www.nature.com/news/validate-personal-air-pollution-sensors-1.20195)

[^5]:  [**Spinelle L., Gerboles M., Villani M.G., Aleixandre M., Bonavitacola F.** - 2015: Field calibration of a cluster of low-cost available sensors for air quality monitoring: Part A: Ozone and nitrogen dioxide](https://www.sciencedirect.com/science/article/pii/S092540051500355X)

[^6]: [**Spinelle L., Gerboles M., Villani M.G., Aleixandre M., Bonavitacola F.** - 2015: Field calibration of a cluster of low-cost available sensors for air quality monitoring: Part B: NO, CO and CO2](https://www.sciencedirect.com/science/article/pii/S092540051631070X#)

[^7]: [**David H. Hagan, Gabriel Isaacman-VanWertz, Jonathan P. Franklin, Lisa M. M. Wallace, Benjamin D. Kocar, Colette L. Heald, Jesse H. Kroll** - 2018: Calibration and assessment of electrochemical air quality sensors by co-location with regulatory-grade instruments](https://www.atmos-meas-tech.net/11/315/2018/)

[^8]: [**Olalekan A.M.Popoola, Gregor B.Stewart, Mohammed I.Mead, Roderic L.Jones** - 2016: Development of a baseline-temperature correction methodology forelectrochemical sensors and its implications for long-term stability](https://www.sciencedirect.com/science/article/pii/S1352231016308317?via%3Dihub)

[^9]: [**Sun L., ChunWong K., Wei P., Ye S., Huang H., Yang F.,Westerdahl D., Louie P.K.K., Luk C.W.Y., Ning Z.** - 2016. Development and application of a next generation air sensor network for the Hong Kong Marathon 2015. Air quality monitoring. Sensors 16, 211–229](https://doi.org/10.3390/s16020211)

[^10]: [**A. Ripoll , M. Viana, M. Padrosa, X. Querol, A.Minutolo, K.M. Houc, J.M. Barcelo-Ordinas, J. Garcia-Vidal** - 2018: Testing the performance of sensors for ozone pollution monitoring in a citizen science approach](https://doi.org/10.1016/j.scitotenv.2018.09.257)

[^11]: [**Philip J. D. Peterson, Amrita Aujla, Kirsty H. Grant, Alex G. Brundle, Martin R. Thompson, Josh Vande Hey and Roland J. Leigh** - 2017: Practical Use of Metal Oxide Semiconductor Gas Sensors for Measuring Nitrogen Dioxide and Ozone in Urban Environments, Sensors 2017, 17, 1653](http://www.mdpi.com/1424-8220/17/7/1653)