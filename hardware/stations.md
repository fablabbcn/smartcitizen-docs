<!-- Source: https://docs.smartcitizen.me/hardware/stations/ -->

# Smart Citizen Stations

![]( /assets/images/stations-feature.jpg)

## What are the _Smart Citizen Stations_?

The Smart Citizen Stations (_Stations_ for short) are **open-source environmental monitoring systems**. They build upon the functionalities of the [Smart Citizen Kit](https://docs.smartcitizen.me/hardware/kit.md), extending its sensing capabilities. The idea behind this is to leverage the modularity of the [hardware](https://docs.smartcitizen.me/hardware.md) and include more sensors, making some changes to the enclosures to make everything fit. Anything on our list of [supported sensors](https://docs.smartcitizen.me/knowledge.md) can be used to build a _Station_. Below are summaries of the most common configurations to offer a sample of what can be done. Check the dedicated sections for each to get a complete description!

!!! tip "Questions?"
    How can we collaborate for my next research project? How much will it cost to make one? Is it hard to install? You can contact our team at [info@smartcitizen.me](mailto:info@smartcitizen.me)

The Smart Citizen Stations, from the enclosure to the electronics, are open source. Many components can be fabricated and assembled in a [Fab Lab](https://www.fablabs.io/). By doing so, we hope to encourage **fully open environmental systems**, ensuring reproducibility through accessible resources. We hope that this allows people to make use of the development effort in a distributed way. The _Stations_ come in different flavours and sizes. Sometimes, they are more bulky (the one in the picture above has roughly 15 sensors) and, sometimes, they are a bit smaller. Likewise, there are [air quality](https://docs.smartcitizen.me/hardware/stations/air.md) stations or [water](https://docs.smartcitizen.me/hardware/stations/water.md) ones.

!!! info "Check the Kit first"
    The Stations build on the core components of the Kit (which means, everything [here](https://docs.smartcitizen.me/hardware/kit/features.md) works in **exactly** the same way).

## Who are they for?

Stations can be used to gather _field-specific_ environmental data not only for scientific use but also as a tool to engage local communities with environmental topics. They are generally more complex to use, as they have more sensors and require a bit more involvement from the user. However, not all _Stations_ are the same, and because of that, we have developed some categorisations to help you navigate them.

!!!info ""
    On each page, you will see the _complexity grade_ for the unit, which gives an idea of whether or not the unit requires previous background knowledge. Here is a small explanation of what this _grade_ means:

    - :green_circle: **Basic**: These units are very similar to the [Smart Citizen Kit](https://docs.smartcitizen.me/hardware/kit.md), and they have one or two additional sensors that do not require any additional background knowledge or calibration experience.
    - :yellow_circle: **Intermediate**: These units are still similar to the [Smart Citizen Kit](https://docs.smartcitizen.me/hardware/kit.md), but they have at least one additional sensor that requires some extra care, either because it requires periodic recalibration or due to more complex maintenance.
    - :red_circle: **Advanced**: These beasts are larger and are generally not commercially available, as they require much more work to maintain, calibrate, or process the data.

## What versions are there?

!!! info ""
    The stations below are the current stable designs. If you are looking into developing other versions, feel free to reach out via [info@smartcitizen.me](mailto:info@smartcitizen.me).

- [SCK + 1xCHEM](https://docs.smartcitizen.me/hardware/stations/air/sck-1xchem.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure 1 chemical composition metric with an Alphasense B-series electrochemical sensor.
- [SCK + 2xCHEM](https://docs.smartcitizen.me/hardware/stations/air/sck-2xchem.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure 2 chemical composition metrics with two Alphasense A-series electrochemical sensors.
- [SCK + CO2 + 2xCHEM](https://docs.smartcitizen.me/hardware/stations/air/sck-co2-2xchem.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor and 2 chemical composition metrics with Alphasense A-series electrochemical sensors.
- [SCK + CO2 + HCHO](https://docs.smartcitizen.me/hardware/stations/air/sck-co2-hcho.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 and Formaldehyde!
- [SCK + CO2](https://docs.smartcitizen.me/hardware/stations/air/sck-co2.md) (Grade | intermediate): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure CO2 with a very reliable CO2 sensor!
- [SCK + T / RH](https://docs.smartcitizen.me/hardware/stations/air/sck-temp.md) (Grade | basic): Measure Indoor or Outdoor Air Quality with this unit. Beyond the metrics from the kit, it can measure temperature and humidity with a weatherproof probe!
- [Multi-Sensor Water Station](https://docs.smartcitizen.me/hardware/stations/water/sck-water-multi.md) (Grade | advanced): The Water Station is a multiparametric water unit, capable of measuring pH, Temperature, Dissolved Oxygen, Conductivity and ORP.
- [One-Sensor Water Station](https://docs.smartcitizen.me/hardware/stations/water/sck-water-single.md) (Grade | intermediate): The One-Sensor Water Station is meant to measure one physico-chemical parameter at a time. Choose from pH, Temperature, Dissolved Oxygen, Conductivity or ORP.

