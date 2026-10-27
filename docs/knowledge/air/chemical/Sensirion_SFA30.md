---
card: true
name: Sensirion SFA30
field:
  - air
type:
  - external
target:
  - vocs
feature_img: /assets/images/sensirion-sfa30.jpg
feature_img_credit: "Seeed Studio"
excerpt: "An electrochemical sensor for measuring formaldehyde (HCHO)."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! info "Smart Citizen Station"
    This sensor is part of the [SCK CO2 + HCHO](/hardware/stations/air/sck-co2-hcho/) station.

## Working principle

**Formaldehyde** (HCHO) is a VOC commonly found in indoor environments, emitted by furniture, building materials (pressed wood, insulation), glues, paints or cleaning products. It is classified as a carcinogen, and several organisations have defined indoor exposure guidelines for it [^1].

The SFA30 is an **electrochemical** sensor. Like the [Alphasense electrochemical sensors](/knowledge/air/chemical/Alphasense_Electrochemical/), the target gas reacts on the surface of an electrode inside the sensor, producing a small electric current that is proportional to the gas concentration. Unlike most VOC sensors, which measure the total amount of VOCs (tVOC), the SFA30 is designed to be **selective** to formaldehyde, with a low cross-sensitivity to other VOCs like ethanol [^2].

The sensor integrates the electronics to amplify the signal, a temperature and humidity sensor for compensation, and the algorithms to convert the signal into a concentration, so it provides a calibrated digital output.

## Usage and considerations

### Connection

The SFA30 can be directly connected to the [Auxiliary connector](/hardware/boards/data-board#auxiliary-connector) on the data board. If you use the Seeed Studio Grove version, use a [4-wire grove cable](https://www.seeedstudio.com/cables-c-949.html). For other boards, use [4-wire grove to female header cables](https://www.seeedstudio.com/Grove-4-pin-Female-Jumper-to-Grove-4-pin-Conversion-Cable-5-PCs-per-PAck.html) or a [grove to screw connector](/guides/getting-started/third-party-sensors/#sensors-with-open-leads). The sensor communicates via I2C, on the address `0x5D`.

The sensor is enabled in all the default _air_ firmware builds (SCK2.1 onwards), and it is automatically detected on boot. The following metrics are available:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| Formaldehyde | `SFA30 Formaldehyde` | ppb | [212](https://api.smartcitizen.me/v0/sensors/212) |
| Temperature | `SFA30 Temperature` | ºC | [211](https://api.smartcitizen.me/v0/sensors/211) |
| Humidity | `SFA30 Humidity` | % | [210](https://api.smartcitizen.me/v0/sensors/210) |

You can check the readings with the `read` and `monitor` commands:

```
read sfa30 formaldehyde
```

### Considerations

The [datasheet](https://sensirion.com/products/catalog/SFA30) can be found on Sensirion's website.

!!! warning "Stabilisation"
    As with all electrochemical sensors, the readings need some time to stabilise after the sensor is powered on. Do not trust the first readings after connecting the sensor.

!!! info "Temperature and humidity"
    The temperature and humidity sensor inside the SFA30 is mainly meant for the internal compensation of the formaldehyde readings, and might be affected by the heat of the sensor itself. For air temperature and humidity, use the [SHT3X](/knowledge/air/temperature_rel_humidity/Sensirion_SHT3X/) in the Urban Board.

The sensor does not have any control commands in the SCK firmware.

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Sensor type            |Electrochemical sensor with digital interface (I2C)                            |
|Measurement range      |0 – 1000 ppb                                                                   |
|Accuracy               |±20 ppb or ±20% of reading (the larger)                                        |
|Deployment type        |Indoor                                                                         |

!!! info "Check the latest datasheet"
    The specifications above are taken from the manufacturer's datasheet at the time of writing. Check the [product page](https://sensirion.com/products/catalog/SFA30) for the latest values.

### Limitations

Electrochemical sensors are affected by changes in temperature and humidity, and their sensitivity decreases over time, so they have a limited lifetime. They can also show interferences to other gases. Given the low concentrations of formaldehyde that are relevant for health, and the accuracy of the sensor, the SFA30 is better suited for **detecting sources and trends** of formaldehyde in indoor spaces, rather than for an accurate assessment of exposure.

## Resources

- [Official product page and datasheet](https://sensirion.com/products/catalog/SFA30)
- [Firmware implementation](https://github.com/fablabbcn/smartcitizen-kit-2x/blob/master/sam/src/SckAux.cpp)

### References

[^1]:
    World Health Organization. “WHO Guidelines for Indoor Air Quality: Selected Pollutants.” Copenhagen: WHO Regional Office for Europe, 2010. https://www.who.int/publications/i/item/9789289002134.
[^2]:
    Sensirion. “SFA30 Formaldehyde Sensor Module - Datasheet.” https://sensirion.com/products/catalog/SFA30.
