---
card: false
name: Seeed Grove ADC
field:
  - other
type:
  - external
target:
  - location
feature_img: /assets/images/seeed-grove-adc.jpg
feature_img_credit: "Seeed Studio"
excerpt: "An ADC breakout board by Seeed Studio."
---

# {{ name }}

{%if excerpt %}{{ excerpt }}{%endif%}

{%if feature_img %}![]({{feature_img}}){.banner-box}{%endif%}

{%if feature_img_credit %}_Image Credit: **{{ feature_img_credit }}**_{.image-credit-banner-box}{%endif%}

!!! warning "Under Construction"

    More details on working principles, usage, considerations, and resources are coming soon.

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Converter type         |TI ADC121C021, 12-bit ADC with digital interface (I2C)                         |
|Resolution             |12 bits                                                                        |
|Channels               |1                                                                              |
|Input range (SCK)      |0 – 6.6V (the firmware uses a 3.3V reference and the 1/2 input divider of the board) |
|I2C address            |`0x59`                                                                         |
