<!-- Source: https://docs.smartcitizen.me/knowledge/air/ -->

# Air measurements

*Air measurements* are the most common use case in the Smart Citizen Kit. These are measurements that imply measuring _physical_ properties of the air (temperature, pressure, relative humidity), things that _are_ in the air (gases, particulate matter) or things that _travel through_ the air (noise, ambient light, UV-index). For this, we use a series of different sensors. These sensors can be _standalone units_ (for instance, a CO2 sensor), or can be in _sensor boards_. When the data board by itself can't read the sensor directly, we need to use _interface electronics_ to get reading from them. Below you can find a list of metrics that are already supported, but bear in mind that there are plenty of other options possible!

- [Particulate Matter](https://docs.smartcitizen.me/knowledge/air/pm.md)
- [Temperature and relative humidity](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity.md)
- [Barometric pressure](https://docs.smartcitizen.me/knowledge/air/pressure.md)
- [Noise](https://docs.smartcitizen.me/knowledge/air/noise.md)
- [Light](https://docs.smartcitizen.me/knowledge/air/light.md)
- [CO2](https://docs.smartcitizen.me/knowledge/air/co2.md)
- [Chemical composition (besides CO2)](https://docs.smartcitizen.me/knowledge/air/chemical.md), including [VOCs](https://docs.smartcitizen.me/knowledge/air/chemical.md#voc)

## Supported sensors

- [AMS AS7331](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7331.md) (Field | air; Metric | light; Connection | onboard): A sensor for measuring UV-A, UV-B and UV-C light! Available in SCK2.2 and above.
- [AMS AS7341](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7341.md) (Field | air; Metric | light; Connection | external): The AS7341 is an 11-channel spectral sensor by ams OSRAM. You can use it to measure the color composition of light, from violet to near infrared, and to detect light flicker.
- [AMS CCS811](https://docs.smartcitizen.me/knowledge/air/chemical/AMS_CCS811.md) (Field | air; Metric | chemical; Connection | onboard): The AMS CCS811 is a Metal Oxide Sensor with I2C connectivity which is capable of measuring a VOCs.
- [Alphasense EC Sensors](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_Electrochemical.md) (Field | air; Metric | chemical; Connection | external): Electrochemical sensors for a variety of chemical pollutants
- [Alphasense PID](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_PID.md) (Field | air; Metric | vocs; Connection | external): A high-end PID from Alphasense to measure VOCs.
- [Bosch BME680](https://docs.smartcitizen.me/knowledge/air/chemical/Bosch_BME680.md) (Field | air; Metric | chemical; Connection | external): A multi-sensor node for environmental metrics and air quality.
- [Dallas DS18B20](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/DS18B20.md) (Field | air; Metric | temperature; Connection | external): One-wire weather-proof temperature sensor.
- [Figaro TGS260X](https://docs.smartcitizen.me/knowledge/air/chemical/Figaro_TGS260X.md) (Field | air; Metric | vocs; Connection | external): Low cost Metal Oxide sensors for VOCs
- [NXP MPL3115A2](https://docs.smartcitizen.me/knowledge/air/pressure/NXP_MPL3115A2.md) (Field | air; Metric | pressure; Connection | onboard): A barometric pressure sensor, that can also estimate altitude. Available in SCK2.1 and SCK2.3.
- [Plantower PMS5003](https://docs.smartcitizen.me/knowledge/air/pm/Plantower_PMS5003.md) (Field | air; Metric | pm; Connection | onboard): The PMS5003 is an Optical PM sensor by Plantower at a very low cost!
- [Rohm BH1730FVC](https://docs.smartcitizen.me/knowledge/air/light/Rohm_BH1730FVC.md) (Field | air; Metric | light; Connection | onboard): A digital ambient light sensor, that measures light as perceived by the human eye. Available in all SCK2.X versions.
- [SGX MiCS](https://docs.smartcitizen.me/knowledge/air/chemical/SGX_MICS.md) (Field | air; Metric | chemical; Connection | onboard): The classic Metal Oxyde for CO and NO2 measurements!
- [ST LPS33K](https://docs.smartcitizen.me/knowledge/air/pressure/ST_LPS33K.md) (Field | air; Metric | pressure; Connection | onboard): A compact barometric pressure sensor. Available in SCK2.2.
- [Sensirion SCD30](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD30.md) (Field | air; Metric | co2; Connection | external): The SCD30 is a NDIR CO2 sensor by Sensirion. You can use it to measure CO2 in indoor spaces or for experiments where you need to know an accurate CO2 level.
- [Sensirion SCD4X](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD4X.md) (Field | air; Metric | co2; Connection | external): The SCD4X (SCD40 and SCD41) is a miniature photoacoustic NDIR CO2 sensor by Sensirion. You can use it to measure CO2 in indoor spaces, in mobile setups, or for experiments where you need to know an accurate CO2 level.
- [Sensirion SEN5X](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SEN5X.md) (Field | air; Metric | pm; Connection | onboard): The Sensirion SEN5X is a newer PM sensor with a very good performance for such low cost. Available in SCK2.2 and above!
- [Sensirion SFA30](https://docs.smartcitizen.me/knowledge/air/chemical/Sensirion_SFA30.md) (Field | air; Metric | vocs; Connection | external): An electrochemical sensor for measuring formaldehyde (HCHO).
- [Sensirion SHT3X Weatherproof](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X-weatherproof.md) (Field | air; Metric | temperature; Connection | external): A temperature and humidity sensor in a weatherproof capsule
- [Sensirion SHT3X](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X.md) (Field | air; Metric | temperature; Connection | onboard): A temperature and humidity sensor that we love! Available in SCK2.X.
- [Sensirion SPS30](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SPS30.md) (Field | air; Metric | pm; Connection | external): The Sensirion SPS30 is PM sensor with a very good performance for such low cost. Only supported for experimental setups!
- [TDK ICS43432](https://docs.smartcitizen.me/knowledge/air/noise/TDK_ICS43432.md) (Field | air; Metric | noise; Connection | onboard): A MEMs microphone with high sensitivity, available on SCK2.X series by default.
