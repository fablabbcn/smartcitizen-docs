Welcome!
========

!!! info "A note about versions"

    <a href="https://www.iscapeproject.eu/"><img src="https://i.imgur.com/ud8lUOo.png" width="120" alt=""></a>

    The new [**Smart Citizen Kit**](Smart Citizen Kit) and the [**Smart Citizen Station**](Smart Citizen Station) development has been developed as part of the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

![](https://i.imgur.com/0U9T29b.jpg)

## Sections

* **Main:** Contains the [**Smart Citizen Kit**](Smart Citizen Kit) and [**Smart Citizen Station**](Smart Citizen Station) documentation to help you use them.

* **Sensor Platform:** Contains all the documentation on the [**sensors web platform**](Sensor Platform) where data is collected, stored and visualised.

* **Sensor Analysis Framework:** Contains all the documentation on the [**data post-processing framework**](Sensor Analysis Framework) to obtain insights from the data calibrated by the sensors.

* **Guides:** Contains step-by-step [**Guides**](Guides) for different features of the kit, how to get started, use the shell, or make some more advanced analysis of the sensor readings!

* **Legacy Hardware:** Are you a pioneer of participatory sensing looking for the original SCK 1.0 and SCK 1.1 documentation? Check the [**Legacy Hardware**](Legacy Hardware) section!

## Components

The project's sensor platform builds on the legacy of previous Smart Citizen Kit generations to develop a new set of tools especially aimed at providing meaningful data insights on a low budget. The system is designed in a extendable way, with a central data logger with network connectivity to which the different components are branched and aims to give support to a various activities ranging from education to more advanced scientific research.

![](https://i.imgur.com/qTh4CpB.jpg)

### Hardware

![](https://i.imgur.com/4lPC9rA.png)

* [**Data Board**](Components/Data Board): A datalogger at the heart of the sensors architecure supporting the [Smart Citizen Kit](Smart Citizen Kit) and the [Smart Citizen Stations](Smart Citizen Station).

* **Sensor Boards:** Multiple sensor boards have been developed. They can be combined to built the different sensor solutions as the [Smart Citizen Kit](Smart Citizen Kit) and the [Smart Citizen Stations](Smart Citizen Station):

    * [**Urban Sensor Board**](Components/Urban Sensor Board): A selection of low-cost sensors in a board ready to measure the urban environment: temperature, humidity, noise, light, and PM2.5, among others. Together with the [Data Board](/Components/Data Board) they create the [Smart Citizen Kit](/Smart Citizen Kit).

    * [**PM Sensor Board**](Components/PM Sensor Board): An auxiliary board capable of driving two Particulate Matter sensors as well as other auxiliary sensors required for specific deployments as an external temperature sensor or an anemometer. It is used in the [Smart Citizen Station](/Smart Citizen Station).

    * [**Gas Pro Sensor Board**](Components/Gas Pro Sensor Board): An auxiliary board driving 3 Alphasense Ltd. Electrochemical Series B Gas Sensors designed for ultra-low noise, high-performance and low power operation. It is used in the [Smart Citizen Station](/Smart Citizen Station).

### Firmware

Here you can find more information about the [**firmware**](Components/Firmware): the software running inside the Smart Citizen Kit.

## Guides

The documentation contains multiple guides as step-by-step tutorials to perform essential tasks as installing a kit or upgrading it's firmware.

!!! info "Example guides"

    * [Installing the Smart Citizen Kit](Smart Citizen Kit/#how-to-install)
    * [Installing the Smart Citizen Station](Smart Citizen Station/#how-to-install)
    * [Installing the Smart Citizen Kit 1.0 / 1.1](/Legacy Hardware)
    * [Onboarding new Sensors](Sensor Platform/guides/Onboarding Sensors)
    * [Uploading SD Card Data](Sensor Platform/guides/Uploading SD Card Data)
    * [Update the Firmware](Components/Firmware/guides/Update the firmware)
    * [Edit the Firmware](Components/Firmware/guides/Edit the Firmware)
    * [Use Machine Learning to Create Models for Sensors Calibration](/Sensor Analysis Framework/guides/Creating Models for Sensors Calibration)

## Open Source

**We're against black boxes!**

The entire project is released under open source licenses: 

* Hardware components: [CERN Open Hardware License v1.2](https://www.ohwr.org/licenses/cern-ohl/license_versions/v1.2)
* Core firmware: [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
* Software platform: [GNU AGLP v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

!!! info
    Check the **Source files** section for each component and explore the software source code and the hardware blueprints.

    ![](https://i.imgur.com/X1fUET3.png)
