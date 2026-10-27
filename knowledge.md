<!-- Source: https://docs.smartcitizen.me/knowledge/ -->

# Knowledge

In this section, you will find a compilation of the different environmental variables, and the sensors used to monitor them, available in the Smart Citizen Kit. Feel free to contribute!

## Onboard Sensors

Below, you will find the sensors that are included by _default_ in any of the Smart Citizen Kit versions (2.1, 2.2 or 2.3).

- [AMS AS7331](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7331.md) (Field | air; Metric | light; Connection | onboard): A sensor for measuring UV-A, UV-B and UV-C light! Available in SCK2.2 and above.
- [AMS CCS811](https://docs.smartcitizen.me/knowledge/air/chemical/AMS_CCS811.md) (Field | air; Metric | chemical; Connection | onboard): The AMS CCS811 is a Metal Oxide Sensor with I2C connectivity which is capable of measuring a VOCs.
- [NXP MPL3115A2](https://docs.smartcitizen.me/knowledge/air/pressure/NXP_MPL3115A2.md) (Field | air; Metric | pressure; Connection | onboard): A barometric pressure sensor, that can also estimate altitude. Available in SCK2.1 and SCK2.3.
- [Plantower PMS5003](https://docs.smartcitizen.me/knowledge/air/pm/Plantower_PMS5003.md) (Field | air; Metric | pm; Connection | onboard): The PMS5003 is an Optical PM sensor by Plantower at a very low cost!
- [Rohm BH1730FVC](https://docs.smartcitizen.me/knowledge/air/light/Rohm_BH1730FVC.md) (Field | air; Metric | light; Connection | onboard): A digital ambient light sensor, that measures light as perceived by the human eye. Available in all SCK2.X versions.
- [SGX MiCS](https://docs.smartcitizen.me/knowledge/air/chemical/SGX_MICS.md) (Field | air; Metric | chemical; Connection | onboard): The classic Metal Oxyde for CO and NO2 measurements!
- [ST LPS33K](https://docs.smartcitizen.me/knowledge/air/pressure/ST_LPS33K.md) (Field | air; Metric | pressure; Connection | onboard): A compact barometric pressure sensor. Available in SCK2.2.
- [Sensirion SEN5X](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SEN5X.md) (Field | air; Metric | pm; Connection | onboard): The Sensirion SEN5X is a newer PM sensor with a very good performance for such low cost. Available in SCK2.2 and above!
- [Sensirion SHT3X](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X.md) (Field | air; Metric | temperature; Connection | onboard): A temperature and humidity sensor that we love! Available in SCK2.X.
- [TDK ICS43432](https://docs.smartcitizen.me/knowledge/air/noise/TDK_ICS43432.md) (Field | air; Metric | noise; Connection | onboard): A MEMs microphone with high sensitivity, available on SCK2.X series by default.


## Auxiliary Connector

This is a list of supported sensors and other components that you can connect directly to the **auxiliary port**. The links provided below are for breakout boards by some other open hardware provided such as [Sparkfun](https://sparkfun.com), [Adafruit](https://adafruit.com) or [Seeed Studio](https://seeedstudio.com). However, any other format or breakout board would work.

- [AMS AS7341](https://docs.smartcitizen.me/knowledge/air/light/AMS_AS7341.md) (Field | air; Metric | light; Connection | external): The AS7341 is an 11-channel spectral sensor by ams OSRAM. You can use it to measure the color composition of light, from violet to near infrared, and to detect light flicker.
- [Alphasense EC Sensors](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_Electrochemical.md) (Field | air; Metric | chemical; Connection | external): Electrochemical sensors for a variety of chemical pollutants
- [Alphasense PID](https://docs.smartcitizen.me/knowledge/air/chemical/Alphasense_PID.md) (Field | air; Metric | vocs; Connection | external): A high-end PID from Alphasense to measure VOCs.
- [Atlas DO](https://docs.smartcitizen.me/knowledge/soil-water/DO/Atlas_DO.md) (Field | water; Metric | dissolved oxygen; Connection | external): A galvanic probe that can measure dissolved oxygen in water.
- [Atlas EC](https://docs.smartcitizen.me/knowledge/soil-water/EC/Atlas_EC.md) (Field | watersoil; Metric | electrical conductivity; Connection | external): A conductivity meter to measure electrolytes in a liquid!
- [Atlas ORP](https://docs.smartcitizen.me/knowledge/soil-water/ORP/Atlas_ORP.md) (Field | water; Metric | orp; Connection | external): An ORP probe is a passive device that detects a current generated from the oxidation or reduction of chemical substances in water.
- [Atlas Temperature](https://docs.smartcitizen.me/knowledge/soil-water/temperature/Atlas_Temperature.md) (Field | watersoil; Metric | temperature; Connection | external): An encapsulated resistive sensor (RTD, resistance temperature detector).
- [Atlas pH](https://docs.smartcitizen.me/knowledge/soil-water/pH/Atlas_pH.md) (Field | watersoil; Metric | pH; Connection | external): The pH probe is a very delicate submerged electrode in a thin glass bubble.
- [Bosch BME680](https://docs.smartcitizen.me/knowledge/air/chemical/Bosch_BME680.md) (Field | air; Metric | chemical; Connection | external): A multi-sensor node for environmental metrics and air quality.
- [Chirp Soil Moisture](https://docs.smartcitizen.me/knowledge/soil-water/moisture/Chirp_Soil_Moisture.md) (Field | soil; Metric | moisture; Connection | external)
- [Dallas DS18B20](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/DS18B20.md) (Field | air; Metric | temperature; Connection | external): One-wire weather-proof temperature sensor.
- [Figaro TGS260X](https://docs.smartcitizen.me/knowledge/air/chemical/Figaro_TGS260X.md) (Field | air; Metric | vocs; Connection | external): Low cost Metal Oxide sensors for VOCs
- [Sensirion SCD30](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD30.md) (Field | air; Metric | co2; Connection | external): The SCD30 is a NDIR CO2 sensor by Sensirion. You can use it to measure CO2 in indoor spaces or for experiments where you need to know an accurate CO2 level.
- [Sensirion SCD4X](https://docs.smartcitizen.me/knowledge/air/co2/Sensirion_SCD4X.md) (Field | air; Metric | co2; Connection | external): The SCD4X (SCD40 and SCD41) is a miniature photoacoustic NDIR CO2 sensor by Sensirion. You can use it to measure CO2 in indoor spaces, in mobile setups, or for experiments where you need to know an accurate CO2 level.
- [Sensirion SFA30](https://docs.smartcitizen.me/knowledge/air/chemical/Sensirion_SFA30.md) (Field | air; Metric | vocs; Connection | external): An electrochemical sensor for measuring formaldehyde (HCHO).
- [Sensirion SHT3X Weatherproof](https://docs.smartcitizen.me/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X-weatherproof.md) (Field | air; Metric | temperature; Connection | external): A temperature and humidity sensor in a weatherproof capsule
- [Sensirion SPS30](https://docs.smartcitizen.me/knowledge/air/pm/Sensirion_SPS30.md) (Field | air; Metric | pm; Connection | external): The Sensirion SPS30 is PM sensor with a very good performance for such low cost. Only supported for experimental setups!
- [TI ADS1115](https://docs.smartcitizen.me/knowledge/other/TI_ADS1X15.md) (Field | other; Metric | current; Connection | external): A high precision 16-bit, 4 channel ADC, used in the Analog Sensor Board.
- [TI INA219](https://docs.smartcitizen.me/knowledge/other/TI_INA219.md) (Field | other; Metric | current; Connection | external): A digital sensor for measuring electric current and voltage!
- [Tensiometer / Irrometer](https://docs.smartcitizen.me/knowledge/soil-water/moisture/Tensiometer.md) (Field | soil; Metric | soil tension; Connection | external)
