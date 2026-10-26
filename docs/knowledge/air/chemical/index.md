# Chemical Composition Measurements in Air

This page links to various sensors that can be used to measure chemical compounds found in the air, such as Volatile Organic Compounds (VOCs) and other chemical substances, such as Nitrogen Oxides (NO2, NO), Carbon Monoxide (CO), and many more!

## VOC

Volatile Organic Compounds (VOCs) are a complex mixture of chemical substances that are not simple, quick or cheap to characterise [^1]. In the case of VOCs, there are different techniques in the market for measuring them, for which there are very few performance evaluation studies that have tested systematically whether or not this type of sensor solutions qualify as quantitative Data Quality Objectives (DQO) as indicated by the AQD [^41]. It is generally not possible to confirm the sensor performances claimed by the manufacturers for various reasons, which are detailed below, so systematic testing of the devices and particular attention to the field of study at hand is necessary.

Almost all low-cost sensors for measuring VOCs use one of the following techniques [^1][^41]:

* Photo Ionization Detector (PID)
* Metal Oxide Sensors (MOx)
* Electrochemical sensors

Almost all the techniques above, except some cases of MOx sensors, only provide measurements of **total Volatile Organic Compounds (tVOCs)**, and in all cases they provide decent readings in the ppb range (see PIDs). It is then important to emphasise the limitations of measuring them for exposure studies. In cases where selectivity (the ability to measure individual VOCs or aggregated tVOCs) and low concentrations are needed, other techniques are more reliable, but not necessarily cheap in cost (price range up to USD 10k) [^45][^46].

For simpler, cheaper devices, tVOCs are generally the metric provided with very low selectivity, and the difficulty comes in when trying to perform sensor quality assessments in relation to reference equipment. This is due to the fact that a low-cost tVOCs sensor will not distinguish between different target species, and the sensitivity to each of them is not generally provided or determined by the manufacturer. This presents a challenge in defining firstly exactly what they are responding to, and in the case of using this data for scientific studies, what practical use this non-specific data has [^46]. Reference equipment might show different sensitivities to the same target species, and be more or less selective, so the tVOCs measurement is rendered useless for quantitative measurements, and should be used for trend assessment or qualitative analysis, especially at low ppb levels (<50 ppb) [^26][^28][^40][^41].

### Reference levels

There are no health-based guidelines for **total VOCs**, since their effect depends on the specific compounds in the mixture. As an orientation, the German Environment Agency (UBA) uses the following levels for indoor air [^47]:

| Level | TVOC (mg/m3) | Interpretation |
|:-: |:-: |:- |
| 1 | < 0.3 | Hygienically safe. Target value |
| 2 | 0.3 – 1 | Still hygienically safe, if no individual substance is too high |
| 3 | 1 – 3 | Hygienically noticeable. Look for sources and ventilate more. Should not stay above this level for more than 12 months |
| 4 | 3 – 10 | Hygienically of concern. Ventilate and find the source. Should not stay above this level for more than one month |
| 5 | > 10 | Hygienically unacceptable. Avoid using the room |

The conversion between mg/m3 and ppb depends on the mixture of compounds, so these levels can only be compared with sensors that report TVOC in mass units, and after a proper calibration. Most low-cost sensors report **relative** values, which are better interpreted as trends:

- **Sensirion VOC index** ([SEN5X](/knowledge/air/pm/Sensirion_SEN5X/)): a value of **100** corresponds to the average conditions of the last 24 hours. Values above 100 mean more VOCs than usual (for instance, cooking or cleaning), and values below 100 mean less. Similarly, the **NOx index** has a baseline of **1**, and higher values indicate NOx events (for instance, a gas stove)
- **MOx resistance** ([BME680](/knowledge/air/chemical/Bosch_BME680/), [TGS260X](/knowledge/air/chemical/Figaro_TGS260X/)): a **lower** resistance means **more** reducing gases. Compare with the sensor's own baseline in clean air
- **eTVOC** ([CCS811](/knowledge/air/chemical/AMS_CCS811/)): an estimated value in ppb, useful to detect events, but not comparable with the levels above

For **formaldehyde** (measured by the [SFA30](/knowledge/air/chemical/Sensirion_SFA30/)), the WHO indoor air quality guideline is **0.1 mg/m3** (around **80 ppb**) as a 30-minute average, to prevent sensory irritation, which also protects from long-term effects [^48].

