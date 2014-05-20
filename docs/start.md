Getting Started
=====

### Adding a Smart Citizen Kit

![Smart Citizen kit 1.1](img/sck_1.1_3.jpg)

Thanks! The Smart Citizen Team wants to thank you for being here, for purchasing a kit, joining the platform taking part on this adventure.

### Manual set up: The Serial Way 

SET UP YOUR KIT USING THE SERIAL COMMUNICATION

In this tutorial we will configure your Smart Citizen Kit (SCK) by using the Serial communication. We will register your Wi-Fi settings into the SCK and save the SCK’s MAC address in our server.
 
The SCK, like most Arduino chips, has the ability to communicate through serial communication (when plugged with the USB cable). The SCK uses the WiFly module to communicate with your Wi-Fi router. Through serial, we will send the commands directly with this module to set your Wi-Fi settings and extract the MAC address used by our server to verify your identity.
 
This tutorial works for both SCK v1.0 (from the Goteo crowdfunding campaign) and SCK v1.1 (from the KickStarter crowdfunding campaign), independently from the firmware version.
 
This tutorial have been tested with Arduino 1.0.5. We strongly recommend not to use the Beta version of Arduino IDE as we encountered issues with drivers and serial communications.

Configure Wifi Setting

- Open Arduino IDE
- Connect your SCK via USB
- Choose the right USB port (generally the last one)
- Select the right board: Leonardo for SCK v1.0 (Goteo) or LilyPad for SCK v1.1 (Kickstarter)
- Open the serial monitor in the Arduino IDE (button at the top-right of the main window)
- Set the options to "115200 baud" and “No line return” (drop-down menu at the bottom-right of the monitor window)
- Wake up the module and activate the Wi-Fi command mode:
*$$$*
- Change to “Carriage return” option (drop-down menu at the bottom-right of the monitor window)
- Add a new SSID to memory by typing :
*set wlan ssid XXX*
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
- Copy / Save the answer for further use
- Exit and go back to the normal operational mode
*exit*
 
*replace XXX with your value, filling any space with the dollar character ( $ ).

Register your kit online

- Go to the configuration page of your kit: http://smartcitizen.me/devices/configure/XXX (do not forget to replace XXX with your kit's ID)
- In the MAC address text input, paste the MAC address given by the command get mac. It should be something like: 00:06:66:21:17:33
- Click Register the kit
 
You are now done with the manual configuration of your SCK. Wait for a few minutes to see your data coming on the server and being displayed on the web page. You can also check that everything is ok by looking at the Arduino serial monitor. Debug messages coming from your SCK should look like this :


If you want to explore further options with the WiFly module, a full list of commands is available at:
https://github.com/fablabbcn/Smart-Citizen-Kit/blob/master/sck-commands.md
If you encounter any issue, please share your problem on the forum :
http://forum.smartcitizen.me/

### Manual set up: The Compilation Way
### Attaching the solar panel
### Sensor calibration
### Connecting from an iPhone


The Sck Command Line
=====
### Basic SCK commands
### Special SCK commands
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
