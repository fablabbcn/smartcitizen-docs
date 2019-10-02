The [data board](/Components/Data Board/) features a standard Grove connector where off-the-shelf modules from the same manufacturer can be connected. The connector supports an independent I2C bus by default, but by software it can be configured to support other uses (GPIO, I2C and UART). It can supply power up to 750mA, and it can be enabled or disabled by software to save power.

<div style="text-align: center">
    <img src="https://i.imgur.com/5nEc922.jpg" width="350px">
</div>

!!!info "There is a lot more to it!"
    The Smart Citizen Kit is designed with a modular approach in mind. This means that the [Urban Board](/Components/Urban%20Sensor%20Board/) is only a selection of low cost sensors for air quality, but the hardware itself can be expanded for other use cases such as a more advanced air quality monitoring setup, soil monitoring, or water quality. Make sure you check our [guide on how to use them](/Components/Auxiliary/guides/thirdparty/).
## Supported sensors

### General purpose

- [Seeed Groove ADC](http://wiki.seeedstudio.com/Grove-I2C_ADC/) - 12 bit ADC from Seeed Studio
- [Adafruit INA219](https://www.adafruit.com/product/904) - Supports Bus voltage, shunt voltage, current and load voltage
- [SparkFun ToF Range Finder Sensor - VL6180](https://www.sparkfun.com/products/12785) - supports distance and light. Can be used for water level measurements

### Environmental and air quality

- [Seeed Grove SHT31 Temperature/Humidity](https://www.seeedstudio.com/Grove-Temperature-Humidity-Sensor-SHT31.html)
- [Adafruit BME680](https://www.adafruit.com/product/3660) - supports temperature, humidity, barometric pressure and VOC gas
- [Atlas Scientific Temperature](https://www.atlas-scientific.com/product_pages/kits/temp_kit.html) - can be used with any PT-100 or PT-1000 temperature probes

!!! info "Smart Citizen Station"
    Expanding the base air quality solution, the [Smart Citizen Station](/Smart Citizen Station) is a more advanced setup in a more rugged enclosure. The sensors below can be directly plugged in and detected by the SCK:

    - [Smart Citizen Gases Pro Board](http://docs.smartcitizen.me/Components/Gas%20Pro%20Sensor%20Board/#gases-pro-sensor-board): supports 3 electrochemical alphasense sensors, temperature and humidity 
    - [Smart Citizen PM Board](http://docs.smartcitizen.me/Components/PM%20Sensor%20Board/#pm-sensor-board): supports 2 Plantower PMS5003 sensors, I2C extension, 4 ADC pins, 2 GPIO and a UART Serial port

    ![](https://i.imgur.com/RRu8MiV.jpg)

### Water measurements

- [Atlas Scientific Dissolved Oxygen](https://www.atlas-scientific.com/product_pages/kits/do_kit.html) - suports dissolved oxygen and saturation.
- [DS18B20 Water Temperature](https://www.adafruit.com/product/381) - it's a waterproof sensor, which can be used as well in humid air quality conditions

### Soil measurements

- [Chirp Soil Moisture](https://www.tindie.com/products/miceuz/i2c-soil-moisture-sensor/) - supports soil moisture (requires calibration), temperature and ambient light
- [Atlas Scientific PH](https://www.atlas-scientific.com/product_pages/kits/ph-kit.html) - also usable for water measurements
- [Atlas Scientific Conductivity](https://www.atlas-scientific.com/product_pages/kits/ec_k1_0_kit.html) - supports reading conductivity and specific gravity

## Other auxiliaries

- [Seeed Groove OLED screen (96x96)](http://wiki.seeedstudio.com/Grove-OLED_Display_1.12inch/) - the screen cycles through sensor readings

!!! info "Implement your own"
    **Shortly**, we will publish a guide for supporting the implementation of sensors by others.
