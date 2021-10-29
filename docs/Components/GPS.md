# GPS

You can now connect a GPS to the SCK2.1. The supported GPS units are in [this list](/Components/Auxiliary Connector/#other-auxiliaries). We recommend using a ceramic patch antenna for better gain:

![](/assets/images/ceramic_antenna.png){: style="width:400px"}

The U.FL antenna connector **does not need to be unplugged** from the board, specially never when the board is being powered in order to avoid damaging the circuitry:

![](/assets/images/UFL.png){: style="width:400px"}

> Antenna images by [Sparkfun](https://www.sparkfun.com) (License [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)) and edited by Smart Citizen.

!!! info "Harsher environments?"
	In harser environments, a magnetic mounted waterproof antenna like [this one](https://eu.mouser.com/ProductDetail/Taoglas/AA171301111?qs=%2Fha2pyFaduhLT2djiVcQ%252BmKy6lTU1e7%2FjAvHSK%252B8w22J1i%252BNOh5WUg%3D%3D) would be preferred.

## Data Acquisition

Data can be recorded offline or published online to the Smart Citizen Platform. The SCK owner needs to configure how the data is going to be stored in the Setup process, either in the SD card or via network connectivity (WiFi) to the platform.

When the SCK is configured in _sdcard mode_, it will store the data at the **requested interval\*** in the SD card.

In the case of network connectivity, in normal conditions, the device will send data over to the Smart Citizen Platform via WiFi (WPA2 Personal or WEP). Additionally, when configured to send data over WiFi, if there is a SD card present, it will also store the data in it as a backup. Finally, in the special case of mobile sensors, where network connectivity is not always present, the data can be recorded offline on its internal dedicated flash memory of 8MB and later publish this over WiFi connectivity. Data is published using MQTT messages to the Smart Citizen Platform. NTP is used for syncing the built-in RTC.

!!! info "Make sure data is recorded"

    It is important to follow the steps below in order to select the correct _kit blueprint_ while registering the sensor:

    1. Click the 🛠️ icon in the bottom right corner

    2. Choose the blueprint of the device you want to setup, in this case: `#32 SCK 2.1 GPS`

    3. Click save and continue the process as usual

### Recording interval

In order to understand the reading and publication intervals, it is important to describe how the structure of the measurements is done:

1. **Overall reading interval**: base period for the SCK to take a measurement
2. **Individual sensor reading interval**: period for each sensor to take a measurement. It is defined as N times the _Overall reading interval_
3. **Publication interval**: time for the SCK to publish to the Smart Citizen Platform, independent of the reading interval.

Each of the sensors can be configured independently, with a reading interval N times the _overall reading interval_. **When a GPS is connected**, all the sensors are read every 60s if the sensors are static. When a GPS movement is detected, the reading interval goes down to 5s.

If you use the sensor out of WiFi connectivity (i.e. moving), the sensors store data internally in the Flash memory during the trips and publish it in batch when the configured WiFi network is visible. Data is also stored in the SD card for later use in CSV file format.

![](/assets/images/bike_trip.jpg)

### Data formats

Data from the GPS are timestamped in ISO8601 format with the following metrics:

| Metric                    | Units | Description               |
|--------------------------------|-------|-----------------------|
| GPS_ALT                  | m   | GPS Altitude        |
| GPS_DIL            | n/a    | GPS Horizontal Dilution of Position        |
| GPS_FIX_QUALITY      | n/a   | GPS Fix Quality            |
| GPS_LAT    | º   | GPS Latitude            |
| GPS_LONG | º | GPS Longitude            |
| GPS_SAT_N | n/a | GPS Number Tracked Satellites            |
| GPS_SPEED | m/s | GPS Horizontal Speed         |


## GPS Specifics

### NEO-M8U

The selected NEO-M8U GPS Breakout from Sparkfun is a high quality GPS board. The NEO-M8U takes advantage of u-blox's Untethered Dead Reckoning (UDR) technology. The NEO-M8U module is a 72-channel u-blox M8 engine GNSS receiver, meaning it can receive signals from the GPS, GLONASS, Galileo, and BeiDou constellations with **ca. 2.5 meter accuracy**. The module supports concurrent reception of three GNSS systems. The combination of GNSS and integrated 3D sensor measurements on the NEO-M8U provide accurate, real-time positioning rates of up to 30Hz.

Compared to other GPS modules, this breakout maximizes position accuracy in dense cities or covered areas. Even under poor signal conditions, continuous positioning is provided in urban environments and is also available during complete signal loss (e.g. short tunnels and parking garages). Lock time is further reduced with on-board rechargeable battery; there is a backup power enabling the GPS to get a hot lock within seconds.

The SparkFun NEO-M8U GPS Breakout is also equipped with an on-board rechargeable battery that provides power to the RTC on the NEO-M8U. This reduces the time-to-first fix from a cold start (ca. 26s) to a hot start (ca. 1.5s). The battery will maintain RTC and GNSS orbit data without being connected to power for plenty of time.

![](/assets/images/NEO_M8U_GPS-Diagram.png)

> GPS image by [Sparkfun](https://www.sparkfun.com) (License [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)) and edited by Smart Citizen.
