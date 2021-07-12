Smart Citizen Kit
===========

!!! info "A note about versions"

    The [**SCK 2.0**](/Components/legacy/sck) was the development version for the now commercially available **SCK 2.1** sponsored thanks to the [iSCAPE project](https://www.iscapeproject.eu/) under European Community’s H2020 Programme under Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en)

!!! tip "Quick links"

    :gift: **Buy: [seeedstudio.com](https://www.seeedstudio.com/Smart-Citizen-Starter-Kit-p-2865.html)**

	:rocket: **Installation: [start.smartcitizen.me](https://start.smartcitizen.me/)**

	:earth_africa: **Platform: [smartcitizen.me](https://smartcitizen.me)**

    :speech_balloon: **Discuss: [forum.smartcitizen.me](https://forum.smartcitizen.me)**

	:question: **Support: [support@smartcitizen.me](mailto: support@smartcitizen.me)**

    :sparkles: **Something big?: [info@smartcitizen.me](mailto: info@smartcitizen.me)**

## What is it?

The Smart Citizen Kit is the core of what we call the Smart Citizen System: a complete set of **modular hardware components** aiming to provide tools for **environmental monitoring**, ranging from **citizen science** and **educational activities** to more **advanced scientific research**.

<a data-flickr-embed="true" title="SCK 2.1 All parts">![](https://live.staticflickr.com/65535/47950912168_fcf8fa398c_h.jpg)</a>

The system is designed in a extendable way, with a central data logger (the [Data Board](/Components/boards/Data Board)) with network connectivity to which the different components are branched. The system is based on the principle of reproducibility, also integrating non-hardware components such as a dedicated [Storage platform](/Data/Sensor Platform) and a [Sensor analysis framework](/Data/Data Analysis).

![](https://i.imgur.com/i2qzNVl.jpg)

On top of that, the system is meant to serve as a **base solution for more complex settings**, not only related with air quality monitoring. For that purpose, in addition to the [Urban Board](/Components/boards/Urban Board), the system also provides off-the-shelf support for a wide variety of third party sensors, using the expansion bus as a common port. One example is what we call the [Smart Citizen Station](/Smart Citizen Station): a full solution for low cost air pollution monitoring.

!!! info "The sensors"
    Have a look a the supported sensors in the [Firmware](https://github.com/fablabbcn/smartcitizen-kit-21/blob/master/lib/Sensors/Sensors.h)!

## :ear: Measurements

All the Smart Citizen Kit new sensors generation measure **at least** air temperature, relative humidity, noise level, ambient light, barometric pressure and particulate matter (PM).

### SCK 2.1

![](https://i.imgur.com/4UEoDoW.png)

Here is the table summarising the sensors:

| Measurement                    | Units | Sensors               |
|:--------------------------------|:-------:|:-----------------------:|
| Air temperature                | ºC    | Sensirion SHT-31      |
| Relative Humidity              | % REL | Sensirion SHT-31      |
| Noise level                    | dBA   | Invensense ICS-434342 |
| Ambient light                  | Lux   | Rohm BH1721FVC        |
| Barometric pressure            | Pa    | NXP MPL3115A26        |
| Equivalent Carbon Dioxide      | ppm   | AMS CCS811            |
| Volatile Organic Compounds     | ppb   | AMS CCS811            |
| Particulate Matter PM 1 / 2.5 / 10 | µg/m3 | Planttower PMS 5003              |

!!! info "Sensor performance"
    Make sure you visit the [sensor performance page](/Components/sensors/performance/) for further information about the sensors.

## :notebook: Installation instructions

The sensor comes mounted and almost ready to be used:

![](https://live.staticflickr.com/65535/47950999751_13e6e00f49_b.jpg)

The first step is to connect the battery. The kit will light in red (configuration mode) and we will be able to configure it by following the instructions at [start.smartcitizen.me](https://start.smartcitizen.me).

![](https://i.imgur.com/NhSNXJ8.png)

After the configuration process, data will be available on the SmartCitizen platform. You can explore the data there or download it using the `CSV Download` option (guide [here](/Guides/getting started/Downloading the Data/))

![](https://i.imgur.com/5NlWx6O.jpg)

## :battery: Power management

### Battery duration

The SCK comes with a 2000mAh LiPo battery. The battery is meant to be a complete power option for short-term measurements and a backup solution when the kit it is used for long periods. For long exposures, we recommend to permanently connect the USB to kit. The battery duration is dependent on which sensors are enabled or disabled.

You will note that the kit _turns itself off_ while operating on battery. Actually, this is what we call `sleep-mode`, an operation mode implemented to reduce consumption while on battery operation.

!!! info "PM Sensor management"
    If you want to save battery, the [basic interval](/Guides/getting started/Using the Shell/#set-recording-and-publication-intervals) for the sensors shouldn't be below 30s. This is due to the minimum stabilisation time the PM sensor requires to take stable readings. For this reason, **the minimum interval available without turning off the PM sensor between readings is 30s**. If a lower interval is required, the PM sensor will be permanently ON and battery will drain faster.

#### Battery calculator

You can use the battery calculator to estimate how much your battery would last.

!!! tip "SCK Battery Calculator"

    **WIP!**

    <iframe id="github-iframe" src="" width="100%" height="40%" frameborder="0" scrolling="no" style="min-height: 570px;"></iframe>

!!! info "What's the SCK's Shell?"
        Learn how to use the powerful SCK Shell. Check the [guide](/Guides/getting%20started/Using%20the%20Shell/).
    

<script>
    fetch('https://api.github.com/repos/fablabbcn/smartcitizen-tools/contents/calculator.htm')
        .then(function(response) {
            return response.json();
        }).then(function(data) {
            var iframe = document.getElementById('github-iframe');
            iframe.src = 'data:text/html;base64,' + encodeURIComponent(data['content']);
        });
</script>

### Battery charging

The SCK has a micro USB port and can be charged like any smartphone or tablet using a dedicated adapter or a computer USB port.

We recommend using an external USB power adaptor, instead of a computer USB port, for quicker charging. Autonomy can be extended by using a Power Bank, or a [5V PV Panel](/Components/Solar Panel/).

### Power Supply

The SCK needs 5V input via the micro USB connector. A normal 5V power charger can be used, although for outdoor developments we recommend using a waterproof power supply. Find more info in the [power supply section](/Components/boards/Power Supply/).

### User feedback

The LED serves as an indication of the battery status. If the LED is flashing orange <span class="led small orange"> </span> it indicates that the battery must be charged. The battery takes about 4 hours to fully charge. When the battery is fully charged, the LED will change from orange to green <span class="led small green"> </span>.

![](https://i.imgur.com/ABSXX4w.jpg){: style="max-width:400px !important"}

_Remember that in addition to these colors you will have the state color of the kit: configuration, network and sd._

!!! info "More details"
    Find more details under the [data board section](/Components/boards/Data Board/#power-management)

## :triangular_flag_on_post: User interfaces

The data board features a set of user interfaces which provide feedback to the user, as well as two buttons with different functionalities. The main RGB LED provides general feedback of the data board status. Additionally, two buttons are provided for user action. A hardware reset button, which forces a power cut to the board, and a power button, used to change the device's mode, turn on and off the device, and to perform a factory reset. You can see both buttons below:

![](https://i.imgur.com/AmlA8e2.png)

### The button

The main button interaction is detailed below:

| Function          | Button action     |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ON**            | Push the button   |
| **OFF**           | Push the button for 5 seconds |
| **CHANGE MODE**   | Push the button multiple times to choose: *Setup* <span class="led small red"></span>  *Wi-Fi* <span class="led small blue"></span> *Pink* <span class="led small pink"></span> |
| **FACTORY RESET** | Push the button 15 seconds for a full reset |

An example is shown below:

![](https://live.staticflickr.com/65535/48439505516_d210ce2c8a_h.jpg)

!!! info "Troubleshooting"
    Have a look at the [troubleshoothing section](/Troubleshooting) to check how you can use the buttons in case of problems with your SCK!

### Operation modes

!!! warning "New WARNING feature"
    After release `0.9.8`, a new warning feature was introduced. In an overall sense, this is the interpretation of each state:

    - **Normal**: no problem! **Slow fading in the LED.**
    - **Warning**: can take readings, but can't save them in the sdcard or can't send them to the platform (problem with network). Data is stored in the onboard Flash memory and will be saved after the problem is solved - either network comes back or the sdcard is OK. **Partial blink in LED.**
    - **Error**: can't take readings. Either there is "no time", or there is a big problem that prevents data to be read. **Full fast blink in LED.**

#### <span class="led small red"> </span> Setup mode

In this mode, the Kit is ready to be configured in **network** mode or **SD card** in [start.smartcitizen.me](https://start.smartcitizen.me/).

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led setup"></span>            | :thumbsup: Ready to be setup
| <span class="led setup-lowbat"></span>     | :battery: Ready to be setup but battery is low, charge the Kit    |
| <span class="led setup-chargebat"></span>  | :battery: Ready to be setup, battery charging            |
| <span class="led setup-fullbat"></span>    | :battery: Ready to be setup, battery charged                |

#### <span class="led small blue"> </span> Wi-Fi mode

This is the standard mode for a network that requires a Wi-Fi connection. In this way, the device will publish the data every minute on the [smartcitizen.me](https://smartcitizen.me) platform. If there is an inserted micro SD card, the data will be stored in it as well.

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led net"></span>            | :thumbsup: Collecting data online                 |
| <span class="led net-warning"></span>    | :warning: Warning. Collecting data but not sending it online         |
| <span class="led net-error"></span>      | ❌ Error. Not collecting data         |
| <span class="led net-lowbat"></span>     | :battery: Collecting data online but battery is low, charge the Kit    |
| <span class="led net-chargebat"></span>  | :battery: Collecting data online, battery charging              |
| <span class="led net-fullbat"></span>    | :battery: Collecting data online, battery charged               |


!!! warning
	:white_check_mark: The kit supports Wi-Fi WEP, WPA/WPA2 and open networks that are common networks in domestic environments and small businesses.

	:negative_squared_cross_mark: But, it **does not** support WPA/WPA2 Enterprise networks such as EDUROAM or networks with captive portals such as those found in Airports and Hotels

!!! info "Error in network mode"
    If you configure the SCK with a network that is not visible at the moment of configuring it, it will raise an error and it will not take data.

##### Flash memory

After firmware version `0.9.8`, a new flash memory feature was implemented. This changed completely the arrangement of sensor readings vs publication/storage, and how errors are handled. Data is now always stored in flash memory before storage in sdcard or network publication. This means, that data can be always recovered if there is a problem with the sdcard or the connection to the network, i.e. if we lose connection, the SCK will still store data and publish it in batch once the network is back!

!!! info "Flash chip and sizes"
    The flash chip [**S25FL064L**](https://www.cypress.com/file/316661/download) that we use it's a 8MB SPI flash nonvolatile memory. The minimum erasable unit is a 4kb sector, the full memory contains 2,048 sectors with a total of 8,388,608 bytes or 8MB.

    A normal reading group with the default urban board hardware installed is composed by 11 readings, hence we expect each reading to take 7 bytes: an average of 5 bytes for the reading itself plus 2 overhead bytes for SensorType and size. Each group should have a total of 77 bytes of readings, 2 byte of size, 2 bytes of flags and 4 bytes of the time stamp. That means we can expect a normal group to be around 85 bytes. This means we can store almost 100,000 groups of readings or around 70 days of readings with standard sensor hardware. This number can vary a little though.

    About flash memory lifespan, rounding numbers we can say we have enough space to store 2 months (60 days) of readings, according to the Flash memory [datasheet](https://www.cypress.com/file/316661/download) we have at least 100,000 erase cycles: 2 months per cycle means 200,000 months so we can expect more than **16k years!!**.

This can be very useful in many situations, for instance, where we cannot use permament network connectivity or we have intermitent network brownouts. Of course, everything has it's limitations, and the flash memory follows a _[circular buffer](https://en.wikipedia.org/wiki/Circular_buffer)_, that means that when the flash memory is full, it will start overwritting data no matter if it was published or not. In a normal SCK the flash memory will last for some weeks though, but it's better to always be on the safe side and not lose any data.

When the SCK loses connection, after **three attempts to connect**, it will enter _warning mode_ (see [here](/Smart Citizen Kit/#operation-modes)). After this, it will try again after 5 times the publication interval (by default 3'), which means, after WiFi being visible, by default, the **SCK will take at maximum 15' to connect to it** and start pushing data. The data publication is not inmediate and will take some minutes. If you are in a hurry, click the user button twice (net-setup-net mode) or reset the kit and data will start being posted right away.

!!! warning "Be careful"
    That we have a non permanent WiFi connection, means that we can also risk entering in error mode if the SCK depletes it's battery. Since the only way for the to know the time is to get it from the internet (or we give it to it from the phone in the setup process), if we lose network connection and the SCK runs out of battery, when coming back to life, it will need to receive the time again.

!!! info "Debugging commands"
    Check [this guide](/Guides/getting started/Using the Shell/#accessing-the-flash-memory) for more debugging commands.

#### <span class="led small pink"> </span> SD card mode (offline)

If we do not have an internet connection we can use the SD mode. In this case the device will record the data on the micro SD card. Later we can read the card using a card reader. The data can be visually spaced in a spreadsheet but also published on the [smartcitizen.me](https://smartcitizen.me) platform using the **UPLOAD CSV** option.

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led sd"></span>             | :thumbsup: Collecting data offline              |
| <span class="led sd-warning"></span>    | :warning: Warning. Collecting data but not storing it in sdcard       |
| <span class="led sd-error"></span>       |  ❌ Error. Not collecting data         |
| <span class="led sd-lowbat"></span>      | :battery: Collecting data offline but battery is low, charge the Kit    |
| <span class="led sd-chargebat"></span>   | :battery: Collecting data offline,  battery charging              |
| <span class="led sd-fullbat"></span>     | :battery: Collecting data offline, battery charged          |

!!! warning "Guide"
    Check the guide on how to upload the sd card data [here](/Guides/getting started/Uploading SD Card Data/)

!!! info "Weird files?"
    The files in the sdcard have the following naming: YYYY-MM-DD.CSV, however, you will find in the some extra files (.01, .02...) These are data files that the sensor creates once there is a reset and, to avoid corruption, it creates a new file in the sd-card, by changing the file-extension. 

    A reset takes place every night at 3-4am with the purpose to avoid data loss because a problem. The SCK then stores the data in a file with a sequential name, and does so by changing the filename to YYYY-MM-DD.01, .02… etc depending on the amount of resets it sees during that day. You can see the data and work with it by changing the name from YYYY-MM-DD.01 to YYYY-MM-DD_01.CSV. [Check the guide on how to organise your data](/Guides/data/Organise your data/#pre-process-the-sd-card-data) to automatise this.

#### Especial status

You will see these colors in special moments, mostly when the kit is booting or being updated.

| LED color                            |  Kit status                             |
|------------------------------------------|------------------------------------------- |
| <span class="led busy"></span>           |  :hourglass_flowing_sand:  Busy, please wait!                 |
| <span class="led firmware"></span>       | :wrench: Software update going on!                 |
| <span class="led yellow"></span>          | :computer: Shell mode [more info here](/Guides/getting started/Using the Shell/#shell-mode)                |

## Software Updates

Sofware updates are release frequently in the [Firmware repository](https://github.com/fablabbcn/smartcitizen-kit-21). These updates will need to be applied periodically to the two main components of the SCK: the SAMD21 (main processor) and the ESP8266 (Wi-Fi module). Check the instructions under the [Update the Firmware](/Guides/firmware/Update the firmware/) section for more information.

<img src="https://live.staticflickr.com/65535/50976345583_1099828518_k.jpg" width="2000" height="1333" alt="Smart Citizen Kits being tested at Fab Lab Barcelona">

!!! info "Test plan"
    You can find the Test plan, in case you are producing the SCK [here](/assets/notes/SCK_2.1_TESTPLAN.pdf).