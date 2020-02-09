Smart Citizen Kit
===========

!!! info "A note about versions"

    The [**SCK 2.0**](/Legacy Hardware/sck) was the development version for the now commercially available **SCK 2.1** sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

!!! tip "Quick links"
	:rocket: **Installation**: [start.smartcitizen.me](https://start.smartcitizen.me/)

	:earth_africa: **Platform: [smartcitizen.me](https://smartcitizen.me)**


    :speech_balloon: **Discuss: [forum.smartcitizen.me](https://forum.smartcitizen.me)**


	:question: **Support: [support@smartcitizen.me](mailto: support@smartcitizen.me)**

## What is it?

The Smart Citizen Kit is the core of what we call the Smart Citizen System: a complete set of **modular hardware components** aiming to provide tools for **environmental monitoring**, ranging from **citizen science** and **educational activities** to more **advanced scientific research**. The system is designed in a extendable way, with a central data logger (the [Data Board](/Components/Data Board)) with network connectivity to which the different components are branched. The system is based on the principle of reproducibility, also integrating non-hardware components such as a dedicated [Storage platform](/Sensor Platform) and a [Sensor analysis framework](/Data Analysis).

On top of that, the system is meant to serve as a **base solution for more complex settings**, not only related with air quality monitoring. For that purpose, in addition to the [Urban Board](/Components/Urban Board), the system also provides off-the-shelf support for a wide variety of third party sensors, using the expansion bus as a common port. One example is what we call the [Smart Citizen Station](/Smart Citizen Station): a full solution for low cost air pollution monitoring.

!!! info "The sensors"
    Have a look a the supported sensors in the [Firmware](https://github.com/fablabbcn/smartcitizen-kit-21/blob/master/lib/Sensors/Sensors.h)!

## :ear: Measurements

All the Smart Citizen Kit new sensors generation measure **at least** air temperature, relative humidity, noise level, ambient light, barometric pressure and particulate matter (PM).

### SCK 2.1

<a data-flickr-embed="true" title="SCK 2.1 All parts"><img src="https://live.staticflickr.com/65535/47950912168_fcf8fa398c_h.jpg" alt="SCK 2.1 All parts"></a>

The SCK 2.1 components are listed below:

1. Smart Citizen Kit 2.1 with Particle Sensor and battery (brackets or rain-proof enclosure currently not included)
2. MicroSD card and microSD adapter to SD.
3. USB cable and a USB charger.

| Measurement                    | Units | Sensors               |
|--------------------------------|-------|-----------------------|
| Air temperature                | ºC    | Sensirion SHT-31      |
| Relative Humidity              | % REL | Sensirion SHT-31      |
| Noise level                    | dBA   | Invensense ICS-434342 |
| Ambient light                  | Lux   | Rohm BH1721FVC        |
| Barometric pressure            | Pa    | NXP MPL3115A26        |
| Equivalent Carbon Dioxide      | ppm   | AMS CCS811            |
| Volatile Organic Compounds     | ppb   | AMS CCS811            |
| Particulate Matter PM 1 / 2.5 / 10 | µg/m3 | Planttower PMS 5003              |

## :notebook: Installation instructions

The sensor comes mounted and almost ready to be used:

<img src="https://live.staticflickr.com/65535/47950999751_13e6e00f49_b.jpg" alt="SCK 2.1 How to start?">

The first step is to connect the battery. The kit will light in red (configuration mode) and we will be able to configure it by following the instructions at [start.smartcitizen.me](https://start.smartcitizen.me).

![](https://i.imgur.com/NhSNXJ8.png)

After the configuration process, data will be available on the SmartCitizen platform. You can explore the data there or download it using the `CSV Download` option (guide [here](/Guides/Downloading the Data/))

![](https://i.imgur.com/5NlWx6O.jpg)

## :battery: Power management

### Battery duration

The SCK comes with a 2000mAh LiPo battery. The battery is meant to be a complete power option for short-term measurements and a backup solution when the kit it is used for long periods. For long exposures, we recommend to permanently connect the USB to kit. The battery duration is dependent on which sensors are enabled or disabled:

* All sensors publishing over Wi-Fi: 12 hrs.
* All sensors publishing on SD card: 13 hrs.
* Without air quality sensors over Wi-Fi: 10 days
* Without air quality sensors on SD card: 25 days

You will note that the kit _turns itself off_ while operating on battery. Actually, this is what we call `sleep-mode`, an operation mode implemented to reduce consumption while on battery operation.

### Battery charging

The SCK has a micro USB port and can be charged like any Smartphone or Tablet using a dedicated adapter or a computer USB port.

We recommend using a tablet power adaptor, instead of a computer USB port, for quicker charging. Autonomy can be extended by using a Power Bank, or a 5V PV Panel.

### User feedback

The LED serves as an indication of the battery status. If the LED is flashing orange <span class="led small orange"> </span> it indicates that the battery must be charged. The battery takes about 4 hours to fully charge. When the battery is fully charged, the LED will change from orange to green <span class="led small green"> </span>.

<div style="text-align: center">
<img src="https://i.imgur.com/ABSXX4w.jpg" alt="SCK 2.1" width="400px"></div>

_Remember that in addition to these colors you will have the state color of the kit: configuration, network and sd._

!!! info "More details"
    Find more details under the [data board section](/Components/Data Board/#power-management)

## :triangular_flag_on_post: User interfaces

The data board features a set of user interfaces which provide feedback to the user, as well as two buttons with different functionalities. The main RGB LED provides general feedback of the data board status. Additionally, two buttons are provided for user action. A hardware reset button, which forces a power cut to the board, and a power button, used to change the device's mode, turn on and off the device, and to perform a factory reset. You can see both buttons below:

<div style="text-align: center">
<img src="https://i.imgur.com/AmlA8e2.png" alt="SCK 2.1" width="400px"></div>

### The button

The main button interaction is detailed below:

| Function          | Button action     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ON**            | Push the button   |
| **OFF**           | Push the button for 5 seconds |
| **CHANGE MODE**   | Push the button multiple times to choose: *Setup* <span class="led small red"></span>  *Wi-Fi* <span class="led small blue"></span> *Pink* <span class="led small pink"></span> |
| **FACTORY RESET** | Push the button 15 seconds for a full reset |

An example is shown below:

<img src="https://live.staticflickr.com/65535/48439505516_d210ce2c8a_h.jpg" alt="SCK 2.1">

!!! info "Troubleshooting"
    Have a look at the [troubleshoothing section](/Troubleshooting) to check how you can use the buttons in case of problems with your SCK!

### Operation modes

#### <span class="led small red"> </span> Setup mode

In this mode, the Kit is ready to be configured in **network** mode or **SD card** in [start.smartcitizen.me](https://start.smartcitizen.me/).

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

If we do not have an internet connection we can use the SD mode. In this case the device will record the data on the micro SD card. Later we can read the card using a card reader. The data can be visually spaced in a spreadsheet but also published on the [smartcitizen.me](https://smartcitizen.me) platform using the **UPLOAD CSV** option.

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

## Software Updates

Sofware updates are release frequently in the [Firmware repository](https://github.com/fablabbcn/smartcitizen-kit-21). These updates will need to be applied periodically to the two main components of the SCK: the SAMD21 (main processor) and the ESP8266 (Wi-Fi module). Check the instructions under the [Update the Firmware](/Components/Firmware/guides/Update the firmware/) section for more information.

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

