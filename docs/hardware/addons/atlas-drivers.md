# Atlas EZO Drivers

TODO - FINISH THIS PAGE

## Setup

!!! danger "Only if you bought them separately"
    This guide describes the setup procedure of the Atlas Scientific probes in case you bought them separately. If you have a [Water Station](/Components/Soil and water/#water-station), you don't need to do this.

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

