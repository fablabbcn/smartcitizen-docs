---
card: true
name: Power Supply
feature_img: https://live.staticflickr.com/65535/54334059575_d4968cf083_h.jpg
custom_color: black
type:
    - addon
excerpt: The Smart Citizen Power Supply is a simple power supply to power the SCK and the Smart Citizen Station.
---

# Smart Citizen Power Supply

![]({{ feature_img }})

{{ excerpt }} It supports an input of 110-230 VAC, including a 1.6A input fuse protection and a 5VDC regulated output.

The power supply can be one of two options:

- MeanWell-IRM-10-5 (datasheet in References folder and [here](https://www.meanwell.com/Upload/PDF/IRM-10/IRM-10-SPEC.PDF))
- TracoPower-TMPS-10105 (datasheet in References folder and [here](https://www.tracopower.com/products/tmps10.pdf))

Check the datasheets for other available input convertions and limits.

## Enclosure

The PCB has the footprint to fit inside a [Bopla Ref. 38102200](https://octopart.com/search?q=bopla+38102200) IP65 Enclosure with two built-in cable glands.

A [Bopla Polymas PK 102-211](https://www.bopla.de/en/enclosure-technology/product/euromas-polymas/euromas-polymas-enclosures/pk-102-211.html) enclosure is used. The models can be found in the manufacturer's site in STP format.

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Power%20Options#smart-citizen-power-supply" aria-label="Check the source code">Check the source</a>

## Handling

The power supply is very simple to operate. If you have purchased one, normally, everything should be connected and ready to go. In some cases, the AC cable (left screw connector) is not connected, and it can be simply connected through the cable gland into the terminals. No ground is required.

![](/assets/images/power-supply-off.jpeg)

When connecting the plug to the wall socket, the red LED should turn on indicating 5V output. The input is protected with a 1A Fuse and the pack should be enclosed in a waterproof enclosure as detailed [here](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Power%20Options).

The indication LED shows the Power Supply is active. It is also a warning in case you have unplugged it but there is still some charge in it (it might take some seconds to fade out):

![](https://i.imgur.com/rVHeuyY.jpg)
![](/assets/images/power-supply-on.jpeg)

More information regarding the power input is shown below and available [in the datasheet](hhttps://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Power%20Options/References/IRM-10-SPEC.PDF):

- Input range: 100V-240VAC 50-60Hz, max 0.25A input, 1A Fused, or 277VAC 0.125A, also 50-60Hz
- Output range: 5V DC, max 2.0A
