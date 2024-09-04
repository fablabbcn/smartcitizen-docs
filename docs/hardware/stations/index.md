---
toc_depth: 2
---

# Smart Citizen Stations

![Smart Citizen Station v3](/assets/images/station-field.jpg)

The Smart Citizen Stations (_Stations_ for short) are **open-source environmental monitoring systems**. They build upon the functionalities of the [Smart Citizen Kit](/hardware/Smart Citizen Kit), extending its sensing capabilities. The idea behind is to leverage the modularity of the [hardware](/hardware) and include more sensors, making some changes on the [enclosures](/hardware/enclosures) to make everything fit.

The _Stations_ come in different flavours and sizes. Sometimes, they are more bulky (the one in the picture above has roughly 15 sensors) and, sometimes, they are a bit smaller. For instance, there are [air quality](#air-quality) stations, or [water and soil](#soil-and-water) ones.

!!! info "Check the Kit first"
    Any Smart Citizen Station builds on the core components of the Kit (which means, everything [here](/hardware/Smart Citizen Kit) works the same way). The units can be used by to gather _field-specific_ environmental data, not only from a scientific point of view but also as a tool to engage local communities on environmental topics.

![Station Small Front](/assets/images/station-small-front.jpg)

!!! tip "Questions?"
    How can we collaborate for my next research project? How much will it cost to make one? Is it hard to install? You can contact our team at [info@smartcitizen.me](mailto: info@smartcitizen.me)

![Station Stack](/assets/images/station-v3-stack.jpg)

!!! info "Intentionally _hackable_, intentionally _fabbable_"
    The Smart Citizen Stations, from the enclosure, to the electronics, are _obviously_ open source. Many components can be fabricated and assembled in a [Fablab](https://www.fablabs.io/). By doing so, we hope to encourage **fully open environmental systems**, ensuring reproducibility through accessible resources. We hope that this allows people to make use of the development effort in a distributed way.

Any of the sensors in the list of [supported sensors](/knowledge/) can be used to build a _Station_. Below you have a summary of the most common configurations to get a taste of what it can do. Make sure to check the dedicated sections for each to get a complete description!

## Air Quality

The [Air Quality (AQ)](/knowledge/air/) versions are designed to expand the [Kit](/hardware/Smart Citizen Kit/) with more advanced sensors, such as [electrochemical](/knowledge/air/chemical) or [CO2](/knowledge/air/co2) sensors. The units can be adapted to the particular monitoring needs, thanks to their modular approach and _fabbability_.

### Available Metrics

In general, an AQ station is a [Kit](/hardware/Smart Citizen Kit) with either [CO2](/knowledge/air/co2) or some [chemical composition](/knowledge/air/chemical) sensors. You can also measure other _analog_ sensors (besides the electrochemical ones, **up to 16 analog channels!** in total), with a couple [Analog Sensor Boards](/hardware/boards/Analog Sensor Board/).

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

### Versions

{{ insert_cards(type="stations", filter="field", value=["air"]) }}

#### Legacy versions

Below you will find some legacy (aka _development_) versions. These are left here for you to identify them, or in case you want some inspiration!

![iSCAPE Station V2.0](/assets/images/station-iscape-v2.jpg)
_Final iSCAPE Station version (iSCAPE-V2.0)_

!!! info "A note about versions"

    The **iScape Living Lab Station 1.0** was the development version for the 2.0 version. It was sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

![iSCAPE Station V1.0](/assets/images/station-iscape-v1.jpg)
_iSCAPE Living Lab Station version (iSCAPE-V1.0)_

## Water

Although most of the time we have been working with _air quality_ sensors and other related metrics, we also work with water metrics. This section summarises our integration of water sensors, in some cases, with interchangeable probes or drivers for soil measurements. For example, the setup shown above is designed for water measurements and includes [Atlas Scientific](https://www.atlas-scientific.com) [temperature](/knowledge/soil-water/Atlas_Temperature/), [conductivity](/knowledge/soil-water/Atlas_EC/) and [pH](/knowledge/soil-water/Atlas_pH/) probes and a [GPS](/hardware/extras/GPS/).

!!! info "Soil Stations"
    The Water Stations can support additional sensors, such as the [Chirp Moisture Sensor](/knowledge/soil-water/Chirp_Soil_Moisture/). More soil sensors can be added as well, by using the [Auxiliary connector](/hardware/Smart Citizen Kit/#auxiliary-connector).

<img src="https://live.staticflickr.com/65535/51232063715_5e37cfb1a0_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

### Available metrics

| Metric | Usage | Sensor | Interface Board | Calibration |
| :-: | :-: | :-: | :-: | :-: |
| Temperature | Soil and water | [Atlas Temperature](/knowledge/soil-water/temperature/Atlas_Temperature) | Atlas EZO-RTD | See [temperature calibration page](/knowledge/soil-water/temperature/Atlas_Temperature#calibration) |
| pH | Soil and water |  [Atlas Water pH](/knowledge/soil-water/pH/Atlas_pH) and [Atlas Soil pH](/knowledge/soil-water/Atlas_pH)  | Atlas EZO-PH | See [pH calibration page](/knowledge/soil-water/pH/Atlas_pH#calibration) |
| Electrical Conductivity, total dissolved solids, salinity and specific gravity | Soil and water | [Atlas Conductivity](/knowledge/soil-water/EC/Atlas_EC) | Atlas EZO-EC | See [EC calibration page](/knowledge/soil-water/EC/Atlas_EC#calibration)  |
| Dissolved Oxygen and oxygen saturation | Water | [Atlas DO](/knowledge/soil-water/DO/Atlas_DO) | Atlas EZO-DO | See [DO calibration page](/knowledge/soil-water/DO/Atlas_DO#calibration)  |
| Soil Moisture | Soil | [Catnip Chirp!](/knowledge/soil-water/moisture/Chirp_Soil_Moisture) | Data Board | See [moisture calibration page](/knowledge/soil-water/moisture/Chirp_Soil_Moisture#calibration) |

!!! warning "Soil and water"
    Some probes can be used for both, soil and water. Make sure to check each sensor page to see how they work.

### Versions

{{ insert_cards(type="stations", filter="field", value=["water"]) }}

#### Legacy versions

Below you will find some legacy (aka _development_) versions. These are left here for you to identify them, or in case you want some inspiration.

Through a collaboration with [Aquapioners](http://aquapioneers.io), we designed the [custom enclosure](https://github.com/fablabbcn/monitoring-kit-hardware) below.

<img src="https://live.staticflickr.com/65535/47957175206_4a63cbdda9_k.jpg" alt="SCK Aquapionners Prototype 2016"/>