# Adding External Sensors

This page reflects examples on how to use and implement [compatible third party sensors](/Components/Auxiliary/).

!!! info "What are _third party sensors_?"
    By third party sensors, we mean sensors that have been developed by others, with no affiliation to the Smart Citizen Team.

!!! warning ""
    This page is a digest and updated version of the [Making Sense D2.3 Smart Citizen Toolkit report](http://making-sense.eu/wp-content/uploads/2016/08/Making-Sense-D23-Smart-Citizen-Toolkit.pdf) and [Making Sense D.24 Smart Citizen Toolkit report updates](http://making-sense.eu/wp-content/uploads/2017/09/Making-Sense-D2.4-Documentation-on-Toolkit-add-ons.pdf). Both these reports reflect information for the **SCK 1.5**, which is not a commercially available version of the kit. This guide is an update version for the SCK 2.1.

## Use of already supported sensors

The auxiliary port is designed to expand the sensor board by adding new sensors via the common I2C standard. However other protocols are supported, such as SPI or UART. The pins have the following default configuration:

|PIN|PORT|Function|
|:-:|:-:|:-:|
|1|SCL|I2C (by software: 1-WIRE or other)|
|2|SDA|I2C (by software: 1-WIRE or other)|
|3|VCC| Voltage |
|4|GND| Ground |

By connecting any of the [supported sensors](/Components/Auxiliary/) to the SCK, it will automatically be detected and data will be logged into the SD-card. You can check the output of the `sensor` command in the [Serial output](/Components/Firmware/guides/Using the Shell/):

```
> sensor
Enabled
----------
Temperature (60 sec)
Humidity (60 sec)
Ext Temperature (60 sec)
Ext Humidity (60 sec)
Battery (60 sec)
Light (60 sec)
Noise dBA (60 sec)
Barometric pressure (60 sec)
PM 1.0 (60 sec)
PM 2.5 (60 sec)
PM 10.0 (60 sec)
```

### Publishing data using custom devices

The Smart Citizen Platform supports data from any sensor that has a
**numerical digital output**. The Smart Citizen API supports other devices to publish data to the platform by previously agreeing with the Smart Citizen terms and conditions.

For each device type, a new device blueprint needs to be created. **A device blueprint defines the sensors and the metrics that your devices will have.** This will include the hardware details of your sensors and the kind of data that will be published to the platform. Custom calibration formulas to be applied to the data when processed in the platform can be also added.

!!! info "How to do it?"
    Once a device blueprint is added to the platform, any user can create as many devices as needed and publish data to them following the standard Smart Citizen API. It is important to note that Device Blueprint currently cannot be created by users and should be requested by contacting support@smartcitizen.me.

The minimal Device Blueprint includes all the necessary data that a user might provide in order to create a [Kit](http://developer.smartcitizen.me/#kits). It is composed of [Components](http://developer.smartcitizen.me/#components
) and those can reuse existing [Sensors](http://developer.smartcitizen.me/#sensors
) and [Measurements](http://developer.smartcitizen.me/#measurements
) definitions. Sensors define the hardware or software component that records the data.  Measurements are descriptions of what sensors are recording. Blueprints can be shared across many devices or can be tailored per device in order to provide dedicated calibration formulas per individual sensor. This is achieved with the _Components_ binding.

The following example shows a basic Device Blueprint in JSON. This is the minimum of information that a blueprint needs:

```
{
    “name”: “The Frog”,
    “description”: “Custom Arduino Humidity Sensor”,
    “slug”: “ms:0,5”,
    “components”: [{
        “map”: “hum”,
        “equation”: “(125.0 / 65536.0 * x) + 7”,
        “sensor”: {
            “name”: “HPP828E031”,
            “description”: “Humidity”,
            “unit”: “%”,
            “measurement”: {
                “name”: “relative humidity”,
                “description”: “Relative humidity is a measure...”
            }
        }
    }]
}
```

The following examples expand the previous Device Blueprint with the complete data model:

```
{
    “id”: 10,
    “uuid”: “056e452d-41c4-436d-a640-2157a278037d”,
    “slug”: “ms:0,5”,
    “name”: “The Frog”,
    “description”: “Custom Arduino Humidity Sensor”,
    “created_at”: “2016-06-18T16:25:02Z”,
    “updated_at”: “2016-06-18T16:25:02Z”,
    “components”: [{
        “id”: 35,
        “uuid”: “22da9377-5151-4547-a71b-6fd8958e1330”,
        “equation”: “(125.0 / 65536.0 * x) + 7”,
        “map”: “hum”,
        “sensor”: {
            “id”: 13,
            “uuid”: “1c19ae8f-b995-460f-87a3-a9d0c140abfb”,
            “parent_id”: 19,
            “name”: “HPP828E031”,
            “description”: “Humidity”,
            “unit”: “%”,
            “created_at”: “2015-02-02T18:24:30Z”,
            “updated_at”: “2015-07-05T19:54:54Z”,
            “measurement”: {
                “id”: 2,
                “uuid”: “9cbbd396-5bd3-44be-adc0-7ffba778072d”,
                “name”: “relative humidity”,
                “description”: “Relative humidity is a measure of the amount of
                moisture in the air relative to the total amount of moisture the    air    can    hold.  For instance,
                if the relative humidity was 50%, then the air is only half         saturated   with  moisture.”
            }
        }
    }]
}
```

!!! warning "Too much information?"
    Drop an email to support@smartcitizen.me and we will try to help!

!!! info "Using SEEED Studio Grove bricks"
    You can use off-the-shelf sensors from the extensive Grove open hardware sensor library, removing the need to build our own sensor add-ons from scratch.
    Foto seeed sensors
    ![Seeed Grove Bricks](/assets/images/grove_bricks.png)

## Implementing other sensors

!!! warning "This is a WIP"
    This section is under heavy development. Thanks for your patience!

Implementation of other sensors goes through the modification of the [Firmware](/Components/Firmware/). This is an advanced user feature, and previous programming experience in C++ is necessary.

The workflow we normally follow for this goes like:

1. Find out if there is an already existing library for the desired sensor. Good places to look at are [Adafruit's repository](https://github.com/adafruit), [Sparkfun's repository](https://github.com/sparkfun) or a global [Github](https://github.com/) search

2. Implement this library in the firmware. The library needs certain functions to be valid. (More info soon!)

3. If the device needs to log the data on the platform, you can email us at support@smartcitizen.me with a request for a new device blueprint. However, it is easier to simply log the data in SD-card in this case, if the online recording is not fully mandatory.

!!! info "Contribute it back to the community"
    Make a pull request with your contribution back to the firmware so that other can use it!


Additional sensors can be added to the Smart Citizen Kit as seen in the [Supported Sensors page](/Components/Auxiliary Connector/). The [PM Board](/Components/boards/PM Board/) is one of the options, and a powerful auxiliary board that can connect to many things on the auxiliary bus of the Smart Citizen Kit. However, it's not the only way to attach sensors.

## Example

The example below shows how to connect the PM board to different sensors:

![](/assets/images/pm-board-example.png)

Make sure that the Grove cables that will have the I2C connections are short (max 20-30cm).
You can also use [this grove hub](https://www.seeedstudio.com/Grove-I2C-Hub.html) and [this grove to screw connector](https://www.seeedstudio.com/Grove-Screw-Terminal.html).

### Configuration

To use a configuration with additional sensors (with or without PM Board), and in case you want to store the data on the platform, you will need to select the appropiate blueprint for it. When doing the onboarding process, make sure you select the proper blueprint in the [advanced sensor selection](/Guides/getting started/Onboarding Sensors/#advanced-kit-selection). 

!!! warning "Important to know which sensor you have"
	To distinguish the sensors you have plugged in onto your kit, make sure you know what sensor model they are. You can [check these instructions](/#understanding-sensor-names) to get around.

Some examples are shown below:

- **38** SCK 2.1 Soil and Air (SCK 2.1 - Soil Moisture, Soil Temperature and Air)

<div class="table-compact"></div>

| Sensor ID | Name | Units |
| :- | :- | :-: |
| 10 | Battery SCK | (%) |
| 10 | Battery SCK | (%) |
| 55 | SHT31 - Temperature | (ºC) |
| 56 | SHT31 - Humidity | (%) |
| 58 | MPL3115A2 - Barometric Pressure | (kPa) |
| 112 | AMS CCS811 - eCO2 | (ppm) |
| 113 | AMS CCS811 - TVOC | (ppb) |
| 14 | BH1730FVC - Light | (lux) |
| 87 | PMS5003 - PM2.5 | (ug/m3) |
| 88 | PMS5003 - PM10 | (ug/m3) |
| 89 | PMS5003 - PM1.0 | (ug/m3) |
| 53 | ICS43432 - Noise | (dBA) |
| 51 | AS EZO RTD | (ºC) |
| 50 | Chirp Capacitive Soil Moisture | (%) |
| 96 | DS18B20 | (°C) |
| 79 | Ext SHT31 - Temperature | (°C) |
| 80 | Ext SHT31 - Humidity | (%) |
| 45 | AS EZO Electrical Conductivity | (µS/cm) |
| 43 | AS EZO PH | (-) |

- **34** BioPV Kit 2.1 (SCK 2.1 - Urban Board + PM + Atlas + Soil Moisture + ADC ADS1115)

<div class="table-compact"></div>

| Sensor ID | Name | Units |
| :- | :- | :-: |
| 10 | Battery SCK | (%) |
| 14 | BH1730FVC - Light | (lux) |
| 53 | ICS43432 - Noise | (dBA) |
| 55 | SHT31 - Temperature | (ºC) |
| 56 | SHT31 - Humidity | (%) |
| 58 | MPL3115A2 - Barometric Pressure | (kPa) |
| 87 | PMS5003 - PM2.5 | (ug/m3) |
| 88 | PMS5003 - PM10 | (ug/m3) |
| 89 | PMS5003 - PM1.0 | (ug/m3) |
| 133 | ADC_48_0 | (V) |
| 134 | ADC_48_1 | (V) |
| 135 | ADC_48_2 | (V) |
| 136 | ADC_48_3 | (V) |
| 112 | AMS CCS811 - eCO2 | (ppm) |
| 113 | AMS CCS811 - TVOC | (ppb) |
| 50 | Chirp Capacitive Soil Moisture | (%) |
| 51 | AS EZO RTD | (ºC) |
| 43 | AS EZO PH | (-) |
| 48 | AS EZO Dissolved Oxygen | (mg/L) |


- **31** SCK 2.1 Sea Water (Smart Citizen Kit 2.1 with Sea Water Sensors)

<div class="table-compact"></div>

| Sensor ID | Name | Units |
| :- | :- | :-: |
| 14 | BH1730FVC - Light | (lux) |
| 53 | ICS43432 - Noise | (dBA) |
| 55 | SHT31 - Temperature | (ºC) |
| 56 | SHT31 - Humidity | (%) |
| 58 | MPL3115A2 - Barometric Pressure | (kPa) |
| 113 | AMS CCS811 - TVOC | (ppb) |
| 10 | Battery SCK | (%) |
| 112 | AMS CCS811 - eCO2 | (ppm) |
| 51 | AS EZO RTD | (ºC) |
| 45 | AS EZO Electrical Conductivity | (µS/cm) |
| 122 | AS EZO Total Dissolved Solids | (ppm) |
| 123 | AS EZO Salinity | (PSU(ppt)) |
| 46 | AS EZO  Specific Gravity | (SG) |
| 125 | Latitude | (deg.) |
| 126 | Longitude | (deg.) |
| 127 | Altitude | (meters) |
| 128 | Fix | (fix code) |
| 129 | Horizontal Speed |  (m/s) |
| 130 | Satellite Number | (number) |
| 131 | Horizontal Dilution | ( ) |
| 43 | AS EZO PH | (-) |
| 48 | AS EZO Dissolved Oxygen | (mg/L) |
| 49 | AS EZO Oxygen Saturation | (%) |
| 42 | DS18B20 | (°C) |


### Understanding sensor names

Using additional sensors, can be at times confusing, because we might end up in the same kit with several sensors that measure exactly the same metric (for instance, 5 different temperature sensors!). To be able to differentiate between them, use the actual model of the hardware. An example is shown below for different temperature sensors in the same device:

* This is an air temperature sensor (a Sensirion SHT31), which you can find in the [Urban Board 2.1](/Components/boards/Urban Board/):

![](/assets/images/sensor_names_1.png)

* This is an **external air temperature sensor** (also a Sensirion SHT31), which is an external probe. You can differentiate it because is an external sensor:

![](/assets/images/sensor_names_2.png)


* This is an **external temperature sensor** (this time a MAXIM DS18B20), which is an external probe, and waterproof - not only meant for air measurements (but also water or soil):

![](/assets/images/sensor_names_3.png)

* This is also **external temperature sensor** (this time a Atlas EZO RTD - a PT1000 probe), which is an external probe, and waterproof - not only meant for air measurements (but also water or soil):

![](/assets/images/sensor_names_4.png)

!!! info "No graph?"
	This time you didn't see a graph because there was no data being sent to that metric in the kit. Normally, this is not the normal behaviour, but sometimes, if you are using blueprints for more advanced configurations, you will see that not all the sensors possible are actually in the hardware!

 
### Sensors with open leads

If you are using sensors with open leads (not terminated cables), you can use [this grove to screw connector](https://www.seeedstudio.com/Grove-Screw-Terminal.html). However, you need to know how to connect the cables to it:

!!! info "Examples"

	If you are using a [Catnip Chirp Soil Moisture](https://wemakethings.net/chirp/) sensor:
	
	![](/assets/images/chirp-screw-connector.jpeg)

	Or if you are using a [DF-Robot Weather proof temperature sensor](https://www.dfrobot.com/product-2160.html):

	![](/assets/images/df-robot-screw-connector.jpeg)