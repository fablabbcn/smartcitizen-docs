---
field: soil
target: moisture
type: external
feature_img: /assets/images/chirp.png
status: stable
versions:
    hardware: 2.1
    firmware: 0.9.8
---

# Soil Moisture

The Chirp! Sensor is a low cost moisture and temperature sensor developed by [WeMakeThings](https://wemakethings.net/chirp/): a hackers and engineers collective based in Vilnius, Lithuania. Their hardware and software are fully open-source, and it can be easily integrated but also replicated and customized for new projects.

## Working principle

The sensor uses capacitive sensing to measure soil's moisture. A 1MHz square wave is output from the chip through a resistor into a big pad that, together with the surrounding ground plane, it forms a parasitic capacitor. The resistor and the capacitor create a low pass filter which cut-off frequency changes with changing capacitance. The soil around the sensor acts as an electrolyte whose dielectric constant changes depending on the amount of moisture in it, so the capacitance of our makeshift capacitor changes too. The filtered square wave is then fed into a peak detector formed of out a diode and a capacitor. An ADC measures this voltage in the microcontroller. The sensor also includes a temperature sensor with a calculated absolute measurement accuracy around 2%.

## Usage and considerations

<!-- TODO - Check if we want to do this -->

There are different versions of the Chirp sensor, and for this application we chose the Chirp I2C sensor. The sensor was integrated on to the SCK's firmware, and it is automatically recognized by the board once it is plugged into the SCK using the Aux sensor connector. A Grove 4 pin Female Jumper to Grove will need to be used with the sensor to connect it to the SCK. The original Chirp sensors come coated with PRF202 - a moisture resistant varnish for electronics, but it is not enough for actual deployment. For such, one must add additional protection to the whole sensor. We suggest polyester or epoxy resin. However, you must note that sensitivity of the sensor will decrease depending on how thick the layer you are going to apply and might need to be recalibrated. We also recommend covering the electronics with heat shrink to fully waterproof the sensor. Some versions already include a pre-ruggedized sensor, which is a recommended solution for a faster use.

![](/assets/images/chirp_01.jpg)

### Sensor validation

![](/assets/images/chirp_02.jpg)

Three Chirp sensors were compared to the [Parrot](https://www.parrot.com/) Flower Power (now discontinued). The Flower Power can measure several metrics, such as light, temperature, fertilizer and soil moisture. In this test, we compared the soil moisture readings for three Flower Parrot sensors, compared to three Chirp sensors. Both sensors show a good behaviour and the values can be correlated with good R2 scores. The approach for this low-cost sensors, in general, should be more qualitative than quantitative (analyse the trends rather than the absolute values), since their values appear to differ between sensors, even when normalised. In the particular case of the Chirp sensor, the sensor seems to be fairly normalised with simply a two calibration values (water and air) as a first approach.

![](/assets/images/chirp_test.png)

## Resources
