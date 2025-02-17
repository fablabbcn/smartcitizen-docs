# Chemical Composition Measurements in Air

This page links to various sensors that can be used to measure chemical compounds found in the air, such as Volatile Organic Compounds (VOCs) and other chemical substances, such as Nitrogen Oxides (NO2, NO), Carbon Monoxide (CO), and many more!

## Supported sensors

### VOCs

{{ insert_cards(type="sensor", filter="target", value=["vocs"])}}

### Chemical substances: CO, NO2, NO, SO2, ...

We currently support electrochemical sensors from [Alphasense Ltd.](https://www.alphasense.com/index.php/air/) with a digital interface [Analog Sensor Board](/hardware/boards/analog-sensor-board/) that can operate at 3.3V or 5V. The basic data postprocessing that is specified in [Alphasense Application Note 803_04](/assets/notes/alphasense-an-803-04-zero-offset.pdf) is implemented as a default processing for these sensors and that we can [trigger automatically](/guides/data/custom-data-processing/).

Other sensors can be used, such as [SPEC Sensors](https://www.spec-sensors.com/), with the same hardware (**note that these sensors operate at 3.3V**). The process is now been worked on in this [thread in our forum](https://forum.smartcitizen.me/t/smart-citizen-station-extended-with-anemometer-rain-gps-4g-radio-and-solar/1622) and will be integrated in the basic data postprocessing as with Alphasense sensors to be triggered automatically.

The sensors that are currently supported are:

- [Alphasense Sensors](https://www.alphasense.com/product_type/air-quality-sensors/): CO, NO2, NO, OX, SO2, H2S, both in A or B-Series. These sensors are affected differently by temperature and humidity (some of them are by both, some of them are not). It is important to consider cross-sensitivity of the sensors in this case, for instance:
    + OX sensor is affected by NO2 and O3
    + SO2 is affected by SO2 and O3
- [SPEC Sensors (experimental)](https://www.spec-sensors.com/product-category/analog-gas-sensors/): CO, NO2, SO2, O3, H2S

{{ insert_cards(type="sensor", filter="target", value=["chemical"])}}