---
card: true
type: unit
custom_color: blue
name: Smart Citizen Stations
short_name: Stations
feature_img: https://live.staticflickr.com/65535/50977039556_541c4727a6_k.jpg
excerpt: The Smart Citizen Stations are open-source environmental monitoring systems. They build upon the functionalities of the Smart Citizen Kit, extending its sensing capabilities.
---

# {{ name }}

![]( {{ feature_img }})

## What are the _{{ name }}_?

The {{ name }} (_{{ short_name }}_ for short) are **open-source environmental monitoring systems**. They build upon the functionalities of the [Smart Citizen Kit](/hardware/kit/), extending its sensing capabilities. The idea behind is to leverage the modularity of the [hardware](/hardware) and include more sensors, making some changes on the enclosures to make everything fit. Any of the sensors in the list of [supported sensors](/knowledge/) can be used to build a _Station_. Below you have a summary of the most common configurations to get a taste of what it can do. Make sure to check the dedicated sections for each to get a complete description!

!!! tip "Questions?"
    How can we collaborate for my next research project? How much will it cost to make one? Is it hard to install? You can contact our team at [{{ extra.urls.info.name }}]({{ extra.urls.info.link }})

The {{ name }}, from the enclosure, to the electronics, are _obviously_ open source. Many components can be fabricated and assembled in a [Fab Lab](https://www.fablabs.io/). By doing so, we hope to encourage **fully open environmental systems**, ensuring reproducibility through accessible resources. We hope that this allows people to make use of the development effort in a distributed way. The _{{ short_name }}_ come in different flavours and sizes. Sometimes, they are more bulky (the one in the picture above has roughly 15 sensors) and, sometimes, they are a bit smaller. For instance, there are [air quality](/hardware/stations/air/) stations, or [water](/docs/hardware/stations/water/) ones.

!!! info "Check the Kit first"
    The {{ short_name }} build on the core components of the Kit (which means, everything [here](/hardware/kit/features/) works in **exactly** the same way).

## Who are they for?

The units can be used by to gather _field-specific_ environmental data, not only from a scientific point of view but also as a tool to engage local communities on environmental topics. They are generally more complex to use, as they have more sensors, and require a bit more involvement from the user, however, not all _{{ short_name }}_ are the same, and because of that, we have developed some categorisation to help you navigate them.

!!!info ""
    On each page, you will see the _complexity grade_ for the unit, which gives an idea of whether or not the unit requires previous background knowledge or not. Here is a small explanation of what this _grades_ mean:

    - :green_circle: **Basic**: These units are very similar to the [Smart Citizen Kit](/hardware/kit/), and they have one or two additional sensors that do not require any additional background knowledge, or calibration experience.
    - :yellow_circle: **Intermediate**: These units are still similar to the [Smart Citizen Kit](/hardware/kit/), but they have at least one additional sensors that requires some extra care: either because it requires periodic recalibration, or because they have some more
    - :red_circle: **Advanced**: These units are bigger beasts, and are generally not commercially available, as they require much more work to maintain, calibrate, or process the data.

## What versions are there?

{{ insert_cards(type="stations", filter="field", value=["air", "water"]) }}
