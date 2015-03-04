Getting Started
=====

### Adding a Smart Citizen Kit

![Smart Citizen kit 1.1](img/sck_1.1_3.jpg)

Welcome aboard! The Smart Citizen Team wants to thank you for being here, for purchasing a kit, and for joining the community taking part in this adventure.

To join the Smart Citizen family, we're going to walk you through the steps to add your Smart Citizen Kit to the platform. (we'll refer to the Smart Citizen Kit as the "SCK" for now on).

First, go to <a href="https://smartcitizen.me/" target="_blank">smartcitizen.me</a> in a web browser (please choose Firefox or CHROME). Click <a href="https://smartcitizen.me/users/add" target="_blank">REGISTER</a> in the upper right menu. Complete the required fields and click REGISTER button.

Required Fields:

- USERNAME - Pick any name you want as long as someone else isn't already using the it.

- EMAIL - Enter your email address.

- PASSWORD - Must be at least 6 characters.

- CITY - Enter the name of the city you're located (doesn't need to be the same as you SCK).

- COUNTRY - Enter your Country (doesn't need to be the same as you SCK).

Optional Fields:

 - WEBSITE - If you add a website, a link is added to your CITIZEN profile page (which can be viewed by the public).

 - FILE - This adds a custom avatar. Click "Choose File" then find the image you want to use.  The image will appear next to you profile information.

Once you’ve completed the required fields, click REGISTER.  Congratulations!! You've registered yourself and will be directed to your CITIZEN dashboard. (You can always return to your CITIZEN dashboard by clicking the LOG-IN button at the very top right of the <a href="https://smartcitizen.me/" target="_blank">smartcitizen.me</a> homepage)

Now, let's add your SCK! From you CITIZEN dashboard, click on ADD SMART CITIZEN KIT.  Complete each field: 

 - TITLE - Give your SCK a name.  This title will be associated with your SCK data.

 - ELEVATION - If you don't know it, a simple Google search should help you.  Knowing your SCK's elevation helps to understand the data it collects.

 - EXPOSURE - Choose INDOOR or OUTDOOR.  Again, this helps to understand the data.

 - KIT VERSION - Most likely you have a 1.1 SCK. The only way you would be using a 1.0 SCK is if you got it from the original GOTEO crowdfunding campaign, or if you got it from someone else that got it from GOTEO. 

 - GEOLOCATION - There are two ways to complete this section: AUTO COMPLETE ON or AUTO COMPLETE OFF.  AUTO COMPLETE ON lets you type in the name of your city, then lets you choose it from a drop-down list (This will give you an approximate latitude and longitude).  AUTO COMPLETE OFF will put a blue flag on the map to the left of the form.  You then drag the flag to the SCK's location on the map.  By zooming in you can pin-point the exact latitude and longitude of your SCK (the closer you get, the better the data will be).

 - DESCRIPTION - This is an optional field that helps inform others of your SCK's unique set-up.  Information like "in my garage" or "im my woodshop" could help others understand why some of your data looks the way it does.

Click on the SAVE SENSOR button. Congratulations!! You've added your first SCK and will be directed to your SENSOR dashboard. Your SCK now has an official device ID (it can bee seen in your browser's address bar, it is the number at the end of the url). 

Good job, both you and your SCK are registered. Now it's time to configure and upload the firmware that will be the brains of your SCK.

If this is the first time registering a SCK, you should install the <a href="https://codebender.cc/static/plugin" target="_blank">Codebender</a> plugin extention for your browser (Codebender lets you configure the SCK from the Smart Citizen website rather than hard coding everything).  Also, you'll need to download the <a href="http://arduino.cc/en/Main/Software" target="_blank">Arduino</a> drivers (if you haven't already done this for something else you've built).

OK, time to unpack your SCK. Connect the USB cable to your SCK and your computer. Turn on your SCK at the switch in the upper left corner of the base board.  Now, go back to the Smart Citizen website and to your SENSOR dashboard. Click on the CONFIGURE button.

