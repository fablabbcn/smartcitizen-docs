Smart Citizen Station
==================

![](/assets/images/station30bottom.jpg)

The Smart Citizen Station is a modular environmental monitoring system. Multiple sensors can be added easily added, expanding the capabilities of the installation or replaced when they are damaged or the sensors lifetime is over. From a costs perspective, while being more expensive than the Smart Citizen Kit, it is also conceived as a low-cost solution. The design builds on top of the Smart Citizen Kit, adding an extra set of more accurate sensors, primarily aimed at measuring air pollutants. It aims at providing a solution that can be used by Citizens and Researchers to gather _advanced air pollution data_ not only from a scientific point of view but also as a tool to engage local communities on air pollution-related issues.

The sensors can include **some, or all of**:

- **Up to 16 analog sensors!**, some of which can be gas sensors detailed as below
- **Gas sensors** for gases such as B4 or A4 sensors from [Alphasense Ltd.](http://www.alphasense.com/index.php/air/) such as: CO, NO2, NO, O3, SO2, H2S. These are normally in configurations of 2, 4, or 6 sensors (normally O3 needs NO2 to compensate for cross-sensitivity)
- **CO2 NDIR Sensor** with a [sensirion SCD30](https://www.sensirion.com/en/environmental-sensors/carbon-dioxide-sensors/carbon-dioxide-sensors-co2/)
- **PM sensors** from Plantower or others similar optical particle counters ([OPC](https://en.wikipedia.org/wiki/Particle_counter#Optical_counting))
- **Temperature probe**: external temperature probe for more reliable air temperature sensing
- **Ultra-violet** radiation
- **Noise levels** and FFT spectrum from the Smart Citizen Kit
- **Environmental metrics**: temperature, humidity, ambient pressure from the Smart Citizen Kit

![](/assets/images/station30inside.jpg)

!!! info "From the ground up"
    The station uses the same core functionality, interface and feedback as the Smart Citizen Kit. Make sure you are familiar with them before jumping into the station!

    - [User feedback](/Smart Citizen Kit/#user-feedback) 
    - [LED states and operation modes](/Smart Citizen Kit/#operation-modes)
    - [User interfaces](/Smart Citizen Kit/#user-interfaces)

### Exposure methods

Two possible options are available:

- Passive sensor exposure
- Forced ventilation sensor exposure (experimental)

![](/assets/images/station30.jpg)
_Passive exposure example_

## Power

Currently, the Smart Citizen Station is only available with an external power supply (230VAC to 5V). Find more info in the [power supply section](/Components/Power Supply).

## Connectivity

Currently, the Smart Citizen Station requires a Wi-Fi connection to report data to the [online platform](Sensor Platform) and it can also store data offline locally. Read more about the [operation modes](https://docs.smartcitizen.me/Smart%20Citizen%20Kit/#operation-modes) and the supported networks.

!!! tip "Connectivity Units"
	We tested customized connectivity units capable of deploying a local Wi-Fi network where multiple Smart Citizen Station can connect, data can be relied over GSM (3/4/5G) or other IoT connectivity standards.

## Development versions

![](https://i.imgur.com/CiFikz8.jpg)
_Final iSCAPE Station version (iSCAPE-V2.0)_

!!! info "A note about versions"

    The **iScape Living Lab Station 1.0** was the development version for the 2.0 version. It was sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

![](https://i.imgur.com/QB5P4r9.jpg)
_Middle iSCAPE Station version (iSCAPE-V1.0)_
