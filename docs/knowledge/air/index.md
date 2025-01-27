---
hide:
    - toc
---

# Air measurements

*Air measurements* are the most common use case in the Smart Citizen Kit. These are measurements that imply measuring _physical_ properties of the air (temperature, pressure, relative humidity), things that _are_ in the air (gases, particulate matter) or things that _travel through_ the air (noise, ambient light, UV-index). For this, we use a series of different sensors. These sensors can be _standalone units_ (for instance, a CO2 sensor), or can be in _sensor boards_. When the data board by itself can't read the sensor directly, we need to use _interface electronics_ to get reading from them. Below you can find a list of metrics that are already supported, but bear in mind that there are plenty of other options possible!

- [Particulate Matter](pm/index.md)
- [Temperature and relative humidity](temperature_rel_humidity/index.md)
- [Barometric pressure](pressure/index.md)
- [Noise](noise/index.md)
- [Light](light/index.md)
- [CO2](co2/index.md)
- [Chemical composition (besides CO2)](chemical/index.md), including [VOCs](chemical/index#vocs)

## Supported sensors

{{ insert_cards(type="sensors", filter="field", value=["air"]) }}