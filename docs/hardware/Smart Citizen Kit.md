<!-- TODO - Proofread -->

# Smart Citizen Kit

![Smart Citizen Kit 2.1 in Context](/assets/images/sck21-in-context.jpg)

!!! tip "Quick links"

    :gift: **Buy: [seeedstudio.com](https://www.seeedstudio.com/Smart-Citizen-Starter-Kit-p-2865.html)**

	:rocket: **Installation: [start.smartcitizen.me](https://start.smartcitizen.me/)**

	:earth_africa: **Platform: [smartcitizen.me](https://smartcitizen.me/kits)**

    :computer: **API: [api.smartcitizen.me](https://api.smartcitizen.me)**

    :speech_balloon: **Discuss: [forum.smartcitizen.me](https://forum.smartcitizen.me)**

	:question: **Support: [support@smartcitizen.me](mailto: support@smartcitizen.me)**

    :sparkles: **Something big?: [info@smartcitizen.me](mailto: info@smartcitizen.me)**

    :rotating_light: **Platform status: [uptimerobot.com](https://status.smartcitizen.me)**

## What is it?

The Smart Citizen Kit (_SCK_ for short, also just _the kit_) is an open hardware solution for **environmental monitoring** that can be used by **citizen scientists**,  **educators** and **researchers**. It is one of the most important parts of our project, and in it's most basic version collects various [metrics](#ear-measurements), such as particulate matter, noise, light and temperature.

!!!tip "More on the use cases"
    If you want to learn more about how to use it, visit our [Use Cases page](/Resources/Use Cases/).

<!-- TODO Add Use Cases Page -->

![SCK 2.1 All parts](/assets/images/sck21-components.jpg)

The system is designed in a **modular** way, with a central _data logger_ (the [Data Board](/Components/boards/Data Board)) with WiFi connectivity, a micro SD Card slot, a micro USB slot and a battery. Various components can be added to the **Data Board**, being the default the [Urban Board](/Components/boards/Urban Board), featuring different onboard sensors and a particulate matter sensor connector.

![SCK 2.1 Outdoors](/assets/images/sck21-outdoor.jpg)

The Smart Citizen Kit connects to non-hardware components such as a dedicated [Storage platform](/Data/), and a web interface for visualising the data. Any other configuration based on the Smart Citizen Kit core components also connects to such platform with all features freely available. On top of that, the Smart Citize Kit can also be a starting point for **more complex settings**, not only related with air quality monitoring. For that purpose, in addition to the [Urban Board](/Components/boards/Urban Board), the system also provides off-the-shelf support for a [wide variety of third party sensors](/hardware/sensors/), using the [Auxiliary Connector](Auxiliary Connector) for that purpose. One example is what we call the [Smart Citizen Stations](/Smart Citizen Stations).

!!! info "More on the supported sensors"
    Have a look a the supported sensors in our [knowledge section](/hardware/sensors/)!

!!! tip "Want to contribute?"
    The whole project is open source, and it makes us **very** happy when we see contributions to it! Feel free to check, copy and modify the firmware/hardware [repository](https://github.com/fablabbcn/smartcitizen-kit-21), or [any other](https://github.com/search?q=org%3Afablabbcn+smartcitizen&type=repositories)!

## :hash: Versions

<!-- TODO - Think how to show this part -->

Most of the documentation applies to the **Smart Citizen Kit 2.1 and the 2.2**.

![SCK 2.1 All parts](/assets/images/sck21-components.jpg)

<!-- TODO Add photo -->

![SCK 2.2 All parts](/assets/images/sck22-components.jpg)

A summary of the **differences**:

- **Data Board**: 2.1 and 2.2 are mostly the same. [Check here for details on the differences](/hardware/boards/Data Board/)
- **Urban Board**: 2.1 and 2.2 have many differences: the PM sensor has changed, so has the pressure sensor. We have added a UV Sensor, and removed the tVOC sensor, as it was discontinued. The rest stays the same (noise, light, temperature and humidity)

## :ear: Measurements

All the Smart Citizen Kit new sensors generation measure **at least** air temperature, relative humidity, noise level, ambient light, barometric pressure and particulate matter (PM).

!!! info "Sensor performance"
    Make sure you visit the [sensor knowledge page](/hardware/sensors/) for _a lot_ more information.

### SCK 2.1

![SCK 2.1 Measurements](/assets/images/sck21-measurements.png)

Here is the table summarising the measurements and the corresponding sensors:

| Measurement                           | Units | Sensor                |
|:-                                     |:-:    |:-:                    |
| Air temperature                       | ºC    | Sensirion SHT-31      |
| Relative Humidity                     | % REL | Sensirion SHT-31      |
| Noise level                           | dBA   | Invensense ICS-434342 |
| Ambient light                         | lux   | Rohm BH1721FVC        |
| Barometric pressure                   | kPa   | NXP MPL3115A26        |
| Equivalent Carbon Dioxide             | ppm   | AMS CCS811            |
| Volatile Organic Compounds            | ppb   | AMS CCS811            |
| Particulate Matter PM1, PM2.5, PM10   | µg/m3 | Plantower PMS 5003    |

### SCK 2.2

![SCK 2.2 Measurements](/assets/images/sck22-measurements.png)

Here is the table summarising the measurements and the corresponding sensors:

| Measurement                               | Units | Sensor                |
|:-                                         |:-:    |:-:                    |
| Air temperature                           | ºC    | Sensirion SHT-31      |
| Relative Humidity                         | % REL | Sensirion SHT-31      |
| Noise level                               | dBA   | Invensense ICS-434342 |
| Ambient light                             | lux   | Rohm BH1721FVC        |
| Barometric pressure                       | kPa   | ST LPS33K             |
| UV-A, B, C                                | uW/cm2| AMS AS7311            |
| Particulate Matter PM1, PM2.5, PM4, PM10  | µg/m3 | Sensirion SEN5X       |
| NOx Index, VOx Index                      | -     | Sensirion SEN5X       |

!!! info "About the SEN5X"
    `SEN5X` refers to the different configurations of the PM sensors in that series: `SEN50`, `SEN54`, `SEN55`.

    We chose the SEN55 for it's additional metrics, but the SEN50 and the SEN54 are also compatible! The SEN50 measures only PM, the SEN54 PM and NOx index, and the SEN55 PM, NOx and VOC indexes.

## :notebook: Installation instructions

The sensor comes almost ready to be used:

![SCK Assembly](/assets/images/sck-assembly.jpg)

You can head over to the onboarding at [start.smartcitizen.me](https://start.smartcitizen.me) for all the instructions:

![Onboarding main](/assets/images/onboarding-main.png)

!!! info "Detailed guide"
    Have a look [at this guide](/Guides/getting started/Onboarding Sensors/) for a step-by-step installation.

If you selected the WiFi option, once you are done, data will be available on the [Smart Citizen Plafform](https://smartcitizen.me/kits). You can explore the data there or download it using the [CSV Download](/Guides/getting started/Downloading the Data/) option, or by using the [API](https://api.smartcitizen.me).

![SC Platform components](/assets/images/platform-components.jpg)

## :battery: Power management

The Smart Citizen Kit features a micro USB slot and a LiPo Battery charger. The micro USB slot can be used with different power supplies: any USB compatible power supply with 2A will do. There is also a [custom-made outdoor power supply](/hardware/power/Power Supply/) and the possibility to use a [solar panel](/hardware/power/Solar Panel/). Check [the power supply section](#power-supply) for more information.

!!! info "Kit turning itself off?"
    You will note that the kit _turns itself off_. This is what we call `sleep-mode`, an operation mode implemented to reduce consumption. Check the [operation modes section](#operation-modes) below.

### Battery duration

The Smart Citizen Kit has off-the-shelf support for LiPo batteries. If you got the Starter Kit, you should have already a 2000mAh battery. The battery is meant to be a power option for short-term measurements (_roughly 2-3 days_) and a backup solution when the kit it is used for longer periods.

!!! info "Long term measurements?"
    In case you want to take long term measurements, we recommend to permanently power the kit via USB with a [power supply](#power-supply) or use a [solar panel](/hardware/power/Solar Panel/).

The battery duration is dependent on which sensors are enabled, and how frequent you take measurements and send data to the platform. All these options can be configured with [the shell](/Guides/getting started/Using the Shell/).

!!! info "Sensor and publication interval management"
    If you want to save battery, the [basic interval](/Guides/getting started/Using the Shell/#set-recording-and-publication-intervals) for the sensors shouldn't be below 30s. This is because the minimum stabilisation time the PM sensor requires to take stable readings is around 15-20s. For this reason, **the minimum interval available without turning off the PM sensor between readings is 30s**. If a lower interval is required, the PM sensor will be permanently `ON` and the battery won't last as long.

#### Battery calculator

You can use the battery calculator to estimate how much your battery would last.

!!! tip "SCK Battery Calculator"

    **WIP!**

    <iframe id="github-iframe" src="" width="100%" height="40%" frameborder="0" scrolling="no" style="min-height: 570px;"></iframe>

<script>
    fetch('https://api.github.com/repos/fablabbcn/smartcitizen-tools/contents/calculator.htm')
        .then(function(response) {
            return response.json();
        }).then(function(data) {
            var iframe = document.getElementById('github-iframe');
            iframe.src = 'data:text/html;base64,' + encodeURIComponent(data['content']);
        });
</script>

!!! info "What's the SCK's Shell?"
    Learn how to use the powerful SCK Shell. Check the [guide](/guides/getting%20started/Using%20the%20Shell/).

### Battery charging

The SCK has a micro USB port and can be charged like any smartphone or tablet using a dedicated adapter or a computer USB port.

We recommend using an external USB power adaptor, instead of a computer USB port, for quicker charging. You can also use a power bank, or a [5V PV Panel](/hardware/power/Solar Panel/).

### Power Supply

The SCK needs 5V input via the micro USB connector. A normal 5V power charger can be used, as long as it's USB compatible, and provides 2A. For outdoor developments we recommend using a waterproof [power supply](/hardware/power/Power Supply/). Optionally, you can use a [solar panel](/hardware/power/Solar Panel).

### Battery Status

The SCK will display _user_ feedback via a set of LEDs. To show the battery status, we use the `STATUS` LED. There are two more LEDs, one that shows if the WiFi antenna is ON, or if there is data being transmitted via USB.

![SCK LEDs](/assets/images/sck-leds.jpg){: style="max-width:400px !important"}

If the `STATUS` LED is _agressively_ flashing in orange <span class="led small orange"> </span> it indicates that the battery must be charged. The default 2000mAh battery **takes about 4 hours** to fully charge. If you have the USB charger connected, you will see that when the battery is charging, the LED will flash in orange <span class="led small orange"> </span>, and when it's fully charged, it will flash in green <span class="led small green"> </span>.

!!! tip "Other colors"
    Remember that in addition to these colors you will have the state color of the kit: _setup_, _online_ and _offline_ modes.

## :triangular_flag_on_post: User interfaces

The [Data board](/hardware/boards/Data Board/) features a set of LEDs that provide feedback to the user, as well as two buttons with different functionalities. The `STATUS` LED provides general feedback of the data board status, both on the [operation mode](#operation-modes) and on the [battery status](#battery-status). Additionally, two buttons are provided for user actio: a hardware `reset` button, which literally does a full reset on the board, and an `ON/OFF` button, used to change the device's mode, turn on and off the device, and to perform a _factory reset_. You can see both buttons below:

![SCK Buttons](/assets/images/sck-buttons.png){: style="max-width:500px !important"}

### The `ON/OFF` button

The main button interaction is detailed below:

| Function          | Button action                 |
|-                  |-                              |
| **ON**            | Push the button               |
| **OFF**           | Push the button for 5 seconds |
| **CHANGE MODE**   | Push the button multiple times to change mode between: *Setup* <span class="led small red"></span> *Wi-Fi mode (online)* <span class="led small blue"></span> or *SD Card mode (offline)* <span class="led small pink"></span> |
| **FACTORY RESET** | Push the button 15 seconds for a full reset |

!!! info "Changing mode"
    When you change the mode, you will switch between *Setup* mode, and whatever mode you have configured (online or offline).

    For instance, if you configured your kit in _online_ mode, clicking the `ON/OFF` button will switch you to _setup_ mode. Hitting it again will switch you back to _online_ mode.

You can see it in action below (remember, the SCK 2.1 and SCK 2.2 share the same data board!):

![SCK ON-OFF Button](/assets/images/sck-onoff-button.jpg)

!!! info "Troubleshooting"
    Have a look at the [troubleshoothing section](/Troubleshooting) to check how you can use the buttons in case of problems with your SCK!

### The `reset` button

This button is used for [_troubleshooting_](/Troubleshooting) your kit, or to [_upgrade_](/guides/firmware/Update the firmware/) the firmware. Unless you are in any of these situations, you shouldn't need it! In any case, it's handy and useful to know what it's for.

<!-- TODO - Make this image nicer? -->

![SCK Reset](/assets/images/sck-reset.png)

!!! info "Using the button inside a box"
    If you are using the kit inside a box, it may be tricky to access the `reset` button. Check the [enclosures page](/hardware/enclosures/) for more options.

## Operation modes

!!! warning "New `WARNING` mode"

    After firmware version `0.9.8`, a new `WARNING` mode was introduced. This feature gives feedback to the user in case something _not too bad_ happened, and the kit is able to still collect data, but not store it on the micro SD card or send it to the platform. This `WARNING` mode is a new addition to the already existing `NORMAL` and `ERROR` modes. For a more formal explanation of each mode:

    - `NORMAL`: no problem! **The `STATUS` LED is _slowly_ breathing**
    - `WARNING`: can take readings, but can't save them to the micro SD card (problem with SD card) or send them to the platform (problem with network). Data is stored in the onboard [Flash memory](#flash-memory) and will be stored on the SD card or sent to the platform after the problem is solved: either because the network comes back or the SD card is OK. **The `STATUS` LED is _partially blinking_**
    - `ERROR`: can't take readings. Either there is "no time", or there is a big problem that prevents data to be read. **The `STATUS` LED is _agressively blinking_**

    :bulb: Remember, you can check your SCK firmware version quickly following this [guide](/guides/getting%20started/Getting%20firmware%20information/).

The different operation modes are described below. The animations help to understand what _partially blinking_, _agressively blinking_ or _breathing_ means.

### <span class="led small red"> </span> Setup mode

In this mode, the kit is ready to be configured in [WiFi](#wi-fi-mode) or in [SD card](#sd-card-mode).

| LED color                                  | Kit status                                                          |
| :-:                                        | :-:                                                                  |
| <span class="led setup"></span>            | :thumbsup: Ready to be setup                                         |
| <span class="led setup-lowbat"></span>     | :battery: Ready to be setup but battery is low, charge the Kit       |
| <span class="led setup-chargebat"></span>  | :battery: Ready to be setup, battery charging                        |
| <span class="led setup-fullbat"></span>    | :battery: Ready to be setup, battery charged                         |

### <span class="led small blue"> </span> Wi-Fi mode

WiFi mode (or online), is the most common mode for the kit. In this mode, it will publish data to the [Smart Citizen Platform](https://smartcitizen.me/kits) (although you can [change this](/guides/getting started/Using the shell)). If there is micro SD card in the kit, data will be stored in it too.

| LED color                                | Kit status                                                              |
| :-:                                      | :-:                                                                     |
| <span class="led net"></span>            | :thumbsup: Collecting data online                                       |
| <span class="led net-warning"></span>    | :warning: Warning. Collecting data but not sending it online            |
| <span class="led net-error"></span>      | ❌ Error. Not collecting data                                            |
| <span class="led net-lowbat"></span>     | :battery: Collecting data online but battery is low, charge the Kit     |
| <span class="led net-chargebat"></span>  | :battery: Collecting data online, battery charging                      |
| <span class="led net-fullbat"></span>    | :battery: Collecting data online, battery charged                       |
| <span class="led net-sleep"></span>      | :bed: Sleep-mode. Collecting data online and saving battery             |

!!! warning
	:white_check_mark: The kit supports Wi-Fi WEP, WPA/WPA2 and open networks that are common networks in domestic environments and small businesses.

	:negative_squared_cross_mark: But, it **does not** support WPA/WPA2 Enterprise networks such as EDUROAM or networks with captive portals such as those found in Airports and Hotels

!!! danger "Error in network mode"
    If you configure the SCK with a network that is not visible (or working) at the moment of configuring it, it will raise an error and it will not take data.

### <span class="led small pink"> </span> SD card mode

SD Card mode (or offline), can be used if you do not have an internet connection available. In this case, the device will record the data on the micro SD card, in [CSV format](/data#csv-format). You can take a look at this data in a spreadsheet, or upload it to the [Smart Citizen Platform](https://smartcitizen.me/kits) by using the [CSV Upload](/guides/getting started/Uploading SD Card Data/) option, or via the [API](/data/Smart Citizen API#using-the-api).

| LED color                                 |  Kit status                                                           |
| :-:                                       | :-:                                                                   |
| <span class="led sd"></span>              | :thumbsup: Collecting data offline                                    |
| <span class="led sd-warning"></span>      | :warning: Warning. Collecting data but not storing it in sdcard       |
| <span class="led sd-error"></span>        |  ❌ Error. Not collecting data                                         |
| <span class="led sd-lowbat"></span>       | :battery: Collecting data offline but battery is low, charge the Kit  |
| <span class="led sd-chargebat"></span>    | :battery: Collecting data offline,  battery charging                  |
| <span class="led sd-fullbat"></span>      | :battery: Collecting data offline, battery charged                    |
| <span class="led sd-sleep"></span>        | :bed: Sleep-mode. Collecting data offline and saving battery          |


!!! info "Weird files?"
    The CSV files in the SD card have the following naming: YY-MM-DD.CSV. However, sometimes you may find some extra files:

    - **Before `0.9.9`** firmware version: the files are YY-MM-DD.01, YY-MM-DD.02...
    - **After `0.9.9`** firmware version: the files are YY-MM-DD_01.CSV, YY-MM-DD_02.CSV...

    These are data files that the sensor creates once there it _resets_ to avoid file corruption. It does so by creating a new file in the SD card. In _older_ firmware versions, it's normal to have some additional files, specially because of the [sanity reset](#sanity-reset). Note that **after `0.9.9` firmware version** you should only get one file per day, even with the _sanity reset_. If you have more than one, the kit had was reset.

### Special status

You will see these colors _only_ in special moments, most of the times when the kit is booting or is being updated.

| LED color                                 | Kit status                                                                                                 |
| :-:                                       | :-:                                                                                                        |
| <span class="led busy"></span>            | :hourglass_flowing_sand:  Busy, please wait!                                                               |
| <span class="led firmware"></span>        | :wrench: Software update going on!                                                                         |
| <span class="led yellow"></span>          | :computer: Shell mode [more info here](/Guides/getting started/Using the Shell/#shell-mode)                |

## Software Updates

Sofware updates are released in the [firmware repository](https://github.com/fablabbcn/smartcitizen-kit-21/releases). These updates will need to be applied periodically to the [two main microcontrollers of the Data Board](/hardware/boards/Data Board/#microcontrollers): the Atmel SAMD21 (main processor) and the Espressif ESP8266 (Wi-Fi module). Check the instructions in the [firmware upgrade](/Guides/firmware/Update the firmware/) guide for more information.

![Smart Citizen Kits being tested at Fab Lab Barcelona](/assets/images/sck-test.jpg)

## Special features

### Flash memory

After firmware version `0.9.8`, a new [flash memory](/firmware/Flash Storage/) feature was implemented. The flash memory changes completely the arrangement of sensor readings vs publication/storage, and how errors are handled. From there on, data is always stored in flash memory before stored in **SD card** or published over **Wi-Fi**. That means that data can be always recovered if there is a problem with the SD card or the connection to the Internet fails, i.e. if we have poor network connectivity, the SCK will still store data and publish it in batch once the network is back.

!!! tip "Check and update your Kit software version"
	:bulb: Remember, you can check your SCK firmware version quickly following this [guide](/Guides/getting%20started/Getting%20firmware%20information/). Later, learn [here](/Guides/firmware/Update%20the%20firmware/) how to update it.

That can be very useful in many situations, for instance, whenever we cannot use permanent network connection, or you are using the SCK while going around in the city. Of course, everything has its limitations: the flash memory follows a _[circular buffer](https://en.wikipedia.org/wiki/Circular_buffer)_, which means that, whenever the flash memory is full, it will start overwriting data, no matter if it was published or not. In a normal SCK, the flash memory will last for some weeks though, but it's better to always be on the safe side and not lose any data.

When the SCK doesn't have , after **three attempts to connect**, it will enter _warning mode_ (see [here](/Smart Citizen Kit/#operation-modes)). After this, it will try again after 5 times the publication interval (by default 3'), which means, after the Internet connection is back the **SCK will take a maximum of 15' to connect to it** and start pushing data. The data publication is not immediate and will take some minutes. If you are in a hurry, click the user button twice (blue-red-blue mode) or reset the kit and data will start being posted right away.

!!! warning "Be careful!"
    Having a non-permanent WiFi connection means that we can also risk entering error mode if the SCK runs out of battery because it obtains the time from the internet (or from a phone during the SD card setup process). **Losing the network connection and running out of battery means the device will lose the internal clock time, and the device will stop taking readings until it has power and can connect to the internet to sync, again.**

!!! info "Debugging commands"
    Check [this guide](/Guides/getting started/Using the Shell/#accessing-the-flash-memory) for more debugging commands.

### USB reset

### Sanity reset

The kit will reboot itself takes place every night at 2am CET. ith the purpose to avoid data loss because a problem. The SCK then stores the data in a file with a sequential name, and does so by changing the filename to YY-MM-DD.01, .02… etc depending on the amount of resets it sees during that day. You can see the data and work with it by changing the name from YY-MM-DD.01 to YY-MM-DD_01.CSV. [Check the guide on how to organise your data](/Guides/data/Organise your data/#pre-process-the-sd-card-data) to automatise this.

### Massive storage mode

