---
field: other
target: location
type: external
feature_img:
status: stable
versions:
    hardware: 2.1
    firmware: 0.9.8
interface:
    - Auxiliary Port:
        description: I2C via Auxiliary Port
        image:
        comment:
resources:
    datasheet:
    papers:
    guides:
    external:
---

# GPS

You can now connect a GPS to the [Data Board](/Components/boards/Data Board/) through the [Auxiliary Connector](/Components/Auxiliary Connector/). This means, that you can measure while moving, but that you can also retrieve `date and time` from GPS in case you don't have a network connection.

Some modules are implemented at the moment. See the table below to see the metrics and the available modules.

<!-- {{ get_snippet_rel("docs/includes/supported sensors/location/en/index.md") }} -->

## Data Acquisition

As usual, data can be recorded offline or published online to the Smart Citizen Platform. If you use the sensor out of WiFi connectivity (i.e. moving), the sensors store data internally in the [Flash memory](/Components/Flash Storage/) during the trips and publish it in batch when the configured WiFi network is visible. Data is also stored in the SD card for later use in CSV file format.

![](/assets/images/bike_trip.jpg)

!!! info "Make sure data is recorded"

    It is important to follow the steps below in order to select the correct _kit blueprint_ while registering the sensor:

    1. Click the 🛠️ icon in the bottom right corner

    2. Choose the blueprint of the device you want to setup, in this case: `#32 SCK 2.1 GPS`

    3. Click save and continue the process as usual

### Recording interval

Similarly to the general configuration, you can [change the recording interval](/Guides/getting started/Using the Shell/#set-recording-and-publication-intervals). **However, when a GPS is connected**, all the sensors are read every 60s if the sensors are static. When a GPS movement is detected, the reading interval goes down to 5s.

### Data formats

Data from the GPS are timestamped in ISO8601 format with the following metrics:

| Metric                    | Units | Description                           |
|---------------------------|-----  |---------------------------------------|
| GPS_ALT                   | m     | GPS Altitude                          |
| GPS_DIL                   | n/a   | GPS Horizontal Dilution of Position   |
| GPS_FIX_QUALITY           | n/a   | GPS Fix Quality                       |
| GPS_LAT                   | º     | GPS Latitude                          |
| GPS_LONG                  | º     | GPS Longitude                         |
| GPS_SAT_N                 | n/a   | GPS Number Tracked Satellites         |
| GPS_SPEED                 | m/s   | GPS Horizontal Speed                  |

## Antenna

The supported GPS units are in [this list](/Components/Auxiliary Connector/#other-auxiliaries). For the modules that support it, we recommend using an external ceramic patch antenna for better gain (unless it already has one):

![](/assets/images/ceramic_antenna.png){: style="width:400px"}

The U.FL antenna connector **does not need to be unplugged** from the board, specially never when the board is being powered in order to avoid damaging the circuitry:

![](/assets/images/UFL.png){: style="width:400px"}

> Antenna images by [Sparkfun](https://www.sparkfun.com) (License [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)) and edited by Smart Citizen.

!!! info "Harsher environments?"
    In harser environments, a magnetic mounted waterproof antenna like [this one](https://eu.mouser.com/ProductDetail/Taoglas/AA171301111?qs=%2Fha2pyFaduhLT2djiVcQ%252BmKy6lTU1e7%2FjAvHSK%252B8w22J1i%252BNOh5WUg%3D%3D) would be preferred.

# Supported GPSs

Here you have a list of supported GPSs:

- [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329)
- [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414)
- [SparkFun GPS SAM-M8Q](https://www.sparkfun.com/products/15210), only in a forked repository for now by [serialc](https://github.com/serialc/) [here](https://github.com/serialc/smartcitizen-kit-21). Read this post [here](https://forum.smartcitizen.me/t/power-off-qwiic-on-sck2-1-power-off/1623)
- [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html) (only via [PM Board](/Components/boards/PM Board/) as it uses UART to communicate)

!!! warning "Sparkfun QWIIC GPS"
    If you are using Sparkfun QWIIC GPS, note that you will need [an adaptor from GROVE to QWIIC](https://www.sparkfun.com/products/15109)

!!! info "Implement your own"
    Check the guide on [integrating other sensors](/Guides/getting started/Third party sensors/), or [contact us](mailto:support@smartcitizen.me) to know how to implement sensors made by others.