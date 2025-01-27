---
toc_depth: 1
---

# Hardware Architecture

The core of the system is the [Data Board](hardware/boards/Data Board), a data logger with Wi-Fi connectivity, a micro SD-card, micro USB and battery connectors. Different components can be connected to the board: customized sensor boards, or a wide range of digital and analog sensors. The idea is to make it very easy to get started, no matter if you want to collect air quality or noise data, working on educational settings, or on more _advanced_ scientific research. The type of sensors that we normally work with can take [air](#air), [water](#water) or [soil](#soil) measurements.

<img src="https://live.staticflickr.com/65535/47950912298_3bc1587732_k.jpg" alt="SCK 2.1 Data Board"/>

The _Data Board_ by itself is always used with other components. Depending on what you want to measure, additional expansion boards or sensors are used. Some of those boards are custom designed boards to work with the _Data Board_, while other are _off-the-self_ components. Below, we list the most common use cases. Any configuration can send the data to a dedicated [Storage platform](/data/Data Platform/), which can then be visualised through a web interface.

## Air

_Air measurements_ are the most common use case. These are measurements that imply measuring _physical_ properties of the air (temperature, pressure, relative humidity), things that _are_ in the air (gases, particulate matter) or things that _travel through_ the air (noise, ambient light, UV-index). For this, we use a series of different sensors. These sensors can be _standalone units_ (for instance, a CO2 sensor), or can be in _sensor boards_. When the data board by itself can't read the sensor directly, we need to use _interface electronics_ to get reading from them.

### Sensor Boards

The most popular one of these boards are the [Urban Boards](/hardware/boards/Urban Board). These boards offer a selection of low-cost sensors in a board ready to measure the urban environment: temperature, humidity, noise, light, and PM2.5, among others. Together with the [Data Board](/hardware/boards/Data Board), and a PM sensor, they create the [Smart Citizen Kit](/hardware/Smart Citizen Kit).

<img src="https://live.staticflickr.com/65535/53968621878_f3e3878856_k.jpg" alt="Urban-Board-composite"/>

### Interface Boards

These boards are used to interface with sensors that the _data board_ can't interface with directly:

* [Analog Sensors Board](/hardware/boards/Analog Sensor Board): An auxiliary board using two high-resolution Analog to Digital Converters (ADCs) capable of reading 8 analog channels at 16 bit resolution. It is used in the [Smart Citizen Stations](/hardware/stations/) for the interfacing with sensors such as [electrochemical cells](/knwoledge/sensors/air/chemical/Alphasense_Electrochemical/) or [PIDs](/knwoledge/sensors/air/chemical/Alphasense_PID/).

<img src="https://live.staticflickr.com/65535/53968621883_5c4f1ab625_k.jpg" width="2048" height="1364" alt="Analog-Sensor-Board-front-b"/>

* The [PM Sensors Board](/hardware/boards/PM Board): An auxiliary board capable of driving two [PMS5003 Particulate Matter sensors](/hardware/sensors/air/OPCs/) as well as other auxiliary sensors required for specific deployments. It is generally used in the big [Smart Citizen Stations](/hardware/stations/).

<img src="https://live.staticflickr.com/65535/47950953122_788b43618a_k.jpg" alt="SCK 2.1 PM Board"/>

!!! info "Take a deeper look"
    Air sensors are fully detailed in the [air section](/knowledge/sensors/air/).

## Water

Another common use case is the measurement of physico-chemical parameters in water. These parameters are measured with specialised sensor probes that can measure pH, water temperature, conductivity or dissolved oxygen. We have generally worked with [Atlas Scientific](https://atlas-scientific.com) probes, which use dedicated drivers to interface with those probes. The [Data Board](/hardware/boards/Data Board) can directly inferface with those drivers via I2C through the [auxiliary port](boards/Data%20Board#auxiliary-connector).

<img src="https://live.staticflickr.com/65535/53968745679_f7f4b54509_k.jpg" alt="Water Station"/>

There are various configurations possible for the water measurements. Typically, we have built multi-parametric units, but also simpler units are possible with one or two probes. The different configurations are all modular, and can add more or less probes depending on the particular needs. Some interface boards, like the [Analog Sensor Board](boards/Analog%20Sensor%20Board) can also be used in this context, to read for instance analog turbidimetry sensors, or water level sensors.

!!! info "Take a deeper look"
    Water sensors are fully detailed in the [Soil and water section](/knowledge/sensors/soil-water/).

## Soil

Similar to water measurements, soil parameters require specialised sensor probes. In this case, some water probes can be also used in soil (conductivity, temperature, pH), but we also support additional sensor probes, such as soil moisture probes. These probes are also interfaced through the auxiliary port via I2C.

## _Other_

_Of course_ there's more to it. In _other_ measurements we include everything that you can do with the hardware that goes beyond taking air or water measurements. This section is a bit more _eclectic_ in the sense that there is no single category of parameters measured: from electric properties such as current, voltage, to geolocation. Take a look at the [_other_ measurements section](/knowledge/sensors/other/).