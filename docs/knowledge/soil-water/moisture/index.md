---
internal:
  proofread: false
  links: false
  images: false
---

# Soil Moisture Measurements

Soil moisture sensors can be used for schedule irrigations (i.e. determine when to water the plants); or for calculating soil water deficit to work out how much water to apply.

## Reference levels

For irrigation, the most useful measurement is the **soil water tension**, which tells how much effort the plants need to extract water from the soil, independently of the type of soil. These are the reference levels for the [Watermark tensiometer](/knowledge/soil-water/moisture/Tensiometer/), according to the manufacturer [^1]:

| Soil water tension (centibars) | Interpretation |
|:-: |:- |
| 0 – 10 | Saturated soil |
| 10 – 30 | Soil is adequately wet (except coarse sands, which are beginning to lose water) |
| 30 – 60 | Usual range to irrigate (most soils) |
| 60 – 100 | Usual range to irrigate in heavy clay soils |
| 100 – 200 | Soil is becoming dangerously dry |

Capacitive sensors like the [Chirp](/knowledge/soil-water/moisture/Chirp_Soil_Moisture/) give a relative value (%) between their dry and wet calibration points, so the right level for irrigation depends on the soil and the crop. A good practice is to note the reading right after a deep irrigation (field capacity) and the reading when plants start to show stress, and use them as the upper and lower references.

## Supported sensors

{{ insert_cards(type="sensors", filter="field", value=["soil"]) }}

## References

[^1]:
    IRROMETER Company. “WATERMARK Soil Moisture Sensor - Model 200SS.” https://www.irrometer.com/pdf/403.pdf.
