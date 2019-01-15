Smart Citizen Station
==================

![](https://i.imgur.com/p9lDxiv.jpg)

The Smart Citizen Station, formerly known as the High-End Sensors, is aimed at providing the Living Labs with a system for monitoring the performance of their interventions. The Station aims at providing a solution that can be used by the Living Labs not just from a scientific point of view but also as a tool to engage local communities on air pollution related issues.

![](https://i.imgur.com/QB5P4r9.jpg)

The station is designed with a modular principle where sensors can be added easily added expanding the capabilities of the installation or replaced when they are damaged or the sensors lifetime is over. From a costs perspective while being more expensive than the Smart Citizen Kit it is also conceived as a low-cost solution. That allows to guarantee at least four stations will be available for each Living Lab to increase the spatial resolution and reliability of the measurements.

![](https://i.imgur.com/HUq7Anz.jpg)

The design builds on top of the Smart Citizen Kit adding an extra set of more accurate sensors especially aimed at measuring air pollutants. The sensors include the Gas Sensor Board, featuring EC Carbon Monoxide, Nitrogen Dioxide and Ozone sensors and the PM Sensor Board, featuring a PM 2.5 / PM 10 sensor.

With all the sensor together this Kit provides information on Air Temperature, Relative Humidity, Noise Level, Ambient Light, Barometric Pressure, Particles Matter (PM 2.5 / 10),  Carbon Monoxide, Nitrogen Dioxide and Ozone. The sensors are later described in detail in the document at the Sensor Components section.

## Components

The Living Labs Station is a modular system based on different sensor board that connected to a central datalogger.

![](https://i.imgur.com/n5oiMwY.png)

!!! info "Smart Citizen Stations Components Setup"
    ![](https://i.imgur.com/vh4OLFX.png)

The station operates as a platform where new sensor modules can be shipped and deployed by the Living Labs themselves when they are finished enabling faster iterations and upgrades even after the project finishes.

![](https://i.imgur.com/FFUvfR6.jpg)

![](https://i.imgur.com/RRu8MiV.jpg)

!!! tip "Learn more"
    Learn more about all the components and the software inside the station in the [**Components**](/Components) documentation section.

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

![](https://i.imgur.com/zVPlOcz.jpg)


* iSCAPE Smart Citizen Station
    * Urban Board 2.0
    * Data Board 2.0
    * PM Board 2.0 + 2 PM sensors
    * Gas Pro Board 2.0 with 3 EC sensors
    * 6Ah Battery

* Accessories
    * MicroSD card 512MB
    * USB Charger
    * MicroSD to SD card adapter
    * USB Power Supply
    * 2m 3 Wire 220V cable
    * Mounting brackets and screws
    * Mounting tools (1x Wrench + 2 Allen Keys)

## Instructions

To start the installation simply visit the setup website [**stations.iscape.smartcitizen.me**](https://stations.iscape.smartcitizen.me)

![](https://i.imgur.com/9slH1Ze.png)

Some helpful and important notes before you start:

!!! warning
    We keep track internally of all sensor deployments and it is very important not to swap the internal components between Station to avoid mismatchs on the calibration data.

!!! info "Done for today? Turn off"
    Every time you want to stop the Kit from logging simply press the button for 5 seconds. The led should stop bliking and your Kit will be _OFF_. To turn it _ON_ simply press the button again.

!!! info "Get your data from the SD card"

    _Download the data from the SD card_

    First turn off your Kit by pressing the button for 5 seconds. Then remove the micro SD card and plug the card on your computer using a Micro SD card reader.

    You will find inside a `YYYY-MM-DD.CSV`  with all the data. You can follow the [**Manual CSV data upload**](/Sensor Platform/guides/Uploading SD Card Data/) guide to manually upload the data to the platform.

    _:warning: **Data processing** The collected data requires a custom and complex data processing using the **[iScape Sensor Analysis Framework](https://github.com/fablabbcn/smartcitizen-iscape-data)** The process will be fully documented here on the next few weeks._

### Outdoor

Use the perforated steel tape and the M6 provided to mount the Station on any street light or pole. The Pack also includes the required wrench.

![](https://i.imgur.com/36El7ds.jpg)

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

!!! warning "Get in contact"
    Currently we will run the algorithm manually for each station. Please, contact us once you finish the installation.

!!! info "Sensor Analysis Framework"
    Learn more about the sensors calibration on the [Sensor Analysis Framework](/Sensor Analysis Framework) section.

## Power

The kit has a battery life of 12 hours as is intended as a backup solution only. That's why a power supply needs to be installed as decribed below.

When we no longer want to publish or save more data for a few days we can turn off the kit. To do this, press the button for 5 seconds.

If the colors of the LED appear orange <span class="led small orange"> </span> indicates that the battery must be charged.

The battery takes about 4 hours to fully charge. When the battery is fully charged, change the orange to green <span class="led small green"> </span>.

_Remember that in addition to the colors you will have the state color of the kit: configuration, network and sd._

### Power supply

The Station can be directly powered at 220V AC (Consumption MAX 33W).

!!! warning "Batteries"
    The Smart Citizen Station has a higher consumption, mostly due to the fans on the two PM sensors.

    That means the internal battery last just for 20h, and it is only aimed at providing backup power.

    _For example, we can connect the station on the street light electric line, so the Station gets charged during the night when the lights are on._

!!! info "Solar Panel"
    Unfortunately, we are having some problems with the PV Solar Panel system to power the Station independently. The system is currently under tests, and it will be available in the next few months.

    ![](https://i.imgur.com/vfp6nB5.jpg)

!!! example "Step by step"

    * Remove the two covers using the allen keys as explained on the setup instructions.
        ![](https://i.imgur.com/WPb3tnr.jpg)

    * Remove the USB cable and bring inside the 220V power cable.

        ![](https://i.imgur.com/y54xC4p.jpg)

    * Connect the cable wires with the power supply.

        ![](https://i.imgur.com/U49BppQ.jpg)

    * Remove the third cover and place the power adapter as seen on the picture.

        ![](https://i.imgur.com/WYvxUyy.jpg)

    * Close the cover and run the Setup process again

        ![](https://i.imgur.com/JAK6NMd.jpg)


## States of the Kit

## The button

| Funció            | Acció del botó                                                                                   |
|-------------------|--------------------------------------------------------------------------------------------------|
| **ON**                | Push the button                                                                                  |
| **OFF**               | Push the button for 5 seconds                                                                |
| **CHANGE MODE**       | Push the button multiple times to choose: *Setup* <span class="led small red"></span>  *Wi-Fi* <span class="led small blue"></span> *Pink* <span class="led small pink"></span> |
| **FACTORY RESET** | Push the button 15 seconds for a full reset                                              |


![](https://i.imgur.com/uJ0JJIb.jpg)


## Operation modes

#### <span class="led small red"> </span> Setup mode

In this mode, the Kit is ready to be configured in **network** mode or **SD card** in [**start.smartcitizen.me**](https://start.smartcitizen.me/).

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led setup"></span>            | :thumbsup: Ready to be setup
| <span class="led setup-lowbat"></span>     | :battery: Ready to be setup but battery is low, charge the Kit    |
| <span class="led setup-chargebat"></span>  | :battery: Ready to be setup, battery charging            |
| <span class="led setup-fullbat"></span>    | :battery: Ready to be setup, battery charged                |


#### <span class="led small blue"> </span> Wi-Fi mode

This is the standard mode for a network that requires a Wi-Fi connection. In this way, the device will publish the data every minute on the [smartcitizen.me](https://smartcitizen.me) platform. If there is an inserted micro SD card, the data will be stored in duplicate.

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led net"></span>            | :thumbsup: Collecting data online                 |
| <span class="led net-error"></span>      | :warning: Error while collecting data         |
| <span class="led net-lowbat"></span>     | :battery: Collecting data online but battery is low, charge the Kit    |
| <span class="led net-chargebat"></span>  | :battery: Collecting data online, battery charging              |
| <span class="led net-fullbat"></span>    | :battery: Collecting data online, battery charged               |

!!! warning
    :white_check_mark: The kit supports Wi-Fi WEP, WPA/WPA2 and open networks that are common networks in domestic environments and small businesses.

    :negative_squared_cross_mark: But, it **does not** support WPA/WPA2 Enterprise networks such as EDUROAM or networks with captive portals such as those found in Airports and Hotels

#### <span class="led small pink"> </span> SD card mode (offline)

If we do not have an internet connection we can use the SD mode. In this case the device will record the data on the micro SD card. Later we can read the card using a card reader. The data can be visually spaced in a spreadsheet but also published on the [**smartcitizen.me**](https://smartcitizen.me) platform using the **UPLOAD CSV** option.

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led sd"></span>             | :thumbsup: Collecting data offline              |
| <span class="led sd-error"></span>       | :warning: Error while collecting data         |
| <span class="led sd-lowbat"></span>      | :battery: Collecting data offline but battery is low, charge the Kit    |
| <span class="led sd-chargebat"></span>   | :battery: Collecting data offline,  battery charging              |
| <span class="led sd-fullbat"></span>     | :battery: Collecting data offline, battery charged          |

#### Especial status
| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led busy"></span>           |  :hourglass_flowing_sand:  Busy, please wait!                 |
| <span class="led firmware"></span>       | :wrench: Software update going on!

## Troubleshooting

### Before setup

Before configuring the Station setup make sure the LED is red. If not, press the button multiple times until the LED turns red.

![](https://i.imgur.com/uJ0JJIb.jpg)

### The station does not respond

If the station does not respond or does not work properly you can do two things:

!!! info "Reboot your Station"
    You can fully reboot your Station by pressing the reset button located under the sensors board as seen on the picture.
    That will not delete any configuration, it will simply restart your device.
    Press the `RESET` button for a second. The light will go off and on and the device will start again.

    ![](https://i.imgur.com/tAofJ0g.png)

    You can also perform a reboot by disconnecting the battery and the USB cable so that the station is restarted. In this way we will not lose any data and configuration except the time in case of being in **SD mode**.

    ![](https://i.imgur.com/uJ0JJIb.jpg)


!!! info "Factory reset your Station"

    You can fully reset the Station to the default settings so you can register again your device. Press the main button for **15 seconds**.

    ![](https://i.imgur.com/uJ0JJIb.jpg)

    After 5 seconds the light will go off and will go on again after 15 seconds. Then you can release the button and your device will be fully resetted as a brand new Station.


### The LED does not turn on and the station does not work

First of all, push the station button. Maybe it's simply off.

If this does not work, surely the station has been left without battery. You will have to charge it using the USB charger. Any other mobile charger will also work.

We will know that it is charging when the LED emits <span class="led orange blink"></span> orange pulses and once the battery is charged it will emit green <span class = "led green blink"> </ span>

### The station does not store the data on the SD card.

Some SD cards may have problems over time. We can try [formatting it]() but in case it does not work any micro SD card we buy at any mobile or computer store it will work. The size is not important and any micro SD or micro SDHC 512MB card up to 32GB will work.

![](https://i.imgur.com/h2db2Ch.jpg)

## Dimensions

![](https://i.imgur.com/udiYnTe.png)


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