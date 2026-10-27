<!-- Source: https://docs.smartcitizen.me/hardware/stations/air/ -->

# Smart Citizen Air Quality Stations

The Air Quality (AQ) Station variations expand the [Kit](https://docs.smartcitizen.me/hardware/kit.md) with more advanced sensors, such as [electrochemical](https://docs.smartcitizen.me/knowledge/air/chemical.md) or [CO2](https://docs.smartcitizen.me/knowledge/air/co2.md) sensors. The units can be adapted to the particular monitoring needs of each case, thanks to their modular approach and _fab-ability_.

## Metrics

Generally, an AQ Station is a [Kit](https://docs.smartcitizen.me/hardware/kit.md) with either [CO2](https://docs.smartcitizen.me/knowledge/air/co2.md) or another [chemical composition](https://docs.smartcitizen.me/knowledge/air/chemical.md) sensor. You can also measure with other _analog_ sensors (besides the electrochemical ones, **up to 16 analog channels** in total!), with a couple of [Analog Sensor Boards](https://docs.smartcitizen.me/hardware/boards/analog-sensor-board.md).

| Metric | Usage | Sensor | Interface Board | Calibration |
| :-: | :-: | :-: | :-: | :-: |
| Temperature and RH | Environmental Parameters | [Sensirion SHT3X](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X.md) | [Data board](https://docs.smartcitizen.me/hardware/boards/data-board.md) | See [SHT31 page](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X.md#calibration)  |
| CO2 | _Normally_ Indoor AQ | [Sensirion SCD30](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD30.md) or [Sensirion SCD4X](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD4X.md) | [Data board](https://docs.smartcitizen.me/hardware/boards/data-board.md)  | See [SCD30 CO2 page](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD30.md#calibration) |
| PM | AQ | [Plantower PMS5003](https://docs.smartcitizen.me/knowledge/air/pm/Plantower_PMS5003.md),  [Sensirion SEN5X](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SEN5X.md) or [Sensirion SPS30](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SPS30.md) | [Urban Board](https://docs.smartcitizen.me/hardware/boards/urban-board.md) or [PM Board](https://docs.smartcitizen.me/hardware/boards/pm-board.md) for PMS5003 only. See sensor pages. | See [PM Knowledge page](https://docs.smartcitizen.me/knowledge/air/pm.md) |
| Chemical | AQ | [Alphasense Electrochemical](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_Electrochemical.md), also compatible with other Analog Sensors | [Analog Sensor Board](https://docs.smartcitizen.me/hardware/boards/analog-sensor-board.md) | See [Chemical Composition Knowledge page](https://docs.smartcitizen.me/knowledge/air/chemical.md) |

![Smart Citizen Station Components](https://docs.smartcitizen.me/assets/images/station-components.jpg)

!!! info "From the ground up"
    The Station uses the same core functionality, interface, and feedback as the Smart Citizen Kit. Get familiar with it before jumping into the Station!

    - [User interfaces](https://docs.smartcitizen.me/hardware/kit/features.md#user-interfaces)
    - [LED states and operation modes](https://docs.smartcitizen.me/hardware/kit/features.md#operation-modes)
    - [Software upgrades](https://docs.smartcitizen.me/hardware/kit/features.md#software-updates)

## Versions

!!! info ""
    The stations below are the current stable designs. If you are looking into developing other versions, feel free to reach out via [info@smartcitizen.me](mailto:info@smartcitizen.me).

- [SCK + 1xCHEM](https://docs.smartcitizen.me/hardware/stations/air/sck-1xchem.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure 1 chemical composition metric with an Alphasense B-series electrochemical sensor.
- [SCK + 2xCHEM](https://docs.smartcitizen.me/hardware/stations/air/sck-2xchem.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure 2 chemical composition metrics with two Alphasense A-series electrochemical sensors.
- [SCK + CO2 + 2xCHEM](https://docs.smartcitizen.me/hardware/stations/air/sck-co2-2xchem.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor and 2 chemical composition metrics with Alphasense A-series electrochemical sensors.
- [SCK + CO2 + HCHO](https://docs.smartcitizen.me/hardware/stations/air/sck-co2-hcho.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 and Formaldehyde!
- [SCK + CO2](https://docs.smartcitizen.me/hardware/stations/air/sck-co2.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor!
- [SCK + T / RH](https://docs.smartcitizen.me/hardware/stations/air/sck-temp.md) (Grade | basic): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure temperature and humidity with a weatherproof probe!


### Legacy versions

Below you will find some legacy (aka _development_) versions. These are left here for you to identify them, or in case you want some inspiration!

![iSCAPE Station V2.0](https://docs.smartcitizen.me/assets/images/station-iscape-v2.jpg)
_Final iSCAPE Station version (iSCAPE-V2.0)_

!!! info "A note about versions"

    The **iScape Living Lab Station 1.0** was the development version for the 2.0 version. It was sponsored thanks to the [iSCAPE project](https://cordis.europa.eu/project/id/689954/results) under the European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en).

![iSCAPE Station V1.0](https://docs.smartcitizen.me/assets/images/station-iscape-v1.jpg)
_iSCAPE Living Lab Station version (iSCAPE-V1.0)_