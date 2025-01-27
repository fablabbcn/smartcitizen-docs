# Smart Citizen Hardware

The Smart Citizen Hardware is an **open source boilerplate for anyone, no matter their expertise**, to capture environmental data, with modular, hackable and easy to use electronics. The hardware has been developed after various [projects and collaborations](/resources/research), resulting in different hardware _generations_, but always aimed at providing meaningful data insights on a _relatively_ **low budget**.

<img src="https://live.staticflickr.com/65535/50977039386_c250d3141d_k.jpg" alt="Smart Citizen Kits being tested at Fab Lab Barcelona"/>

!!! warning "Building upon previous versions"
    The hardware architecture is **always evolving**, and it will always remain as a set of tools for experimentation. As so, it should be seen more as a toolset for communities, research, education, and not as a final commercial product with full-fledged _big-corporation-type-of-support_.

!!!info "Is it _low-cost_?"

    Well, it depends on many factors, even on the definition of _low-cost_. When you get the [Smart Citizen Kit](kit/index.md) in [SeeedStudio](https://www.seeedstudio.com/Smart-Citizen2-3-p-6327.html) costs around 150 (USD or EUR), and it's the central piece of the ecosystem. This can be _low-cost_ in some contexts, and expensive in others. There are more advanced configurations available, which they normally feature more sensors and require more _lab_ work. Obviously, the cost increases as we include other sensors in the budget, but the idea is to try to keep it affordable, easy to use and hackable. Being an open source project, the _hardware_, _firmware_ and _data platform_ are provided _as-is_.

    However, if you are looking at making more advanced configurations, or want to develop a project together, you can write us at [info@smartcitizen.me](mailto:info@smartcitizen.me).

## Applications

### Air

_Air measurements_ are the most common use case. These are measurements that imply measuring _physical_ properties of the air (temperature, pressure, relative humidity), things that _are_ in the air (gases, particulate matter) or things that _travel through_ the air (noise, ambient light, UV-index). For this, we use a series of different [sensors](/knowledge/air). These sensors can be _standalone units_ (for instance, a CO2 sensor), or can be in [_sensor boards_](/hardware/boards#sensor-boards) (like the [Urban Board](/hardware/boards/urban-board/)). When the [Data Board](/hardware/boards/data-board/) by itself can't read the sensor directly, we need to use [_interface electronics_](/hardware/boards/#interface-boards) to get reading from them.

!!! info "Take a deeper look"
    Water sensors are fully detailed in the [air section](/knowledge/sensors/air/).

### Soil and Water

Another common use case is the measurement of physico-chemical parameters in [water](/knowledge/soil-water/). These parameters are measured with specialised sensor probes that can measure pH, water temperature, conductivity or dissolved oxygen. We have generally worked with [Atlas Scientific](https://atlas-scientific.com) probes, which use dedicated drivers to interface with those probes. The [Data Board](/hardware/boards/data-board/) can directly inferface with those drivers via I2C through the [auxiliary port](/hardware/boards/data-board#auxiliary-connector).

<img src="https://live.staticflickr.com/65535/53968745679_f7f4b54509_k.jpg" alt="Water Station"/>

There are various configurations possible for the water measurements. Typically, we have built multi-parametric units, but also simpler units are possible with one or two probes. The different configurations are all modular, and can add more or less probes depending on the particular needs. Some interface boards, like the [Analog Sensor Board](/hardware/boards/analog-sensor-board/) can also be used in this context, to read for instance analog turbidimetry sensors, or water level sensors.

!!! info "Take a deeper look"
    Water sensors are fully detailed in the [Soil and water section](/knowledge/sensors/soil-water/).

Similar to water measurements, soil parameters require specialised sensor probes. In this case, some water probes can be also used in soil (conductivity, temperature, pH), but we also support additional sensor probes, such as soil moisture probes. These probes are also interfaced through the auxiliary port via I2C.

### _Other_

_Of course_ there's more to it. In _other_ measurements we include everything that you can do with the hardware that goes beyond taking air or water measurements. This section is a bit more _eclectic_ in the sense that there is no single category of parameters measured: from electric properties such as current, voltage, to geolocation. Take a look at the [_other_ measurements section](/knowledge/sensors/other/).
