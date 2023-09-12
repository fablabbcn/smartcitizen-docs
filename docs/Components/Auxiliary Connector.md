# Auxiliary connector

The [data board](/Components/Data Board/) features a standard [Grove connector](https://wiki.seeedstudio.com/Grove_System/) where external modules can be connected. The connector supports an independent I2C bus by default, but by software it can be configured to support other uses (GPIO, I2C and UART). It can supply power **up to 750mA**, and it can be enabled or disabled by software to save energy.

![](/assets/images/sck_2/SCK21_Aux.png)

!!!info "There is a lot more to it!"
    The Smart Citizen Kit is designed with a modular approach in mind. This means that the [Urban Board](/Components/Urban%20Sensor%20Board/) is only a selection of low cost sensors for air quality, but the hardware itself can be expanded for other use cases such as a more advanced air quality monitoring setup, soil monitoring, or water quality. Make sure you check our [guide on how to use them](/Guides/getting%20started/Third%20party%20sensors/).

## Supported sensors

This is a list of supported sensors and other components that you can connect directly to the **auxiliary port**. The links provided below are for breakout boards by some other open hardware provided such as [Sparkfun](https://sparkfun.com), [Adafruit](https://adafruit.com) or [Seeed Studio](https://seeedstudio.com). However, any other format or breakout board would work. 

!!! info "Looking for datasheets?"
    Refer to the [Performance section](/Components/sensors/performance) for more information and datasheets.

### General purpose

- [Seeed Grove ADC](http://wiki.seeedstudio.com/Grove-I2C_ADC/) - 12 bit ADC from Seeed Studio
- [Adafruit breakout for INA219](https://www.adafruit.com/product/904) - Supports Bus voltage, shunt voltage, current and load voltage
- [SparkFun breakout for ToF Range Finder Sensor - VL6180](https://www.sparkfun.com/products/12785) - supports distance and light. Can be used for water level measurements
- [Adafruit breakout for ADS1X15](https://www.adafruit.com/product/1085) - 16 bit ADC from Texas instruments also found in Adafruit development boards

### Air

You will find below sensors that are deployed in air. Many anufacturers offer them: Seeed, Adafruit, Sparkfun and many more.

- [Sensirion SHT31](https://sensirion.com/products/catalog/SHT31-DIS-F) - supports temperature and humidity. 
- [Bosch BME680](https://www.adafruit.com/product/3660) - supports temperature, humidity, barometric pressure and tVOC
- [AMS CCS811](https://www.adafruit.com/product/3660) (deprecated) - supports tVOC

!!! info "Smart Citizen Station"
    Expanding the base air quality solution, the [Smart Citizen Station](/Smart Citizen Station) is a more advanced hardware setup in a more rugged enclosure. The sensors below can be directly plugged in and detected by the SCK:

    - [Smart Citizen Analog Sensor Board](/Components/Analog Sensor Board/): supports 4 or 8 analog channels at 16bit resolution.
    - [Smart Citizen Gases Pro Board](/Components/Gases Pro Board/) (deprecated): supports 3 electrochemical Alphasense sensors, and has an onboard temperature and humidity sensor
    - [Smart Citizen PM Board](/Components/PM Board/): supports 2 Plantower PMS5003 sensors, I2C extension, 4 ADC pins, 2 GPIO and a UART Serial port

    
    ![](https://i.imgur.com/RRu8MiV.jpg)

### Soil and Water

Check the [Soil and water measurements](/Components/Soil and water/) documentation with examples on sensors such as:

- [Atlas Scientific](https://atlas-scientific.com):
    - [Temperature](https://atlas-scientific.com/temperature)
    - [pH](https://atlas-scientific.com/ph)
    - [ORP](https://atlas-scientific.com/orp)
    - [Electric Conductivity](https://atlas-scientific.com/conductivity)
    - [Dissolved Oxygen](https://atlas-scientific.com/dissolved-oxygen)
- [DS18B20 Water Temperature](https://www.adafruit.com/product/381)
- [Chirp Soil Moisture](https://www.tindie.com/products/miceuz/i2c-soil-moisture-sensor/), with support of soil moisture (requires calibration), temperature and ambient light.

## Other auxiliaries

- [Seeed Grove OLED screen (128x128)](http://wiki.seeedstudio.com/Grove-OLED_Display_1.12inch/), check the [documentation](/Guides/auxiliaries/OLED%20display/) for more details. 
- [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329)
- [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414)
- [SparkFun GPS SAM-M8Q](https://www.sparkfun.com/products/15210), only in a forked repository for now by [serialc](https://github.com/serialc/) [here](https://github.com/serialc/smartcitizen-kit-21). Read this post [here](https://forum.smartcitizen.me/t/power-off-qwiic-on-sck2-1-power-off/1623)
- [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html) (only via [PM Board](/Components/boards/PM Board/) as it uses UART to communicate)

!!! warning "Sparkfun QWIIC GPS"
    If you are using Sparkfun QWIIC GPS, note that you will need [an adaptor from GROVE to QWIIC](https://www.sparkfun.com/products/15109)

!!! info "Implement your own"
    Check the guide on [integrating other sensors](/Guides/getting started/Third party sensors/), or [contact us](mailto:support@smartcitizen.me) to know how to implement sensors made by others.

## Full list

This is a list of supported sensors:

{{ get_snippet_rel("docs/includes/supported sensors/index.md") }}