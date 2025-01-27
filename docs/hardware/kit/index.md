---
card: true
type: unit
custom_color: orange
name: Smart Citizen Kit
short_name: SCK
feature_img: https://live.staticflickr.com/65535/54183550083_58f8204c78_k.jpg
excerpt: The Smart Citizen Kit is an open hardware solution for environmental monitoring designed to be used by anyone.
---

# {{ name }}

![]({{ feature_img }})

!!! tip "Quick links"

    :gift: **Buy: [{{ extra.urls.buy.name }}]({{ extra.urls.buy.link }})**

	:rocket: **Installation: [{{ extra.urls.installation.name }}]({{ extra.urls.installation.link }})**

	:earth_africa: **Platform: [{{ extra.urls.platform.name }}]({{ extra.urls.platform.link }})**

    :computer: **API: [{{ extra.urls.api.name }}]({{ extra.urls.api.link }})**

    :speech_balloon: **Discuss: [{{ extra.urls.forum.name }}]({{ extra.urls.forum.link }})**

	:question: **Support: [{{ extra.urls.support.name }}]({{ extra.urls.support.link }})**

    :sparkles: **Something big?: [{{ extra.urls.info.name }}]({{ extra.urls.info.link }})**

    :rotating_light: **Platform status: [{{ extra.urls.status.name }}]({{ extra.urls.status.link }})**

    :umbrella: **Enclosures: [{{ extra.urls.enclosures.name }}]({{ extra.urls.enclosures.link }})**

## What is the {{ name }}?

