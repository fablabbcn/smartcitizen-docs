---
hide:
  - toc
---

# CO2 Measurements

<!-- TODO - Proofread + check on links -->

**Carbon dioxide (CO2)** is a colorless gas produced by the combustion of all carbon-based fuels, such as methane (natural gas), petroleum distillates (gasoline, diesel, kerosene, propane), coal, wood and generic organic matter. Carbon dioxide is the most significant long-lived greenhouse gas in Earth's atmosphere. Although not a pollutant *per se*, CO2 can also be considered an indicator of ventilation, and several international norms indicate levels of CO2 that are recommended depending on different indoor space categories (EN 15251, EN 16789, EN 13779 and ASHRAE 62.1 standards).

## Supported sensors

Most CO2 sensors in the _low cost range_ are [NDIR (NonDispersive InfraRed sensors)](https://en.wikipedia.org/wiki/Nondispersive_infrared_sensor), a type of _sensor_ that emits light and uses _infrared absorption_ to measure CO2. This is the principle that the [SCD30](/hardware/sensors/air/co2/Sensirion_SCD30/) uses, which you can directly plug into the [Auxiliary port](/hardware/Auxiliary Connector/) of the Smart Citizen Kit (2.1 and above). There are some other types of sensor, for instance the [SCD4X](/hardware/sensors/air/co2/Sensirion_SCD4X/) which is on its way to be supported on the SCK.

{{ insert_cards(type="sensor", filter="target", value=["co2"])}}