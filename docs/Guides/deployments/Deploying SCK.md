# Deploying the Smart Citizen Kit

The Smart Citizen Kit can be used in both, indoor or outdoor setups. This page gives guidelines on how to install in either situation.

![](https://camo.githubusercontent.com/bfecdc4c79c986951a73b62df7fe74ebbced1b83/68747470733a2f2f6c6976652e737461746963666c69636b722e636f6d2f36353533352f34383433393530353430365f633331336537656461335f682e6a7067)

## Indoor installation

In indoor conditions, the Kit can be installed using this [3D printed clip](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20Outdoor%20Cases%20V2.0-2.1/Milled%20HDPE/components/CLIP_NO_ORING.stl).

![](https://live.staticflickr.com/65535/48020070592_ebad902f1d_h.jpg)

### How to install the kit

Make sure you read the information about each type of sensor before installation:

- [eCO2 and tVOCs sensor](/Components/sensors/CCS811/#sensor-considerations)
- [Noise](/Components/sensors/Noise/#sensor-considerations)
- [PM sensor](/Components/sensors/PM Sensors/#sensor-considerations)

#### General tips

- Keep the sensors powered if they are going to be mounted in a fixed point
- Avoid areas with moist accumulation when possible
- Avoid temperature and humidity transients, specially for the eCO2/tVOC sensor
- Avoid covering the sensors, specially the PM sensor
- Avoid covering the microphone and particles to go in the microphone port
- Avoid direct flow towards the sensors. If exposed under flow conditions, have the flow go parallel to the sensors' surface

## Outdoor installation

For outdoor installation, an enclosure is recommended in order to avoid moisture to damage the sensors and electronics. The [Enclosures Repository](https://github.com/fablabbcn/smartcitizen-enclosures) contains various types (3D printed, milled, DIY) from us and contributions from users that customise their own! Feel free to download the models and tweak them, and if happy, share them back via pull request to the repository.

![](https://raw.githubusercontent.com/fablabbcn/smartcitizen-enclosures/master/SmartCitizen%20Outdoor%20Cases%20V2.0-2.1/Milled%20HDPE/final_render.png)

The general tips from above also apply, as well as:

- Avoid exhausts from air conditioning units, kitchens and others
- Protect the sensors from moisture either using filtering foam or nail polish to cover the sensor pads (see [here](/_FAQ/#are-the-electronics-waterproof))
- Avoid temperature transients, specially due to sun radiation

### Powering the sensor

The SCK can be powered through:

- LiPo 3.7V Battery: default 2000mAh - large 6000mAh
- Mains power, through an USB adaptor (not recommended) or a [custom power supply](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20PowerSupply) in [this enclosure](https://uk.rs-online.com/web/p/junction-boxes/2663120/)
- [Solar panel](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20PowerSupply#solar-power-controller-optional): we use the [Solar Panel 6W 6V from Voltaic Systems](https://voltaicsystems.com/6-watt-panel/) with the [MPTT DF Robot DFR0559](https://wiki.dfrobot.com/Solar_Power_Manager_5V_SKU__DFR0559) and an additional LiPo Battery, all in [this enclosure](https://uk.rs-online.com/web/p/junction-boxes/2663120/)

!!! tip "Using the power supply"
    If you are using the Smart Citizen Power Supply, have a look at [this guide](/Guides/deployments/Using the power supply.md) for safety instructions.

### Connectivity

The sensors can log data in sd card or remote post data to the Smart Citizen Platform. In the case of remote logging and outdoor deployments, a _connectivity unit_ can be used with a SIM Card data plan. These units are enclosed in a waterproof box and can be powered from 230VAC 3m cable (or more), deploying a network to which several SCKs can be connected in an outdoor deployment. 

You can check the BOM and installation/building [here](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Connectivity%20Unit) and you can email us at [info@smartcitizen](mailto:info@smartcitizen.me) for more information.

![](https://i.imgur.com/y9ap4LK.jpg)

!!! info "Got one?"
    Check this [installation guide to get started](/Guides/Installing Connectivity Units)