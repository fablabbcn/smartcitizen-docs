# Smart Citizen Stations

<img src="https://live.staticflickr.com/65535/50976345233_cae6391c94_k.jpg" width="2000" height="1333" alt="Smart Citizen Station v3">

The Smart Citizen Stations are **modular open-source environmental monitoring systems**. They are based on the [Smart Citizen Kit](/Smart Citizen Kit), but the Station is an expanded configuration in which multiple sensors can be easily added, expanding the capabilities of the Kit in different ways: for more advanced air quality monitoring, or water and soil metrics. From a cost perspective, while being more expensive than the Kit, it is also designed to be a low-cost, customisable and _hackable_ solution. It aims at providing a range of solutions that can build upon the core components of the hardware ecosystems, and that can be used by citizens and researchers to gather environmental data, not only from a scientific point of view but also as a tool to engage local communities on environmental topics

The Stations come in different flavours and sizes. Sometimes, they are more bulky (because of the number of sensors, the one in the picture above has roughly 15 sensors). Sometimes, the Stations sometimes look a bit smaller...

![](/assets/images/small-station-front.jpg)

!!! tip "Questions?"

    How can we collaborate for my next research project? How much will it cost to make one? Is it hard to install? You can contact our team at [info@smartcitizen.me](mailto: info@smartcitizen.me)

<img src="https://live.staticflickr.com/65535/50977039556_541c4727a6_k.jpg" width="2000" height="1333" alt="Smart Citizen Station v3">