If you've installed the Codebender extention and the Arduino drivers, you'll be able to click on START PROCESS button. Wait a few seconds while Codebender plugin does its job. 

When it has finished you’ll see a form to setup your wifi connection and data update interval parameters. Complete the fields with your SSID (this is your wifi network's name), ENCRYPTION MODE and PASSWORD PHRASE. Then, click on SYNC button. Wait a few seconds (your SCK is learning your wifi credentials).

When the sync has finished, you should see something similar to "00:06:66:21:16:E4" in the MAC ADDRESS field. Click on the REGISTER THE KIT button. Now reset your SCK in order the changes take effect.

Wow! That was so easy!!

Back to your SENSOR dashboard. Wait a few minutes and reload the page. See if some data has been uploaded to the Smart Citizen database. To check this take a look at the field "Last Update" (If everything worked, you should see something like "Last Update: 31 seconds ago").  After the Smart Citizen database has had a few days to gather your data, you'll be able to check it from <a href="https://smartcitizen.me/" target="_blank">smartcitizen.me</a>. 

### Manual set up: The Serial Way 

In this tutorial you will configure your SCK using serial communication. By using serial communication, you will register your Wi-Fi settings into the SCK and save the SCK’s MAC address in our server.
 
The SCK, like most Arduino chips, has the ability to communicate through serial protocol (when plugged with a proper USB cable). The SCK uses the WiFly module to communicate with your Wi-Fi router. Anyway, through serial communication you will be able to send the commands directly with this module to set your Wi-Fi settings and extract the MAC address used by our server to verify your identity.
 
Note that this tutorial works for both SCK v1.0 (from the Goteo crowdfunding campaign) and SCK v1.1 (from the KickStarter crowdfunding campaign), independently of the firmware version used.
 
All the steps in this tutorial have been tested with Arduino 1.0.5. We strongly recommend not to use the Beta version of Arduino IDE as we encountered issues with drivers and serial communication.

STEP 1: Configuring the Wi-Fi settings

- Open Arduino IDE.
- Connect your SCK via USB.
- From the Tools > Board menu, choose the right USB port (generally the last one).
- From the Tools > Serial port menu, select the right board. This is Leonardo for SCK v1.0 (Goteo) or LilyPad Arduino USB for SCK v1.1 (Kickstarter).
- Open the serial monitor window in the Arduino IDE (button at the top-right of the main window).
- Set the options to "115200 baud" and “No line return” (drop-down menu at the bottom-right of the monitor window).
- Wake up the module and activate the Wi-Fi command mode by typing in the serial monitor:

*$$$*

- Change to “Carriage return” option (drop-down menu at the bottom-right of the monitor window)

- Add a new SSID to memory by typing:

*set wlan ssid XXX*

Note: You have to replace XXX with your ssid name, filling any space with the dollar ($) character.

- Add a new phrase to memory (optional, password for WPA1 & WPA2):

*set wlan phrase XXX*

Note: You have to replace XXX with your phrase, filling any space with the dollar ($) character.

- Add a new key to memory  (optional, password for WEP & WEP64):

*set wlan key XXX*

- Add an authentication method into memory (replace XXX by “0” for Open,  “1” for WEP, “2” for WPA1, “4” for WPA2, “8” for WEP64):

*set wlan auth XXX*

- Add an antenna type into memory (replace XXX by “0” to use the internal antenna or “1” if you use an external antenna):

*set wlan ext_antenna XXX*

- Get the MAC address of the kit by typing:

*get mac*

- Copy/Save the answer for further use.

- Exit and go back to the normal operational mode by typing:

*exit*
 

STEP 2: Registering your kit online

- Go to the configuration page of your kit: http://smartcitizen.me/devices/configure/XXX (do not forget to replace XXX with your kit's ID)

- In the MAC address text input, paste the MAC address given by the command *get mac*. It should be something like: *00:06:66:21:17:33*

- Click on "Register the kit"
 
You are now done with the manual configuration of your SCK. Wait for a few minutes to see your data coming on the server and being displayed on the web page. You can also check that everything is ok by looking at the Arduino serial monitor. Debug messages coming from your SCK should look like this:


If you want to explore further options with the WiFly module, a full list of commands is available at:
https://github.com/fablabbcn/Smart-Citizen-Kit/blob/master/sck-commands.md

If you encounter any issue, please share your problem on the forum:
http://forum.smartcitizen.me/



### Manual set up: The Compilation Way

This tutorial will drive you toward a manual way of setting your Smart Citizen Kit (SCK) by editing directly the source code. As the code is Open Source, one way of setting the Wi-Fi of your SCK is to download the latest firmware, edit some lines of code, recompile it and upload it to the kit. 
 
One advantage of this system is that it gives you the opportunity to register multiple Wi-Fi networks at the same time. This is useful if your SCK is traveling from one location to another where the Wi-Fi credentials are known. The downside of this method is that you can not extract the MAC address of your kit, therefore making it this way is not suitable for the first setup of your kit. Please, refer to other tutorials available.
 

#### STEP 1: Getting the Firmware

You can download the latest firmware on our Github : 
https://github.com/fablabbcn/Smart-Citizen-Kit/releases
As you may know, the hardware and software are based on the arduino project. we will use the Arduino IDE to edit the firmware and upload it to the kit. This tutorial have been tested with arduino 1.0.5. Get the Arduino IDE at http://arduino.cc/en/Main/Software.

Open the file Smart-Citizen-Kit/sck_beta_v0_8_5/sck_beta_v0_X_X.ino

#### STEP 2: Editing the code

If you want to set the network configuration manually, you should go to the SCKBase tab and modify the lines you see below:
 
```Arduino
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
 
The easiest way would be to write "#define networks X" (where X is the number of WI-FI networks you are going to use),  add the name of your network in "RedX" and the corresponding password in "PassX". You could also choose the encryption mode that fits with your network's configuration (OPEN, WEP, WPA1, WPA2, WEP64) or the type of antenna you are using (*INT_ANT* for internal antenna (default) or *EXT_ANT* for external antenna).
 
If you register only one wifi credential, you should obtain something like:
 
 ```Arduino 
#define networks 1
#if (networks > 0)
char* mySSID[networks]      = { 
  "MyWifiSSID"    };
char* myPassword[networks]  = { 
  "MyPassword"    };
char* wifiEncript[networks] = { 
  WPA2            };
char* antennaExt[networks]  = { 
  INT_ANT         }; //EXT_ANT
#endif
 ```
 
#### STEP 3: Registering the kit in the database

After you've uploaded your own script, don't forget to register the kit in our database and save there your kit mac address. To find this mac address, you can use the serial command "get mac". by following the tutorial Manual Setup, the Serial way. 

Alternatively, have a look at the wifi module on the board and read the serial number  under the bar code (something like "131G0006662116E4" on kit v1.0 or "0006662116E4" on kit v.1.1). 

The mac adress is the last 12 digit of this serial, separated by colon every two number. You should obtain something similar to "00:06:66:21:16:E4".

In both cases, you have to pass by the configuration page of your kit, and fill the mac address input field. Then press the register your kit button.
 
Wait for some minutes and you should see data comming to the website !
 
If you have any question or are looking for more information, have a look at our forum :
http://forum.smartcitizen.me

### Attaching the solar panel

![Solar Panel](img/v1.0/main_board_solar_panel.jpg)
![Solar Panel](img/main_board_solar_panel.jpg)

The solar panel it should fulfil the specification of a voltage bigger than 8v and less than 15v, 12v is the recommended voltage, and a minimum of 500mA.

In order to attach the solar panel you have to solder the cables of the solar panel to the pads marked in the next image for version 1.0 of the SCK. For version 1.1 you have to connect the cables to the connector marked in the next image. 

In both versions, yo have to attach the plus of solar panel to the plus pad of the SCK, and the minus of the solar panel to the minus pad of the SCK.

### Sensor calibration

### Connecting from an iPhone


The Sck Command Line
=====

The Smart Citizen Kit can be managed over a basic serial protocol. You just need the Arduino IDE Serial Monitor or any other Serial Utility like Screen in order to use it.

**How to use it**

- Connect to your kit using any serial utility, any baud-rate should work but 115200 is recommendable.
- Send the starting commands.
- Notice all the commands except the starting command($$$) require a carriage return at the end: CR or \r. If you are using the Arduino IDE is enough if you change to “Carriage return” option (drop-down menu at the bottom-right of the monitor window).
- Call any command you want, change XXX with the corresponding value, filling any space with the dollar ($) character.

### Basic SCK commands

- **$$$** (Wake up the module and activate the Wi-Fi)
- **set wlan ssid XXX** (Add a new SSID to memory9)
- **set wlan phrase XXX** (Add a new phrase to memory)
- **set wlan key XXX** (Add a new key to memmory)
- **set wlan auth XXX** (Add an authentication method into memory)
- **set wlan ext_antenna XXX** (Add an antenna type into memmory)
- **get mac** (Get the MAC address of the kit)
- **exit** (Go back to normal operational mode)

### Special SCK commands

- **get time update** (Retrieve the sensor update interval)
- **set time update XXX** (Update the sensor update interval)
- **get number updates** (Retrieve the max number of bulk updates allowed)
- **set number updates XXX** (Update the max number of bulk updates allowed)
- **get apikey** (Retrieve the kit APIKEY)
- **set apikey XXX** (Update the kit APIKEY)
- **get wlan ssid** (Retrieve the SSID saved on the kit)
- **get wlan phrase** (Retrieve the phrase and KEY saved on the kit)
- **get wlan auth** (Retrieve the authentication methods saved on the kit)
- **get wlan ext_antenna** (Retrieve the antenna types saved on the kit)
- **clear nets** (Remove all saved Wi-Fi configuration information)
- **exit** (Goes back to normal operational mode)
- **data** (Retrieves sensor readings stored in memory)

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

**CPU** 

Both versions of the SCK (1.0 and 1.1) are using the same CPU, ATMEGA32U4(Arduino Leonardo). With the difference that the 1.0 works at 5V and 16MHZ and the 1.1 works at 3.3V and 8MHZ. In the 1.1 version we’ve improved the power consumption. 

This CPU has native USB and an UART TTL port allowing us to connect directly with the WIFI module.

<a href="http://www.atmel.com/images/doc7766.pdf" target="_blank">ATMEGA32U4 datasheet</a>

![usb connectors](img/usb_connectors.png)

**USB CONNECTOR**

The 1.0 version uses a Mini USB connector and 1.1 version uses a Micro USB.

![wifly module](img/v1.0/main_board_wifly.jpg)
![wifly module](img/main_board_wifly.jpg)

**WIFI MODULE**

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

**BATTERY POWERING**

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

**BATTERY CHARGING**

For charging the battery there are two ways, USB or solar panel. To carry out the charging we are using MCP73831 IC. 

For the solar panel way, in 1.0 version the solar panel have to be 12v and 500mA. In 1.1 version, the solar panel can be more versatile in terms of amperage. 

<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/20001984g.pdf" target="_blank">MCP73831 datasheet</a>

![LM2674](img/v1.0/main_board_LM2674.jpg)
![LM2674](img/main_board_LM2674.jpg)

**SOLAR PANEL CHARGING**

As the solar panel produces 12v, depending on the sunlight conditions, we have to reduce the voltage to 5v to feed up the Vin of the MCP73831 charger IC. 

To carry out this task we are using the LM2674 IC, a very efficient IC, with a rate of 91% of performance.

<a href="http://www.ti.com/lit/ds/symlink/lm2674.pdf" target="_blank">LM2674 datasheet</a>

![DS1307](img/v1.0/main_board_DS1307.jpg)
![DS1339Y-3+](img/main_board_DS1339Y-3+.jpg)

**RTC (REAL TIME CLOCK)**

The SCK has a real time clock for when the kit is offline. For this task we chose the DS1307 IC for the 1.0 version and the DS1339Y-3+ IC for the 1.1 version. Different IC due to the different voltages, 5V for the 1.0 version and 3.3V for the 1.1 version.

<a href="http://datasheets.maximintegrated.com/en/ds/DS1307.pdf" target="_blank">DS1307 datasheet</a><br>
<a href="http://datasheets.maximintegrated.com/en/ds/DS1339-DS1339U.pdf" target="_blank">DS1339Y-3+ datasheet</a>

![DM3CS](img/v1.0/main_board_DM3CS.jpg)
![DM3CS](img/main_board_DM3CS.jpg)

**SD CARD READER**

The SD card is used to store the data captured by the sensors when the kit is offline. Then, when the kit is online, the data will be uploaded to the platform. 

To hold the SD card we are using the DM3CS holder. The SD card is powered at 3.3V and communicates with the CPU through SPI protocol.

<a href="http://www.mouser.com/ds/2/185/e60900232-38395.pdf" target="_blank">DM3CS datasheet</a>

![24LC256](img/v1.0/main_board_24LC256.jpg)
![24LC256](img/main_board_24LC256.jpg)

**EEPROM MEMORY**

For the users that don’t have a SD card we’ve added an EEPROM memory to store the data when the SCK is offline.

We chose the 24LC256 IC that can store 32kBytes, it communicates with the CPU through I2C protocol.

<a href="http://ww1.microchip.com/downloads/en/DeviceDoc/20001203U.pdf" target="_blank">24LC256 datasheet</a>


**MAIN BOARD BASIC SENSORS**

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

**NO2 AND CO2 SENSORS**

To measure these two gases we chose <a href="http://www.e2v.com/" target="_blank">e2v</a> sensors. In particular, metal oxide sensors MICS5525 and MICS2710, for version 1.0. And MICS4514, for version 1.1, that contains both sensors in one.

Metal oxide sensors are based on oxide semiconductors. Their electrical conductivity is modulated due to the reaction between the semiconductor and the gases in the atmosphere.

<a href="http://www.e2v.com/shared/content/resources/File/sensors_datasheets/Metal_Oxide/mics-5525.pdf" target="_blank">MICS5525 datasheet</a><br>
<a href="http://www.cdiweb.com/datasheets/e2v/mics-2710.pdf" target="_blank">MICS2710 datasheet</a><br>
<a href="http://files.manylabs.org/datasheets/MICS-4514.pdf" target="_blank">MICS4514 datasheet</a>

![LDR](img/v1.0/sensor_board_LDR.jpg)
![H1730FVC](img/sensor_board_BH1730FVC.jpg)

**LIGHT SENSOR**

The light sensor is a basic element to know the light pollution. In version 1.0, was used a LDR(light-dependent resistor) whose voltage varies depending on the light conditions.

For version 1.1, was used a photodiode BH1730FVC. This sensor contains an I2C bus that gives us directly the amount of lux of ambient and infrared light.

<a href="http://www.farnell.com/datasheets/1813319.pdf" target="_blank">BH1730FVC datasheet</a>

![Noise Sensor](img/v1.0/sensor_board_noise_sensor.jpg)
![Noise Sensor](img/sensor_board_noise_sensor.jpg)

**NOISE SENSOR**

The noise sensor is based on an electret microphone. For the version 1.0, the audio signal is passed through an operational amplifier configured as band pass filter.

For the version 1.0, WM-61A was used for the microphone.

For the version 1.1, POM-3044P-R was used. The amplification step was modified adding a variable gain, allowing us to measure very low and very high signals.

<a href="http://industrial.panasonic.com/www-data/pdf/ABA5000/ABA5000CE22.pdf" target="_blank">WM-61A datasheet</a><br>
<a href="http://www.farnell.com/datasheets/40113.pdf" target="_blank">POM-3044P-R datasheet</a>

![RHT22 Sensor](img/v1.0/sensor_board_RHT22.jpg)
![SHT21 Sensor](img/sensor_board_SHT21.jpg)

**TEMPERATURE AND HUMIDITY SENSOR**

To measure temperature and humidity was used a module that integrates both sensors. 

For version 1.0 was used the RHT22, it has one wire digital interface.

For version 1.1 was used the SHT21, it has I2C protocol and a more fast response between measures than the RHT22.

<a href="https://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.pdf" target="_blank">RHT22 datasheet</a><br>
<a href="http://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/Humidity/Sensirion_Humidity_SHT21_Datasheet_V4.pdf" target="_blank">SHT21 datasheet</a>

![ADXL345](img/sensor_board_ADXL345.jpg)

**3 AXIS ACCELEROMETEER**

In version 1.0 was detected that some measures vary depending on the orientation the SCK. 

For this, in version 1.1, was added an accelerometer(ADXL345) to detect the position and to compensate the measures depending on the orientation of the SCK.

The ADXL345 has I2C protocol to interface with.

<a href="http://www.analog.com/static/imported-files/data_sheets/ADXL345.pdf" target="_blank">ADXL345 datasheet</a>

![I2C Bus](img/v1.0/sensor_board_i2c_bus.jpg)
![I2C Bus](img/sensor_board_i2c_bus.jpg)

**I2C EXPANSION BUS**

Due to the ease of the I2C protocol. We’ve included and I2C bus to provide to the community the opportunity of expanding the SCK.

### Enclosures

![Enclosure](img/case.jpg)

We have designed a laser cut cover for an acrylic material and a 3D-Printed enclosure to better safeguard the hardware, particularly for outdoor applications.

You can download the files through this links.

<a href="http://www.thingiverse.com/thing:262891" target="_blank">Smart Citizen Enclosure 1.0</a><br>
<a href="http://www.thingiverse.com/thing:236976" target="_blank">Smart Citizen Enclosure 1.1</a>

![Enclosure](img/new_case.jpg)

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

The Smart Citizen Kit is publishing by default the data as a PUT Http request, the sensor data is encoded as JSON.

Here you can see how a kit's request will look like.

``
curl -X PUT -H 'Host: data.smartcitizen.me' -H 'User-Agent: SmartCitizen' -H 'X-SmartCitizenMacADDR: 00:00:00:00:00:00' -H 'X-SmartCitizenVersion: 1.1-0.8.5-A' -H 'X-SmartCitizenData: [{"temp":"29090.6", "hum":"6815.74", "light":"30000", "bat":"786", "panel":"0", "co":"112500", "no2":"200000", "noise":"2", "nets":"10", "timestamp":"2013-10-28 1:34:26"}]' data.smartcitizen.me/add
``

Data for the temperature, humidity and noise is sent it in raw and then calibrated in our platform.

Here are the different paths you can take in order to built your own backend.

- Create a fork of the the <a href="https://github.com/fablabbcn/Smart-Citizen-Kit/tree/master" target="_blank">Smart Citizen Kit firmware</a> in order to send the data as your custom backend expect it.

- Create your own custom backend. We can share all the different modules of our backend in order for you to receive data as on the curl example above, calibrate it and store it. Contact us at <a href="mailto:support@smartcitizen.me">support@smartcitizen.me</a>.

- Keep using our backend but request our public API <a href="http://api.smartcitizen.me/" target="_blank">api.smartcitizen.me</a> and then fill your local Mysql with it.

### How to use the SD Card?

You have to use <a href="https://github.com/fablabbcn/Smart-Citizen-Kit/tree/master/sck_beta_v0_8_6_SDCARD" target="_blank">sck_beta_v0_8_6_SDCARD firmware</a> that is a version optimized for SD cards.

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
