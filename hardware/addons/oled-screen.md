<!-- Source: https://docs.smartcitizen.me/hardware/addons/oled-screen/ -->

# OLED Display

An experimental OLED Screen to visualise sensor values and plot data!

![](https://docs.smartcitizen.me/assets/images/oled-screen-feature.jpg){.banner-box}



Supported [screens](https://wiki.seeedstudio.com/Grove-OLED_Display_1.12inch/) are 128x128 and use the SH1107 controller, we have tested the code with displays labeled as v2.0 and v2.1. If the screen is connected to the _AUX_ grove connector on the SCK it will be autodetected on boot:

![](https://docs.smartcitizen.me/assets/images/oled-logo.jpg)

## Enable

To enable this screen, you need to compile the firmware with a `SCK_WITH_SENSOR_GROVE_OLED` flag. The easiest way is to use one of the environments that already include it in `platformio.ini`, in the `sam` directory: `sck21_air_oled`, `sck22_air_oled`, `sck23_air_oled` or `sck_water_oled`. For instance, for the `SCK 2.3`, the environment reads:

```
[env:sck23_air_oled]
extends = env:sck23_air
build_flags =
    ${env_common.build_flags}
    !sh ../tools/git-rev.sh -e sck23_air_oled
    -D SCK23_AIR
    -D SCK_WITH_SENSOR_GROVE_OLED
lib_deps =
    ${env:sck23_air.lib_deps}
    https://github.com/fablabbcn/U8g2_Arduino
```

!!! info "Custom configurations"
    If you are adding the screen to your own environment, add both the `-D SCK_WITH_SENSOR_GROVE_OLED` flag and the `U8g2_Arduino` library, as above. Check the guide on [enabling additional features](https://docs.smartcitizen.me/guides/firmware/enabling-additional-features.md) for more details.

## Features

### Info bar

![](https://docs.smartcitizen.me/assets/images/oled-infobar.jpg)

From left to right on the info bar we will find:

![](https://docs.smartcitizen.me/assets/images/oled-icons.png)

**Mode:** The [Operation mode](https://docs.smartcitizen.me/hardware/kit/features.md#operation-modes) in which our kit is now (_SETUP_, _WIFI_, _SD_ or _SHELL_). No icon, just text on this one.
**Wi-Fi:** This icon will appear when the kit is connected to the internet.
**SD card:** Present when an SD card is inserted and writable.
**Time synced:** Shown when the SCK internal clock has been synced.
**External power:** Shown when the USB cable that provides power to the kit is connected.
**Battery states:** Charging, full (75%-100%), half (25%-75%), empty (<25%). The battery level is also shown as a percentage. When the battery is disconnected, no icon or percentage are shown.

### Setup screen
When the SCK is in setup mode, it will display the name of the Wi-Fi Access point network and some simple instructions.

![](https://docs.smartcitizen.me/assets/images/oled-setup.jpg)

### Readings display

Enabled sensors will be shown by default in a three-second loop (except the battery, that's already on the info bar).

![](https://docs.smartcitizen.me/assets/images/oled-readings.jpg)

Using the [command shell](https://docs.smartcitizen.me/guides/getting-started/using-the-shell.md), you can manually add/remove sensors from the display loop with the command `sensor sensorName -oled` that will toggle the state of the selected sensor.

~~~
SCK > sensor temperature -oled
Temperature will not show on oled display
~~~
And check which sensors are displayed with the command `sensor`.

~~~
SCK > sensor
...
Temperature (60 sec)
Humidity (60 sec) - oled
Light (60 sec) - oled
Noise dBA (60 sec) - oled
...
~~~

### Error bar

Errors related to SD card, time sync, Wi-Fi, missing configuration or general network errors are shown in a pop-up at the bottom of the screen.

![](https://docs.smartcitizen.me/assets/images/oled-error.jpg)

### Monitor plot

You can plot one sensor in real time directly to the OLED screen, to use this feature you need to issue the command `monitor -oled sensorName` via the [command shell](https://docs.smartcitizen.me/guides/getting-started/using-the-shell.md). During the execution, the kit will stop all other tasks and try to send readings as fast as it can. Update speed depends on which sensor you are plotting.

~~~
SCK > monitor -oled light
~~~

![](https://docs.smartcitizen.me/assets/images/oled-plot.jpg)

### Debug log view

Debug output to OLED screen is supported, it has to be enabled via the [command shell](https://docs.smartcitizen.me/guides/getting-started/using-the-shell.md). You can toggle debug output with the command `debug -oled`. Everything that is normally printed on the shell will also be redirected to the OLED screen with a very small font!!

~~~
SCK > debug -oled
Oled display debug: true
~~~

## Known issues

* All this development has been done with a short (~5 cm) grove cable, when testing longer cables we have seen instabilities that prevent the display refresh or even hang the SCK kit. More tests with bus speed and related issues are needed.
* Using this display simultaneously with other external sensors on the auxiliary I2C bus may cause instabilities.

!!! danger "Using with GPS"
    Read this issue if you are using the screen with a GPS: https://github.com/fablabbcn/smartcitizen-kit-2x/issues/96