!!! info "Intentionally _hackable_, intentionally _fabbable_"

    The Smart Citizen Stations, from the enclosure, to the electronics, are open source. Many components can be fabricated and assembled in a [Fablab](https://www.fablabs.io/). By doing so, we hope to encourage **fully open environmental systems**, ensuring reproducibility through accessible resources.

The sensors the station can include are listed in the list of [supported sensors](/Components/Auxiliary Connector/). Below you have a summary to get a taste of what it can do. Make sure to check the dedicated sections for each to get a complete description!

## Air Quality

The [air quality (AQ) versions](/Configurations/Air Quality Station) are designed to expand the Kit with more advanced sensors, such as electrochemical or NDIR sensors. The units can be adapted to the particular monitoring needs, thanks to their modular approach.

### Available metrics

- **Up to 16 analog sensors!**, some of which can be gas sensors detailed as below
- **Gas sensors** for gases such as [electrochemical sensors](/Components/sensors/air/electrochemical sensors/) or [Metal Oxydes](/Components/sensors/air/metal oxides). A common solution are the [B4 or A4 sensors](http://www.alphasense.com/index.php/air/) from [Alphasense](/Components/sensors/air/electrochemical sensors/alphasense/) such as: CO, NO2, NO, O3, SO2, H2S
- **CO2 NDIR Sensor** such as [these ones](/Componentes/sensors/air/NDIR/)
- **PM sensors** from Plantower or others similar [optical particle counters](/Components/sensors/air/OPCs) (OPCs)
- **Temperature probe and humidity probes**: external temperature probe for more reliable air temperature sensing
- **Ultra-violet** radiation
- **Noise levels** and (optional FFT spectrum, only on sd-card)
- **Environmental metrics**: temperature, humidity, ambient pressure

<img src="https://live.staticflickr.com/65535/50812574093_2e9493d105_k.jpg" width="2001" height="1334" alt="Smart Citizen Station rev3">

!!! info "From the ground up"

    The station uses the same core functionality, interface and feedback as the Smart Citizen Kit. Make sure you are familiar with them before jumping into the station!
    - [User feedback](/Smart Citizen Kit/#user-feedback)
    - [LED states and operation modes](/Smart Citizen Kit/#operation-modes)
    - [User interfaces](/Smart Citizen Kit/#user-interfaces)

![](/assets/images/station30bottom.jpg)

!!! tip "Dimensions"
    If you are looking at the dimensions and mechanical/electrical information about the Smart Citizen Station, have a look at the [enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Station)

### Enclosures

The enclosures can be found in the [enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures). Make sure to check the version that works for your particular configuration in case you want to make your own!

![](/assets/images/station30.jpg)

_Full equip station_

### Power

Currently, the Smart Citizen Air Quality Stations are only available with an external power supply (230VAC to 5V), with a small battery for backup during power brownouts. Due to the number of sensors, and depending on the configuration, the solution is normally not meant for long term deployment only on battery power). For specifications of the power supply, find more info in the [power supply section](/Components/boards/Power Supply/).

!!! warning "Battery or solar operation?"
    The Smart Citizen Station currently supports battery operation only for short periods of time (<2d days). Depending on the location, solar power might not be available due to the unit's consumption.

### Connectivity

If you want to have your data online, the Smart Citizen Air Quality Station requires a Wi-Fi connection to report data to the [platform](/Data/Sensor Platform). If not, the unit can also store data locally on its onboard sd-card. Read more about the [operation modes](/Smart%20Citizen%20Kit/#operation-modes) and the [supported networks](/_FAQ/#what-networks-does-it-support).

!!! tip "Connectivity Units"
    We tested customized connectivity units capable of deploying a local Wi-Fi network where multiple Smart Citizen Station can connect, data can be relied over GSM (3/4/5G) or other IoT connectivity standards.

### Development versions

Below you will find some development versions. These are left here for you to identify them, or in case you want some inspiration!

![](/assets/images/CiFikz8.jpg)

_Final iSCAPE Station version (iSCAPE-V2.0)_

!!! info "A note about versions"

    The **iScape Living Lab Station 1.0** was the development version for the 2.0 version. It was sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

![](/assets/images/QB5P4r9.jpg)

_Middle iSCAPE Station version (iSCAPE-V1.0)_

## Soil and water

<img src="https://live.staticflickr.com/65535/51124639732_90241111a9_k.jpg" alt="Water Station - Patí Científic">

Although most of the time we have been working with _air quality_ sensors and air metrics, we also work with soil and water metrics. This section summarises our integration of water and soil sensors, often interchangeable in some cases. For example the setup shown above is designed for soil measurements and includes [Atlas Scientific](https://www.atlas-scientific.com) temperature, conductivity and PH probes and a GPS. Additional sensors include a Chirp Moisture Sensor as described in the [soil section](/Components/sensors/soil/Soil Moisture Sensors/). Another example is the setup in the figure below is designed for water monitoring on aquaponics systems and includes Atlas Scientific probes for PH, conductivity and dissolved oxygen. More soil sensors can be added as well, not only Atlas Scientific sensors. For instance the [WeMakeThings Chirp](https://wemakethings.net/chirp/) sensor for Soil moisture has been added in some configurations, and more developments are available upon request.

<img src="https://live.staticflickr.com/65535/51232063715_5e37cfb1a0_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

### Available metrics

!!! warning "Soil and water"
    Some probes can be used for both, soil and water. Make sure to [follow this procedure](https://atlas-scientific.com/files/ec_soil.pdf) for those.

![](/assets/images/DT45dpM.jpg)

!!! info "Ready to set it all up"
    Visit [this guide](/Guides/deployments/Water sensors/) to get started.

### Enclosures

A normal IP enclosure can be used for this setup. More information about the BOM and design files can be found [in the enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Water%20Enclosures/SmartCitizen%20Water%20Station).

<img src="https://live.staticflickr.com/65535/51125200496_67b06e79bd_k.jpg" alt="Water Station - Patí Científic">

!!! info "Thanks!"

    This enclosure and development has been done in collaboration with [ICM-CSIC](https://www.icm.csic.es/en) and the [Club Pati Vela de Barcelona](https://pativelabarcelona.com/).

### Power

Currently, the Smart Citizen Water and Soil Stations are only available with an external power supply (230VAC to 5V), with a small battery for brownouts. Due to the number of sensors, and depending on the configuration, the solution is normally not meant for long term deployment only on battery power). For specifications of the power supply, find more info in the [power supply section](/Components/boards/Power Supply/).

!!! warning "Battery or solar operation?"

    The Smart Citizen Station currently supports battery operation only for short periods of time (<2d days). Depending on the location, solar power might not be available due to the unit's consumption.

### Connectivity

The Smart Citizen Air Quality Station requires a Wi-Fi connection to report data to the [online platform](/Data/Sensor Platform) and it can also store data offline locally. Read more about the [operation modes](/Smart%20Citizen%20Kit/#operation-modes) and the supported networks.

!!! tip "Connectivity Units"

    We tested customized connectivity units capable of deploying a local Wi-Fi network where multiple Smart Citizen Station can connect, data can be relied over GSM (3/4/5G) or other IoT connectivity standards.

### Development versions

In collaboration in with [Aquapiooners](http://aquapioneers.io) we designed the [custom enclosure](https://github.com/fablabbcn/monitoring-kit-hardware) below.

![](/assets/images/aowaWtl.png)

The enclosure of the monitoring board and the smart citizen have been designed on Onshape, you can either download the STL files or copy the project to your onshape account and modify them as you wish : [The Onshape documents of the monitoring case](https://cad.onshape.com/documents/50f1112a541136a65bec4a67/w/db735112a72871fb7c20053e/e/57e22425fb47d5e8030621de)

![](/assets/images/tXNBC5e.png)

We have also designed a probe holder if you want to hold your probes on the side of you fish tank. Here you can find the [Onshape document of the probes holder](https://cad.onshape.com/documents/8977ef824f45a910c0b8beaa/w/7ac458735dae629f0a5a73cd/e/be59d435418832bfe5f78afb)

![](/assets/images/6sM3sCY.jpg)