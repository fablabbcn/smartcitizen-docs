<!-- Source: https://docs.smartcitizen.me/knowledge/soil-water/ -->

# Soil and water measurements

*Water measurements* are a bit more complex than those in air, at least for _lower-cost sensors_. Here, we are generally limited to physico-chemical parameters such as pH, conductivity, dissolved oxygen and similar. Similar to [air measurements](https://docs.smartcitizen.me/knowledge/air.md), when the data board by itself can't read the sensor directly, we need to use _interface electronics_ to get reading from them.

!!! info "Before we start"

    **Two important notes:**
    
    1. A lot of the materials from this guide are taken from [Atlas Scientific](https://atlas-scientific.com) datasheets. All credit to the well-designed images is theirs. We have integrated these probes in the Smart Citizen Kit because of their quality and good documentation. **This page is not meant to be a replacement for Atlas Scientific documents and we do not have any affiliation to Atlas Scientific**.
    2. There is also additional webinars that can support this page in more detail. Here [you can find the presentation](https://s3.eu-west-3.amazonaws.com/storage.smartcitizen.me/presentations/Minke-WEBINAR_WQ.pdf) and the link to the videos below:
        - [Smart Citizen Webinar - 3.1 Water sensors (Part 1)](https://www.youtube.com/watch?v=u4zUqcp17-g&list=PL33KKs9g8Y1IWsTZZmDc-46yFuuIRZEmi&index=10)
        - [Smart Citizen Webinar - 3.2 Water sensors (Part 2)](https://www.youtube.com/watch?v=aGtT2JRmkaY&list=PL33KKs9g8Y1IWsTZZmDc-46yFuuIRZEmi&index=12)
        - [Smart Citizen Webinar - 3.3 Water sensors preparation](https://www.youtube.com/watch?v=xpk4Jxd-E04&list=PL33KKs9g8Y1IWsTZZmDc-46yFuuIRZEmi&index=13)
        - [Smart Citizen Webinar - 3.4 Water sensors calibration](https://www.youtube.com/watch?v=FXsMiyONtF4&list=PL33KKs9g8Y1IWsTZZmDc-46yFuuIRZEmi&index=14)
        - [Smart Citizen Webinar - 3.5 Water sensors deployment](https://www.youtube.com/watch?v=b3ftsRNpDzA&list=PL33KKs9g8Y1IWsTZZmDc-46yFuuIRZEmi&index=15)

## Supported sensors

- [Atlas DO](https://docs.smartcitizen.me/knowledge/soil-water/DO/Atlas_DO.md) (Field | water; Metric | dissolved oxygen; Connection | external): A galvanic probe that can measure dissolved oxygen in water.
- [Atlas EC](https://docs.smartcitizen.me/knowledge/soil-water/EC/Atlas_EC.md) (Field | watersoil; Metric | electrical conductivity; Connection | external): A conductivity meter to measure electrolytes in a liquid!
- [Atlas ORP](https://docs.smartcitizen.me/knowledge/soil-water/ORP/Atlas_ORP.md) (Field | water; Metric | orp; Connection | external): An ORP probe is a passive device that detects a current generated from the oxidation or reduction of chemical substances in water.
- [Atlas Temperature](https://docs.smartcitizen.me/knowledge/soil-water/temperature/Atlas_Temperature.md) (Field | watersoil; Metric | temperature; Connection | external): An encapsulated resistive sensor (RTD, resistance temperature detector).
- [Atlas pH](https://docs.smartcitizen.me/knowledge/soil-water/pH/Atlas_pH.md) (Field | watersoil; Metric | pH; Connection | external): The pH probe is a very delicate submerged electrode in a thin glass bubble.
- [Chirp Soil Moisture](https://docs.smartcitizen.me/knowledge/soil-water/moisture/Chirp_Soil_Moisture.md) (Field | soil; Metric | moisture; Connection | external)
- [Tensiometer / Irrometer](https://docs.smartcitizen.me/knowledge/soil-water/moisture/Tensiometer.md) (Field | soil; Metric | soil tension; Connection | external)
