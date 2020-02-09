Using the Shell
==========

!!! warning
    This guide is a work in progress!


The SCK (from V2.0 onwards) has an integrated command shell over USB to manage all the kits functionalities for advanced users. In this guide, we will cover how to access to this functionality in different platforms, and some examples.

## What is it?

We could define the `shell` as a text-based interface to access almost any SCK functionality. In terms of hardware, it relies on the [serial communication](https://en.wikipedia.org/wiki/Serial_communication) between the SCK and your computer, so any **decent** USB cable connected between them will do.

## How to access it?

Software-wise, different platforms will have different interfaces. The easiest and most reliable for all of them would be through the [Arduino IDE](https://www.arduino.cc/en/Main/Software).

!!! example "Using the Arduino IDE"
    - Launch the _Arduino IDE_ and select the port under `Tools > Port >`:
    
    ![](https://i.imgur.com/XEZXoyy.png)

    - Launch the `Serial Monitor` under `Tools > Serial Monitor`. Make sure that the dropdowns in the bottom are set as in the image below (`Carriage return` and `115200 baud`)

    - Type in `help` to get started.

    ![](https://i.imgur.com/iSONfFB.png)

More advanced users would probably rather use a more _rugged_ interface. In this case, you could use `screen` in your terminal of choice:

```
> ls /dev/cu | grep usb
cu.usbmodem1411
tty.usbmodem1411
> screen /dev/cu.usmodem1411
SCK >
...
```

If you already installed [platformio](https://platformio.org/) to [edit the firmware](/Guides/Edit%20the%20Firmware/) you can use it here, too

```
> pio device monitor
SCK >
...
```

!!! warning "Be patient!"
    The port will take a little time to appear in your list of devices. Normally the LED of your SCK will be **static white** during that period.

## Some examples!

The `help` command outputs a quite intuitive explanation of all the commands:

```
SCK > help
reset:       Resets the SCK
version:     Shows versions and Hardware ID
rcause:      Show last reset cause (debug)
outlevel:    Shows/sets outlevel [0:silent, 1:normal, 2:verbose]
help:        Duhhhh!!
pinmux:      Shows SAMD pin mapping status
sensor:      Shows/sets enabled/disabled sensor [-enable or -disable sensor-name] or [-interval sensor-name interval(seconds)]
read:        Reads sensor [sensorName]
control:     Control sensor [sensorName] [command]
monitor:     Continously read sensor [-sd] [-notime] [-noms] [sensorName[,sensorNameN]]
saved:       Shows locally stored sensor readings [-details] [-publish]
free:        Shows the amount of free RAM memory
i2c:         Search the I2C bus for devices
charger:     Controls or shows charger configuration [-otg on/off] [-charge on/off]
config:      Shows/sets configuration [-defaults] [-mode sdcard/network] [-pubint seconds] [-readint seconds] [-wifi "ssid" ["pass"]] [-token token]
esp:         Controls or shows info from ESP [-on -off -sleep -wake -reboot -flash]
netinfo:     Shows network information
time:        Shows/sets time [epoch time] [-sync]
state:       Shows state flags
hello:       Sends MQTT hello to platform
debug:       Toggle debug messages [-sdcard] [-espcom] [-list]
shell:       Shows or sets shell mode [-on] [-off]
mqtt:        Publish custom mqtt message ('topic' 'message')
```

!!! info "Pro tip"
    The SCK outputs  a lot of information via serial. This can be sometimes confusing while typing commands. You can silent it a bit with this command:

    ```
    SCK > shell -on
    Shell mode: on
    ```

    This will turn your LED static yellow, and no output except responses to your commands will be given. 

    Remember to turn it off after you are done experimenting!

    ```
    SCK > shell -off
    Shell mode: off
    ```

### Set the recording configuration

If you want to change your recording mode to, for instance, `sdcard` mode, you could do so by typing:

```
SCK > config -mode sdcard
```

To set it up in `network` mode:

```
SCK > config -mode network -wifi "SSID" "PASSWORD" -token 123456
```

!!! warning
    Note that the token is not between quotes since it's always 6 digits

To modify your wifi:

```
SCK > config -wifi "NEWSSID" "NEWPASSWORD"
```

You can check your current configuration by typing `config`:

```
SCK > config
Mode: sdcard
Publish interval: 60
Reading interval: 60
Wifi credentials: not configured
Token: not configured
Mac address:  11:22:33:44:55:66
```

### Get version data

Check your **hardware and firmware version** data with the command `version`:

```
SCK > version
Hardware Version: 2.1
SAM Hardware ID: 5934C4B550515157382E3120FF151210
SAM version: 0.9.1-30e1776
SAM build date: 2019-05-07T02:45:29Z
ESP MAC address: 86:0D:8E:A7:7F:CC
ESP version: not synced
ESP build date: not synced
```

### List/modify the active sensors

By typing in `sensor`, a **list of enabled and supported sensors** is displayed:

```
SCK > sensor

Disabled
----------
PM board Dallas Temperature
[...]

Enabled
----------
Temperature (60 sec)
Humidity (60 sec)
Battery (60 sec)
Light (60 sec)
Noise dBA (60 sec)
Barometric pressure (60 sec)
VOC Gas CCS811 (60 sec)
eCO2 Gas CCS811 (60 sec)
PM 1.0 (60 sec)
PM 2.5 (60 sec)
PM 10.0 (60 sec)
```

To **disable** one sensor, you can type in part of the sensor name:

```
SCK > sensor -disable Noise
Disabling Noise dBA
Saved configuration on eeprom!!
```

To **enable** it, if it's present:

```
SCK > sensor -enable Noise
Enabling Noise dBA
Saved configuration on eeprom!!
```

!!! warning "Only if available!"
    If the sensor you are trying to connect is not recognised, the kit will complain:

    ```
    SCK > sensor -enable atlas
    Failed enabling Atlas Temperature
    ```

### Read/Monitor some sensors

If one sensor is enabled, you can `read` it (once) or `monitor` it (as fast as the SCK can):

```
SCK > read Noise
Noise dBA: 53.85 dBA
```

To monitor **one sensor**:

```
SCK > monitor light
Time    Miliseconds     Light
2019-07-10T17:58:07Z    6       137
2019-07-10T17:58:07Z    98      137
2019-07-10T17:58:07Z    98      136
2019-07-10T17:58:07Z    98      137
2019-07-10T17:58:07Z    108     137
2019-07-10T17:58:07Z    98      137
2019-07-10T17:58:07Z    98      137
2019-07-10T17:58:07Z    108     137
2019-07-10T17:58:07Z    98      137
2019-07-10T17:58:08Z    98      137
2019-07-10T17:58:08Z    108     137
2019-07-10T17:58:08Z    98      136
...
```

Or all of them, with no arguments:

```
SCK > monitor
Time    Miliseconds     Battery Light   Temperature     Humidity        Noise dBA       Barometric pressure     VOC Gas CCS811  eCO2 Gas CCS811 PM 1.0  PM 2.5  PM 10.0
2019-07-11T09:13:04Z    5       37      137     28.75   57.72   1.5    101.29  1.00    408.00  1.5    1.5    1.5
2019-07-11T09:13:07Z    3195    37      138     28.78   57.65   1.5    101.30  1.00    408.00  1.5    1.5    1.5
2019-07-11T09:13:08Z    694     37      136     28.77   57.62   1.5    101.29  1.00    408.00  1.5    1.5    1.5
```

If you don't need to output the `miliseconds` column (the time since last reading) or the `timestamp`, you can do so by:

```
SCK > monitor -noms light
Time    Light
2019-07-10T17:58:58Z    136
2019-07-10T17:58:58Z    136
2019-07-10T17:58:58Z    137
2019-07-10T17:58:58Z    137
2019-07-10T17:58:59Z    136
...
```

```
SCK > monitor -notime light
Miliseconds     Light
6       137
98      137
98      137
99      137
108     137
...
```

!!! warning 
    If your kit has no time configured (the LED should be flashing), the output would look like:

    ```
    SCK > monitor Noise
    Time    Miliseconds     Noise dBA
    0       1       52.83
    0       187     50.36
    0       187     52.05
    0       187     51.95
    0       187     48.28
    0       187     48.72
    0       187     50.81
    ...
    ```

Something cool to do with the `monitor`, is to log the sensor output into a file for later analysis. For instance, in your terminal you could do:

```
> echo "monitor pm light" > /dev/cu.usbmodem1411 && screen -L /dev/cu.usbmodem1411
```

Then, if we check the contents of the file (normally something like `screenlog.X`:

```
monitor light
Time    Miliseconds     Light
2019-07-11T09:10:05Z    6       141
2019-07-11T09:10:05Z    98      141
2019-07-11T09:10:05Z    99      141
2019-07-11T09:10:05Z    98      141
2019-07-11T09:10:05Z    108     141
2019-07-11T09:10:05Z    98      141
2019-07-11T09:10:05Z    98      141
2019-07-11T09:10:05Z    98      141
2019-07-11T09:10:06Z    98      141
2019-07-11T09:10:06Z    98      141
2019-07-11T09:10:06Z    108     141
2019-07-11T09:10:06Z    98      141
2019-07-11T09:10:06Z    98      141
...
```

This can be useful in case you want to log data as fast as possible, with little delay between readings (~100ms).    

## Advanced (but cool) example!

!!! example "Making most of the digital microphone"
    - The digital microphone in your SCK uses an FFT algorithm to calculate the final sound pressure level (SPL) in different scales (A, C, Z). The FFT spectrum is also available for user analysis. Let's have a look!

    - First, enable it with:

    ```
    SCK > sensor -enable fft
    Enabling Noise FFT
    ```

    - Then, monitor and log it in a file with:

    ```
    echo "monitor fft" > /dev/cu.usbmodem1411 && screen -L /dev/cu.usbmodem1411
    ```

    - In this file, we will have something like:

    ```
    12
    15
    19
    20
    0
    ...
    12
    23
    2019-07-11T09:30:01Z    5   null
    ...
    ```

    - The values between the dates are the actual FFT spectrum. We will now clean the lines with the dates and then plot the data. For this, we will use a `python` code to make things easier. You can download the code [here](/assets/examples/spectrum_example.py).

    - If we run this code in `python3` in the same folder where the screenlog from before is:

    ```
    > python spectrum_example.py
    ```

    We will have two outputs: a `csv` file with the spectrums in rows, and a png image that looks like this!

    ![](https://i.imgur.com/KZfFDam.png)

    You can see that we were playing with a [tone generator](http://onlinetonegenerator.com/) to make some high pitch noises at 10kHz and 20kHz. 


