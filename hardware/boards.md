<!-- Source: https://docs.smartcitizen.me/hardware/boards/ -->

# Boards

The core of the system is the [Data Board](https://docs.smartcitizen.me/hardware/boards/data-board.md), a data logger with Wi-Fi connectivity, a micro SD-card, micro USB and battery connectors. Different components can be connected to the board: customized sensor boards, or a wide range of digital and analog sensors. The idea is to make it very easy to get started, no matter if you want to collect air quality or noise data, working on educational settings, or on more _advanced_ scientific research. The type of sensors that we normally work with can take [air](https://docs.smartcitizen.me/knowledge/air.md), [water, or soil](https://docs.smartcitizen.me/knowledge/soil-water.md) measurements.

<img style="max-height: 350px; width: 100%; object-fit: cover;" src="https://docs.smartcitizen.me/assets/images/sck2-3-data-board.jpg" alt="SCK 2.3 Data Board"/>

The [Data Board](https://docs.smartcitizen.me/hardware/boards/data-board.md) is always used with other components, depending on what you want to measure. Below, we list the most common use cases. Any configuration can send the data to a dedicated [Smart Citizen platform](https://docs.smartcitizen.me/data/data-platform.md), which can then be visualised through a web interface.

## Sensor Boards

The most popular one of these boards are the [Urban Boards](https://docs.smartcitizen.me/hardware/boards/urban-board.md). These boards offer a selection of low-cost sensors in a board ready to measure the urban environment: temperature, humidity, noise, light, and PM2.5, among others. Together with the [Data Board](https://docs.smartcitizen.me/hardware/boards/data-board.md), and a PM sensor, they create the [Smart Citizen Kit](https://docs.smartcitizen.me/hardware/kit.md).

<img style="max-height: 370px; width: 80%; object-fit: cover;" src="https://docs.smartcitizen.me/assets/images/sck2-3-urban-board.jpg" alt="SCK2.3 Urban Board"/>

## Interface Boards

These boards are used to interface with sensors that the _data board_ can't interface with directly:

* [**Analog Sensors Board**](https://docs.smartcitizen.me/hardware/boards/analog-sensor-board.md): An auxiliary board using two high-resolution Analog to Digital Converters (ADCs) capable of reading 8 analog channels at 16 bit resolution. It is used in the [Smart Citizen Stations](https://docs.smartcitizen.me/hardware/stations.md) for the interfacing with sensors such as [electrochemical cells](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_Electrochemical.md) or [PIDs](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_PID.md).

<img style="max-height: 350px; width: 100%; object-fit: cover;" src="https://docs.smartcitizen.me/assets/images/analog-sensor-board-front-b.jpg" alt="Analog-Sensor-Board-front-b"/>

* [**PM Sensor Board**](https://docs.smartcitizen.me/hardware/boards/pm-board.md): An auxiliary board capable of driving two [PMS5003 Particulate Matter sensors](https://docs.smartcitizen.me/knowledge/air/pm.md) as well as other auxiliary sensors required for specific deployments. It is generally used in the big [Smart Citizen Stations](https://docs.smartcitizen.me/hardware/stations.md).

<img src="https://docs.smartcitizen.me/assets/images/sck-2-1-pm-board.jpg" alt="SCK 2.1 PM Board"/>

!!! info "Commercial availability"
    All interface boards are currently not available for purchases, except from Fab Lab Barcelona directly. Email us at [info@smartcitizen.me](mailto:info@smartcitizen.me) in case you are interested.