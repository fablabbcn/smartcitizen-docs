# Soil and water sensors

<img src="https://live.staticflickr.com/65535/51124639732_90241111a9_k.jpg" alt="Water Station - Patí Científic">

Although most of the time we have been working with air quality sensors and air metrics, we also like to keep an eye on soil and water sensors. This page details our integration of water and soil sensors, often interchangeable in some cases.

Different sensor probes can be combined for different configurations. For example the setup shown above is designed for soil measurements and includes [Atlas Scientific](https://www.atlas-scientific.com) temperature, conductivity and PH probes and a GPS. Additional sensors include a Chirp Moisture Sensor as described in the [soil section](/Components/sensors/soil/Soil Moisture Sensors/). Another example is the setup in the figure below is designed for water monitoring on aquaponics systems and includes Atlas Scientific probes for PH, conductivity and dissolved oxygen.

![](/assets/images/gQavZqU.png)

Some of the sensors selected are from Atlas Scientific, a New York-based company that _converts devices that were originally designed to be used by humans into devices that are specifically designed to be used by robots_. The sensors are not entirely open source as the other sensors (the Chirp Sensor is a low cost moisture and temperature sensor developed by [WeMakeThings](https://wemakethings.net/chirp/): a hackers and engineers collective based in Vilnius, Lithuania). However, they are modular and exceptionally well documented by the manufacturer. That includes **excellent** documentation on how to install, calibrate and integrate them with additional existing hardware. In this direction, we developed a full library for the SCK to support the sensors via the Auxiliary sensor connector. As the sensors can be configured in different ways, we do not provide a full step-by-step guide. Instead, we refer to the documentation on the [project's repository](https://github.com/fablabbcn/smartcitizen-grow/tree/master/soil-water-probes).

!!! info "Use cases"
    Check how we have used the water or soil sensors in various projects in the [Use cases section](/Use cases/Research/)

## Hardware

<img src="https://live.staticflickr.com/65535/51232063715_5e37cfb1a0_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

### Available measurements

The sensors described below are additional to those already supported on the [Smart Citizen Kit base sensors](/Smart Citizen Kit/#sck-21). 

{{ get_snippet_rel("docs/includes/en/sensors/water.md") }}

!!! warning "Soil and water"
    For probes that can be used in both, soil and water, make sure to [follow this procedure](https://atlas-scientific.com/files/ec_soil.pdf).

### Atlas Scientific Carrier board

We recommend using [Whitebox Labs Tentacle T3](https://www.whiteboxes.ch/shop/tentacle-t3-for-raspberry-pi/) that hosts up to 3 Atlas Scientific Probes, and can be stacked with several units. It connects to the SCK via the Aux sensor connector, and needs external 5V connection, which means that it can't run on battery directly connected to the SCK without extras. If you want to make your own, before the Tentacle T3 existed we designed a [custom board](https://github.com/fablabbcn/monitoring-kit-hardware) in collaboration in with [Aquapiooners](http://aquapioneers.io).

![](/assets/images/6FysvIl.png)

!!! info "Ready to set it all up"
    Visit [this guide](/Guides/deployments/Water sensors/) to get started.

### Enclosures

A normal IP enclosure can be used for this setup. More information about the BOM and design files can be found [in the enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Water%20Enclosures/SmartCitizen%20Water%20Station).

<img src="https://live.staticflickr.com/65535/51125200496_67b06e79bd_k.jpg" alt="Water Station - Patí Científic">

!!! info "Thanks!"
    This enclosure and development has been done in collaboration with [ICM-CSIC](https://www.icm.csic.es/en) and the [Club Pati Vela de Barcelona](https://pativelabarcelona.com/).

#### Legacy enclosures

In collaboration in with [Aquapiooners](http://aquapioneers.io) we designed the [custom enclosure](https://github.com/fablabbcn/monitoring-kit-hardware) below.

![](/assets/images/aowaWtl.png)

The enclosure of the monitoring board and the smart citizen have been designed on Onshape, you can either download the STL files or copy the project to your onshape account and modify them as you wish : [The Onshape documents of the monitoring case](https://cad.onshape.com/documents/50f1112a541136a65bec4a67/w/db735112a72871fb7c20053e/e/57e22425fb47d5e8030621de)

![](/assets/images/tXNBC5e.png)

We have also designed a probe holder if you want to hold your probes on the side of you fish tank. Here you can find the [Onshape document of the probes holder](https://cad.onshape.com/documents/8977ef824f45a910c0b8beaa/w/7ac458735dae629f0a5a73cd/e/be59d435418832bfe5f78afb)

![](/assets/images/6sM3sCY.jpg)

## Soil Station

More soil sensors can be added as well, not only Atlas Scientific sensors, or  the [WeMakeThings Chirp](https://wemakethings.net/chirp/) sensor for Soil moisture. More developments available upon request.

![](/assets/images/DT45dpM.jpg)

## Water Station

An specific Water Station was designed as part of the [Pati Scientific](https://paticientific.org/) project in colaboration with the [Institut de Ciències del Mar](https://www.icm.csic.es/en). The station currently measures the sensors below, but virtually any [supported sensor](/Components/Auxiliary Connector/#full-list) can be added:

![](/assets/images/pativela.jpg)
_Image credit: Pati Scientific_

- Temperature
- PH
- Electrical Conductivity
- Dissolved Oxygen
- GPS location

!!! info "Came to stay"

	This unit is here to stay. It is used in [MINKE](https://minke.eu) and it's also available upon request!