The {{ name }} (_{{ short_name}}_ for short, also just _the Kit_) is an open hardware solution for **environmental monitoring** designed to be used by **anyone** (you name it: _citizen scientists_,  _educators_, _researchers_...). It can take [measurements](#measurements) of many variables, such as particulate matter, noise, light and temperature, among many other things. The latest version is the {{ short_name }}2.3 (below you can see other [versions](#versions) too).

<img src="https://live.staticflickr.com/65535/54162814232_2eae94de74_k.jpg" alt="SCK2.3"/>

!!!tip "More on the use cases"
    If you want to learn more about how to use it, visit our [resources](/resources/) page.

The SCK is designed in a **modular** way, with a central _data logger_ (the [Data Board](/hardware/boards/data-board/)) with Wi-Fi connectivity, a micro SD-card slot, micro USB and a battery connectors. Various sensors can be connected, either via the [Urban Boards](/hardware/boards/urban-board/), featuring different onboard sensors and a particulate matter sensor connector, or through the [Auxiliary port](/hardware/kit/features/#auxiliary-connector).

![SCK 2.1 Outdoors](/assets/images/sck21-outdoor.jpg)

The {{ short_name }} can send the data to the [Smart Citizen Platform](/data/data-platform/), which offers a [web interface](/data/data-platform/#front-end-applications) to vizualise data, and an [open API](/data/data-platform/#api) that can be interfaced with [many other tools](/data/data-tools/).

The {{ short_name}} is designed to be **flexible**, and many custom configurations are possible by adding a [wide variety of third party sensors](/knowledge/). This can be the starting point for more complex setups, monitoring [air](/knowledge/air/), [soil or water](/knowledge/soil-water/) parameters. Any _custom_ configuration based on the {{ short_name }} also connects to the Smart Citizen Platform with all features freely available. Some more complex configurations are what we call the [Smart Citizen Stations](/hardware/stations/).

!!! tip "Want to contribute?"
    The whole project is open source, and it makes us **very** happy when we see contributions to it! Feel free to check, copy and modify the firmware/hardware [repository]({{ extra.urls.firmware.link}}), or [any other]({{ extra.urls.ghfablab.link }})!

## :hash: Versions

Most of the documentation applies to the **{{ short_name }} 2.1, the 2.2 and the 2.3 versions**.

=== "{{ short_name }} 2.3"
    <img src="https://live.staticflickr.com/65535/54162814232_2eae94de74_k.jpg" alt="{{ short_name }}2.3"/>
=== "{{ short_name }} 2.2"
    TODO
=== "{{ short_name }} 2.1"
    <img src="https://live.staticflickr.com/65535/47950912168_931d0b0e5a_k.jpg" alt="{{ short_name }} 2.1 All parts"/>

!!! info "Differences"
    A summary of the **differences**:

    - **Data Board**: 2.1, 2.2 and 2.3 are mostly the same, only some tweaks on the silkscreen and passive components have changed.
    - **Urban Board**: 2.1, 2.2 and 2.3 have many differences: from version 2.1 to 2.2 the PM sensor was changed, so has the pressure sensor. We have added a UV Sensor, and removed the tVOC/eCO2 sensor, as it was discontinued by the manufacturer (AMS). The rest stays the same (noise, light, temperature and humidity). The 2.3 version features a small hole to be able to reset the Data board from outside the box, and changes the pressure sensor again, back to the one we had in the {{ short_name }} 2.1.

!!! info "A note about versions and compatibility"
    All the {{ short_name }}2.X generations above 2.1 (included) are fully compatible in terms of firmware, and their respective [Urban Boards](/hardware/boards/urban-board/) are fully compatible with any [Data Board](/hardware/boards/data-board/) of the _2.X series_ (above 2.1).

## :ear: Measurements

All the {{ short_name }}2.X generations above 2.1 (included) measure **at least** air temperature, relative humidity, noise level, ambient light, barometric pressure and particulate matter (PM).

!!! info "Sensor performance"
    Make sure you visit the [sensor knowledge page](/knowledge/) for more information!

=== "{{ short_name }} 2.1"
    | Measurement                               | Units | Sensor                    |
    |:-                                         |:-:    |:-:                        |
    | Air temperature                           | ºC    | Sensirion SHT-31          |
    | Relative Humidity                         | % REL | Sensirion SHT-31          |
    | Noise level                               | dBA   | Invensense ICS-434342     |
    | Ambient light                             | lux   | Rohm BH1721FVC            |
    | Barometric pressure                       | kPa   | NXP MPL3115A26            |
    | Equivalent Carbon Dioxide                 | ppm   | AMS CCS811                |
    | Volatile Organic Compounds                | ppb   | AMS CCS811                |
    | Particulate Matter PM1, PM2.5, PM10       | µg/m3 | Plantower PMS 5003        |
=== "{{ short_name }} 2.2"
    | Measurement                               | Units | Sensor                    |
    |:-                                         |:-:    |:-:                        |
    | Air temperature                           | ºC    | Sensirion SHT-31          |
    | Relative Humidity                         | % REL | Sensirion SHT-31          |
    | Noise level                               | dBA   | Invensense ICS-434342     |
    | Ambient light                             | lux   | Rohm BH1721FVC            |
    | Barometric pressure                       | kPa   | ST LPS33K                 |
    | UV-A, B, C                                | uW/cm2| AMS AS7311                |
    | Particulate Matter PM1, PM2.5, PM4, PM10  | µg/m3 | Sensirion SEN5X           |
    | NOx Index, VOx Index (Optional)           | -     | Sensirion SEN54, 55       |
=== "{{ short_name }} 2.3"
    | Measurement                               | Units | Sensor                    |
    |:-                                         |:-:    |:-:                        |
    | Air temperature                           | ºC    | Sensirion SHT-31          |
    | Relative Humidity                         | % REL | Sensirion SHT-31          |
    | Noise level                               | dBA   | Invensense ICS-434342     |
    | Ambient light                             | lux   | Rohm BH1721FVC            |
    | Barometric pressure                       | kPa   | NXP MPL3115A26S           |
    | UV-A, B, C                                | uW/cm2| AMS AS7311                |
    | Particulate Matter PM1, PM2.5, PM4, PM10  | µg/m3 | Sensirion SEN5X           |
    | NOx Index, VOx Index (Optional)           | -     | Sensirion SEN54, 55       |

!!! info "About the SEN5X"
    `SEN5X` refers to the different configurations of the PM sensors in that series: `SEN50`, `SEN54`, `SEN55`.

    We chose the SEN50 as it's a cheap, good solution to measure PM. The SEN55 and the SEN54 are also compatible with the same connector in {{ short_name }}2.2 or {{ short_name }}2.3! The SEN50 measures _only_ PM, the SEN54 PM and NOx index, and the SEN55 PM, NOx and VOC indexes.

## :notebook: Installation instructions

The {{ short_name }} comes almost ready to be used:

![{{ short_name }} Assembly](/assets/images/sck-assembly.jpg)

You can head over to the onboarding at [start.smartcitizen.me](https://start.smartcitizen.me) for all the setup instructions:

![Onboarding main](/assets/images/onboarding-main.png)

!!! info "Detailed guide"
    Have a look [at this guide](/Guides/getting-started/onboarding-sensors/) for a step-by-step installation.

If you selected the **Wi-Fi** option, data will be available on the [Smart Citizen Plafform]({{ extra.urls.platform.link }}). You can explore the data there or download it, either using the [CSV Download](/guides/getting-started/downloading-data/#direct-csv-download) option, or by using the [API](/guides/getting-started/downloading-data/#api). If you rather work **Offline**, data will be available on the [SD-card](/data/sd-card/) in CSV format.

![SC Platform components](/assets/images/platform-components.jpg)

!!!info "Internal memory"
    An additional mode, somewhat in between **online** and **offline** is possible with the [internal memory feature](/hardware/kit/features/#internal-memory).

## :umbrella: Enclosures

If you want to leave the {{ short_name }} outdoors you will need protect the electronics.

<img src="https://live.staticflickr.com/65535/54172280536_a67af99ddc_k.jpg" alt="Code Lab, kits in progress"/>

There are plenty of freely available designs on our [enclosures repository]({{ extra.urls.enclosures.link }}). We have a wide range of open source designs that you can 3D print and build yourself, saving some industrial plastic manufacturing in the process. If you don’t have a 3D printer, you can always find a [Fab Lab near you](https://fablabs.io/labs/map) and once the enclosure’s life is done, you can repurpose it to make more 3D printing filament!

!!! info "Want to contribute? Or buy one?"
    Visit the [Smart Citizen Enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures) to download, modify, or add your own! Also, make sure you read [this fantastic summary](https://hackaday.com/2023/03/27/a-survey-of-long-term-waterproofing-options/) on how to waterproof sensors.

    The enclosure is not available for purchases through _official_ channels, but for _large_ orders, we can provide it from [the Fab Lab Barcelona sales channel]({{ extra.urls.info.link }}).

## Deployment tips

!!! danger "SCK2.3 needs a battery"
    Due to the power needs of the SCK2.3 (and SCK2.2), it always needs a battery connected.

Some basic deployment tips below:

- Try to have the {{ short_name }} always powered if they are going to be installed on a fixed location.
- Avoid using the {{ short_name }} in places with high humidity or a lot of dust, or clean/check the device periodically otherwise.
- Avoid covering the sensors, specially the PM sensor.
- Deploy the {{ short_name }} facing downwards if outdoors, so that dust doesn't accumulate on the sensors.
- Avoid direct air flow towards the sensors. If exposed under flow conditions, have the flow go parallel to the sensors' surface.
- Avoid exhausts from air conditioning units, kitchens and others
- Protect the sensors from moisture either using filtering foam or nail polish to cover the sensor pads (see [here](/_FAQ/#are-the-electronics-waterproof))

