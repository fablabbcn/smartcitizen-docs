Getting Started
=====

### Adding a Smart Citizen Kit

![Smart Citizen kit 1.1](img/sck_1.1_3.jpg)

Welcome aboard! The Smart Citizen Team wants to thank you for being here, for purchasing a kit, and for joining the community taking part in this adventure.

To join the Smart Citizen family, we're going to walk you through the steps to add your Smart Citizen Kit to the platform *(we'll refer to the Smart Citizen Kit as the "SCK" for now on)*.

First, go to <a href="https://smartcitizen.me/" target="_blank">smartcitizen.me</a> using your web browser, currently only Google Chrome is supported for this process. Click <a href="https://smartcitizen.me/users/add" target="_blank">**REGISTER**</a> in the upper right menu. Complete the required fields and click REGISTER button.

Required Fields:

- **Username** - Pick any name you want as long as someone else isn't already using the it.

- **Email** - Enter your email address.

- **Password** - Must be at least 6 characters.

- **City** - Enter the name of the city you're located (doesn't need to be the same as you SCK).

- **Country** - Enter your Country (doesn't need to be the same as you SCK).

Optional Fields:

 - **Website** - If you add a website, a link is added to your CITIZEN profile page (which can be viewed by the public).

 - **File** - This adds a custom avatar. Click "Choose File" then find the image you want to use.  The image will appear next to you profile information.

Once you’ve completed the required fields, click REGISTER.  Congratulations!! You've registered yourself and will be directed to your CITIZEN dashboard. (You can always return to your CITIZEN dashboard by clicking the LOG-IN button at the very top right of the <a href="https://smartcitizen.me/" target="_blank">smartcitizen.me</a> homepage)

Now, let's add your SCK! From you CITIZEN dashboard, click on ADD SMART CITIZEN KIT.  Complete each field: 

 - **Title** - Give your SCK a name.  This title will be associated with your SCK data.

 - **Elevation** - If you don't know it, a simple Google search should help you.  Knowing your SCK's elevation helps to understand the data it collects.

 - **Exposure** - Choose INDOOR or OUTDOOR.  Again, this helps to understand the data.

 - **Kit Version** - Most likely you have a 1.1 SCK. The only way you would be using a 1.0 SCK is if you got it from the original GOTEO crowdfunding campaign, or if you got it from someone else that got it from GOTEO. 

 - **Geolocation** - There are two ways to complete this section: AUTO COMPLETE ON or AUTO COMPLETE OFF.  AUTO COMPLETE ON lets you type in the name of your city, then lets you choose it from a drop-down list (This will give you an approximate latitude and longitude).  AUTO COMPLETE OFF will put a blue flag on the map to the left of the form.  You then drag the flag to the SCK's location on the map.  By zooming in you can pin-point the exact latitude and longitude of your SCK (the closer you get, the better the data will be).

 - **Description** - This is an optional field that helps inform others of your SCK's unique set-up.  Information like "in my garage" or "im my woodshop" could help others understand why some of your data looks the way it does.

Click on the **Save sensor** button. Congratulations!! You've added your first ** and will be directed to your ** dashboard. Your SCK now has an official device ID (it can bee seen in your browser's address bar, it is the number at the end of the url). 

Good job, both you and your SCK are registered. Now it's time to configure and upload the firmware that will be the brains of your SCK.

If this is the first time registering a SCK, you should install the <a href="https://chrome.google.com/webstore/detail/smart-citizen-kit/llohmdkdoablhnefekgllopdgmmphpif" target="_blank">Smart Citizen Kit Chrome Extension</a>. Click on the ADD TO CHROME button. 

![Sck Chrome App](img/sck_app_chrome.png)

In Windows you will need to install the Arduino Drivers if you haven't done it before. If you already have Arduino installed you should not need to reinstall it.

