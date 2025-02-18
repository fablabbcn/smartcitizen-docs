# Frequently asked questions

![Making Sense Toolkit Operation manuals](/assets/images/toolkit-operation-manuals.jpg)

## Can the sensors be placed outdoors?

Yes. The sensor is designed for both indoors and outdoors use. But if you’re planning to use it outdoors, you will have to consider purchasing or making a rainproof enclosure.

## Can I make my own rainproof enclosure?
Of course! The manufacturing files for the 3D printed enclosure will be available to download in the [Enclosures repository]({{ extra.urls.enclosures.link }}). Throughout the history of the Smart Citizen project, we’ve seen many inventive solutions for placing the sensor outdoors.

## Can I charge the sensors with a solar panel?
Sure! But note that the sensor requires a 5V solar panel to work properly. More information [here](/hardware/addons/solar-panel/).

## Can I add external sensors to the system?
Yes. The sensor has an independently configurable auxiliary bus at 3.3V with a SEEED Grove connector. The Bus has native support for I2C, but it can also be setup on firmware as a GPIO or UART. It can supply power up to 750mA, and it can be enabled or disabled by software. More info [here](/hardware/boards/data-board/#auxiliary-connector).

## What happens if there is a loss of network connectivity?

If the sensor is working in network mode and at any time the network is not available, it will store the data on its internal memory and publish all the collected data as soon as the network is available again.

## Which external sensors can be added?
Quite a few! Check [here](/knowledge).

## Will I be able to access the collected data?
Of course! The data collected by your sensor is available for anyone on the [Smart Citizen Platform]({{ extra.urls.platform.link }}), and you can download it at any time as a CSV file. Besides, you can also use the API to built custom applications to interact with your device. If you are familiar with python, check also [scdata](https://pypi.org/project/scdata/)

## How does the kit record the data?

The sensor can work in network and SD card modes. In network mode, the sensor publish data to the SC platform over Wi-Fi (every minute by default, but configurable). In SD card mode, all the collected data is stored locally in CSV format, and it can be later uploaded manually to the platform using the "Manual Data Upload" option.

## What networks does it support?

The SCK supports Wi-Fi WEP, WPA/WPA2 and open networks that are common networks in domestic environments and small businesses. However, like many other embedded devices such as Apple TV® or Chromecast®, it **does not** support networks with captive portals such as those found in Airports and Hotels. Currently, it also **does not** WPA/WPA2 Enterprise networks such as EDUROAM. However, the viability to support those in the future is under analysis.

In addition, the WiFi antenna is based on the low-cost ESP8266 chip, which supports **802.11b/g/n networks.**

## I have a firewall. What do I need to know?

Here are the ports and protocols used by the Kit to communicate with the platform:

| Service | Function  | Protocol | Port   | Address                                              |
| ------- | --------- | -------- | ------ | ---------------------------------------------------- |
| MQTT    | Send Data | TCP      | 1883 (80 legacy firmware)   | mqtt.smartcitizen.me |
| NTP     | Sync Time | UDP      | 80     | ntp.smartcitizen.me  |

_Notice we use custom ports already to avoid some firewall restrictions_

## Is there a mobile phone app that lets me view the data?

Currently there is an android app available, but we are working to make the website fully mobile device friendly, so that no mobile phone app is required. We would rather focus the time of our small team on the kits themselves instead of maintaining apps. So our final aim is to be app free, but fully mobile friendly.

## How accurate are the measurements?

Weather, noise, light and PM sensor measurements have been calibrated and validated against reference sensors through both in-house and external validations and they provide accurate data. Make sure you check the [performance section](https://docs.smartcitizen.me/Components/sensors/performance/) for more information.

<!-- ## Will the global platform be maintained after the project finishes release?
Yes, it will be maintained just as it has been for the past five years. Also, the platform is fully open source so the community can take over the maintenance if at some point the Smart Citizen core team can no longer run it. -->

## Are there any notable case studies using similar sensors?

Yes! Check all of them [here](https://docs.smartcitizen.me/Use%20cases/). A particularly interesting case study is the Making Sense project at Plaça del Sol in Barcelona, where a group of 15 technology enthusiasts and environmentalists joined a community of neighbours from a middle-class district that has been suffering from noise issues due to the nightlife in the square. You can find more information about this case study at: www.making-sense.eu

## What happens if I want to move the device or give it to someone else?

Just by pressing the button you can fully reset your sensor and configure it again using your account or a new one. All your previous data will remain available on the platform as it was before the reset.

## What about using other wireless technologies?

We are working closely with Barcelona’s The Things Network community to develop a TTN enabled sensor. A LoRA prototype has been tested, but we don’t have dates for the final version yet. BLE, Zigbee, or others are not currently supported, and except for G5, we are not planning to implement them unless there is a custom hardware integration demand.

## Can I remove my data from the platform?

Of course. You are the owner of the data that you collect, and you can download and/or delete all your sensor data at any time.

## How can I retrieve the MAC address from my device?

You can retrieve the MAC address with two methods: either you can use your phone (see below), or follow [this guide](/guides/getting-started/using-the-shell) if you want to try out the console interface in the kit.

**Using your phone**

1. Set the SCK in _setup mode_ (press the button once, the LED should turn red).
2. With your phone, join the Wi-Fi network created by your Kit; it should be SmartCitizen[…].
3. Once you are on your Kit configuration page, go to the Info section. You will see a page with all the information about your Kit.
4. Your MAC address is listed as seen below:

![](/assets/images/mobile-phone-setup.jpeg)

## What batteries are shipped with the kits?

The default SCK 2.1 Kits come with a 2000mAh LiPo battery model PL804050 (see [datasheet](/assets/datasheets/batteries/PL804050_2000mAh/PL804050_2000mAh_Datasheet.pdf) and [material safety data sheets](/assets/datasheets/batteries/PL804050_2000mAh/PL804050_2000mAh_Safety_Datasheet.pdf)).

For custom projects we also offer a bigger 6000mAh LiPo battery model DTP605068 (see [datasheet](/assets/datasheets/batteries/DTP605068_6000mAh/DTP605068_6000mAh_Datasheet.pdf) and [material safety data sheets](/assets/datasheets/batteries/DTP605068_6000mAh/DTP605068_6000mAh_Safety_Datasheet.pdf)).

The connector is [JST-PHR-2](https://www.digikey.com/en/products/detail/jst-sales-america-inc/PHR-2/608607). When looking at the data board from the top (white side), the positive of the battery (red) should be on the left.

We are working on a new dynamic battery calculator. Currently, you can find some approximate data [here](/hardware/kit/features/#battery-duration) for the SCK 2.1.

## Are the electronics waterproof?

No. They cannot be exposed to water, high humidity, corrosive environments, or moisture. Always use an enclosure when exposed outdoors. Highly humid environments can provoke corrosion in the sensors (symptom of this is blue powder near the sensors in the urban board). To help protect them, we recommend using _transparent nail polish_ in these areas. **Do not obscure the areas in red**:

![](/assets/images/nail_polish_areas.png)

If you are using any enclosure from [the repository]({{ extra.urls.enclosures.link }}), we also recommend using a filtration foam (PPI-20/10) like [this one](http://www.infiltro.es/index.php/filtro-de-aire-2/prefiltros/item/foam). More info [here](https://forum.smartcitizen.me/t/rain-tests-for-the-sck/1300).

## Can I send data to a different platform?

Yes. There are various ways in which you can do this.

You can either configure your SCK to send data directly to your own [MQTT](https://mqtt.org/) broker via the [Shell](/guides/getting-started/using-the-shell/). Follow this [guide](/guides/data/sending-data-to-other-platforms/) for more details on the payloads.

Otherwise, you can forward incoming data via the Smart Citizen Platform. See details on [data forwarding](/data/data-platform/#data-fowarding) on the [data platform](/data/data-platform) page, or visit the [developer documentation]({{extra.urls.developer.link}}) for more details on our API.

## How can I get a kit?

This is an easy one! Kits are available for purchase at :gift: **[{{ extra.urls.buy.name }}]({{ extra.urls.buy.link }})**.

If you are involved in a research project, an educational initiative, or developing a specialized monitoring system we can support and offer customized solutions. Contact us via **[{{ extra.urls.info.name }}]({{ extra.urls.info.link }})** to discuss your exact needs.

## Are there enclosures included?

The Smart Citizen Kit doesn’t come with an enclosure, but there are plenty of freely available designs on our **[enclosures repository]({{ extra.urls.enclosures.link }})**!. We have a wide range of open source designs that you can 3D print and build yourself, saving some industrial plastic manufacturing in the process. If you don’t have a 3D printer, you can always [find a Fab Lab near you](https://fablabs.io/labs/map) and once the enclosure’s life is done, you can repurpose it to make more 3D printing filament!

## I want to contribute, what can I do?

We would love you to contribute! Is modeling your thing? Take a look at our [enclosure repository]({{ extra.urls.enclosures.link }}) and try your hand at designing or tweaking an enclosure. Are you into tech specs? Help us add information to the documentation! Do you like coding? Take a look at our open source repositories and contribute to the source code of the [firmware]({{extra.urls.firmware.link}}) or the [data platform]({{extra.urls.ghapi.link}})!
If you are using any enclosure from [the repository](https://github.com/fablabbcn/smartcitizen-enclosures/), we also recommend using a filtration foam (PPI-20/10) like [this one](http://www.infiltro.es/index.php/filtro-de-aire-2/prefiltros/item/foam). More info [here](https://forum.smartcitizen.me/t/rain-tests-for-the-sck/1300)

## What is `reset cause`?

The kit is able to store the last reason by which it _restarted_. This information can be very helpful to know in order to _debug_ problems with a faulty kit.

| Code | Explanation | Comment |
|:-:   |:-           | :-      |
| `POR`    | Power On Reset                 | This reset takes place when you connect the USB cable to the Kit. |
| `BOD12` and `BOD33` | Brown Out `12` and `33` Detector Reset    | This reset takes place when there is a low voltage on the supply (more in the SAMD21 [docs](https://microchipdeveloper.com/32arm:samd21-pm-overview)) |
| `EXT`    | External Reset                 | This reset takes place when you press the _reset_ button |
| `WDT`    | Watchdog Reset                 | This reset takes place when the _watchdog timer_ from the SAMD21 _orders it_. Currently not suported |
| `SYST`   | System Reset Request           | This reset takes place when the Kit _orders_ it (sanity reset), or when you type `reset` in the [shell](/guides/getting-started/using-the-shell/) |

## What can I do in unstable Wi-Fi environments?

Unstable Wi-Fi environments are problematic if there are [low RSSI values](#what-are-good-rssi-values). Not only data can get to the platform in unconsistent frequency, but can cause the SCK to malfunction in some cases. Although we try to make the SCK as robust as possible, sometimes it helps to use some _special configuration_. This configuration will **increase energy consumption**, so it's not recommended for battery use.

You can use the [Shell](/guides/getting-started/using-the-shell/) and change the configuration with the commands below:

```
config -pubint 60
power -sleep 0
offline -retryint 60
```

## What are good RSSI values?

Starting from firmware version `0.9.9`, the kit also keeps track of the Wi-Fi signal strength (RSSI in dBm - decibel miliWatts) to help you get a grasp of the signal strength **seen by the kit** (this relativeness is important, as many other devices will see a stronger signal potentially thanks to a better antenna). Based on [this reference](https://techmusa.com/wireless-dbm-table/) here you have some indicators of how good or bad the value you see is:

* `-30 to -50dBm`: Excellent single strength (Next to Router).
* `-50 to -67dBm`: At Good signal strength for Web browsing, voice/video calls.
* `-67 to -70dBm`: Best effort for Web browsing for reliable packet delivery.
* `-70 to -80dBm`: Experience bad connectivity, Packet delivery may be unreliable.
* `-90 to 100dBm`: Worst single strength.

We recommend to stay between the `-30 to -70dBm` range if possible. Remeber that this value must be _seen_ by the Kit!
