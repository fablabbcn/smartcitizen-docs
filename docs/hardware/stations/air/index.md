# Smart Citizen Air Quality Stations

The Air Quality (AQ) versions are designed to expand the [Kit](/hardware/kit/) with more advanced sensors, such as [electrochemical](/knowledge/air/chemical) or [CO2](/knowledge/air/co2) sensors. The units can be adapted to the particular monitoring needs, thanks to their modular approach and _fabbability_.

## Versions

{{ insert_cards(type="stations", filter="field", value=["air"]) }}

## Metrics

In general, a AQ station is a [Kit](/hardware/kit) with either [CO2](/knowledge/air/co2) or some [chemical composition](/knowledge/air/chemical) sensors. You can also measure other _analog_ sensors (besides the electrochemical ones, **up to 16 analog channels!** in total), with a couple [Analog Sensor Boards](/hardware/boards/Analog Sensor Board/).

| Metric | Usage | Sensor | Interface Board | Calibration |
| :-: | :-: | :-: | :-: | :-: |
| Temperature and RH | Environmental Parameters | [Sensirion SHT3X](/knowledge/air/temperature/Sensirion_SHT3X) | [Data board](/hardware/boards/Data Board) | See [SHT31 page](/knowledge/air/temperature/Sensirion_SHT3X#calibration)  |
| CO2 | _Normally_ Indoor AQ | [Sensirion SCD30](/knowledge/air/co2/Sensirion_SCD30) or [Sensirion SCD4X](/knowledge/air/co2/Sensirion_SCD4X) | [Data board](/hardware/boards/Data Board)  | See [SCD30 CO2 page](/knowledge/air/co2/Sensirion_SCD30X#calibration) |
| PM | AQ | [Plantower PMS5003](/knowledge/air/pm/Plantower_PMS5003),  [Sensirion SEN5X](/knowledge/air/pm/Sensirion_SEN5X) or [Sensirion SPS30](/knowledge/air/pm/Sensirion_SPS30) | [Urban Board](/hardware/boards/Urban Board) or [PM Board](/hardware/boards/PM Board) for PMS5003 only. See sensor pages. | See [PM Knowledge page](/knowledge/air/pm/) |
| Chemical | AQ | [Alphasense Electrochemical](/knowledge/air/chemical/Alphasense_Electrochemical), also compatible with other Analog Sensors | [Analog Sensor Board](/hardware/boards/Analog Sensor Board) | See [Chemical Composition Knowledge page](/knowledge/air/chemical/) |

![Smart Citizen Station Components](/assets/images/station-components.jpg)

!!! info "From the ground up"
    The Station uses the same core functionality, interface and feedback as the Smart Citizen Kit. Make sure you are familiar with them before jumping into the Station!

    - [User interfacees](/hardware/Smart Citizen Kit/#user-interfaces)
    - [LED states and operation modes](/hardware/Smart Citizen Kit/#operation-modes)
    - [Software upgrades](/hardware/Smart Citizen Kit/#software-updates)

### Legacy versions

Below you will find some legacy (aka _development_) versions. These are left here for you to identify them, or in case you want some inspiration!

![iSCAPE Station V2.0](/assets/images/station-iscape-v2.jpg)
_Final iSCAPE Station version (iSCAPE-V2.0)_

!!! info "A note about versions"

    The **iScape Living Lab Station 1.0** was the development version for the 2.0 version. It was sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

![iSCAPE Station V1.0](/assets/images/station-iscape-v1.jpg)
_iSCAPE Living Lab Station version (iSCAPE-V1.0)_