Hardware Architecture
=====================

![](https://i.imgur.com/qTh4CpB.jpg)

The project's sensor platform builds on the legacy of previous Smart Citizen Kit generations to develop a new set of tools especially aimed at providing meaningful data insights on a low budget. The system is designed in a extendable way, with a central data logger with network connectivity to which the different components are branched and aims to give support to a various activities ranging from education to more advanced scientific research.

We believe building modular and reusable hardware is critical towards optimizing the research and development effort. By increasing the technology readiness levels of existing technologies, we can drastically improve the project exploitation strategy.

## Hardware

The core system bases its sensing capabilities in widely reviewed low cost sensors, and aims to provide a solid framework for environmental monitoring activities. Each of the modules is shown in the Figure below:

![](https://i.imgur.com/4lPC9rA.png)

* [**Data Board:**](Data Board) A datalogger at the heart of the sensors architecure supporting the [Smart Citizen Kit](/Smart Citizen Kit) and the [Smart Citizen Stations](/Smart Citizen Station).

* [**Firmware:**](Firmware) The software running inside the sensors.

* **Sensor Board:** Multiple sensor board have been developed. They can be combined to built the different sensor solutions as the [Smart Citizen Kit](/Smart Citizen Kit) and the [Smart Citizen Stations](/Smart Citizen Station):

	* [**Urban Sensor Board:**](Urban Sensor Board) A selection of low-cost sensors in a board ready to measure the urban environment: temperature, humidity, noise, light, and PM2.5, among others. Together with the [Data Board](Data Board) they create the [Smart Citizen Kit](/Smart Citizen Kit).

	* [**PM Sensor Board:**](PM Sensor Board) An auxiliary board capable of driving two Particulate Matter sensor as well as other auxiliary sensors required for specific deployments as an external temperature sensor or an anemometer. It is used in the [Smart Citizen Stations](/Smart Citizen Station).

	* [**Gas Pro Sensor Board:**](Gas Pro Sensor Board) An auxiliary board driving 3 Alphasense Ltd. Electrochemical Series B Gas Sensors designed for ultra-low noise, high-performance and low power operation. It is used in the [Smart Citizen Stations](/Smart Citizen Station).

## Open Source

**We're against black boxes!**

The entire project it is released under open source licenses: 

* Hardware components: [CERN Open Hardware License v1.2](https://www.ohwr.org/licenses/cern-ohl/license_versions/v1.2)
* Core firmware: [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
* Software platform: [GNU AGLP v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

!!! info
	Check the **Source files** section for each component and explore the software source code and the hardware blueprints.

	![](https://i.imgur.com/X1fUET3.png)