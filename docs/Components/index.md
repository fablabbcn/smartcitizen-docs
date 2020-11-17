Hardware Architecture
=====================

![](https://i.imgur.com/qTh4CpB.jpg)

The Smart Citizen sensor portfolio aims to **create a boilerplate for individuals and communities with different sensing expertise levels in a modular, expandable and intuitive way**. Building on the legacy of previous Smart Citizen Kit generations, the hardware is especially aimed at providing meaningful data insights on a low budget. The core of the system is a central data logger with network connectivity to which the different components can be connected and aims to give support to a wide range of activities ranging from education to more advanced scientific research, in **various environmental fields such as air, water or soil quality**.

!!! warning "A bit of philosophy"
    The hardware architecture is **always evolving**, and it will always remain as a set of tools for experimentation. As so, it should be seen more as a toolset for communities, research, education, and not as a final commercial product with full-fledged _big-corporation-type-of-support_.

## Core

The core system provides the logging, interface and management features creating a solid while highly configurable framework for environmental monitoring activities. Each of the modules is shown in the Figure below:

* [**Data Board**](/Components/boards/Data Board): A datalogger at the heart of the sensors architecure supporting the [Smart Citizen Kit](/Smart Citizen Kit) and the [Smart Citizen Stations](/Smart Citizen Station).

* [**Firmware**](Firmware): The software running inside the Data Board.

## Air

![](/assets/images/air-architecture.png)

* **Sensor Boards:** Multiple sensor board have been developed. They can be combined to built the different sensor solutions as the [Smart Citizen Kit](/Smart Citizen Kit) and the [Smart Citizen Stations](/Smart Citizen Station):

	* [**Urban Sensor Board**](/Components/boards/Urban Board): A selection of low-cost sensors in a board ready to measure the urban environment: temperature, humidity, noise, light, and PM2.5, among others. Together with the [Data Board](/Components/boards/Data Board) they create the [Smart Citizen Kit](/Smart Citizen Kit).

	* [**PM Sensor Board**](/Components/boards/PM Board): An auxiliary board capable of driving two Particulate Matter sensor as well as other auxiliary sensors required for specific deployments as an external temperature sensor or an anemometer. It is used in the [Smart Citizen Stations](/Smart Citizen Station).

	* [**Gas Pro Sensor Board**](/Components/boards/Gases Pro Board): An auxiliary board driving 3 Alphasense Ltd. Electrochemical Series B Gas Sensors designed for ultra-low noise, high-performance and low power operation. It is used in the [Smart Citizen Stations](/Smart Citizen Station) for sensors with no offset voltage compensation, i.e. it's not valid for NO, NO2 or OX sensors
   
    * [**Analog Sensors Board**](/Components/boards/Analog Sensor Board): An auxiliary board using a high-resolution ADC capable of reading 4 or 8 analog channels at 16bit resolution. It is used in the [Smart Citizen Stations](/Smart Citizen Station) for the Analog front-end by Alphasense Ltd. which interface with any type of Electrochemical Series B Gas Sensors (NO, NO2 or OX sensors as well)

!!! tips "Expand the SCK"
    Check how to expand the SCK for air quality in the [auxiliary connector section](/Components/Auxiliary Connector#air)

## Soil and Water

![](/assets/images/water-architecture.png)

Having a robust portfolio of the sensor for measuring soil and water characteristics is a need found by many research communities. In this direction, we include a collection of sensors that despite not being low cost or open source, they are still affordable and well documented when compared to other commercial solution. From a cost perspective, they are not aimed at being massively deployed but instead used individually in a specific site for specific needs.

![](/assets/images/soil-architecture.png)

!!! info "Take a deeper look"
    Soil and water sensors are fully detailed in the [Soil and water section](/Components/Soil and water).

## Open Source

**We're against black boxes!**

The entire project it is released under open source licenses: 

* Hardware components: [CERN Open Hardware License v1.2](https://www.ohwr.org/licenses/cern-ohl/license_versions/v1.2)
* Core firmware: [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
* Software platform: [GNU AGLP v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

!!! info
	Check the **Source files** section for each component and explore the software source code and the hardware blueprints.

	![](https://i.imgur.com/X1fUET3.png)
