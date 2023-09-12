# Solar Panel

Solar Panels can be a good option for powering your SCK (and maybe some stations).

!!! warning "What is this for?"
    Currently, and depending on the location, this option is only usable for the Smart Citizen Kit with small accessories, like a CO2 sensor and _maybe_ electrochemical sensors, but it's not suitable for a larger options like the Smart Citizen Station. For this, we recommend a larger solar panel with a lead-acid battery instead as back-up.

![](https://cdn11.bigcommerce.com/s-6ubn8z08et/images/stencil/500x659/products/185/1049/Bracket_Pole_Mount-6_Watt_Panel__96828.1583444808.jpg)
_Image credit: [Voltaic System](https://voltaicsystems.com/6-watt-panel/)_

## Calculating the system

TODO

## Hardware options

We recommend a Solar Panel from [Voltaic Systems](https://voltaicsystems.com/), either with their [battery packs](TODO) or with a [dedicated MPTT](#dedicated-mptt).

### Dedicated MPTT

We use an [MPTT Sunflower Solar power manager 5V](https://wiki.dfrobot.com/Solar_Power_Manager_5V_SKU__DFR0559) from DF Robot for managing the solar input with an additional 2Ah battery. It is fitted inside the enclosure with a small laser cut (or 3D printed if not available) flange. This is the [BOM](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Power%20Options/Solar) for this option.

![](/assets/images/dfrobot.jpeg)

!!! info "Installation"
    Have a look at the installation guide for [Solar Panel](/Guides/deployments/Installing solar panel/)

!!! info "Source files"
    Find all the information [here](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Power%20Options#solar-panel)