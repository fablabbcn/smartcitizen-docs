# Boards

The core of the system is the [Data Board](/hardware/boards/data-board), a data logger with Wi-Fi connectivity, a micro SD-card, micro USB and battery connectors. Different components can be connected to the board: customized sensor boards, or a wide range of digital and analog sensors. The idea is to make it very easy to get started, no matter if you want to collect air quality or noise data, working on educational settings, or on more _advanced_ scientific research. The type of sensors that we normally work with can take [air](/knowledge/air), [water](/knowledge/water) or [soil](/knowledge/soil) measurements.

<img style="max-height: 350px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281911435_c1ae473a74_o.jpg" alt="SCK 2.3 Data Board"/>

The [Data Board](/hardware/boards/data-board) is always used with other components, depending on what you want to measure. Below, we list the most common use cases. Any configuration can send the data to a dedicated [Smart Citizen platform](/data/data-platform/), which can then be visualised through a web interface.

## Sensor Boards

The most popular one of these boards are the [Urban Boards](/hardware/boards/urban-board/). These boards offer a selection of low-cost sensors in a board ready to measure the urban environment: temperature, humidity, noise, light, and PM2.5, among others. Together with the [Data Board](/hardware/boards/data-board), and a PM sensor, they create the [Smart Citizen Kit](/hardware/kit/).

<img style="max-height: 370px; width: 80%; object-fit: cover;" src="https://live.staticflickr.com/65535/54281726349_e3353f828b_o.jpg" alt="SCK2.3 Urban Board"/>

## Interface Boards

These boards are used to interface with sensors that the _data board_ can't interface with directly:

* [Analog Sensors Board](/hardware/boards/analog-sensor-board/): An auxiliary board using two high-resolution Analog to Digital Converters (ADCs) capable of reading 8 analog channels at 16 bit resolution. It is used in the [Smart Citizen Stations](/hardware/stations/) for the interfacing with sensors such as [electrochemical cells](/knwoledge/sensors/air/chemical/Alphasense_Electrochemical/) or [PIDs](/knwoledge/sensors/air/chemical/Alphasense_PID/).

<img style="max-height: 350px; width: 100%; object-fit: cover;" src="https://live.staticflickr.com/65535/53968621883_5c4f1ab625_k.jpg" alt="Analog-Sensor-Board-front-b"/>

* The [PM Sensors Board](/hardware/boards/pm-board/): An auxiliary board capable of driving two [PMS5003 Particulate Matter sensors](/hardware/sensors/air/OPCs/) as well as other auxiliary sensors required for specific deployments. It is generally used in the big [Smart Citizen Stations](/hardware/stations/).

<img src="https://live.staticflickr.com/65535/47950953122_788b43618a_k.jpg" alt="SCK 2.1 PM Board"/>
