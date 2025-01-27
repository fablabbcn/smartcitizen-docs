# Smart Citizen Water Stations

Although most of the time we have been working with _air quality_ sensors and other related metrics, we also work with water metrics. This section summarises our integration of water sensors, in some cases, with interchangeable probes or drivers for soil measurements. For example, the setup shown above is designed for water measurements and includes [Atlas Scientific](https://www.atlas-scientific.com) [temperature](/knowledge/soil-water/Atlas_Temperature/), [conductivity](/knowledge/soil-water/Atlas_EC/) and [pH](/knowledge/soil-water/Atlas_pH/) probes and a [GPS](/hardware/extras/GPS/).

!!! info "Soil Stations"
    The Water Stations can support additional sensors, such as the [Chirp Moisture Sensor](/knowledge/soil-water/Chirp_Soil_Moisture/). More soil sensors can be added as well, by using the [Auxiliary connector](/hardware/Smart Citizen Kit/#auxiliary-connector).

<img src="https://live.staticflickr.com/65535/51232063715_5e37cfb1a0_k.jpg" width="2000" height="1333" alt="Patí Científic Workshop">

## Available metrics

| Metric | Usage | Sensor | Interface Board | Calibration |
| :-: | :-: | :-: | :-: | :-: |
| Temperature | Soil and water | [Atlas Temperature](/knowledge/soil-water/temperature/Atlas_Temperature) | Atlas EZO-RTD | See [temperature calibration page](/knowledge/soil-water/temperature/Atlas_Temperature#calibration) |
| pH | Soil and water |  [Atlas Water pH](/knowledge/soil-water/pH/Atlas_pH) and [Atlas Soil pH](/knowledge/soil-water/Atlas_pH)  | Atlas EZO-PH | See [pH calibration page](/knowledge/soil-water/pH/Atlas_pH#calibration) |
| Electrical Conductivity, total dissolved solids, salinity and specific gravity | Soil and water | [Atlas Conductivity](/knowledge/soil-water/EC/Atlas_EC) | Atlas EZO-EC | See [EC calibration page](/knowledge/soil-water/EC/Atlas_EC#calibration)  |
| Dissolved Oxygen and oxygen saturation | Water | [Atlas DO](/knowledge/soil-water/DO/Atlas_DO) | Atlas EZO-DO | See [DO calibration page](/knowledge/soil-water/DO/Atlas_DO#calibration)  |
| Soil Moisture | Soil | [Catnip Chirp!](/knowledge/soil-water/moisture/Chirp_Soil_Moisture) | Data Board | See [moisture calibration page](/knowledge/soil-water/moisture/Chirp_Soil_Moisture#calibration) |

!!! warning "Soil and water"
    Some probes can be used for both, soil and water. Make sure to check each sensor page to see how they work.

## Versions

{{ insert_cards(type="stations", filter="field", value=["water"]) }}

### Legacy versions

Below you will find some legacy (aka _development_) versions. These are left here for you to identify them, or in case you want some inspiration.

Through a collaboration with [Aquapioners](http://aquapioneers.io), we designed the [custom enclosure](https://github.com/fablabbcn/monitoring-kit-hardware) below.

<img src="https://live.staticflickr.com/65535/47957175206_4a63cbdda9_k.jpg" alt="SCK Aquapionners Prototype 2016"/>