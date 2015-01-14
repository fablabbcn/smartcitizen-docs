Getting Started
=====

### Adding a Smart Citizen Kit

![Smart Citizen kit 1.1](img/sck_1.1_3.jpg)

Thanks! The Smart Citizen Team wants to thank you for being here, for purchasing a kit, joining the platform taking part on this adventure.

### Manual set up: The Serial Way 

In this tutorial you will configure your Smart Citizen Kit (hereafter SCK) using serial communication. By using serial communication, you will register your Wi-Fi settings into the SCK and save the SCK’s MAC address in our server.
 
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
- Wake up the module and activate the Wi-Fi command mode:
*$$$*

- Change to “Carriage return” option (drop-down menu at the bottom-right of the monitor window)

- Add a new SSID to memory by typing:

*set wlan ssid XXX**

- Add a new phrase to memory (optional, password for WPA1 & WPA2):*

*set wlan phrase XXX**

- Add a new key to memory  (optional, password for WEP & WEP64):*

*set wlan key XXX*

- Add an authentication method into memory (replace XXX by “0” for Open,  “1” for WEP, “2” for WPA1, “4” for WPA2, “8” for WEP64):

*set wlan auth XXX*

- Add an antenna type into memory (replace XXX by “0” to use the internal antenna or “1” if you use an external antenna):

*set wlan ext_antenna XXX*

- Get the MAC address of the kit

*get mac*

- Copy/Save the answer for further use.

- Exit and go back to the normal operational mode

*exit*
 
*Note: You have to replace XXX with your value, filling any space with the dollar ($) character .


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

Open the file Smart-Citizen-Kit/sck_beta_v0_9/sck_beta_v0_9.ino

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
 
The easiest way would be to write "#define redes X" (where X is the number of WI-FI networks you are going to use),  add the name of your network in "RedX" and the corresponding password in "PassX". You could also choose the encryption mode that fits with your network's configuration (OPEN, WEP, WPA1, WPA2, WEP64) or the type of antenna you are using (*INT_ANT* for internal antenna (default) or *EXT_ANT* for external antenna).
 
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
### Sensor calibration
### Connecting from an iPhone


The Sck Command Line
=====
### Basic SCK commands

- $$$ Wake up the module and activate the Wi-Fi
- set wlan ssid XXX\r Add a new SSID to memory
- set wlan phrase XXX\r Add a new phrase to memory
- set wlan key XXX\r Add a new key to memmory
- set wlan auth XXX\r Add an authentication method into memory
- set wlan ext_antenna XXX\r Add an antenna type into memmory
- get mac\r Get the MAC address of the kit
- exit\r Go back to normal operational mode

### Special SCK commands

- get time update\r Retrieve the sensor update interval
- set time update XXX\r Update the sensor update interval
- get number updates\r Retrieve the max number of bulk updates allowed
- set number updates XXX\r Update the max number of bulk updates allowed
- get apikey\r Retrieve the kit APIKEY
- set apikey XXX\r Update the kit APIKEY
- get wlan ssid\r Retrieve the SSID saved on the kit
- get wlan phrase\r Retrieve the phrase and KEY saved on the kit
- get wlan auth\r Retrieve the authentication methods saved on the kit
- get wlan ext_antenna\r Retrieve the antenna types saved on the kit
- clear nets\r Remove all saved Wi-Fi configuration information
- exit\r Goes back to normal operational mode
- data\r Retrieves sensor readings stored in memory

### Basic WiFly commands

Hardware
=====
### Inside the SCK
### Enclosures
### Acrylic cases 


Software
====
### Inside the SC Platform



Faq
====
### How to store data in your own database?
### How to use the SD Card?
### Which LiPo batteries to use?
### Which solar panels to use?
### How to setup the SCK on Ubuntu?
### Actual accuracy of all the sensors? 
### What is the spec (battery type) for the button-cell for the RTC?
### Why is 50dB the microphone lowest value?
### How do I calibrate the sensors?


Troubleshooting
====
### Add an SSID with two words
### Serial port already in use
### No port available
### Unable to connect to the Board
### Unable to connect to the Internet
### No data received yet
### Error in connection
### Port is not appearing on the drop down
### Performed install but still no data
### Firmware update problem
### Sensors erratic behaviour
### No MAC address registered
### Collapsed USB port
### Broken LiPo battery wire




Apps
====
### iOS
### Android
