Firmware
========

The firmware is OOP and is entirely written in C++. Both processors the core ARM MCU and the ESP8266 WIFI are developed as part of the same framework integrating seemingly by using a set of bridge libraries that provide a unifies the RPC architecture.

The following software was partially developed by IAAC as part of the Making Sense project under the European Community's H2020 Programme Grant Agreement No. 688620.

![](https://i.imgur.com/aDfydqU.png)

Firmware updates are done via the micro USB port using the Platform IO software available for Linux, Mac and Windows. 

## Architecture

### Core Microcontroller


| Name       | Functions                                                            |
|------------|----------------------------------------------------------------------|
| Pins       | Definition for the MCU pinout                                        |
| Sensors    | Definition for all the sensors supported                             |
| Sensors    | Absracts the sensors on a common interface                           |
| SckBase    | Manages the core operations: power, connectivity, peripherials       |
| SckAux     | Manages the sensors connected on the AUX connector                   |
| SckUrban   | Manages the sensors on the Urban Sensor Board                        |
| SckCharger | Manages the battery charging process                                 |
| SckButton  | Manages users button interaction actions                             |
| SckLed     | Manages light status for user feedback                               |
| Commands   | Library to absracts the core features on to a simple shell interface |
| ReadLight  | Manages configuration over light                                     |
| ReadSound  | Manages configuration over sound                                     |

#### Dependencies

* Adafruit INA219 Library
* Adafruit MPL3115A2 Library
* Adafruit SHT31 Library
* Arduino Json Library
* Arduino Low Power@ Library
* ArduinoZero PMUX Report Library
* DS2482 Library
* FlashStorage Library
* FlashStorage
* MCP342X Library
* RadioHead Library
* RTCZero Library
* SdFat Library
* SmartSmart Citizen Kit Gases Pro Board Library
* SparkFun BQ27441 Arduino Library
* SparkFun MAX3010x Library
* SPIFlash Library
* U8g2 Library

### WiFi Module

| Name   | Functions                                       |
|--------|-------------------------------------------------|
| SckESP | Runs all the Wi-Fi networking related functions |

### Dependencies

* Time Library
* ArduinoJson Library
* RemoteDebug Library
* RemoteDebug Library
* RadioHead Library
* RadioHead Library
* PubSubclient Library

### Shared

| Name   | Functions                                            |
|--------|------------------------------------------------------|
| Config | Provides a shared configuration between the two MCUs |


## Data management
The board is capable of storing the recorded data offline on its internal dedicated flash memory of 8MB and later publish this over Wi-Fi connectivity provided by an Espressif ESP8266. Data is published using MQTT messages to the Smart Citizen Platform. NTP is used for syncing the built-in RTC. For long term offline storage, the board provides a standard microSD socket where card in the orders of GB can be employed. That ensures extended periods of data in the order of decades can be stored.

### Configuration
The board firmware is fully customizable without requiring any changes to the core software. That includes enabling or disabling sensors, the sampling frequency of the sensors or the operation mode. There different configuration options: via the Serial Shell available when the board is connected over USB, editing the config.txt file when using a microSD card.

```
Detecting: AlphaDelta 1A... found, Enabling AlphaDelta 1A
Detecting: AlphaDelta 1W... found, already enabled!!!
Detecting: AlphaDelta 2A... found, already enabled!!!
Detecting: AlphaDelta 2W... found, already enabled!!!
Detecting: AlphaDelta 3A... found, already enabled!!!
Detecting: AlphaDelta 3W... found, already enabled!!!
Detecting: AlphaDelta Temperature... found, already enabled!!!
Detecting: AlphaDelta Humidity... found, already enabled!!!
Detecting: Groove ADC... nothing!
Detecting: INA219 Bus voltage... nothing!
Detecting: INA219 Shunt voltage... nothing!
Detecting: INA219 Current... nothing!
Detecting: INA219 Load voltage... nothing!
Detecting: DS18B20 Water temperature... nothing!
Detecting: Atlas PH... nothing!
Detecting: Atlas Conductivity... nothing!
Detecting: Atlas Specific gravity... nothing!
Detecting: Atlas Dissolved Oxygen... nothing!
Detecting: Atlas DO Saturation... nothing!
Detecting: Groove OLED... nothing!
```

## Shell

The firmware provides a comprehensive command shell over USB to manage all the kits functionalities for advanced users. 

_Use any Serial console as `screen`, `platformio device monitor`, or the serial monitor on the Arduino IDE_

Example commands:

```

SCK> help

SCK> config -wifi "myWifiName" "myPassword" -token myToken -mode network

```

## Storage

### Configuration file **CONFIG.TXT**

If this file doesn't exist it is generated by the kit with the factory defaults and after that it can be modified by both the user and the kit. `SckBase::resetConfigFile();`

If the modification comes from the kit (sound, platform, etc) it should be saved to the flash and then to the SD.

When the file is read from the SD if it is valid and different from the flash version the flash version should be updated. There is a problem in this approach: if the user insert and old scard with an old config without erasing it he can mess an newly configured kit. To solve this there is the possibility of having a first entry in the config file that is called something like _user_modified_ and the user should modify this so the new config is loaded. If this flag is not true the sdcard config would be overwritten with the one in the flash.

!!! warning "Warning on Factory Reset"
	This file will be restored to default values in a _factory reset event._

### Readings file **POST.CSV**

This file is generated and updated by the kit.

When a SD is detected this file will be synced with the flash version as the correct one. For this to work we need a fast way to compare the files. We need to test if this is doable in terms of speed. Maybe only do this when it is requested via a command or user input.

There should be a way to know if a post has been uploaded to the platform, so when the kit doesn't have a wifi connection it saves the readings and publish them as soon as a network connection is available.

!!! warning "Warning on Factory Reset"
	This file will be restored to default values in a _factory reset event._

### Debug log file **DEBUG.CSV**

The debug file is generated and updated by the kit, only if the debug mode is enabled on the configuration.

When the debug mode is enabled the verbosity level of this file is defined by the outlevel (_normal, verbose or silent_).

!!! warning "Warning on Factory Reset"
	This file will be restored to default values in a _factory reset event._

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-20/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-kit-20" aria-label="Check the source code">Check the source code</a>
