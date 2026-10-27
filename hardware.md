<!-- Source: https://docs.smartcitizen.me/hardware/ -->

# Smart Citizen Hardware

The Smart Citizen Hardware is an **open source boilerplate for anyone, no matter their expertise**, to capture environmental data with modular, hackable, and easy-to-use electronics. The hardware has been developed through various [projects and collaborations](https://docs.smartcitizen.me/resources/research.md), resulting in different hardware _generations_, but it has always aimed at providing meaningful data insights on a _relatively_ **low budget**.

<img src="https://docs.smartcitizen.me/assets/images/smart-citizen-kits-being-tested-at-fab-lab-barcelona.jpg" alt="Smart Citizen Kits being tested at Fab Lab Barcelona"/>

!!! warning "Building upon previous versions"
    Our hardware architecture is **continuously evolving** and will always remain a set of tools for experimentation. Given that, it should be seen more as a toolset for communities, research, and education, not as a final commercial product with full-fledged _big-corporation-type-of-support_.

!!!info "Is it _low-cost_?"

    Well, that depends on many factors, even the definition of _low-cost_. When you purchase the [Smart Citizen Kit](https://docs.smartcitizen.me/hardware/kit.md) through [SeeedStudio](https://www.seeedstudio.com/Smart-Citizen2-3-p-6327.html), it costs around 150 (USD or EUR) and is the central piece of the ecosystem. This price can be _low-cost_ in some contexts and expensive in others. More advanced configurations are available, which generally feature more sensors and require more _lab_ work. The cost increases as we include additional sensors in the budget, but the idea is to keep it affordable, easy to use, and hackable. As an open source project, the _hardware_, _firmware_, and _data platform_ are provided _as-is_.

    However, if you are looking for more advanced environmental monitoring setups or want to develop a project together, you can write us at [info@smartcitizen.me](mailto:info@smartcitizen.me).

## Applications

### Air

_Air measurements_ are the most common use case. These are measurements that imply measuring the _physical_ properties of the air (temperature, pressure, relative humidity), things that _are_ in the air (gases, particulate matter), or things that _travel through_ the air (noise, ambient light, UV-index). For this, we use a series of different [sensors](https://docs.smartcitizen.me/knowledge/air.md). These sensors can be _standalone units_ (for instance, a CO2 sensor) or on [_sensor boards_](https://docs.smartcitizen.me/hardware/boards.md#sensor-boards) (like the [Urban Board](https://docs.smartcitizen.me/hardware/boards/urban-board.md)). When the [Data Board](https://docs.smartcitizen.me/hardware/boards/data-board.md) alone can't read the sensor directly, we need to use [_interface electronics_](https://docs.smartcitizen.me/hardware/boards.md#interface-boards) to get their readings.

!!! info "Take a deeper look"
    Air sensors are fully detailed in the [air section](https://docs.smartcitizen.me/knowledge/air.md).

### Soil and Water

Another common use case is the measurement of physico-chemical parameters in [water](https://docs.smartcitizen.me/knowledge/soil-water.md). These parameters are measured with specialised sensor probes that can measure pH, water temperature, conductivity, or dissolved oxygen. We have generally worked with [Atlas Scientific](https://atlas-scientific.com) probes, which use dedicated drivers to interface with those probes. The [Data Board](https://docs.smartcitizen.me/hardware/boards/data-board.md) can directly interface with those drivers via I2C through the [auxiliary port](https://docs.smartcitizen.me/hardware/boards/data-board.md#auxiliary-connector).

<img src="https://docs.smartcitizen.me/assets/images/sck-water-station.jpg" alt="Water Station"/>

There are various possible configurations for water measurements.  Typically, we have built multi-parametric units, but simpler units are possible with one or two probes. All the different configurations are modular and can include more or less probes depending on the particular needs. Some interface boards, like the [Analog Sensor Board](https://docs.smartcitizen.me/hardware/boards/analog-sensor-board.md), can also be used in this context to read analog turbidimetry sensors or water level sensors, for instance.

!!! info "Take a deeper look"
    Water sensors are fully detailed in the [soil and water section](https://docs.smartcitizen.me/knowledge/soil-water.md).

Similar to water measurements, soil parameters require specialised sensor probes. In this case, some water probes can be also used in soil (conductivity, temperature, pH), but we also support additional sensor probes, such as soil moisture probes. These probes are interfaced with through the auxiliary port via I2C.

### _Other_

_Of course_, there's more to it. In _other_ measurements, we include everything possible with the hardware beyond taking air or water measurements. This section is a bit more _eclectic_ since it uses no single category of parameters. Instead, it includes everything from electric properties, such as current and voltage, to geolocation. Take a look at the [_other_ measurements section](https://docs.smartcitizen.me/knowledge/other.md).