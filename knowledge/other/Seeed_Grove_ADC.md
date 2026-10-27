<!-- Source: https://docs.smartcitizen.me/knowledge/other/Seeed_Grove_ADC/ -->

# Seeed Grove ADC

An ADC breakout board by Seeed Studio.

![](https://docs.smartcitizen.me/assets/images/seeed-grove-adc.jpg){.banner-box}

_Image Credit: **Seeed Studio**_{.image-credit-banner-box}

!!! warning "Under Construction"

    More details on working principles, usage, considerations, and resources are coming soon.

## Usage and considerations

The following metrics are available:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| Input voltage | `Groove ADC` | V | [25](https://api.smartcitizen.me/v0/sensors/25) |

### Performance

|Property               |Value                                                                          |
|:-                     |:-                                                                             |
|Converter type         |TI ADC121C021, 12-bit ADC with digital interface (I2C)                         |
|Resolution             |12 bits                                                                        |
|Channels               |1                                                                              |
|Input range (SCK)      |0 – 6.6V (the firmware uses a 3.3V reference and the 1/2 input divider of the board) |
|I2C address            |`0x59`                                                                         |