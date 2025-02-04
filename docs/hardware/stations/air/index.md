---
internal:
  proofread: true
  links: true
  images: true
---

# Smart Citizen Air Quality Stations

The Air Quality (AQ) Station variations expand the [Kit](/hardware/kit/) with more advanced sensors, such as [electrochemical](/knowledge/air/chemical) or [CO2](/knowledge/air/co2) sensors. The units can be adapted to the particular monitoring needs of each case, thanks to their modular approach and _fab-ability_.

## Metrics

Generally, an AQ Station is a [Kit](/hardware/kit) with either [CO2](/knowledge/air/co2) or another [chemical composition](/knowledge/air/chemical) sensor. You can also measure with other _analog_ sensors (besides the electrochemical ones, **up to 16 analog channels** in total!), with a couple of [Analog Sensor Boards](/hardware/boards/analog-sensor-board/).

| Metric | Usage | Sensor | Interface Board | Calibration |
| :-: | :-: | :-: | :-: | :-: |
| Temperature and RH | Environmental Parameters | [Sensirion SHT3X](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X) | [Data board](/hardware/boards/data-board) | See [SHT31 page](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X#calibration)  |
| CO2 | _Normally_ Indoor AQ | [Sensirion SCD30](/knowledge/air/co2/Sensirion_SCD30) or [Sensirion SCD4X](/knowledge/air/co2/Sensirion_SCD4X) | [Data board](/hardware/boards/data-board)  | See [SCD30 CO2 page](/knowledge/air/co2/Sensirion_SCD30#calibration) |
| PM | AQ | [Plantower PMS5003](/knowledge/air/pm/Plantower_PMS5003),  [Sensirion SEN5X](/knowledge/air/pm/Sensirion_SEN5X) or [Sensirion SPS30](/knowledge/air/pm/Sensirion_SPS30) | [Urban Board](/hardware/boards/urban-board) or [PM Board](/hardware/boards/pm-board) for PMS5003 only. See sensor pages. | See [PM Knowledge page](/knowledge/air/pm/) |
| Chemical | AQ | [Alphasense Electrochemical](/knowledge/air/chemical/Alphasense_Electrochemical), also compatible with other Analog Sensors | [Analog Sensor Board](/hardware/boards/analog-sensor-board) | See [Chemical Composition Knowledge page](/knowledge/air/chemical/) |

![Smart Citizen Station Components](/assets/images/station-components.jpg)

!!! info "From the ground up"
    The Station uses the same core functionality, interface, and feedback as the Smart Citizen Kit. Get familiar with it before jumping into the Station!

    - [User interfaces](/hardware/kit/features/#user-interfaces)
    - [LED states and operation modes](/hardware/kit/features/#operation-modes)
    - [Software upgrades](/hardware/kit/features/#software-updates)

## Versions

{{ insert_cards(type="stations", filter="field", value=["air"]) }}

### Legacy versions

Below you will find some legacy (aka _development_) versions. These are left here for you to identify them, or in case you want some inspiration!

![iSCAPE Station V2.0](/assets/images/station-iscape-v2.jpg)
_Final iSCAPE Station version (iSCAPE-V2.0)_

!!! info "A note about versions"

    The **iScape Living Lab Station 1.0** was the development version for the 2.0 version. It was sponsored thanks to the [iSCAPE project](https://cordis.europa.eu/project/id/689954/results) under the European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en).

![iSCAPE Station V1.0](/assets/images/station-iscape-v1.jpg)
_iSCAPE Living Lab Station version (iSCAPE-V1.0)_