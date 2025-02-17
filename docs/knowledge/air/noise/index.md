# Noise Measurements

Microphones are devices that can take noise measurements, which are sound pressure waves that travel through the air and reach our ears. Real-world sound pressure levels (SPL) travelling around in the air are not fully perceived by our ears, because our ears' cavities filter out some frequencies.

![](http://www.dspguide.com/graphics/F_22_1.gif)

_Image credit: [Human hearing - DSP Guide](http://www.dspguide.com/ch22/1.htm)_

There are several studies and models of what we actually perceive which yield several types of the so called **weighting functions**. Some of them have been standarised for the purpose of SPL measurement, finding different types like **[A-weighting](https://en.wikipedia.org/wiki/A-weighting#Deficiencies_of_A-weighting)** (the most common one), B-weighting, D (both in disuse) and others. In the frequency domain, they look like this:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Acoustic_weighting_curves_%281%29.svg/400px-Acoustic_weighting_curves_%281%29.svg.png" alt="Weighting table)

_Image credit: [A-weighting - Wikipedia](https://en.wikipedia.org/wiki/A-weighting#Deficiencies_of_A-weighting)_

Even if the are high sound pressure levels floating around in the air, we might not hear them just because of the frequency they are at. Normally humans can hear from something around 20Hz to 20kHz, although most adults might not hear anything in out-of-laboratory conditions above 15kHz. Some animals though, can perceive a [great range of frequencies](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Animal_hearing_frequency_range.svg/512px-Animal_hearing_frequency_range.svg.png), and for example mouses can hear up to 80kHz.

Microphones are very interesting in order to **understand sources of urban noise pollution** since it provides us with readings that we can process to obtain dBA levels (SPL with correction).

## Supported sensors

{{ insert_cards(type="sensor", filter="target", value=["noise"])}}
