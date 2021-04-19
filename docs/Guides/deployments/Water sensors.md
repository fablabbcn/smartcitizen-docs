# Water sensors

!!! warning "Only if you bought them separately"
    This guide describes the setup procedure of the Atlas Scientific probes in case you bought them separately. If you have a [Water Station](/Components/Soil and water/#water-station), you don't need to do this.

<img src="https://live.staticflickr.com/65535/51126012000_ef69edea6b_k.jpg" alt="Water Station - Patí Científic">

## Setup

### Manually switching circuits to I2C mode

If the drivers are new normally they come configured in UART mode so we need to change them to I2C mode.

1. Remove circuit from Tentacle shield.
2. Put the circuit into a breadboard.
3. For **PH**, **DO**, **ORP** and **EC**: Short the `PGND` pin to the `TX` pin using a jumper wire.
4. For **RTD** (temperature): Short the `PRB` pin to the `TX` pin using a jumper wire.
5. Power the device (connecting `GND` and `VCC`)
6. Wait for LED to change from green to blue (UART→I2C) or from blue to green (I2C→>UART).
7. Remove the jumper wire from the `PGND` (or `PRB` respectively) pin to the `TX` pin (Do this **before removing power!**).
8. Remove power (`VCC`).
9. Apply power (`VCC`).
10. The device is now in the new mode (repeat all steps to switch back to previous mode).

!!! warning "Official documentation"
    [Atlas Doc](https://www.whiteboxes.ch/tentacle/#tentacle-t3)

## Connection to Smartcitizen Kit

![](https://i.imgur.com/Dc6Us2F.png)

After connecting the [Tentacle 3](https://atlas-scientific.com/carrier-boards/whitebox-labs-tentacle-t3/) to the SCK power your kit and if youre connected to the shell the autodetecition message should look similar to this (depending on the connected drivers and probes):

```
Urban board detected
Enable Atlas Temperature
Enable Atlas PH
Enable Atlas Conductivity
Enable Atlas Specific gravity
...
```

!!! warning "Sensor calibration"
    Make sure to follow our sensor calibration guide for the [water sensors](/Guides/calibration/Water sensors/).

## Raspberry setup

1. Install raspbian
2. Enable I2C with raspi-config, reboot, upgrade.
3. Install packages and reboot.
    ```
    sudo apt-get install python-smbus i2c-tools
    ```
4. Connect the shield with the pi off.
5. Test I2C 
    ```
    sudo i2cdetect -y 1
    ```
6. Code example https://github.com/AtlasScientific/Raspberry-Pi-sample-code/blob/master/i2c.py
