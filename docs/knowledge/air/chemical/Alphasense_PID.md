---
card: true
name: Alphasense PID
field:
  - air
type:
  - external
target:
  - vocs
feature_img: /assets/images/alphasense-pid.jpg
feature_img_credit: "Alphasense"
excerpt: "A high-end PID from Alphasense to measure VOCs."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

## Working principle

PID technology appears to be the primary sensor element of choice for VOCs measurements and is often used for measurement of summary concentration [^2].

The sensor contains a ionization lamp. As compounds enter the detector they are bombarded by high-energy UV photons and are ionized when they absorb the UV light, resulting in ejection of electrons and the formation of positively charged ions. The ions produce an electric current, which is the signal output of the detector. The greater the concentration of the component, the more ions are produced, and the greater the current. The current is amplified and displayed on an ammeter or digital concentration display.

Substances with ionisation potential below the sensor's lamp specification will be measured as a whole, with very little specificity in the readings [^2][^26][^28].

## Usage and considerations

There is no dedicated metric for PID sensors: their output voltage is read by one of the [ADS1X15](/knowledge/other/TI_ADS1X15/) channels, depending on the address and channel where the sensor is connected:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| PID output voltage | `ADS1x15 ADC 0x48 Ch0` to `ADS1x15 ADC 0x4B Ch3` | V | See [ADS1X15](/knowledge/other/TI_ADS1X15/#usage-and-considerations) |

Alphasense PID sensors have an **analog voltage output**, proportional to the concentration of VOCs. They come in different models with different sensitivities and ranges, from ppb to ppm levels. Check the [Alphasense website](https://www.alphasense.com/index.php/products/pid-air/) for the datasheets and application notes of each model.

!!! info "Connecting to the SCK"
    There is no dedicated firmware support for PID sensors. They can be connected to the SCK as analog sensors through the [Analog Sensor Board](/hardware/boards/analog-sensor-board/), which reads the voltage with a [TI ADS1115](/knowledge/other/TI_ADS1X15/) ADC. The SCK will log the **voltage**, which needs to be converted to concentration in post-processing, using the sensitivity of the sensor and its baseline (zero) voltage.

Some considerations for using PID sensors:

- The sensor measures all the compounds with an ionisation potential below the energy of its lamp, so the reading is a **total VOC** measurement. The response to each compound is different, so the readings are normally expressed as _isobutylene equivalent_, the gas used for calibrating the sensors
- The baseline (zero) of the sensor needs to be determined periodically, for instance with a zero air filter
- The lamp and the electrodes get dirty over time and need periodic cleaning or replacement
- PID sensors consume more power than other low cost sensors, and need a stable power supply

### Measurement range

The measurement range depends on the model of the sensor. As an example, the high sensitivity **PID-AH2**, which is suitable for ambient air, has a linear range from **1 ppb to 50 ppm** (isobutylene equivalent). Other models are designed for higher concentrations (ppm level), for industrial safety applications. Make sure to check the datasheet of the model you are using.

## Limitations

When testing PID sensors in laboratory conditions, good performance has been achieved, however this has not been later on comparable to field results [^28]. Careful treatment of the readings, including electromagnetic noise, compensation for relative humidity changes, and power supply voltage stability, are a must for PID sensors [^28][^46].

## References

[^2]:
    Chojer, H., P.T.B.S. Branco, F.G. Martins, M.C.M. Alvim-Ferraz, and S.I.V. Sousa. “Development of Low-Cost Indoor Air Quality Monitoring Devices: Recent Advancements.” Science of The Total Environment 727 (July 2020): 138385. https://doi.org/10.1016/j.scitotenv.2020.138385.
[^26]:
    Zheng, Hailin, Vinayak Krishnan, Shalika Walker, Marcel Loomans, and Wim Zeiler. “Laboratory Evaluation of Low-Cost Air Quality Monitors and Single Sensors for Monitoring Typical Indoor Emission Events in Dutch Daycare Centers.” Environment International 166 (August 2022): 107372. https://doi.org/10.1016/j.envint.2022.107372.
[^28]:
    Xu, Wei, Yunfei Cai, Song Gao, Shuang Hou, Yong Yang, Yusen Duan, Qingyan Fu, Fei Chen, and Jie Wu. “New Understanding of Miniaturized VOCs Monitoring Device: PID-Type Sensors Performance Evaluations in Ambient Air.” Sensors and Actuators B: Chemical 330 (March 2021): 129285. https://doi.org/10.1016/j.snb.2020.129285.
[^46]:
    Lewis, Alastair C., James D. Lee, Peter M. Edwards, Marvin D. Shaw, Mat J. Evans, Sarah J. Moller, Katie R. Smith, et al. “Evaluating the Performance of Low Cost Chemical Sensors for Air Pollution Research.” Faraday Discussions 189 (2016): 85–103. https://doi.org/10.1039/C5FD00201J.