### Supported sensors

{{ insert_cards(type="sensor", filter="target", value=["vocs"])}}

## Other chemical measurements

Chemical composition sensors are those that are able to measure a specific chemical target species that are present in the air. Current state of the art of these sensors has proven capabilities of measuring CO, NO2, NO, SO2, H2S, O3, among others. Measurement principles, limitations and technologies available are different for these different target species. Most of the sensors available in the market are based on two types of technologies: electrochemical sensors, and metal oxides [^14].

### Reference levels

The table below shows the WHO air quality guidelines [^49] and the European Union limit values that apply from 2030 [^50] for the main gaseous pollutants. Concentrations are given in µg/m3 (mg/m3 for CO), and the approximate equivalent in ppb (ppm for CO) at 20 ºC and 1 atm is shown in brackets:

| Pollutant | Averaging period | WHO guideline (2021) | EU limit value (2030) |
|:- |:- |:-: |:-: |
| NO2 | 1 hour | 200 µg/m3 (105 ppb) | 200 µg/m3 (max. 3 hours per year) |
| NO2 | 24 hours | 25 µg/m3 (13 ppb) | 50 µg/m3 (max. 18 days per year) |
| NO2 | Year | 10 µg/m3 (5 ppb) | 20 µg/m3 |
| O3 | 8 hours | 100 µg/m3 (50 ppb) | 120 µg/m3 (target value) |
| O3 | Peak season | 60 µg/m3 (30 ppb) | - |
| SO2 | 10 minutes | 500 µg/m3 (188 ppb) | - |
| SO2 | 1 hour | - | 350 µg/m3 (max. 3 hours per year) |
| SO2 | 24 hours | 40 µg/m3 (15 ppb) | 50 µg/m3 (max. 18 days per year) |
| CO | 8 hours | 10 mg/m3 (8.6 ppm) | 10 mg/m3 |
| CO | 24 hours | 4 mg/m3 (3.4 ppm) | 4 mg/m3 (max. 18 days per year) |

The conversion factors used are: 1 ppb of NO2 = 1.91 µg/m3, 1 ppb of O3 = 2.00 µg/m3, 1 ppb of SO2 = 2.66 µg/m3 and 1 ppm of CO = 1.16 mg/m3.

!!! warning "Low-cost gas sensors"
    Typical outdoor concentrations of these gases are in the low ppb range, which is at the limit of what low-cost sensors can measure. The readings of [MOx sensors](/knowledge/air/chemical/SGX_MICS/) cannot be compared with these values, and [electrochemical sensors](/knowledge/air/chemical/Alphasense_Electrochemical/) need a careful calibration (ideally, co-located with a reference station) before doing so.

### Supported sensors

{{ insert_cards(type="sensor", filter="target", value=["chemical"])}}

