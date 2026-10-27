<!-- Source: https://docs.smartcitizen.me/hardware/stations/water/ -->

# Smart Citizen Water Stations

Although most of our work is with _air quality_ sensors and other related metrics, we also work with water metrics. This section summarises our integration of water sensors, in some cases, with interchangeable probes or drivers for soil measurements. For example, the setup shown below is designed for water measurements and includes [Atlas Scientific](https://www.atlas-scientific.com) [temperature](https://docs.smartcitizen.me/knowledge/soil-water/temperature/Atlas_Temperature.md), [conductivity](https://docs.smartcitizen.me/knowledge/soil-water/EC/Atlas_EC.md), and [pH](https://docs.smartcitizen.me/knowledge/soil-water/pH/Atlas_pH.md) probes, as well as a [GPS](https://docs.smartcitizen.me/hardware/addons/gps.md).

!!! info "Soil Stations"
    The Water Stations can support additional sensors, such as the [Chirp Moisture Sensor](https://docs.smartcitizen.me/knowledge/soil-water/moisture/Chirp_Soil_Moisture.md). More soil sensors can be added as well, by using the [Auxiliary connector](https://docs.smartcitizen.me/hardware/kit/features.md#auxiliary-connector).

<img src="https://docs.smartcitizen.me/assets/images/pati-cientific-workshop-2.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

## Available metrics

| Metric | Usage | Sensor | Interface Board | Calibration |
| :-: | :-: | :-: | :-: | :-: |
| Temperature | Soil and water | [Atlas Temperature](https://docs.smartcitizen.me/knowledge/soil-water/temperature/Atlas_Temperature.md) | Atlas EZO-RTD | See [temperature calibration page](https://docs.smartcitizen.me/knowledge/soil-water/temperature/Atlas_Temperature.md#calibration) |
| pH | Soil and water |  [Atlas Water pH](https://docs.smartcitizen.me/knowledge/soil-water/pH/Atlas_pH.md) and [Atlas Soil pH](https://docs.smartcitizen.me/knowledge/soil-water/pH/Atlas_pH.md)  | Atlas EZO-PH | See [pH calibration page](https://docs.smartcitizen.me/knowledge/soil-water/pH/Atlas_pH.md#calibration) |
| Electrical Conductivity, total dissolved solids, salinity and specific gravity | Soil and water | [Atlas Conductivity](https://docs.smartcitizen.me/knowledge/soil-water/EC/Atlas_EC.md) | Atlas EZO-EC | See [EC calibration page](https://docs.smartcitizen.me/knowledge/soil-water/EC/Atlas_EC.md#calibration)  |
| Dissolved Oxygen and oxygen saturation | Water | [Atlas DO](https://docs.smartcitizen.me/knowledge/soil-water/DO/Atlas_DO.md) | Atlas EZO-DO | See [DO calibration page](https://docs.smartcitizen.me/knowledge/soil-water/DO/Atlas_DO.md#calibration)  |
| Soil Moisture | Soil | [Catnip Chirp!](https://docs.smartcitizen.me/knowledge/soil-water/moisture/Chirp_Soil_Moisture.md) | Data Board | See [moisture calibration page](https://docs.smartcitizen.me/knowledge/soil-water/moisture/Chirp_Soil_Moisture.md#calibration) |

!!! warning "Soil and water"
    Some probes can be used for both soil and water. Make sure to check each sensor page to see how they work.

## Versions

- [Multi-Sensor Water Station](https://docs.smartcitizen.me/hardware/stations/water/sck-water-multi.md) (Grade | advanced): The Water Station is a multiparametric water unit, capable of measuring pH, Temperature, Dissolved Oxygen, Conductivity and ORP.
- [One-Sensor Water Station](https://docs.smartcitizen.me/hardware/stations/water/sck-water-single.md) (Grade | intermediate): The One-Sensor Water Station is meant to measure one physico-chemical parameter at a time. Choose from pH, Temperature, Dissolved Oxygen, Conductivity or ORP.


### Legacy versions

Below you will find some legacy (aka _development_) versions. These are left here for you to identify them, or in case you want some inspiration.

Through a collaboration with [Aquapioneers](https://github.com/aquapioneers), we designed the [custom enclosure](https://github.com/fablabbcn/monitoring-kit-hardware) below.

<img src="https://docs.smartcitizen.me/assets/images/sck-aquapionners-prototype-2016.jpg" alt="SCK Aquapionners Prototype 2016"/>