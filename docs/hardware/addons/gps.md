---
card: true
name: GPS
feature_img: https://live.staticflickr.com/65535/54183550083_58f8204c78_k.jpg
custom_color: blue
type:
    - addon
excerpt: You can connect a GPS to the SCK and collect geolocated data while you are moving!
---

# {{ name }}

![]({{ feature_img }})

{{ excerpt }}

!!! info "Supported hardware"
    Only some [GPS modules](#supported-modules) are supported. See the table below to see the metrics and the available modules.

## Data

As usual, data can be recorded offline or published online to the Smart Citizen Platform. If you use the sensor out of WiFi connectivity (i.e. moving), the sensors store data internally in the [Flash memory](//hardware/firmware/features/#flash-storage) during the trips and publish it in batch when the configured WiFi network is visible. Data is also stored in the SD card for later use in CSV file format.

![](/assets/images/bike_trip.jpg)

### Recording interval

Similarly to the general configuration, you can [change the recording interval](/guides/getting-started/using-the-shell/#set-recording-and-publication-intervals).

!!! info "GPS specific"
    **When a GPS is connected**, and movement is detected, the reading interval goes down to 5s.

### Data formats

Data from the GPS are timestamped in ISO8601 format with the following metrics:

| Metric                    | Units | Description                           |
|---------------------------|-----  |---------------------------------------|
| GPS_ALT                   | m     | GPS Altitude                          |
| GPS_DIL                   | n/a   | GPS Horizontal Dilution of Position   |
| GPS_FIX_QUALITY           | n/a   | GPS Fix Quality (0: bad, 3: great!)   |
| GPS_LAT                   | º     | GPS Latitude                          |
| GPS_LONG                  | º     | GPS Longitude                         |
| GPS_SAT_N                 | n/a   | GPS Number Tracked Satellites         |
| GPS_SPEED                 | m/s   | GPS Horizontal Speed                  |

!!! info "What is the GPS fix?"
    The GPS fix is the term used for describing whether or not the GPS has successfully received a valid location.

## Hardware

### Supported Modules

Here you have a list of supported GPSs:

- [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329)
- [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414)
- [SparkFun GPS SAM-M8Q](https://www.sparkfun.com/products/15210), only in a forked repository by [serialc](https://github.com/serialc/) [here](https://github.com/serialc/smartcitizen-kit-21). Read this post [here](https://forum.smartcitizen.me/t/power-off-qwiic-on-sck2-1-power-off/1623)
- [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html) (only via [PM Board](/Components/boards/PM Board/) as it uses UART to communicate)

!!! warning "Sparkfun QWIIC GPS"
    If you are using Sparkfun QWIIC GPS, note that you will need [an adaptor from GROVE to QWIIC](https://www.sparkfun.com/products/15109)

!!! info "Implement your own"
    Check the guide on [integrating other sensors](/guides/getting-started/third-party-sensors/), or [write on the forum]({{extra.urls.forum.link}}) to know how to implement sensors made by others.

### Antennas

Some modules support an external antenna via U.FL. connector. We recommend uing an external ceramic patch antenna for better gain (unless the module  already has one, like the XA1110):

![](/assets/images/ceramic_antenna.png){: style="width:400px"}

The U.FL antenna connector **shouldn't need to be unplugged** from the board, specially never when the board is being powered in order to avoid damaging the circuitry:

![](/assets/images/UFL.png){: style="width:400px"}

> Antenna images by [Sparkfun](https://www.sparkfun.com) (License [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)) and edited by Smart Citizen.

!!! info "Harsher environments?"
    In harser environments, a magnetic mounted waterproof antenna like [this one](https://eu.mouser.com/ProductDetail/Taoglas/AA171301111?qs=%2Fha2pyFaduhLT2djiVcQ%252BmKy6lTU1e7%2FjAvHSK%252B8w22J1i%252BNOh5WUg%3D%3D) is preferred.

## Known issues

Below, there is a list of known issues with the `0.9.8` version of the firmware.

1. Currently, the SCK does not report errors permanently and only during 10s. This is shown as a fast led blinking (<span class="led net-error"></span>).

2. Under certain conditions, the dynamic interval is not instantly recovered after a quick stop, and it might take 1' to restart

3. Under certain sky visibility conditions, the GPS does not report a valid fix. It is normally fixed with a clear sky view. For this, [follow the instructions below](#before-going-on-a-trip)

## Before going on a trip

Before going on a trip, make sure that:

1. The SCK has enough battery (you can check this with the [shell](/docs/guides/getting-started/using-the-shell/)).
2. The GPS is being powered, and recognized by the data board. You can use the (you can check this with the [shell](/docs/guides/getting-started/using-the-shell/)) for this.
3. If you want to make sure the complete trip is recorded, make sure the GPS can receive a clear view of the sky and that you have a valid [_gps fix_](#data-formats).

## Applications

TODO - Create note with Almabike sensor manual and link it here.