We currently support electrochemical sensors from [Alphasense Ltd.](https://www.alphasense.com/index.php/air/) with a digital interface [Analog Sensor Board](/hardware/boards/analog-sensor-board/) that can operate at 3.3V or 5V. The basic data postprocessing that is specified in [Alphasense Application Note 803_04](/assets/notes/alphasense-an-803-04-zero-offset.pdf) is implemented as a default processing for these sensors and that we can [trigger automatically](/guides/data/custom-data-processing/).

Other sensors can be used, such as [SPEC Sensors](https://www.spec-sensors.com/), with the same hardware (**note that these sensors operate at 3.3V**). The process is now been worked on in this [thread in our forum](https://forum.smartcitizen.me/t/smart-citizen-station-extended-with-anemometer-rain-gps-4g-radio-and-solar/1622) and will be integrated in the basic data postprocessing as with Alphasense sensors to be triggered automatically.

The sensors that are currently supported are:

- [Alphasense Sensors](https://www.alphasense.com/product_type/air-quality-sensors/): CO, NO2, NO, OX, SO2, H2S, both in A or B-Series. These sensors are affected differently by temperature and humidity (some of them are by both, some of them are not). It is important to consider cross-sensitivity of the sensors in this case, for instance:
    + OX sensor is affected by NO2 and O3
    + SO2 is affected by SO2 and O3
- [SPEC Sensors (experimental)](https://www.spec-sensors.com/product-category/analog-gas-sensors/): CO, NO2, SO2, O3, H2S


## References

[^1]:
    Szulczyński, Bartosz, and Jacek Gębicki. “Currently Commercially Available Chemical Sensors Employed for Detection of Volatile Organic Compounds in Outdoor and Indoor Air.” Environments 4, no. 1 (March 6, 2017): 21. https://doi.org/10.3390/environments4010021.
[^14]:
    Clements, A., S. Lung, A. Arfire, AND A. Polidori. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition: Evaluation Activities. An Update on Low-Cost Sensors for the Measurement of Atmospheric Composition. World Meteorological Organization, Geneva, Switzerland, , NA, (2020).
[^26]:
    Zheng, Hailin, Vinayak Krishnan, Shalika Walker, Marcel Loomans, and Wim Zeiler. “Laboratory Evaluation of Low-Cost Air Quality Monitors and Single Sensors for Monitoring Typical Indoor Emission Events in Dutch Daycare Centers.” Environment International 166 (August 2022): 107372. https://doi.org/10.1016/j.envint.2022.107372.
[^28]:
    Xu, Wei, Yunfei Cai, Song Gao, Shuang Hou, Yong Yang, Yusen Duan, Qingyan Fu, Fei Chen, and Jie Wu. “New Understanding of Miniaturized VOCs Monitoring Device: PID-Type Sensors Performance Evaluations in Ambient Air.” Sensors and Actuators B: Chemical 330 (March 2021): 129285. https://doi.org/10.1016/j.snb.2020.129285.
[^41]:
    Spinelle, Laurent, Michel Gerboles, Gertjan Kok, Stefan Persijn, and Tilman Sauerwald. “Review of Portable and Low-Cost Sensors for the Ambient Air Monitoring of Benzene and Other Volatile Organic Compounds.” Sensors 17, no. 7 (June 28, 2017): 1520. https://doi.org/10.3390/s17071520.
[^40]:
    Pang, Xiaobing, Haijun Nan, Jinping Zhong, Daiqi Ye, Marvin D. Shaw, and Alastair C. Lewis. “Low-Cost Photoionization Sensors as Detectors in GC × GC Systems Designed for Ambient VOC Measurements.” Science of The Total Environment 664 (May 2019): 771–79. https://doi.org/10.1016/j.scitotenv.2019.01.348.
[^45]:
    Skog, Kate M., Fulizi Xiong, Hitoshi Kawashima, Evan Doyle, Ricardo Soto, and Drew R. Gentner. “Compact, Automated, Inexpensive, and Field-Deployable Vacuum-Outlet Gas Chromatograph for Trace-Concentration Gas-Phase Organic Compounds.” Analytical Chemistry 91, no. 2 (January 15, 2019): 1318–27. https://doi.org/10.1021/acs.analchem.8b03095.
[^46]:
    Lewis, Alastair C., James D. Lee, Peter M. Edwards, Marvin D. Shaw, Mat J. Evans, Sarah J. Moller, Katie R. Smith, et al. “Evaluating the Performance of Low Cost Chemical Sensors for Air Pollution Research.” Faraday Discussions 189 (2016): 85–103. https://doi.org/10.1039/C5FD00201J.

[^47]:
    Umweltbundesamt. “Beurteilung von Innenraumluftkontaminationen mittels Referenz- und Richtwerten. Handreichung der Ad-hoc-Arbeitsgruppe der Innenraumlufthygiene-Kommission des Umweltbundesamtes und der Obersten Landesgesundheitsbehörden.” Bundesgesundheitsblatt 50 (2007): 990–1005. https://doi.org/10.1007/s00103-007-0290-y.
[^48]:
    World Health Organization. “WHO Guidelines for Indoor Air Quality: Selected Pollutants.” Copenhagen: WHO Regional Office for Europe, 2010. https://www.who.int/publications/i/item/9789289002134.
[^49]:
    World Health Organization. “WHO Global Air Quality Guidelines: Particulate Matter (PM2.5 and PM10), Ozone, Nitrogen Dioxide, Sulfur Dioxide and Carbon Monoxide.” Geneva: World Health Organization, 2021. https://www.who.int/publications/i/item/9789240034228.
[^50]:
    Directive (EU) 2024/2881 of the European Parliament and of the Council of 23 October 2024 on ambient air quality and cleaner air for Europe. https://eur-lex.europa.eu/eli/dir/2024/2881/oj/eng.
