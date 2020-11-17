# Soil and water sensors

![](https://live.staticflickr.com/4912/46225599704_bd7d0abec5_k.jpg)

The sensors selected are from Atlas Scientific, a New York-based company that _converts devices that were originally designed to be used by humans into devices that are specifically designed to be used by robots_. The sensors are not entirely open source as the other sensors. However, they are modular and exceptionally well documented by the manufacturer. That includes documentation on how to install, calibrate and integrate them with additional existing hardware. In this direction, we developed a full library for the SCK to support the sensors via the Auxiliary sensor connector. As the sensors can be configured in different ways, we do not provide a full step-by-step guide. Instead, we refer to the documentation on the [project's repository](https://github.com/fablabbcn/smartcitizen-grow/tree/master/soil-water-probes).

The setup is built out of the following main components: 

- Atlas Scientific Sensor Probe: The physical probe we will insert on to the soil (or water).
- Atlas Scientific EZO Circuit: The driver that will read the analog signal coming from the Sensor Probe and turn it into a meaningful numeric value by applying the different calibration operations. 
- Whitebox Labs Tentacle T3: The motherboard that puts everything together and hosts up to 3 Atlas Scientific Probes. It connects to the SCK via the Aux sensor connector. This boards can be chained to support more sensors, but this is not documented at the moment. 
- SEEED Grove - 4 pin Female Jumper to Grove 4 pin Conversion
- Cable needs to be used to connect the board to the SCK.

Different sensor probes can be selected for different needs. For example the setup shown above is designed for soil measurements and includes Atlas Scientific temperature, conductivity and PH probes. It also consists of a Chirp Moisture Sensor as described in the [above section](/Toolkit/guides/soil/#moisture-sensor). As an additional example the setup in the figure below is designed for water monitoring on aquaponics systems and includes Atlas Scientific probes for PH, conductivity and dissolved oxygen.

![](https://i.imgur.com/DT45dpM.jpg)

## Measurements

  | ID |  Name |  Description  |  Unit |  Measurement  | 
 | ------| :-------- | :-------------| :---------| :-------------------- | 
 | 10 | Battery | Custom Circuit | % | battery |
 | 13 | HPP828E031 | Air Humidity | % | humidity |
 | 12 | HPP828E031 | Air Temperature | ºC | air temperature |
 | 14 | BH1730FVC | Digital Ambient Light Sensor | Lux | light | 
 | 42 | DS18B20 | Submergible Water Temperature sensor | °C | water temperature | 
 | 46 | AS EZO Specific Gravity | Atlas Scientific EZO™ Specific Gravity | SG | specific gravity | 
 | 49 | AS EZO Oxygen Saturation | Atlas Scientific EZO™ Oxygen Saturation | % | oxygen saturation | 
 | 43 | AS EZO PH | Atlas Scientific EZO™ pH | PH | pH | pH is a numeric scale used to specify the acidity or basicity of an aqueous solution. | 
 | 48 | AS EZO Dissolved Oxygen | Atlas Scientific EZO™ Dissolved Oxygen | mg/L | dissolved oxygen |
 | 45 | AS EZO Electrical Conductivity | Atlas Scientific EZO™ Electrical Conductivity | µS/cm | electrical conductivity |
 


!!! info "Use cases"
    Check how we have used the water or soil sensors in various projects in the [Use cases section](/Use cases/Research/)

## Hardware

![](https://i.imgur.com/gQavZqU.png)

### Atlas Scientific Carrier board board 

We recommend using [Whitebox Labs Tentacle T3](https://www.whiteboxes.ch/shop/tentacle-t3-for-raspberry-pi/) that hosts up to 3 Atlas Scientific Probes. It connects to the SCK via the Aux sensor connector. This boards can be chained to support more sensors, but this is not documented at the moment. However, before it existed we designed a [custom board](https://github.com/fablabbcn/monitoring-kit-hardware) in collaboration in with [Aquapiooners](http://aquapioneers.io). 

![](https://i.imgur.com/6FysvIl.png)

### Enclosures

#### Legacy enclosures

In collaboration in with [Aquapiooners](http://aquapioneers.io) we designed the [custom enclosure](https://github.com/fablabbcn/monitoring-kit-hardware) below.

![](https://i.imgur.com/aowaWtl.png)

The enclosure of the monitoring board and the smart citizen have been designed on Onshape, you can either download the STL files or copy the project to your onshape account and modify them as you wish : [The Onshape documents of the monitoring case](https://cad.onshape.com/documents/50f1112a541136a65bec4a67/w/db735112a72871fb7c20053e/e/57e22425fb47d5e8030621de)

![](https://i.imgur.com/tXNBC5e.png)

We have also designed a probe holder if you want to hold your probes on the side of you fish tank : [The Onshape document of the probes holder](https://cad.onshape.com/documents/8977ef824f45a910c0b8beaa/w/7ac458735dae629f0a5a73cd/e/be59d435418832bfe5f78afb)

![](https://i.imgur.com/6sM3sCY.jpg)

## Get started

Visit the guides for getting started with the [water and soil sensors](/Guides/deployments/Soil and water sensors).