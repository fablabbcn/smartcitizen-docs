# Hardware

The Smart Citizen sensor portfolio aims to **create a boilerplate for individuals and communities with different sensing expertise levels in a modular, expandable and intuitive way**. Building on the legacy of previous Smart Citizen Kit generations, the hardware is especially aimed at providing meaningful data insights on a low budget. The core of the system is a central data logger with network connectivity to which the different components can be connected and aims to give support to a wide range of activities ranging from education to more advanced scientific research, in **various environmental fields such as air, water or soil quality**.

!!! warning "A bit of philosophy"
    The hardware architecture is **always evolving**, and it will always remain as a set of tools for experimentation. As so, it should be seen more as a toolset for communities, research, education, and not as a final commercial product with full-fledged _big-corporation-type-of-support_.

## Core

The core system provides the logging, interface and management features creating a solid while highly configurable framework for environmental monitoring activities. It's made out of the two main components listed below:

* [**Data Board**](/Components/boards/Data Board): A datalogger at the heart of the sensors architecure supporting the [Smart Citizen Kit](/Smart Citizen Kit) and the [Smart Citizen Stations](/Smart Citizen Station).
* [**Firmware**](Firmware): The software running inside the Data Board.

## Air

* **Sensor Boards:** Multiple sensor board have been developed. They can be combined to build the different sensor solutions as the [Smart Citizen Kit](/Smart Citizen Kit) and the [Smart Citizen Stations](/Smart Citizen Stations):
	* [**Urban Sensor Board**](/Components/boards/Urban Board): A selection of low-cost sensors in a board ready to measure the urban environment: temperature, humidity, noise, light, and PM2.5, among others. Together with the [Data Board](/Components/boards/Data Board) they create the [Smart Citizen Kit](/Smart Citizen Kit).
	* [**PM Sensors Board**](/Components/boards/PM Board): An auxiliary board capable of driving two [Particulate Matter sensors](/Components/sensors/air/OPCs/) as well as other auxiliary sensors required for specific deployments as an external temperature sensor or an anemometer. It is used in the [Smart Citizen Stations](/Smart Citizen Stations).
    * [**Analog Sensors Board**](/Components/boards/Analog Sensor Board): An auxiliary board using a high-resolution ADC capable of reading 4 or 8 analog channels at 16bit resolution. It is used in the [Smart Citizen Stations](/Smart Citizen Stations) for the measuring sensors such as [electrochemical cells](/Components/sensors/air/electrochemical sensors/) (for instance, by [Alphasense](/Components/sensors/air/electrochemical sensors/alphasense/) Ltd.) [Metal Oxydes](/Components/sensors/air/metal oxides/).

!!! tips "Expand the SCK"
    Check how to expand the SCK for air quality in the [auxiliary connector section](/Components/Auxiliary Connector#air)

## Soil and Water

Having a robust portfolio of the sensor for measuring soil and water characteristics is something many research communities find useful. You can also add soil or water sensors to the mix, and for this we include a collection of sensors that can be interfaced with some commercially available boards, such as

!!! info "Take a deeper look"
    Soil and water sensors are fully detailed in the [Soil and water section](/Components/Soil and water).
