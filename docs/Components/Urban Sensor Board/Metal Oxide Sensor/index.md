Metal Oxide sensors
===================================

The Smart Citizen Kit has been using metal oxide sensors for air quality metrics for a long time, and we thought that it would be interesting to dedicate a section for them!

In this section, we will compile information available for those using the SCK V2.0 (or before) with the SGX MICS 4514 and the SCK V2.1, with the AMS CCS811.

Check the links below for more information about the specifics of:

- CO - NO~2~ sensor from V2.0 and before? Click [here](Metal Oxide Sensor/MICS/)
- eCO2 - TVOC sensor from V2.1? Click [here](/Components/Urban Sensor Board/Metal Oxide Sensor/CCS811/)

## A word about Metal Oxide Sensors

Metal Oxide Sensors measure the resistance (R~S~) of a sensitive layer after heating it up with a _heating element_ (normally another resistor). However, this reading cannot be considered as an absolute measurement of the target pollutant concentration, since the resistance varies from sensor to sensor, and it's affected by several conditions, such as temperature, humidity and other non-target pollutant affectations. To mitigate this problem, the output of the sensor is normalized using the baseline resistance (R~A~): R~S~ is divided by R~A~. This baseline resistance is the resistance that the sensor sees in clean air, and the cleaner the air is, the higher the resistance is.

Unfortunately, since R~A~ varies with the deployment conditions, R~A~ cannot be determined by a one-time calibration; and in the case of the AMS CCS811 included in the SCK V2.1, is maintained on-the-fly in software. This process is known as **baseline correction**. 

Previous versions of the SCK (V1.5, V2.0 and others) included the SGX MICS4514, which was meant to measure CO and NO~2~, and a lot of effort was put in V2.0 to improve the driver for the sensor, aiming to reduce power consumption and improve sensor readings. Unfortunately, this didn't match our expectations in terms of data quality and power consumption, and since individual sensor calibration is not feasible in our case (as some scientific publications have suggested), we decided to focus efforts in simpler, more robust and understandable set of sensors.

That being said, the SCK V2.1 includes the AMS CCS811 for Air Quality indicative measurements for indoor air quality in the Urban Sensor Board, and the PMS5003 for outdoor PM exposure. More complex outdoor set-ups will be also possible, for instance using the [Gas Pro Sensor Board](../Gas Pro Sensor Board) (featuring up to three Alphasense Electrochemical Sensors)[^8][^9][^10]. This board is currently under evaluation and will be available soon. 

### What to expect from Metal Oxide Sensors

As said above, this type of sensors **is not meant for fine pollution monitoring**, but is more oriented for **air quality indications and trends detection**. Our approach is to use them for indicative measurements, and progressively tend towards a more reliable, fine and robust system, once the technology is capable of providing so. 

While deploying them, since the air quality is expected to vary in a typical environment, the minimum time over which a baseline correction is applied is 24 hours. This means that the sensor output will change with time, until the baseline is roughly stable. Since the sensor monitors the baseline resistance periodically, if a cleaner air is found, the new baseline resistance is used to calculate the sensor readings (although this is only done for  future readings). This also means that the SCK should not be interrupted with an _ad hoc_ power cut since this could erase the baseline resistance and the sensor could always yield wrong readings since it never sees _clean air_.