Check [How to install the drivers on Windows?](#/start/how-to-install-the-drivers-on-windows) section for more information.


OK, time to unpack your SCK. Connect the USB cable to your SCK and your computer. Turn on your SCK at the switch in the upper left corner of the base board.  Now, go back to the Smart Citizen website and to your **SENSOR** dashboard. Click on the **CONFIGURE** button.

If you've installed the SCK extension and the Arduino drivers, you'll be able to click on START PROCESS button. Wait a few seconds while SCK extension does its job. 

When it has finished you’ll see a form to setup your wifi connection and data update interval parameters. Complete the fields with your **SSID** (this is your wifi network's name, it can't be longer tham 32 characters), **ENCRYPTION MODE** (you can leave the default for most networks, WPA2) and **PASSWORD PHRASE**. Then, click on **SYNC** button. Wait a few seconds (your SCK is learning your wifi credentials).

When the sync has finished, you should see something similar to "00:06:66:21:16:E4" in the **MAC ADDRESS** field. Click on the **REGISTER THE KIT** button. Now reset your SCK in order the changes take effect.

**Wow! That was so easy!**

**Issues? **Contact us at <a href="mailto:support@smartcitizen.me">support@smartcitizen.me</a> or visit our [forum](http://forum.smartcitizen.me/).

Back to your **SENSOR** dashboard. Wait a few minutes and reload the page. See if some data has been uploaded to the Smart Citizen database. To check this take a look at the field "Last Update" (If everything worked, you should see something like "Last Update: 31 seconds ago").  After the Smart Citizen database has had a few days to gather your data, you'll be able to check it from <a href="https://smartcitizen.me/" target="_blank">smartcitizen.me</a>. 

### Manual set up: The Serial Way 

In this tutorial you will configure your SCK using serial communication. By using serial communication, you will register your Wi-Fi settings into the SCK and save the SCK’s MAC address in our server.
 
The SCK, like most Arduino chips, has the ability to communicate through serial protocol (when plugged with a proper USB cable). The SCK uses the WiFly module to communicate with your Wi-Fi router. Anyway, through serial communication you will be able to send the commands directly with this module to set your Wi-Fi settings and extract the MAC address used by our server to verify your identity.
 
Note that this tutorial works for both SCK v1.0 (from the Goteo crowdfunding campaign) and SCK v1.1 (from the KickStarter crowdfunding campaign), independently of the firmware version used.
 
All the steps in this tutorial have been tested with Arduino 1.0.5. We strongly recommend not to use the Beta version of Arduino IDE as we encountered issues with drivers and serial communication.

#### STEP 1: Configuring the Wi-Fi settings

- Open Arduino IDE.
- Connect your SCK via USB.
- From the Tools > Board menu, choose the right USB port (generally the last one).
- From the Tools > Serial port menu, select the right board. This is Leonardo for SCK v1.0 (Goteo) or LilyPad Arduino USB for SCK v1.1 (Kickstarter).
- Open the serial monitor window in the Arduino IDE (button at the top-right of the main window).
- Set the options to "115200 baud" and “No line return” (drop-down menu at the bottom-right of the monitor window).
- Wake up the module and activate the Wi-Fi command mode by typing in the serial monitor:

`$$$`

- Change to “Carriage return” option (drop-down menu at the bottom-right of the monitor window)

- Add a new SSID to memory by typing:

`set wlan ssid XXX`

Note: You have to replace XXX with your ssid name, filling any space with the dollar ($) character. Due to hardware limitations it can't be longer tham 32 characters.

- Add a new phrase to memory (optional, password for WPA1 & WPA2):

`set wlan phrase XXX`

Note: You have to replace XXX with your phrase, filling any space with the dollar ($) character.

- Add a new key to memory  (optional, password for WEP & WEP64):

`set wlan key XXX`

- Add an authentication method into memory (replace XXX by “0” for Open,  “1” for WEP, “2” for WPA1, “4” for WPA2, “8” for WEP64):

`set wlan auth XXX`

- Add an antenna type into memory (replace XXX by “0” to use the internal antenna or “1” if you use an external antenna):

`set wlan ext_antenna XXX`

- Get the MAC address of the kit by typing:

`get mac`

- Copy/Save the answer for further use.

- Exit and go back to the normal operational mode by typing:

`exit`
 

#### STEP 2: Registering the kit in the platform

After you've uploaded your own script, don't forget to register the kit in our database and save there your kit mac address. To find this mac address, you can use the serial command "get mac". by following the tutorial Manual Setup, the Serial way. 

Alternatively, have a look at the wifi module on the board and read the serial number  under the bar code (something like "131G0006662116E4" on kit v1.0 or "0006662116E4" on kit v.1.1). 

![Find The Mac Address](mac_manual_sticker.jpg)

The [mac adress](http://en.wikipedia.org/wiki/MAC_address) is the last 12 digit of this serial, separated by a colon every two number. From a number like `0006662116E4` you would write `00:06:66:21:16:E4`.

In both cases, you have to pass by the configuration page of your kit, and fill the mac address input field. Then press the register your kit button.

![Register The Kit](img/register_kit.png)


 
You are now done with the manual configuration of your SCK. Wait for a few minutes to see your data coming on the server and being displayed on the web page. You can also check that everything is ok by looking at the Arduino serial monitor. Debug messages coming from your SCK should look like this:

If you want to explore further options with the WiFly module check [The SCK Command Line](http://docs.smartcitizen.me/#/start/the-sck-command-line) section.

If you encounter any issue, please share your problem on the [forum](http://forum.smartcitizen.me/)

### Manual set up: The Compilation Way

This tutorial will drive you toward a manual way of setting your Smart Citizen Kit (SCK) by editing directly the source code. As the code is Open Source, one way of setting the Wi-Fi of your SCK is to download the latest firmware, edit some lines of code, recompile it and upload it to the kit. 
 
One advantage of this system is that it gives you the opportunity to register multiple Wi-Fi networks at the same time. This is useful if your SCK is traveling from one location to another where the Wi-Fi credentials are known. The downside of this method is that you can not extract the MAC address of your kit, therefore making it this way is not suitable for the first setup of your kit. Please, refer to other tutorials available.
 

#### STEP 1: Getting the Firmware

You can download the latest firmware on our Github: 

https://github.com/fablabbcn/Smart-Citizen-Kit/releases

As you may know, the hardware and software are based on the arduino project. We will use the Arduino IDE to edit the firmware and upload it to the kit. This tutorial have been tested with Arduino 1.0.5. Download the [Arduino IDE](http://arduino.cc/en/Main/Software.).

Open the file `Smart-Citizen-Kit/sck_beta_v0_9_0/sck_beta_v0_X_X.ino`

#### STEP 2: Editing the code

If you want to set the network configuration manually, you should go to the SCKBase tab and modify the lines you see below:
 
```	cpp
#define networks 0
#if (networks > 0)
char* mySSID[networks]      = { 
  "Red1"        , "Red2"        , "Red3"             };
char* myPassword[networks]  = { 
  "Pass1"      , "Pass2"       , "Pass3"            };
char* wifiEncript[networks] = { 
  WPA2         , WPA2          , WPA2               };
char* antennaExt[networks]  = { 
  INT_ANT      , INT_ANT       , INT_ANT            }; //EXT_ANT
#endif
```
 
The easiest way would be to write `"#define networks X"` (where X is the number of WI-FI networks you are going to use), add the name of your network in `RedX` and the corresponding password in `PassX`. Due to hardware limitations neither the password or the ssid can't be longer tham 32 characters. On `wifiEncript` you could also choose the encryption mode that fits with your network's configuration (`OPEN`, `WEP`, `WPA1`, `WPA2`, `WEP64`). Om `antennaExt` you can choose the type of antenna you are using (`INT_ANT` for internal antenna (default) or `EXT_ANT` for external antenna).
 
If you register only one wifi credential, you should obtain something like:

```	cpp 
#define networks 1
#if (networks > 0)
char* mySSID[networks]      = { "MyWifiSSID"};
char* myPassword[networks]  = { "MyPassword"};
char* wifiEncript[networks] = { WPA2 };
char* antennaExt[networks]  = { INT_ANT };
#endif
```

#### STEP 3: Registering the kit in the platform

After you've uploaded your own script, don't forget to register the kit in our database and save there your kit mac address. To find this mac address, you can use the serial command "get mac". by following the tutorial Manual Setup, the Serial way. 

Alternatively, have a look at the wifi module on the board and read the serial number  under the bar code (something like "131G0006662116E4" on kit v1.0 or "0006662116E4" on kit v.1.1). 

![Find The Mac Address](mac_manual_sticker.jpg)

The [mac adress](http://en.wikipedia.org/wiki/MAC_address) is the last 12 digit of this serial, separated by a colon every two number. From a number like `0006662116E4` you would write `00:06:66:21:16:E4`.

In both cases, you have to pass by the configuration page of your kit, and fill the mac address input field. Then press the register your kit button.

![Register The Kit](img/register_kit.png)
 
You are now done with the manual configuration of your SCK. Wait for a few minutes to see your data coming on the server and being displayed on the web page. You can also check that everything is ok by looking at the Arduino serial monitor.

If you encounter any issue, please share your problem on the [forum](http://forum.smartcitizen.me/)

### Attaching the solar panel

![Solar Panel](img/v1.0/main_board_solar_panel.jpg)
![Solar Panel](img/main_board_solar_panel.jpg)

The solar panel it should fulfil the specification of a voltage bigger than 8v and less than 15v, 12v is the recommended voltage, and a minimum of 500mA.

In order to attach the solar panel you have to solder the cables of the solar panel to the pads marked in the next image for version 1.0 of the SCK. For version 1.1 you have to connect the cables to the connector marked in the next image. 

In both versions, yo have to attach the plus of solar panel to the plus pad of the SCK, and the minus of the solar panel to the minus pad of the SCK.

### Sensor calibration

**Coming soon!**

### Connecting from an iPhone or Android

**Coming soon!**


The Sck Command Line
=====

The Smart Citizen Kit can be managed over a basic serial protocol. You just need the **Arduino IDE Serial Monitor** or any other **Serial Utility** like **Screen** in order to use it.

**How to use it**

- Connect to your kit using any serial utility, any baud-rate should work but 115200 is recommendable.
- Send the starting commands.
- Notice all the commands except the starting command($$$) require a carriage return at the end: CR or \r. If you are using the Arduino IDE is enough if you change to “Carriage return” option (drop-down menu at the bottom-right of the monitor window).
- Call any command you want, change XXX with the corresponding value, filling any space with the dollar ($) character.

### Basic SCK commands

- `$$$` (Wake up the module and activate the Wi-Fi)
- `set wlan ssid XXX` (Add a new SSID to memory9)
- `set wlan phrase XXX` (Add a new phrase to memory)
- `set wlan key XXX` (Add a new key to memmory)
- `set wlan auth XXX` (Add an authentication method into memory)
- `set wlan ext_antenna XXX` (Add an antenna type into memmory)
- `get mac` (Get the MAC address of the kit)
- `exit` (Go back to normal operational mode)

### Special SCK commands

- `get time update` (Retrieve the sensor update interval)
- `set time update XXX` (Update the sensor update interval)
- `get number updates` (Retrieve the max number of bulk updates allowed)
- `set number updates XXX` (Update the max number of bulk updates allowed)
- `get apikey` (Retrieve the kit APIKEY)
- `set apikey XXX` (Update the kit APIKEY)
- `get wlan ssid` (Retrieve the SSID saved on the kit)
- `get wlan phrase` (Retrieve the phrase and KEY saved on the kit)
- `get wlan auth` (Retrieve the authentication methods saved on the kit)
- `get wlan ext_antenna` (Retrieve the antenna types saved on the kit)
- `clear nets` (Remove all saved Wi-Fi configuration information)
- `exit` (Goes back to normal operational mode)
- `data` (Retrieves sensor readings stored in memory)

### Basic WiFly commands

To deepening into wifly commands look at the link below:

<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/50002230A.pdf" target="_blank">WiFly Command Reference</a>

Hardware
=====
### Inside the SCK


![Main Board](img/v1.0/main_board.jpg)
![Main Board](img/main_board.jpg)

#### Main Board

The main board contains the basic functionality like sensor I/O to read de sensor values, communicate with the platform through the wifi module, manage the power and battery charging.

![Main Board CPU](img/v1.0/main_board_cpu.jpg)
![Main Board CPU](img/main_board_cpu.jpg)

#####PINOUT

The SCK Main Board connects to the Sensor Board 16 pin connectoir. This is are how the pins are laid out on the board. The numbers in brackets are the actual pin numbers of the microcontroller. Pins IO are digital and S are analogue.


|           |           |
| --------- | --------- |
| GND       | GND       |
| IO3 (10)  | IO2 (9)   |
| IO1 (13)  | IO0 (5)   |
| SCL       | SDA       |
| S5  (A1)  | S4  (A0)  |
| S3  (A3)  | S2  (A2)  |
| S1  (A5)  | S0  (A4)  |
| VBAT      | VBAT      |


#####CPU 

Both versions of the SCK (1.0 and 1.1) are using the same CPU, ATMEGA32U4(Arduino Leonardo). With the difference that the 1.0 works at 5V and 16MHZ and the 1.1 works at 3.3V and 8MHZ. In the 1.1 version we’ve improved the power consumption. 

This CPU has native USB and an UART TTL port allowing us to connect directly with the WIFI module.

<a href="http://www.atmel.com/images/doc7766.pdf" target="_blank">ATMEGA32U4 datasheet</a>

![usb connectors](img/usb_connectors.png)

#####USB CONNECTOR

The 1.0 version uses a Mini USB connector and 1.1 version uses a Micro USB.

![wifly module](img/v1.0/main_board_wifly.jpg)
![wifly module](img/main_board_wifly.jpg)

#####WIFI MODULE

The RN-131 module is a standalone, embedded wireless 802.11 b/g networking module. With its small form factor and extremely low power consumption, the RN-131 fits perfectly for the SCK wireless communication requirements.

Main features:

- Qualified 2.4-GHz IEEE 802.11b/g transceiver
- Ultra-low power: 4 uA sleep, 40 mA Rx, 210 mA Tx
- High throughput, 1 Mbps sustained data rate with TCP/IP and WPA2
- Small, compact surface-mount module
- On-board ceramic chip antenna and U.FL connector for external antenna
- 8-Mbit flash memory and 128-KB RAM
- UART hardware interface
- 10 general-purpose digital I/O pins
- 8 analog sensor interfaces
- Real-time clock for wakeup and time stamping
- Accepts 3.3-V regulated or 2 to 3 V battery
- Supports ad hoc and infrastructure networking modes
- On board ECOS -OS, TCP/IP stacks
- Wi-Fi Alliance certified for WPA2-PSK
- FCC/CE/ICS certified and RoHS compliant.
- Industrial (RN-131G) and commercial (RN-131C) grade temperature options

<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/rn-131-ds-v3.2r.pdf" target="_blank">WIFLY module - RN-131 datasheet</a>

![NCP1400](img/v1.0/main_board_NCP1400.jpg)
![MAX604](img/v1.0/main_board_MAX604.jpg)
![MCP1725](img/main_board_MCP1725.jpg)

#####BATTERY POWERING

For powering the SCK, in both versions, we are using a 3.7v 2000 mAh li-on battery. 

In 1.0 version, SCK uses two different voltages, 3.3V and 5V to power the IC’s. 

To elevate to 5V we are using a step-up based on NCP1400, thus having a stable voltage at 5v and 100mA.

On the other hand, to regulate the voltage and to obtain 3.3v, the SCK uses the IC MAX604.

In 1.1 version, to simplify, the voltage of entire SCK was unified to 3.3V. The responsible to regulate the voltage from 3.7v to 3.3v is the MCP1725 IC.

<a href="http://www.onsemi.com/pub_link/Collateral/NCP1400A-D.PDF" target="_blank">NCP1400 datasheet</a><br>
<a href="http://www.solarbotics.net/library/datasheets/MAX604.pdf" target="_blank">MAX604 datasheet</a><br>
<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/22026b.pdf" target="_blank">MCP1725 datasheet</a>

![MCP73831](img/v1.0/main_board_MCP73831.jpg)
![MCP73831](img/main_board_MCP73831.jpg)

#####BATTERY CHARGING

For charging the battery there are two ways, USB or solar panel. To carry out the charging we are using MCP73831 IC. 

For the solar panel way, in 1.0 version the solar panel have to be 12v and 500mA. In 1.1 version, the solar panel can be more versatile in terms of amperage. 

<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/20001984g.pdf" target="_blank">MCP73831 datasheet</a>

![LM2674](img/v1.0/main_board_LM2674.jpg)
![LM2674](img/main_board_LM2674.jpg)

#####SOLAR PANEL CHARGING

As the solar panel produces 12v, depending on the sunlight conditions, we have to reduce the voltage to 5v to feed up the Vin of the MCP73831 charger IC. 

To carry out this task we are using the LM2674 IC, a very efficient IC, with a rate of 91% of performance.

<a href="http://www.ti.com/lit/ds/symlink/lm2674.pdf" target="_blank">LM2674 datasheet</a>

![DS1307](img/v1.0/main_board_DS1307.jpg)
![DS1339Y-3+](img/main_board_DS1339Y-3+.jpg)

#####RTC (REAL TIME CLOCK)

The SCK has a real time clock for when the kit is offline. For this task we chose the DS1307 IC for the 1.0 version and the DS1339Y-3+ IC for the 1.1 version. Different IC due to the different voltages, 5V for the 1.0 version and 3.3V for the 1.1 version.

<a href="http://datasheets.maximintegrated.com/en/ds/DS1307.pdf" target="_blank">DS1307 datasheet</a><br>
<a href="http://datasheets.maximintegrated.com/en/ds/DS1339-DS1339U.pdf" target="_blank">DS1339Y-3+ datasheet</a>

![DM3CS](img/v1.0/main_board_DM3CS.jpg)
![DM3CS](img/main_board_DM3CS.jpg)

#####SD CARD READER

The SD card is used to store the data captured by the sensors when the kit is offline. Then, when the kit is online, the data will be uploaded to the platform. 

To hold the SD card we are using the DM3CS holder. The SD card is powered at 3.3V and communicates with the CPU through SPI protocol.

<a href="http://www.mouser.com/ds/2/185/e60900232-38395.pdf" target="_blank">DM3CS datasheet</a>

![24LC256](img/v1.0/main_board_24LC256.jpg)
![24LC256](img/main_board_24LC256.jpg)

#####EEPROM MEMORY

For the users that don’t have a SD card we’ve added an EEPROM memory to store the data when the SCK is offline.

We chose the 24LC256 IC that can store 32kBytes, it communicates with the CPU through I2C protocol.

<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/20001203U.pdf" target="_blank">24LC256 datasheet</a>


#####MAIN BOARD BASIC SENSORS

The main board has some basic sensors:

- Measurement of the battery level
- Measurement of the solar panel level
- Measurement of the wireless networks detected

![Sensor Board](img/v1.0/sensor_board.jpg)
![Sensor Board](img/sensor_board.jpg)

#### SENSOR BOARD

The sensor board contains the necessary sensors for measuring the pollution parameters. This means NO2 and CO gases, sunlight, noise pollution, temperature, humidity. Also, the sensor board has an I2C bus, this allows to expand the SCK to other kind of sensors.

![MICS5525](img/v1.0/sensor_board_MICS5525.jpg)
![MICS2710](img/v1.0/sensor_board_MICS2710.jpg)
![MICS4514](img/sensor_board_MICS4514.jpg)

#####NO2 AND CO SENSORS

To measure these two gases we chose <a href="http://www.e2v.com/" target="_blank">e2v</a> sensors. In particular, metal oxide sensors MICS5525 and MICS2710, for version 1.0. And MICS4514, for version 1.1, that contains both sensors in one.

Metal oxide sensors are based on oxide semiconductors. Their electrical conductivity is modulated due to the reaction between the semiconductor and the gases in the atmosphere.

<a href="http://www.e2v.com/shared/content/resources/File/sensors_datasheets/Metal_Oxide/mics-5525.pdf" target="_blank">MICS5525 datasheet</a><br>
<a href="http://www.cdiweb.com/datasheets/e2v/mics-2710.pdf" target="_blank">MICS2710 datasheet</a><br>
<a href="http://files.manylabs.org/datasheets/MICS-4514.pdf" target="_blank">MICS4514 datasheet</a>

![LDR](img/v1.0/sensor_board_LDR.jpg)
![H1730FVC](img/sensor_board_BH1730FVC.jpg)

#####LIGHT SENSOR

The light sensor is a basic element to know the light pollution. In version 1.0, was used a LDR(light-dependent resistor) whose voltage varies depending on the light conditions.

For version 1.1, was used a photodiode BH1730FVC. This sensor contains an I2C bus that gives us directly the amount of lux of ambient and infrared light.

<a href="http://www.farnell.com/datasheets/1813319.pdf" target="_blank">BH1730FVC datasheet</a>

![Noise Sensor](img/v1.0/sensor_board_noise_sensor.jpg)
![Noise Sensor](img/sensor_board_noise_sensor.jpg)

#####NOISE SENSOR

The noise sensor is based on an electret microphone. For the version 1.0, the audio signal is passed through an operational amplifier configured as band pass filter.

For the version 1.0, WM-61A was used for the microphone.

For the version 1.1, POM-3044P-R was used. The amplification step was modified adding a variable gain, allowing us to measure very low and very high signals.

<a href="http://industrial.panasonic.com/www-data/pdf/ABA5000/ABA5000CE22.pdf" target="_blank">WM-61A datasheet</a><br>
<a href="http://www.farnell.com/datasheets/40113.pdf" target="_blank">POM-3044P-R datasheet</a>

![RHT22 Sensor](img/v1.0/sensor_board_RHT22.jpg)
![SHT21 Sensor](img/sensor_board_SHT21.jpg)

#####TEMPERATURE AND HUMIDITY SENSOR

To measure temperature and humidity was used a module that integrates both sensors. 

For version 1.0 was used the RHT22, it has one wire digital interface.

For version 1.1 was used the SHT21, it has I2C protocol and a more fast response between measures than the RHT22.

<a href="https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf" target="_blank">RHT22 datasheet</a><br>
<a href="http://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/Humidity/Sensirion_Humidity_SHT21_Datasheet_V4.pdf" target="_blank">SHT21 datasheet</a>

![ADXL345](img/sensor_board_ADXL345.jpg)

#####3 AXIS ACCELEROMETEER

In version 1.0 was detected that some measures vary depending on the orientation the SCK. 

For this, in version 1.1, was added an accelerometer(ADXL345) to detect the position and to compensate the measures depending on the orientation of the SCK.

The ADXL345 has I2C protocol to interface with.

<a href="http://www.analog.com/static/imported-files/data_sheets/ADXL345.pdf" target="_blank">ADXL345 datasheet</a>

![I2C Bus](img/v1.0/sensor_board_i2c_bus.jpg)
![I2C Bus](img/sensor_board_i2c_bus.jpg)

#####I2C EXPANSION BUS

Due to the ease of the I2C protocol. We’ve included and I2C bus to provide to the community the opportunity of expanding the SCK.

### Detailed specifications


| Smart Citizen Kit |           SCK 1.0 (Goteo Board)       | SCK 1.1 (Kickstarter Board)       |
|:-----------|:-----------------:|:-----------------:|
| **Data Board**                  |                                                                                  |                                                                                     |
| **MCU**                         | ATMEGA32U4                                                                       | ATMEGA32U4                                                                          |
| **Clock**                       | 16Mhz                                                                            | 8Mhz                                                                                |
| **WiFi**                       | Microchip RN-131 802.11 b/g                                                                            | Microchip RN-131 802.11 b/g                                                                                |
| **Firmware**                    | [Repository](https://github.com/fablabbcn/Smart-Citizen-Kit)                                    | [Repository](https://github.com/fablabbcn/Smart-Citizen-Kit)                                    |
| **Design files**                 | [v1.01](https://github.com/fablabbcn/Smart-Citizen-Kit/tree/master/hardware/Goteo/v1.01)  | [v1.1](https://github.com/fablabbcn/Smart-Citizen-Kit/tree/master/hardware/Kickstarter)     |
| **Ambient Board**                |                                                                                  |                                                                                     |
| **Light**                    | PVD-P8001                                                                        | BH1730FVC                                                                           |
|                    *Type*      | LDR Analog Light Sensor                                                          | Digital Ambient Light Sensor                                                        |
|                    *Units*     | %                                                                                | Lux                                                                                 |
|                    *Datasheet* | [PDV-P8001.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/PDV-P8001.pdf)     | [BH-1730FCV.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/BH-1730FCV.pdf)       |
|                    *Firmware*   | `SCKAmbient::getLight();`                                                           | `SCKAmbient::getLight():`                                                              |
| **Temp**                     | DHT22                                                                            | HPP828E031 (SHT21)                                                                  |
|                    *Type*      | Digital Temperature and Relative Humidity Sensor                                 | Digital Temperature and Relative Humidity Sensor                                    |
|                    *Units*     | ºC                                                                               | ºC                                                                                  |
|                    *Datasheet* | [DHT22.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/DHT22.pdf)         | [HTU-21D.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/HTU-21D.pdf)          |
|                    *Firmware*   | `SCKAmbient::getDHT22();` `SCKAmbient::getHumidity();`                               | `SCKAmbient::getSHT21();` `SCKAmbient::getTemperature();`                               |
| **Humidity**                 | DHT22                                                                            | HPP828E031 (SHT21)                                                                  |
|                    *Type*      | Digital Temperature and Relative Humidity Sensor                                 | Digital Temperature and Relative Humidity Sensor                                    |
|                    *Units*     | % Rel                                                                            | % Rel                                                                               |
|                    *Datasheet* | [DHT22.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/DHT22.pdf)         | [HTU-21D.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/HTU-21D.pdf)          |
|                    *Firmware*   | `SCKAmbient::getDHT22();` `SCKAmbient::getHumidity();`                               | `SCKAmbient::getSHT21();` `SCKAmbient::getHumidity();`                                  |
| **Noise**                   | POM-3044P-R                                                                      | POM-3044P-R                                                                         |
|                    *Type*      | Electret microphone with envelop follower sound pressure sensor                  | Electret microphone with envelop follower sound pressure sensor                     |
|                    *Units*     | dB                                                                               | dB                                                                                  |
|                    *Datasheet* | [OM-3044P-R.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/POM-3044P-R.pdf)   | [OM-3044P-R.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/POM-3044P-R.pdf)      |
|                    *Firmware*  | `SCKAmbient::getNoise();`                                                          | `SCKAmbient::getNoise();`                                                             |
| **CO**                       | MICS-5525                                                                        | MiCS-4514                                                                           |
|                    *Type*      | MOS CO gas sensor                                                                | MOS CO and NO2 gas sensor                                                           |
|                    *Units*     | kOhm (ppm)                                                                       | kOhm (ppm)                                                                          |
|                    *Datasheet* | [MICS-5525_CO.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/MICS-5525_CO.pdf)  | [MiCS-4514_CO_NO2.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/MiCS-4514_CO_NO2.pdf) |
|                    *Firmware*  | `SCKAmbient::getMICS();`                                                           | `SCKAmbient::getMICS();`                                                              |
| **NO2**                     | MICS-2710                                                                        | MiCS-4514                                                                           |
|                    *Type*      | MOS NO2 gas sensor                                                               | MOS CO and NO2 gas sensor                                                           |
|                    *Units*     | kOhm (ppm)                                                                       | kOhm (ppm)                                                                          |
|                    *Datasheet* | [MICS-2710_NO2.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/MICS-2710_NO2.pdf) | [MiCS-4514_CO_NO2.pdf](https://github.com/fablabbcn/Smart-Citizen-Kit/wiki/Datasheets/MiCS-4514_CO_NO2.pdf) |
|                    *Firmware*  | `SCKAmbient::getMICS();`                                                           | `SCKAmbient::getMICS();`                                                              |


### Enclosures

![Enclosure](img/case.jpg)

We have designed a laser cut cover for an acrylic material and a 3D-Printed enclosure to better safeguard the hardware, particularly for outdoor applications.

You can download the files through this links.

<a href="http://www.thingiverse.com/thing:262891" target="_blank">Smart Citizen Enclosure 1.0</a><br>
<a href="http://www.thingiverse.com/thing:236976" target="_blank">Smart Citizen Enclosure 1.1</a>

![Enclosure](img/case_5.jpg)
![Enclosure2](img/case_6.jpg)

Also, we are working in new cases that will be available soon.

<a href="assets/case_assembly.pdf" target="_blank">Smart Citizen Enclosure Assembly Instructions</a>

### Acrylic cases 

![Acrylic](img/acrylic.jpg)

This case has been designed to protect the electronics on the circuit boards and allows for mount the SCK's hardware on walls and other surfaces without much trouble. Particularly for indoor applications.

<a href="https://github.com/acrobotic/Ai_Enclosure_SCK/tree/master/laser_cut" target="_blank">Acrylic cases</a>


Software
====
### Inside the SC Platform

Once you've added your SCK to the plattform and it's capturing and sending data correctly, you can interact with the plattform in several ways. Visualizing the data, downloading the data and interacting with the data through the API.

**Data Visualization**

To visualize the data of your device, you have to sign in into the platfform. Once you've signed, you'll be in your dashboard, click on SENSORS tab, click on one of your sensors and click in the button SHOW IN MAP.

Now, at bottom of your browser will appear a panel for visulize your data. You can visualize one by one or multiple together. For this, you can switch between the different sensors data clicking on the icons under the label FILTER. Also, you can change between different periods of time, selecting HOUR, DAY, WEEK... in the SHOW LAST drop-down selector.

**Download Data**

If you are interested in use the data captured by your sensors, you can download all the data for later use. To do this, go to your sensor profile, at the bottom there is a selector under the label DOWNLOAD DATA. You can choose between 3 different formats, CSV, XML and JSON.

**API**

The <a href="http://api.smartcitizen.me/" target="_blank">Smart Citizen API</a> allows you to request back information from your devices and do incredible things with it.

It is a <a href="https://en.wikipedia.org/wiki/Representational_state_transfer" target="_blank">REST</a> API and it returns the information in <a href="https://en.wikipedia.org/wiki/Json" target="_blank">JSON</a> format. This means you can easily access the information from any language like Javascript, PHP, Processing.org, Python, and start doing things with it quickly.

To access the API you will always need and api_key you can obtain <a href="http://smartcitizen.me/users/dashboard" target="_blank">here</a>.

The API is currently under BETA more functions will be comming soon. Please, report any problem or suggestion on the <a href="http://forum.smartcitizen.me/" target="_blank">forum</a>.

<a href="http://api.smartcitizen.me/" target="_blank">api.smartcitizen.me</a>


Faq
====
### How to store data in your own database?

**Kit's request**

The Smart Citizen Kit is publishing by default the data as a PUT Http request, the sensor data is encoded as JSON.

Here you can see how a kit's request will look like *(Note the request is not standard as it do not contains a payload)*:

``` shell
PUT /add HTTP/1.1
Host: data.smartcitizen.me
User-Agent: SmartCitizen
X-SmartCitizenMacADDR: 00:00:00:00:00:00
X-SmartCitizenVersion: 1.1-0.8.5-A
X-SmartCitizenData: [{"temp":"29090.6", "hum":"6815.74", "light":"30000", "bat":"786", "panel":"0", "co":"112500", "no2":"200000", "noise":"2", "nets":"10", "timestamp":"2013-10-28 1:34:26"}]
```

Here you have a kit's request as a  **Curl** for test purposes:

``` shell
$ curl -X PUT -H 'Host: data.smartcitizen.me' -H 'User-Agent: SmartCitizen' -H 'X-SmartCitizenMacADDR: 00:00:00:00:00:00' -H 'X-SmartCitizenVersion: 1.1-0.8.5-A' -H 'X-SmartCitizenData: [{"temp":"29090.6", "hum":"6815.74", "light":"30000", "bat":"786", "panel":"0", "co":"112500", "no2":"200000", "noise":"2", "nets":"10", "timestamp":"2013-10-28 1:34:26"}]' data.smartcitizen.me/add
```

**Data processing**

Values are send without the proper scaling and some sensors as temperature, humidity and noise are sent in raw and then calibrated in our platform. This are the conversion required for **SCK 1.1** and above.

| Key       | Sensor      | Units               | Conversion formula                            | Conversion Methos                         |
|-----------|-------------|---------------------|-----------------------------------------------|-------------------------------------------|
| temp      | Temperature | ºC                  | T = -53 + 175.72 / 65536.0 * Traw             | SCKSensorData::tempConversion($rawTemp)   |
| hum       | Humidity    | %Rel                | H = 7 + 125.0 / 65536.0 * Hraw                | SCKSensorData::humConversion($rawHum)     |
| light     | Light       | Lux                 | L = Lraw / 10                                 | SCKSensorData::lightConversion($rawLight) |
| noise     | Noise       | dB                  | Apply the conversion table from mV to dB: [CSV](https://gist.github.com/pral2a/d767cc45874361fd38bf) | SCKSensorData::noiseConversion($rawNoise) |
| co        | CO          | kOhm                | CO = COraw / 10000                            | SCKSensorData::coConversion($rawCO)       |
| no2       | NO2         | kOhm                | NO2 = NO2raw / 10000                          | SCKSensorData::no2Conversion($rawNO2)     |
| bat       | Battery     | %                   | B = Braw / 10                                 | SCKSensorData::batConversion($rawBat)     |
| panel     | Panel       | mV                  | P = Praw / 10000                              | SCKSensorData::panelConversion($rawPanel) |
| nets      | Nets        | Wi-Fi Networks      | Not required                                  | Not required                              |
| timestamp | Timestamp   | YYYY-MM-DD hh:mm:ss | Not required                                  | Not required                              |

You can use the **[SCKSensorData](https://github.com/fablabbcn/Smart-Citizen-Kit/blob/master/data/) php** class to re-scale and calibrate the received data. Check it on [github](https://github.com/fablabbcn/Smart-Citizen-Kit/blob/master/data/).

Here is an example how to use it to receive a request, converted and store it in a CSV file:

``` php
<?php
	include('../sck_sensor_data.php');

	$headers = getallheaders();

	$data = $headers['X-SmartCitizenData'];

	$datapoints = json_decode($data, true);

	foreach ($datapoints as $datapoint) {
	$datapoint = SCKSensorData::SCK11Convert($datapoint);
		$csv .= implode(', ', $datapoint);
	}

	$csv .= PHP_EOL;

	file_put_contents('./data.csv', $csv, FILE_APPEND);
?>
```

You can find the complete example [here](https://github.com/fablabbcn/Smart-Citizen-Kit/blob/master/data/examples/add.php).

Each sensor is implemented as a separate function and some general methods are available for simplifing the work. Here is an example:

``` php
<?php

	/**
	 * noiseCalibration
	 *
	 * Noise calibration for SCK1.1 sound sensor. Converts mV in to dBs. 
	 * Based on a linear regresion from a lookup table (db.json) 
	 * obtained after real measurements from our test facility.
	 * 
	 *
	 * @param float $rawSound
	 * @return float noise as sound pressure in dB
	 *
	 */
	
	public function noiseCalibration($rawSound)
	{
		$dbTable = json_decode(file_get_contents("db.json"), true);
		return round(self::tableCalibration($dbTable, $rawSound), 2);
	}
?>
```
**How to proceed**

Here are the different paths you can take in order to built your own backend:

- Create a fork of the the <a href="https://github.com/fablabbcn/Smart-Citizen-Kit/tree/master" target="_blank">Smart Citizen Kit firmware</a> in order to send the data as your custom backend expect it.

- Create your own custom backend. We can share all the different modules of our backend in order for you to receive data as on the curl example above, calibrate it and store it. Contact us at <a href="mailto:support@smartcitizen.me">support@smartcitizen.me</a>.

- Keep using our backend but request our public API <a href="http://api.smartcitizen.me/" target="_blank">api.smartcitizen.me</a> and then fill database choise with it.

### How to use the SD Card?

1. **microSD**: We recomend formating **micro SD** cards using the official SD tool you can download [here](https://www.sdcard.org/downloads/formatter_4/).

2. **RTC**: Place a **CR1220** cell battery on your kit. Before uploading the SD firmware use the on-line configuration tool at [smartcitizen.me](https://smartcitizen.me) to set your Wi-Fi credentials. Turn your kit off and on for a minute, the blue led's will blink and your kit will connect to the internet and sync its the internal clock with our remote servers. Once the time is set the cell battery will keep SCK time in sync for more than 4 years.

3. You can now install the <a href="https://github.com/fablabbcn/Smart-Citizen-Kit/tree/master/sck_beta_v0_8_7_SDCARD" target="_blank">**SD firmware**</a> using the [Arduino IDE](http://www.arduino.cc/en/Main/Software). 

**Dependencies:**

* In order to compile and upload the firmware you will need to install the **SdFat** library for Arduino.

* Download the library [here](https://github.com/greiman/SdFat) and install the library following the [instructions](http://arduino.cc/en/Guide/Libraries).

**Boards:**

* For SmartCitizen Kit version 1.0 select `Tools/Boards/Arduino Leonardo` on the Arduino IDE (ATmega 32U4 at 16Mhz) 

* For SmartCitizen Kit version 1.1 select `Tools/Boards/Lylipad Arduino USB` on the Arduino IDE (ATmega 32U4 at 8Mhz) 

**SD data format**

When using the **SD firmware** on the SCK, data is stored as **CSV** ([comma separated](http://en.wikipedia.org/wiki/Comma-separated_values)) file on the SD card.

This is an example of the output file once opened on a spreadsheet application:

| Temperature | Humidity | Light   | Battery | Solar Panel | CO     | NO2  | Noise | UTC                 |
|-------------|----------|---------|---------|-------------|--------|------|-------|---------------------|
| 2821.20     | 4072.00  | 4413.10 | 96.40   | 0.00        | 94.67  | 0.65 | 5.23  | 2000-01-01 00:00:02 |
| 2784.40     | 4236.80  | 5936.70 | 96.10   | 0.00        | 278.27 | 1.05 | 2.39  | 2000-01-01 00:00:02 |

**Data Conversions**

The data stored is automatically converted to the proper units in firmware.

If you prefer to do the conversions manually set `DataRaw       false` in the `Constants.h` file and apply the formulas on the following table:

| ID | Sensor      | Units    | Conversion Formula                            |
|----|-------------|----------|-----------------------------------------------|
| 0  | Temperature | ºC       | T = -53 + 175.72 / 65536.0 * ( Traw * 10 )    |
| 1  | Humidity    | %Rel     | H = 7 + 125.0 / 65536.0 * ( Hraw * 10 )       |
| 2  | Light       | Lux      | L = Lraw / 10                                 |
| 3  | Battery     | %        | Not required                                  |
| 4  | Panel       | mV       | Not required                                  |
| 5  | CO          | kOhm     | Not required                                  |
| 6  | NO2         | kOhm     | Not required                                  |
| 7  | Noise       | dB       | Apply the conversion table from mV to dB: [CSV](https://gist.github.com/pral2a/d767cc45874361fd38bf)       |
| 8  | Date        | DD:MM:YY | Not required                                  |
| 9  | Time        | hh:mm:ss | Not required                                  |


### How to import the SD card data?

You can import the recorded data in to [smartcitizen.me](http://smartcitizen.me)

In your device page you will find the **Import SD** along with the Edit and Configure options.

![image](https://smartcitizen.me/img/sck-sd-import.png)

Using a microSD card reader get the **post.csv** file from your card, select it and click import. Data will be imported in to your device, data existing on the file already imported will be skipped. Your kit should be running the latest SD firmware  and the SCK time (RTC) should be set in order data can be imported.

### Is my kit pusblishing data properly?

You can easily check each time your kit is pusblishing data to our platform in real time by enabling the debug mode on your device.

* Go to your device edit page in [smartcitizen.me](http://smartcitizen.me), set Debug Enabled and save it.
* Visit [data.smartcitizen.me/debug](http://data.smartcitizen.me/debug) you will see the data from all the devices on debug mode every time they publish in real time. You can indetify your device by the devie id. **Note data comes uncalibrated.*

![image](img/data_debug.png)

### How to retrieve other kit's data?

Current [API](http://api.smartcitizen.me/) allows you acces historical and latest value of the devices you own. We current offers [special API access](http://api.smartcitizen.me/#api-Devices-GetDevicesInfo) to all devices for research and academic purposes. 

Please contact [support@smartcitizen.me](mailto:support@smartcitizen.me) describing how you expect to use the data and we will give you access to it.

### How to install the drivers on Windows?

In Windows you will need to install the Arduino Drivers if you haven't done it before.

#### Windows 8, 7, Vista, and XP

*   Go to the Arduino [download page](http://arduino.cc/en/Main/Software) and download the latest version of the Arduino software for Windows.
*   When the download is finished, un-zip it and open up the Arduino folder to confirm that yes, there are indeed some files and sub-folders inside. The file structure is important so don’t be moving any files around unless you really know what you’re doing.
*   Power up your Arduino by connecting your Arduino board to your computer with a USB cable (or FTDI connector if you’re using an Arduino pro). You should see the an LED labed ‘ON’ light up. ([this diagram](https://learn.sparkfun.com/tutorials/what-is-an-arduino/whats-on-the-board) shows the placement of the power LED on the UNO).
*   If you’re running Windows 8, you’ll need to disable driver signing, so go see the Windows 8 section. If you’re running Windows 7, Vista, or XP, you’ll need to install some drivers, so head to the Windows 7, Vista, and XP section down below.

#### Windows 8

Windows 8 comes with a nice little security ‘feature’ that ‘protects’ you from unsigned driver installation. The Smart Citizen Kit driver is not signed so you’ll have to tell Windows to disable driver signing. This issue has been addressed in newer releases of the Arduino IDE, but if you run into issues, you can try this fix first.

For a nice, step-by-step tutorial with pictures [click here](https://learn.sparkfun.com/tutorials/disabling-driver-signature-on-windows-8/overview), otherwise the steps are outlined below.

To _temporarily_ disable driver signing:

*   From the Metro Start Screen, open Settings (move your mouse to the bottom-right-corner of the screen and wait for the pop-out bar to appear, then click the Gear icon)
*   Click ‘More PC Settings’
*   Click ‘General’
*   Scroll down, and click ‘Restart now’ under ‘Advanced startup’.
*   Wait a bit.
*   Click ‘Troubleshoot’.
*   Click ‘Advanced Options’
*   Click ‘Windows Startup Settings’
*   Click Restart.
*   When your computer restarts, select ‘Disable driver signature enforcement‘ from the list.

To _permanently_ disable driver signing (recommended, but has some minor security implications):

*   Go to the metro start screen
*   Type in “cmd”
*   Right click “Command Prompt” and select “Run as Administrator” from the buttons on the bottom of your screen
*   Type/paste in the following commands: bcdedit -set loadoptions DISABLE_INTEGRITY_CHECKS bcdedit -set TESTSIGNING ON
*   Reboot!

#### Windows 7, Vista, and XP

Installing the Drivers for the Arduino Uno (from Arduino.cc)

*   Plug in your board and wait for Windows to begin it’s driver installation process
*   After a few moments, the process will fail, despite its best efforts
*   Click on the Start Menu, and open up the Control Panel
*   While in the Control Panel, navigate to System and Security. Next, click on System
*   Once the System window is up, open the Device Manager
*   Look under Ports (COM & LPT). You should see an open port named “Arduino UNO (COMxx)”. If there is no COM & LPT section, look under ‘Other Devices’ for ‘Unknown Device’

[![alt text](img/windows_driver_1.png)](img/windows_driver_1.png)

*   Right click on the “Arduino UNO (COMxx)” or “Unknown Device” port and choose the “Update Driver Software” option
*   Next, choose the “Browse my computer for Driver software” option

[![alt text](img/windows_driver_2.png)](img/windows_driver_2.png)

*   Finally, navigate to and select the Uno’s driver file, named “ArduinoUNO.inf”, located in the “Drivers” folder of the Arduino Software download (not the “FTDI USB Drivers” sub-directory). If you cannot see the .inf file, it is probably just hidden. You can select the ‘drivers’ folder with the ‘search sub-folders’ option selected instead.
*   Windows will finish up the driver installation from there

*This documentaion is proudly based on [Sparkfun Arduino on Windows](https://learn.sparkfun.com/tutorials/installing-arduino-ide/windows) tutorial - CC BY-NC-SA 3.0.*

### Which LiPo batteries to use?

The battery that we are providing is 3.7v and 2000mAh

### Which solar panels to use?

The solar panel it should fulfil the specification of a voltage bigger than 8v and less than 15v, 12v is the recommended voltage, and a minimum of 500mA.

### What is the spec (battery type) for the button-cell for the RTC?

The RTC battery is a CR1220

### Why is 50dB the microphone lowest value?

Because the actual sensor is limited by the curve boundings from 50dB to 103dB

### Browsers compatibility

The SmartCitizen platform is built using the latest Web technologies (such as HTML5, SVG and CSS3). These languages serve as a foundation for today’s websites and web applications. 

To enjoy Smart Citizen, we recommend you to use:

Google Chrome 25+
Firefox Mozilla 20+

### What are the LEDs for, and what does the LED blinking mean?

There are 5 LEDs, they are all on the base half of the SCK.  They can be understood in three groups:

 - LED2 and LED1 - These are the two yellow (or orange) LEDs in the lower center-letf of the board.  You will only see these lit when your USB cable is connected to the SCK and you are configuring or otherwise interacting with the SCK.  LED2 is the "RX USB" and will be lit when the SCK is receiving information via the USB connection. LED1 is the "TX USB" and will be lit when the SCK is sending information via the USB connection.   

 - LED4 and LED3 - These are the two blue LEDs in the lower center of the board.  You will see these blink often. LED3 is the "WiFi Association" and LED4 is the "WiFi Connection." The blue LEDs will blink each time the SCK posts new data wirelessly. This is normal behavior and is expected, but it only happens in bursts (then there will be no blue LED lit for about 30-40 seconds). If your blue LEDs are blinking back and forth non-stop, this means your SCK has lost its WiFi connection. Check to make sure your router is still on, and tht you're still in range of it.

 - LED5 - This is the green LED in the upper left corner.  It will be lit when the SCK is turned on and has power.

Troubleshooting
====

### Add an SSID with two words

If your SSID has more than one word yo have to fill any space with the dollar ($) character.

### Serial port already in use

This happens when one application is already using the serial port. For example, if you have the Arduino IDE serial monitor opened and you're trying to configure your SCK through the web browser. You have yo close the serial monitor first.

### No port available

This message will appear when you have uploaded the wrong firmware version to your SCK.

### Unable to connect to the Board

This happens when one application is already using the serial port. For example, if you have the Arduino IDE serial monitor opened and you're trying to configure your SCK through the web browser. You have yo close the serial monitor first.

### Unable to connect to the Internet

If you're getting the message "Error in connection" when you run the SCK firmware this may be due:

- Your router works with a protocol different than 802.11AG
- You have set wrong SSID name and/or password 
- Your network has an encryption different than OPEN, WEP, WPA1, WPA2 OR WEP64
- Your firewall is blocking the mac address of your SCK
- Your internet connection is not stable

### No data received yet

This message appears the first time you register your kit, is due to cache issues. This issue normally is fixed after a few hours, in any case we are working to improve this issue.

### Port is not appearing on the drop down

This may be due:

- The SCK is turned off.
- The USB cable you're using has wired only power cable and not the data cables.
- The bootloader is corrupted.

### Firmware update problem

If you're having problems updating the firmware you can try one of these two options:

- Update the latest firmware through the web browser configurator.
- Update the latest firmware throught Arduino IDE.

If you're still having problems it's may be due to a hardware or software issue, contact us at <a href="mailto:support@smartcitizen.me">support@smartcitizen.me</a>.

#### No MAC address registered

If you're getting this message, the may be due:

- Configuration process is not finished correctly.
- The WIFI module of your SCK is corrupted, so MAC address is not accesible. To repair your wifi module refer to this <a href="" target="_blank">tutorial</a>.

### Collapsed USB port

First batches of SCK version 1.1 came with this issue. We have a tutorial you can follow to repair it or contact us at <a href="mailto:support@smartcitizen.me" target="_blank">support@smartcitizen.me</a>.

### Broken LiPo battery wire

Depending on the conditions, the battery wires can suffer until its break. We encourage you to read this <a href="https://www.sparkfun.com/tutorials/241" target="_blank">Battery Common Care Techniques</a> in order to preserve your battery.

### Non-Stop Blue LED Blinking

If your blue LEDs are blinking back and forth non-stop, this means your SCK has lost its WiFi connection. Check to make sure your router is still on, and that you're still in range.
