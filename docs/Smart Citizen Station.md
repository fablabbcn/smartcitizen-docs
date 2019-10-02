Smart Citizen Station
==================

![](https://i.imgur.com/p9lDxiv.jpg)

The Smart Citizen Station was born with the idea to provide the iScape Living Labs with a system for monitoring the performance of their interventions. The Station aims at providing a solution that can be used by the Living Labs not just from a scientific point of view but also as a tool to engage local communities on air pollution related issues.

![](https://i.imgur.com/QB5P4r9.jpg)

The station is designed with a modular principle where sensors can be added easily added expanding the capabilities of the installation or replaced when they are damaged or the sensors lifetime is over. From a costs perspective while being more expensive than the Smart Citizen Kit it is also conceived as a low-cost solution.

![](https://i.imgur.com/HUq7Anz.jpg)

The design builds on top of the Smart Citizen Kit adding an extra set of more accurate sensors especially aimed at measuring air pollutants. The sensors include the Gas Sensor Board, featuring EC Carbon Monoxide, Nitrogen Dioxide and Ozone sensors and the PM Sensor Board, featuring a PM 2.5 / PM 10 sensor.

With all the sensor together this Kit provides information on Air Temperature, Relative Humidity, Noise Level, Ambient Light, Barometric Pressure, Particles Matter (PM 2.5 / 10),  Carbon Monoxide, Nitrogen Dioxide and Ozone. The sensors are later described in detail in the document at the Sensor Components section.

!!! info "A note about versions"

    The **iScape Living Lab Station 1.0** was the development version for the 2.0 version. It was sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

## Components

The Station is a modular system based on different sensor board that connected to a central datalogger.

![](https://i.imgur.com/n5oiMwY.png)

!!! info "Smart Citizen Stations Components Setup"
    ![](https://i.imgur.com/vh4OLFX.png)

![](https://i.imgur.com/FFUvfR6.jpg)

![](https://i.imgur.com/RRu8MiV.jpg)

## Sensors

| Measurement                                  | Units                                          | Sensor                        | Component              |
|----------------------------------------------|------------------------------------------------|-------------------------------|------------------------|
| Air Temperature                              | ºC                                             | Sensirion SHT-31              | Urban Sensor Board     |
| Relative Humidity                            | % REL                                          | Sensirion SHT-31              | Urban Sensor Board     |
| Noise Level                                  | dBA                                            | Invensense ICS-434342         | Urban Sensor Board     |
| Ambient Light                                | Lux                                            | Rohm BH1721FVC                | Urban Sensor Board     |
| Barometric pressure and AMSL                 | Pa and Meters                                  | NXP MPL3115A26                | Urban Sensor Board     |
| Carbon Monoxide                              | µg/m3 (Periodic Baseline Calibration Required) | SGX MICS-4514                 | Urban Sensor Board     |
| Nitrogen Dioxide                             | µg/m3 (Periodic Baseline Calibration Required) | SGX MICS-4514                 | Urban Sensor Board     |
| Carbon Monoxide                              | ppm                                            | Alphasense CO-B4              | Gas Sensor Pro Board   |
| Nitrogen Dioxide                             | ppb                                            | Alphasense NO2-B43F           | Gas Sensor Pro Board   |
| Ozone                                        | ppb                                            | Alphasense OX-B431            | Gas Sensor Pro Board   |
| Gases Board Temperature                      | ºC                                             | Sensirion SHT-31              | Gas Sensor Pro Board   |
| Gases Board Rel. Humidity                    | % REL                                          | Sensirion SHT-31              | Gas Sensor Pro Board   |
| PM 1                                         | µg/m3                                          | Plantower PMS5003 Dual System | PM Sensors Board       |
| PM 2.5                                       | µg/m3                                          | Plantower PMS5003 Dual System | PM Sensors Board       |
| PM 10                                        | µg/m3                                          | Plantower PMS5003 Dual System | PM Sensors Board       |


## The Pack

!!! warning "Versions"
    Below the detailed list of components for the Smart Citizen Station V2.0. You can find more information regarding the iScape Living Lab Station V1.0, visit [here](//Smart Citizen Station Deployments/#iscape-living-lab-station-v1).

* Smart Citizen Station
    * Urban Board 2.1
    * Data Board 2.1
    * PM Board 2.0 + 2 PM sensors
    * Gas Pro Board 2.0 with 3 EC sensors
    * 6Ah Battery

* Accessories
    * MicroSD card 512MB
    * USB Charger
    * MicroSD to SD card adapter
    * Smart Citizen Power Supply (Traco P.S. 230AC in - DC5V out)
    * 2m 3-Wire 220V cable
    * Mounting brackets
    * Mounting tools (1 x Allen Key)
    * Enclosure
    * Mounting bracket
    * Thermoconformed Umbrella 

## Instructions

To start the installation simply visit the setup website [stations.iscape.smartcitizen.me](https://stations.iscape.smartcitizen.me)

![](https://i.imgur.com/9slH1Ze.png)

!!! warning
    We keep track internally of all sensor deployments and it is very important not to swap the internal components between Station to avoid mismatchs on the calibration data.

!!! info "More info"
    Deployment considerations are listed [here](/Smart Citizen Station Deployments/#iscape-living-lab-station-v2)

### Sensor considerations

**Electrochemical sensor**

The electrochemical sensors **need stabilisation time under the testing conditions** they will be at. It is important to set and power the sensors with sufficient time (1-2 days) on the test environment for them to adapt. The newer the sensor, the more stabilisation time it requires. For this deployment, you will be receiving brand new sensors.

Humidity and temperature extremes will require of further sensor adaptation, in order to dry out or absorb the necessary humidity for their proper functioning.

!!! danger
    Do not extract/attach the sensor capsule from the base board while powered, this could irreversibly damage the sensor.

**Particle Sensor**

The particle sensors measurements are delivered as averages of the two sensors with periodic validity checks. We are currently developing one-shot strategies for battery life improvement, but in the meantime, please make sure the sensor has reliable energy supply if you will use these sensors permanently.

### Sensor data processing

We have developed an algorithm that ingests the platform data and processes electrochemical sensor sensor data. This algorithm is **in validation stage** and will be included in the online platform flow from Smart Citizen once validated.

!!! info "Sensor Analysis Framework"
    Learn more about the sensors calibration on the [Sensor Analysis Framework](/Sensor Analysis Framework) section.

## Power

The kit has a battery life of 12 hours as is intended as a backup solution only. That's why a power supply needs to be installed as decribed below.

When we no longer want to publish or save more data for a few days we can turn off the kit. To do this, press the button for 5 seconds.

If the colors of the LED appear orange <span class="led small orange"> </span> indicates that the battery must be charged.

The battery takes about 4 hours to fully charge. When the battery is fully charged, change the orange to green <span class="led small green"> </span>.

_Remember that in addition to the colors you will have the state color of the kit: configuration, network and sd._

### Power supply

The Station can be directly powered at 220V AC (max consumption 5W).

!!! warning "Batteries"
    The Smart Citizen Station has a higher consumption than the kit, mostly due to the fans on the two PM sensors.

    That means the internal battery last just for 20h, and it is only aimed at providing backup power.

    _For example, we can connect the station on the street light electric line, so the Station gets charged during the night when the lights are on._

!!! info "Solar Panel"
    Unfortunately, we are having some problems with the PV Solar Panel system to power the Station independently. The system is currently under tests, and it will be available in the next few months.

    ![](https://i.imgur.com/vfp6nB5.jpg)

!!! info "Changing power supplies"
    If you need to change power supplies (iScape Living Lab Station V1.0), please visit [here](/Smart Citizen Station Deployments/#changing-power-supplies)

<style>
.led {
    width: 20px; height: 20px; border-radius:10px; display: inline-block; margin-top: 7px;

}

.small {
    width: 14px; height: 14px; border-radius:7px;

}

.orange {
    background: orange;
}

.green {
    background: lime;
}

.red {
    background: red;
}

.blue {
    background: blue;
}

.pink {
    background: magenta;
}

.blink {
    animation:1s blinker linear infinite;
}

.net {
    animation:2s net ease infinite;
}

.net-error {
    animation:0.4s net linear infinite;
}

.net-lowbat {
    animation:1s net-lowbat ease infinite;
}

.net-chargebat {
    animation:2s net-chargebat ease infinite;
}

.net-fullbat {
    animation:2s net-fullbat ease infinite;
}

.sd {
    animation:2s sd ease infinite;
}

.sd-error {
    animation:0.4s sd linear infinite;
}

.sd-lowbat {
    animation:1s sd-lowbat ease infinite;
}

.sd-chargebat {
    animation:2s sd-chargebat ease infinite;
}

.sd-fullbat {
    animation:2s sd-fullbat ease infinite;
}

.setup {
    animation:2s setup ease infinite;
}

.setup-error {
    animation:0.4s setup linear infinite;
}

.setup-lowbat {
    animation:1s setup-lowbat ease infinite;
}

.setup-chargebat {
    animation:2s setup-chargebat ease infinite;
}

.setup-fullbat {
    animation:2s setup-fullbat ease infinite;
}

.busy {
    animation:2s busy ease infinite;
}

.firmware {
    animation:2s firmware ease infinite;
}

@keyframes blinker {
     0% { opacity: 1.0; }
     50% { opacity: 0.0; }
     100% { opacity: 1.0; }
}

@keyframes setup {
     0% { background: white;}
     50% { background: red;}
     100% { background: white;}
}

@keyframes setup-lowbat {
     0% { background: orange; }
     15% { background: red; }
     85% { background: red; }
     100% { background: orange; }
}

@keyframes setup-chargebat {
     0% { background: orange; }
     50% { background: red; }
     100% { background: orange; }
}

@keyframes setup-fullbat {
     0% { background: lime; }
     50% { background: red; }
     100% { background: lime; }
}

@keyframes firmware {
     0% { background: white;}
     50% { background: lime;}
     100% { background: white;}
}

@keyframes net {
     0% { background: white; }
     50% { background: blue; }
     100% { background: white; }
}

@keyframes net-lowbat {
     0% { background: orange; }
     15% { background: blue; }
     85% { background: blue; }
     100% { background: orange; }
}

@keyframes net-chargebat {
     0% { background: orange; }
     50% { background: blue; }
     100% { background: orange; }
}

@keyframes net-fullbat {
     0% { background: lime; }
     50% { background: blue; }
     100% { background: lime; }
}

@keyframes sd {
     0% { background: white; }
     50% { background: magenta; }
     100% { background: white; }
}

@keyframes sd-lowbat {
     0% { background: orange; }
     15% { background: magenta; }
     85% { background: magenta; }
     100% { background: orange; }
}

@keyframes sd-chargebat {
     0% { background: orange; }
     50% { background: magenta; }
     100% { background: orange; }
}

@keyframes sd-fullbat {
     0% { background: lime; }
     50% { background: magenta; }
     100% { background: lime; }
}

@keyframes busy {
     0% { background: white; }
     50% { background: black; }
     100% { background: white; }
}

</style>