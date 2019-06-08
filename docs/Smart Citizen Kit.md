Smart Citizen Kit
===========

!!! info "A note about versions"
    **The following section contains information about the SCK 2.0 and the SCK 2.1.**

    The **SCK 2.0** was the development version for the now commercially available **SCK 2.1** sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

!!! tip "Quick links"
	:rocket: **Installation: [start.smartcitizen.me](https://start.smartcitizen.me/)**

	:earth_africa: **Platform: [smartcitizen.me](https://smartcitizen.me)**


    :speech_balloon: **Discuss: [forum.smartcitizen.me](https://forum.smartcitizen.me)**


	:question: **Support: [support@smartcitizen.me](mailto: support@smartcitizen.me)**



## :gift: The Kit

The Smart Citizen Kit 2.0.

![](https://i.imgur.com/vgt8m3p.jpg)

1. Smart Smart Citizen Kit 2.0 with particle and battery sensor with two mounting brackets.
2. MicroSD card and microSD adapter to SD.
3. USB cable and a USB charger to charge the battery.

## :ear: Measurements

All the Smart Citizen Kit new sensors generation measure at least air temperature, relative humidity, noise level, ambient light, barometric pressure and particulate matter.

### SCK 2.1

!!! info "Important!"
    Detailed information is currently under development and can be partially found on the previous [SCK 2.0 Urban Sensor Board](/Components/Urban%20Sensor%20Board/) on the [Components](/Components) section.

    **More information coming soon!**

| Measurement                    | Units | Sensors               |
|--------------------------------|-------|-----------------------|
| Air temperature                | ºC    | Sensirion SHT-31      |
| Relative Humidity              | % REL | Sensirion SHT-31      |
| Noise level                    | dBA   | Invensense ICS-434342 |
| Ambient light                  | Lux   | Rohm BH1721FVC        |
| Barometric pressure            | Pa    | NXP MPL3115A26        |
| Equivalent Carbon Dioxide      | ppm   | AMS CCS811            |
| Volatile Organic Compounds     | ppb   | AMS CCS811            |
| Particulate Matter PM 1 / 2.5 / 10 | µg/m3 | PMS 5003              |

### SCK 2.0

!!! info "Important!"
    **SCK 2.0 was the development version for the now commercially available SCK 2.1**

    The board also includes a SGX MICS-4514 and a MAXIM MAX3010 but those are not supported by the standard firmware configuration. Fore more information visit the [Urban Sensor Board](Components/Urban%20Sensor%20Board/) on the [Components](Components) section.

| Measurement                    | Units | Sensors               |
|--------------------------------|-------|-----------------------|
| Air temperature                | ºC    | Sensirion SHT-31      |
| Relative Humidity              | % REL | Sensirion SHT-31      |
| Noise level                    | dBA   | Invensense ICS-434342 |
| Ambient light                  | Lux   | Rohm BH1721FVC        |
| Barometric pressure            | Pa    | NXP MPL3115A26        |
| Particulate Matter PM 1 / 2.5 / 10 | µg/m3 | PMS 5003              |

## :notebook: Instructions

The sensor comes mounted and almost ready to be used

![](https://i.imgur.com/GfQy84y.jpg)

The only thing we should do is connect the battery. The kit will light in red and we will be able to configure it by following the instructions at [**start.smartcitizen.me**](https://start.smartcitizen.me).

![](https://i.imgur.com/5mjUhWr.png)

After the configuration your data will be available on the SmartCitizen platform. You can explore the data there or download it using the `CSV Download` option.

![](https://i.imgur.com/5NlWx6O.jpg)

## :battery: Autonomy

The kit has a battery life of 12 hours. For long exposures, we can permanently connect to the USB.

When we no longer want to publish or save more data for a few days we can turn off the kit. To do this, press the button for 5 seconds.

If the colors of the LED appear orange <span class="led small orange"> </span> indicates that the battery must be charged.

The battery takes about 4 hours to fully charge. When the battery is fully charged, change the orange to green <span class="led small green"> </span>.

![](https://i.imgur.com/RxD960s.jpg)

_Remember that in addition to the colors you will have the state color of the kit: configuration, network and sd._


## :triangular_flag_on_post: States of the Kit

## The button

| Function          | Button action                                                                                                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ON**            | Push the button                                                                                                                                                                 |
| **OFF**           | Push the button for 5 seconds                                                                                                                                                   |
| **CHANGE MODE**   | Push the button multiple times to choose: *Setup* <span class="led small red"></span>  *Wi-Fi* <span class="led small blue"></span> *Pink* <span class="led small pink"></span> |
| **FACTORY RESET** | Push the button 15 seconds for a full reset                                                                                                                                     |

![](https://i.imgur.com/fy3rSbc.png)


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

## :umbrella: Build your own enclosure

If we want to leave the kit on the outside for a few days you will need to provide it with extra protection.
 
!!! warning
    Keep in mind that casing is designed for short outdoor deployments. If you want a case for long exhibitions abroad, we will soon have a much more rugged enclosure ready! Also, feel free to explore all our [enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures) for this and other versions of our hardware.

!!! example "Step by step"

    **First, you will need the two 3D printed clips. You can [download the STL](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20DIY%20Clips%20V2.0-2.1/3D%20Print%20Clips.stl) file and print them easily on any RepRap or similar FDM printer. If you don't know how to find a 3D printer, you can look for your nearest [Fab Lab](https://www.fablabs.io/labs) or use [3D Hubs](https://www.3dhubs.com/3dprint).**

    <script src="https://embed.github.com/view/3d/fablabbcn/smartcitizen-enclosures/master/SmartCitizen%20DIY%20Clips%20V2.0-2.1/3D%20Print%20Clips.stl"></script>


    1.Use scissors to cut an empty plastic bottle at about 12 cm from the top

    ![](https://i.imgur.com/heo8cwW.jpg)

    2.Use the rubber band to fix it using the bottle cap

    ![](https://i.imgur.com/CjKDBBl.jpg)

    3.Place the Kit inside and use the rubber band to hold it

    ![](https://i.imgur.com/8KzbAqV.jpg)

    4.You have now a simple enclosure to use your Kit outdoors for short measurement periods!

    ![](https://i.imgur.com/IhGxV67.jpg)

**You can now install the sensor outdoors!**

![](https://i.imgur.com/0kV6gie.jpg)

## :construction_worker: Troubleshooting

### Before setup

Before configuring the Kit setup make sure the LED is red. If not, press the button multiple times until the LED turns red.

![](https://i.imgur.com/9iK1ZLl.jpg)

### The kit does not respond

If the kit does not respond or does not work properly you can do two things:

!!! info "Reboot your Kit"
	You can fully reboot your Kit by pressing the reset button located under the sensors board as seen on the picture.
 	That will not delete any configuration, it will simply restart your device.
 	Press the `RESET` button for a second. The light will go off and on and the device will start again.

 	![](https://i.imgur.com/tAofJ0g.png)

 	You can also perform a reboot by disconnecting the battery and the USB cable so that the kit is restarted. In this way we will not lose any data and configuration except the time in case of being in **SD mode**.

 	![](https://i.imgur.com/uWJHCyr.jpg)


!!! info "Factory reset your Kit"

	You can fully reset the Kit to the default settings so you can register again your device. Press the main button for **15 seconds**.

	![](https://i.imgur.com/9iK1ZLl.jpg)

	After 5 seconds the light will go off and will go on again after 15 seconds. Then you can release the button and your device will be fully resetted as a brand new Kit.


### The LED does not turn on and the kit does not work

First of all, push the kit button. Maybe it's simply off.

If this does not work, surely the kit has been left without battery. You will have to charge it using the USB charger. Any other mobile charger will also work.

We will know that it is charging when the LED emits <span class="led orange blink"></span> orange pulses and once the battery is charged it will emit green <span class = "led green blink"> </ span>

### The kit does not store the data on the SD card.

Some SD cards may have problems over time. We can try [formatting it]() but in case it does not work any micro SD card we buy at any mobile or computer store it will work. The size is not important and any micro SD or micro SDHC 512MB card up to 32GB will work.


## CSV Upload

Here some instructions on how to upload CSV files to Smartcitizen platform. First be sure to be logged and go to your [profile](https://smartcitizen.me/profile/kits).

On your kits' list, click on the wheel and then on `Upload CSV`.

![](https://i.imgur.com/gyMgl5n.png)

Once on the upload page, you can add some files by clicking on the `Load CSV files` button.

![](https://i.imgur.com/98bcwRj.png)

Select some files as much as you like, to be them ready to upload. Then on the drop-down menu select the `Upload` option

![](https://i.imgur.com/V6LEqrz.png)

Click on the `Apply` button to upload them

![](https://i.imgur.com/gKbq2UB.png)

Congrats! You just uploaded your files CSV files on the Smartcitizen platform.

![](https://i.imgur.com/fw6raGS.png)

## Technical specs

The Smart Citizen Kit, formerly known as the Low-Cost Sensor, is aimed at providing a low-cost environmental sensor solution non-technical users can easily deploy. The design developed for the project is a complete reiteration of the  Smart Smart Citizen Kit, a piece of hardware for citizen sensing already tested in other projects for more than five years. On this iteration, new sensors had been added, and all the electronic design has been redone from the ground up to improve the data accuracy and reduce the manufacturing costs.

### Components

The design is built around two boards the Smart Citizen Data Board and the Smart Citizen Urban Sensor Board. The first board contains the data acquisition, the power management, and the communication unit. The second contains a set of sensors aimed at the outdoor urban environment including: Air Temperature, Relative Humidity, Noise Level, Ambient Light and Barometric Pressure. The board also features a section especially focused on Air Quality including a Air Particles, a Carbon Monoxide, and a Nitrogen Dioxide detectors. This sensor while not capable of offering precise measurements can be used to understand the behavior of different urban locations especially when they are calibrated on the field using certified equipment. Both boards are later described in detail on the Sensor Components section.

!!! info "Smart Citizen Kits Components Setup"
    ![](https://i.imgur.com/il20Xqa.png)

!!! tip "Learn more"
    Learn more about all the components and the software inside the kit in the [**Components**](/Components) documentation section.

### Software Updates
The SCK 2.0 has two components that need periodic updates. The SCK 2.0 appears as a USB Storage device and the new firmware can be installed on your kit by simply downloading the new firmware release and then dragging and dropping into the SCK 2.0 device root folder. The Wi-Fi module firmware is updated automatically over-the-air every time the main processor firmware is updated.

!!! info "Firmware updates"
	[Update the Firmware](Components/Firmware/Guides/Update the firmware)


### Dimensions

* Dimensions: 60 x 60 x 20 mm (approx.)
* Dimensions w/ enclosure: 110 x 110 x 50mm (approx.)
* Weight: 65 gr.
* Weight w/ enclosure: 160 gr.

### Power Management

#### Battery lifetime
The SCK 2.0 comes with a 2000mAh LiPo battery. The battery is meant to be a complete power option for short-term measurements and a backup solution when the kit it is used for long periods. The battery lifetime lifetime is dependent on which sensors are enabled or disabled:

* All sensors publishing over Wi-Fi: 12 hrs.
* All sensors publishing on SD card: 13 hrs.
* Without air quality sensors over Wi-Fi: 10 days
* Without air quality sensors on SD card: 25 days

#### Battery charging
The SCK 2.0 has a micro USB port and can be charged like any Smartphone or Tablet using a dedicated adapter or a computer USB port.
We recommend using a tablet power adaptor, instead of a computer USB port, for quicker charging. Autonomy can be extended by using a Power Bank, a 5V PV Panel, or with a through-glass induction charger (currently under development).



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

