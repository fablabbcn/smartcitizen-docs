SCK Command Line
================

The Smart Smart Citizen Kit can be managed over a basic serial protocol. You just need the **Arduino IDE Serial Monitor** or any other **Serial Utility** like **Screen** in order to use it.

**How to use it**

- Connect to your kit using any serial utility, any baud-rate should work but 115200 is recommendable.
- Send the starting commands.
- Notice all the commands except the starting command($$$) require a carriage return at the end: CR or \r. If you are using the Arduino IDE is enough if you change to “Carriage return” option (drop-down menu at the bottom-right of the monitor window).
- Call any command you want, change XXX with the corresponding value, filling any space with the dollar ($) character.

### SCK Wifly commands

- `$$$` (Wake up the module and activate the Wi-Fi)
- `set wlan ssid XXX` (Add a new SSID to memory9)
- `set wlan phrase XXX` (Add a new phrase to memory)
- `set wlan key XXX` (Add a new key to memory)
- `set wlan auth XXX` (Add an authentication method into memory)
- `set wlan ext_antenna XXX` (Add an antenna type into memory)
- `exit` (Go back to normal operational mode)

If you want to know more about wifly commands look at the [WiFly Command Reference](http://ww1.microchip.com/downloads/en/DeviceDoc/50002230A.pdf)

### SCK commands

- `###` (Wake up the module and enter SCK commands mode)
- `get mac` (Get the MAC address of the kit)
- `get time update` (Retrieve the sensor update interval)
- `set time update XXX` (Update the sensor update interval, *10-3600 sec*)
- `get number updates` (Retrieve the max number of bulk updates)
- `set number updates XXX` (Update the max number of bulk updates, *1-20 updates*)
- `get apikey` (Retrieve the kit APIKEY)
- `set apikey XXX` (Update the kit APIKEY)
- `get wlan ssid` (Retrieve the SSID saved on the kit)
- `get wlan phrase` (Retrieve the phrase and KEY saved on the kit)
- `get wlan auth` (Retrieve the authentication method saved on the kit)
- `get wlan ext_antenna` (Retrieve the antenna type saved on the kit)
- `clear nets` (Remove all saved Wi-Fi configuration information)
- `clear memory` (Reset to defaults all configuration information)
- `get all` (Retrieve all settings saved on the kit in a single line: *|version|MAC|ssid,phrase,auth,ext_antenna|hardcodedNets|timeUpdate|numUpdate|*)
- `data` (Retrieves sensor readings stored in memory)
- `exit` (Goes back to normal operational mode)