---
card: true
type: unit
name: Water Kit
field:
  - water
versions:
    hardware: 2.x
    firmware: 0.9.9_sck_water
feature_img: https://live.staticflickr.com/65535/53909712132_b46cae1a7e_k.jpg
excerpt: The Water Kit is meant to measure one physico chemical parameter at a time. Choose from pH, Temperature, Dissolved Oxygen, Conductivity or ORP.
---

# Water Station

<!-- TODO -->

### Technical specifications

A normal IP enclosure can be used for the Water Station. More information about the BOM and design files can be found [in the enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures/).

<img src="https://live.staticflickr.com/65535/51125200496_67b06e79bd_k.jpg" alt="Water Station - Patí Científic">

!!! info "Thanks!"
    This enclosure and development has been done in collaboration with [ICM-CSIC](https://www.icm.csic.es/en) and the [Club Pati Vela de Barcelona](https://pativelabarcelona.com/).

#### Power

Currently, the Smart Citizen Soil/Water Stations are only available with an external power supply (230VAC to 5V), with a small battery for backup during power brownouts. Due to the number of sensors, and depending on the configuration the solution is normally not meant for long term deployment with just battery power. For specifications of the power supply, find more info in the [power supply section](/hardware/power/Power Supply/).

| Power        |                                                                  |
| :-:          | :-                                                               |
| DC Voltage   | 5V                                                               |
| DC Current   | 2A _recommended_                                                 |
| AC Voltage   | 230V  _into the [Power Supply](/hardware/power/Power Supply/)_   |
| AC Current   | <0.16A _into the [Power Supply](/hardware/power/Power Supply/)_  |

!!! warning "Battery or solar operation?"
    The Station currently supports battery operation only for short periods of time (<2d days). Depending on the location, [solar power](/hardware/power/Solar Panel/) might be available, but we do not recommend it unless you are willing to _experiment_.

#### Dimensions and weight

<!-- TODO - Add table with size -->

| Version       | Dimensions | Weight |
| :-:           | :-         | :-     |
| Box           | | |
| Probe holder  | | |

!!! info "Design files"
    If you are looking for the design files about the Smart Citizen Station, take a look at the [enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures/).

#### Connectivity

Similar to the [Smart Citizen Kit](/hardware/Smart Citizen Kit/), if you want to have your data online, the Smart Citizen Water Station requires a Wi-Fi connection to report data to the [platform](/Data/Sensor Platform). If not, the unit can also store data locally on its onboard sd-card. Read more about the [operation modes](/hardware/Smart%20Citizen%20Kit/#operation-modes) and the [supported networks](/_FAQ/#what-networks-does-it-support).