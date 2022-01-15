!!! warning "WIP"
    This list is _always_ a WIP!

| Field | SCK sensor name | Units | Location | Sensor and datasheet |
| :--- | :--- | :---: | :---: | :---: |
| *Air* | Temperature | ºC | Urban Board | [Sensirion SHT31](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/) |
| *Air* | Humidity | %RH |  Urban Board | [Sensirion SHT31](https://www.sensirion.com/fileadmin/user_upload/customers/sensirion/Dokumente/2_Humidity_Sensors/) |
| *Air* | Light | lux | Urban Board | [ROHM BH1730](http://rohmfs.rohm.com/en/products/databook/datasheet/ic/sensor/light/bh1721fvc-e.pdf) |
| *Air* | Noise dBA | na (dBA scale) | Urban Board | [INVENSENSE 43432](https://www.invensense.com/wp-content/uploads/2015/02/ICS-43432-data-sheet-v1.3.pdf) |
| *Air* | Noise dBC | na (dBC scale) | Urban Board | [INVENSENSE 43432](https://www.invensense.com/wp-content/uploads/2015/02/ICS-43432-data-sheet-v1.3.pdf) |
| *Air* | Noise dBZ | na (dBZ scale) | Urban Board | [INVENSENSE 43432](https://www.invensense.com/wp-content/uploads/2015/02/ICS-43432-data-sheet-v1.3.pdf) |
| *Air* | Noise FFT | na | Urban Board | [INVENSENSE 43432](https://www.invensense.com/wp-content/uploads/2015/02/ICS-43432-data-sheet-v1.3.pdf) |
| *Air* | Barometric pressure | kPa | Urban Board | [NXP MPL3115A2](http://www.nxp.com/docs/en/data-sheet/MPL3115A2.pdf)|
| *Air* | VOC Gas CCS811 | ppb | Urban Board | [AMS CCS811](https://www.sciosense.com/wp-content/uploads/2020/01/SC-001232-DS-2-CCS811B-Datasheet-Revision-2.pdf) |
| *Air* | eCO2 Gas CCS811 | ppm | Urban Board | [AMS CCS811](https://www.sciosense.com/wp-content/uploads/2020/01/SC-001232-DS-2-CCS811B-Datasheet-Revision-2.pdf) |
| *Air* | PM_X (X = [1.0, 2.5, 10]) | ug/m3 | Urban Board | [PLANTOWER PMS5003](https://aqicn.org/air/view/sensor/spec/pms5003.pdf) |
| *Air* | PN_X (X = [0.3, 0.5, 1.0, 2.5, 5.0, 10]) | #/0.1l | Urban Board | [PLANTOWER PMS5003](https://aqicn.org/air/view/sensor/spec/pms5003.pdf) |
| *Air, soil and water* | PM board Dallas Temperature | ºC | External Sensor | [MAXIM DS18B20](https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf) |
| *Air* | Ext PM_X (X = [1.0, 2.5, 10]) | ug/m3 | External Sensor | [PLANTOWER PMS5003](https://aqicn.org/air/view/sensor/spec/pms5003.pdf) |
| *Air* | Ext PN_X (X = [0.3, 0.5, 1.0, 2.5, 5.0, 10]) | #/0.1l | External Sensor | [PLANTOWER PMS5003](https://aqicn.org/air/view/sensor/spec/pms5003.pdf) |
| *Air* | SCD30_CO2 | ppm | External Sensor | [Sensirion SCD30](https://files.seeedstudio.com/wiki/Grove-CO2-Temperature-Humidity-Sensor-SCD30/res/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf) |
| *Air* | SCD30_T | ºC | External Sensor | [Sensirion SCD30](https://files.seeedstudio.com/wiki/Grove-CO2-Temperature-Humidity-Sensor-SCD30/res/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf) |
| *Air* | SCD30_H | %RH | External Sensor | [Sensirion SCD30](https://files.seeedstudio.com/wiki/Grove-CO2-Temperature-Humidity-Sensor-SCD30/res/Sensirion_CO2_Sensors_SCD30_Datasheet.pdf) |
| *Generic* | ADS1x15 ADC 0x4X ChY (X = [8, 9, A, B)], Y = [0, 1, 2, 3]) | V | External Sensor | [ADS 1115](https://www.ti.com/lit/ds/symlink/ads1115.pdf) |
| *Generic* | Grove ADC | V | External Sensor | [Seeed Grove ADC](http://wiki.seeedstudio.com/Grove-I2C_ADC/) |
| *Location* | GPS Fix Quality| na | External Sensor | [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329), [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414) or [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html) |
| *Location* | GPS Latitude | Deg | External Sensor | [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329), [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414) or [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html)  |
| *Location* | GPS Longitude| Deg | External Sensor | [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329) , [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414) or [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html)  |
| *Location* | GPS Altitude| m | External Sensor | [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329), [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414) or [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html)  |
| *Location* | GPS Speed| m/s | External Sensor |  [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329), [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414) or [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html) |
| *Location* | GPS Horizontal Dilution of Position | - | External Sensor |  [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329) , [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414) or [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html)  |
| *Location* | GPS Traked Satellites | - | External Sensor |  [Sparkfun GPS NEO-M8U](https://www.sparkfun.com/products/16329) , [SparkFun GPS XA1110](https://www.sparkfun.com/products/14414) or [SEEED Grove GPS Module](https://www.seeedstudio.com/Grove-GPS-Module.html)  |
| *Soil and water* | Atlas PH | PH | External Sensor | Atlas Scientific pH [Driver](https://www.atlas-scientific.com/product_pages/circuits/ezo_ph.html) - [Probe](https://www.atlas-scientific.com/product_pages/probes/ph_probe.html) - [Calibration Solution](https://atlas-scientific.com/calibration-solutions/ph-4-00-7-00-10-00-calibration-solutions/) |
| *Water* | Atlas Dissolved Oxygen | mg/L | External Sensor | Atlas Scientific Dissolved Oxygen [Driver](https://www.atlas-scientific.com/product_pages/circuits/ezo_do.html) - [Probe](https://www.atlas-scientific.com/product_pages/probes/do_probe.html) - [Calibration solution](https://atlas-scientific.com/calibration-solutions/dissolved-oxygen-calibration-solution-pouch/) |
| *Water* | Atlas DO Saturation | % | External Sensor | Atlas Scientific Oxygen Saturation [Driver](https://www.atlas-scientific.com/product_pages/circuits/ezo_do.html) - [Probe](https://www.atlas-scientific.com/product_pages/probes/do_probe.html) - [Calibration solution](https://atlas-scientific.com/calibration-solutions/dissolved-oxygen-calibration-solution-pouch/) |
| *Soil and water* | Atlas Conductivity | µS/cm | External Sensor | Atlas Scientific Electric Conductivity [Driver](https://www.atlas-scientific.com/product_pages/circuits/ezo_ec.html) - [Probe](https://atlas-scientific.com/probes/conductivity-probe-k-10/) - [Calibration Solution](https://atlas-scientific.com/calibration-solutions/conductivity-calibration-k-10-set/) |
| *Soil and water* | Atlas Total Dissolved Solids | ppm | External Sensor | Atlas Scientific Electric Conductivity [Driver](https://www.atlas-scientific.com/product_pages/circuits/ezo_ec.html) - [Probe](https://atlas-scientific.com/probes/conductivity-probe-k-10/) - [Calibration Solution](https://atlas-scientific.com/calibration-solutions/conductivity-calibration-k-10-set/) |
| *Soil and water* | Atlas Salinity | PSU(ppt) | External Sensor | Atlas Scientific Electric Conductivity [Driver](https://www.atlas-scientific.com/product_pages/circuits/ezo_ec.html) - [Probe](https://atlas-scientific.com/probes/conductivity-probe-k-10/) - [Calibration Solution](https://atlas-scientific.com/calibration-solutions/conductivity-calibration-k-10-set/) |
| *Soil and water* | Atlas Specific gravity | - | External Sensor | Atlas Scientific Electric Conductivity [Driver](https://www.atlas-scientific.com/product_pages/circuits/ezo_ec.html) - [Probe](https://atlas-scientific.com/probes/conductivity-probe-k-10/) - [Calibration Solution](https://atlas-scientific.com/calibration-solutions/conductivity-calibration-k-10-set/) |
| *Soil* | Soil Moisture Raw | - | External Sensor | [Chirp Soil Moisture](https://www.tindie.com/products/miceuz/i2c-soil-moisture-sensor/) |
| *Soil* | Soil Moisture Percent | % | External Sensor | [Chirp Soil Moisture](https://www.tindie.com/products/miceuz/i2c-soil-moisture-sensor/) |
| *Soil* | Soil Temperature | degC | External Sensor | [Chirp Soil Moisture](https://www.tindie.com/products/miceuz/i2c-soil-moisture-sensor/) |
| *Soil* | Soil Light | - | External Sensor | [Chirp Soil Moisture](https://www.tindie.com/products/miceuz/i2c-soil-moisture-sensor/) |
| *Air, soil and water* | Atlas Temperature | degC | External Sensor | PT-100 or PT-1000 [Atlas Scientific Temperature](https://www.atlas-scientific.com/product_pages/kits/temp_kit.html) |
| *Other* | Battery | % |  Urban Board | - |
| *Other* | Battery Voltage | V |  Urban Board | - |
| *Other* | INA219 Bus voltage | V | External Sensor | [Adafruit INA219](https://www.adafruit.com/product/904) |
| *Other* | INA219 Shunt voltage | mV | External Sensor | [Adafruit INA219](https://www.adafruit.com/product/904) |
| *Other* | INA219 Current | mA | External Sensor | [Adafruit INA219](https://www.adafruit.com/product/904) |
| *Other* | INA219 Load voltage | V | External Sensor | [Adafruit INA219](https://www.adafruit.com/product/904) |

