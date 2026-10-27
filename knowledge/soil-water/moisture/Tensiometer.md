<!-- Source: https://docs.smartcitizen.me/knowledge/soil-water/moisture/Tensiometer/ -->

# Tensiometer / Irrometer



![](https://docs.smartcitizen.me/assets/images/tensiometer-irrometer.jpg){.banner-box}

_Image Credit: **WATERMARK**_{.image-credit-banner-box}

!!! danger "WIP"
    This version is a WIP but is not fully functional with the SCK 2.1. It is shown here as a showcase of the project's capabilities. Have a look at the forum or drop us an email to discuss this. Check the source [files](https://github.com/fablabbcn/smartcitizen-grow/tree/master/soil-water-tension).

Soil Moisture data as the one provided by the Chirp Moisture Sensor is interesting for research, but when it comes to crops irrigation management, we usually like to know the soil water tension (SWT). That is because Soil Moisture in water is not directly related to the water plants roots might be able to extract because it is deeply affected by the soil composition. Even soil irrigation can be inferred from soil moisture when the soil type is known we think a soil tensiometer. Also when it is a simple solution, it is a useful tool for crops management.

![Watermark Tensionmeter Demo](https://docs.smartcitizen.me/assets/images/watermark.png)

The design is entirely open source and it is deeply inspired by the work of Reinier Van der Lee from the [Vinduino project](https://github.com/ReiniervdL/Vinduino), using an already calibrated commercial probe like the **Watermark 200SS9**. The sensor itself is straightforward and it consists of two stainless steel screws that work as electrodes cast inside a piece of plaster and covered by a plastic mesh to prevent erosion. As water is added more electrons can pass between the electrodes of the probe reducing the amount of resistance between them. By using this range of values, you can determine the amount of water that exists in your soil. To avoid interferences and degradation of the electrodes the design only applies voltage for a very short time and uses alternating electric polarities. For the sensor to work, we need a minimal circuit that uses two resistors and two diodes. The resistors work together with the electrodes to build a voltage divider. We can calculate the resistance value between the two electrodes by knowing the value of the resistors and the voltage. However to be able to alternate the electric current we need to duplicate the circuit and add two diodes. In total, we need 4 Pins to be connected to a microcontroller like the Arduino or the Smart Citizen Kit.

## Working principle

## Usage and considerations

There is no dedicated metric for the tensiometer: its output voltage is read by one of the [ADS1X15](https://docs.smartcitizen.me/knowledge/other/TI_ADS1X15.md) channels, depending on the address and channel where the sensor is connected:

| Metric | Shell name | Units | API |
|:- |:- |:-: |:- |
| Probe output voltage | `ADS1x15 ADC 0x48 Ch0` to `ADS1x15 ADC 0x4B Ch3` | V | See [ADS1X15](https://docs.smartcitizen.me/knowledge/other/TI_ADS1X15.md#usage-and-considerations) |

The design is entirely open source and it is deeply inspired by the work of Reinier Van der Lee from the [Vinduino project](http://vanderleevineyard.com/vineyard-blog.html), using an already calibrated commercial probe like the **Watermark 200SS9**. The sensor itself is straightforward and it consists of two stainless steel screws that work as electrodes cast inside a piece of plaster and covered by a plastic mesh to prevent erosion. As water is added more electrons can pass between the electrodes of the probe reducing the amount of resistance between them. By using this range of values, you can determine the amount of water that exists in your soil. To avoid interferences and degradation of the electrodes the design only applies voltage for a very short time and uses alternating electric polarities. For the sensor to work, we need a minimal circuit that uses two resistors and two diodes. The resistors work together with the electrodes to build a voltage divider. We can calculate the resistance value between the two electrodes by knowing the value of the resistors and the voltage. However to be able to alternate the electric current we need to duplicate the circuit and add two diodes. In total, we need 4 Pins to be connected to a microcontroller like the Arduino or the Smart Citizen Kit.

### Measurement range

The Watermark 200SS probe measures **soil water tension** in a range of **0 to 239 centibars (kPa)**, according to the manufacturer. A reading of 0 means saturated soil, and higher readings mean drier soil (the plants need to make more effort to extract water from it). Check the [soil moisture page](https://docs.smartcitizen.me/knowledge/soil-water/moisture.md#reference-levels) to interpret the readings.

## Resources