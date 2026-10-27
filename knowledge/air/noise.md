<!-- Source: https://docs.smartcitizen.me/knowledge/air/noise/ -->

# Noise Measurements

Microphones are devices that can take noise measurements, which are sound pressure waves that travel through the air and reach our ears. Real-world sound pressure levels (SPL) travelling around in the air are not fully perceived by our ears, because our ears' cavities filter out some frequencies.

![](http://www.dspguide.com/graphics/F_22_1.gif)

_Image credit: [Human hearing - DSP Guide](http://www.dspguide.com/ch22/1.htm)_

There are several studies and models of what we actually perceive which yield several types of the so called **weighting functions**. Some of them have been standarised for the purpose of SPL measurement, finding different types like **[A-weighting](https://en.wikipedia.org/wiki/A-weighting#Deficiencies_of_A-weighting)** (the most common one), B-weighting, D (both in disuse) and others. In the frequency domain, they look like this:

![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Acoustic_weighting_curves_%281%29.svg/400px-Acoustic_weighting_curves_%281%29.svg.png" alt="Weighting table)

_Image credit: [A-weighting - Wikipedia](https://en.wikipedia.org/wiki/A-weighting#Deficiencies_of_A-weighting)_

Even if the are high sound pressure levels floating around in the air, we might not hear them just because of the frequency they are at. Normally humans can hear from something around 20Hz to 20kHz, although most adults might not hear anything in out-of-laboratory conditions above 15kHz. Some animals though, can perceive a [great range of frequencies](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Animal_hearing_frequency_range.svg/512px-Animal_hearing_frequency_range.svg.png), and for example mouses can hear up to 80kHz.

Microphones are very interesting in order to **understand sources of urban noise pollution** since it provides us with readings that we can process to obtain dBA levels (SPL with correction).

## Reference levels

Noise is one of the main environmental health risks in cities: long-term exposure is related to annoyance, sleep disturbance and cardiovascular disease. Noise levels are generally expressed in **dBA** (A-weighted decibels), and since the scale is logarithmic, an increase of 3 dB means **double** the sound energy, and an increase of 10 dB is perceived as roughly twice as loud.

Some typical sound levels, for orientation:

| Sound level (dBA) | Example |
|:-: |:- |
| 20 – 30 | Very quiet bedroom at night |
| 40 | Quiet library, quiet residential area at night |
| 50 – 60 | Normal conversation, office |
| 70 | Busy street, vacuum cleaner |
| 80 – 90 | Heavy traffic at close distance, loud restaurant |
| 100 – 110 | Concert, nightclub |
| 120+ | Close to a siren, threshold of pain |

The WHO Environmental Noise Guidelines for Europe recommend these **long-term** average levels [^1]:

| Source | Lden (day-evening-night) | Lnight (night) |
|:- |:-: |:-: |
| Road traffic | < 53 dB | < 45 dB |
| Railway | < 54 dB | < 44 dB |
| Aircraft | < 45 dB | < 40 dB |
| Wind turbines | < 45 dB | - |
| Leisure (yearly average of the exposure, for instance concerts or nightclubs) | < 70 dB LAeq,24h | - |

Indoors, the WHO Guidelines for Community Noise recommend keeping the average level below **35 dBA** in living areas during the day, and below **30 dBA** in bedrooms at night (with peaks below 45 dBA) [^2]. At work, the EU establishes that protective measures are needed above a daily exposure of **80 dBA**, hearing protection is mandatory above **85 dBA**, and the exposure must never exceed **87 dBA** (with hearing protection) [^3].

!!! info "Comparing with the guidelines"
    The guidelines refer to averages over long periods (a full day, a night, a year). Individual readings of the kit are short-term averages, so they need to be averaged over the same period before comparing them. Also, a single kit measures the noise at one point, and the levels can change a lot within a few meters (for instance, between the street side and the courtyard side of a building).

## Supported sensors

- [TDK ICS43432](https://docs.smartcitizen.me/knowledge/air/noise/TDK_ICS43432.md) (Field | air; Metric | noise; Connection | onboard): A MEMs microphone with high sensitivity, available on SCK2.X series by default.


## References

[^1]:
    World Health Organization. “Environmental Noise Guidelines for the European Region.” Copenhagen: WHO Regional Office for Europe, 2018. https://www.who.int/europe/publications/i/item/9789289053563.
[^2]:
    Berglund, Birgitta, Thomas Lindvall, and Dietrich H. Schwela. “Guidelines for Community Noise.” Geneva: World Health Organization, 1999. https://iris.who.int/handle/10665/66217.
[^3]:
    Directive 2003/10/EC of the European Parliament and of the Council of 6 February 2003 on the minimum health and safety requirements regarding the exposure of workers to the risks arising from physical agents (noise). https://eur-lex.europa.eu/eli/dir/2003/10/oj.