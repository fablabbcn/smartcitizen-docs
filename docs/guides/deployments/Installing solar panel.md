# Installing solar panel

This guide walks through the process for installing a Solar Panel with the Smart Citizen Kit.

!!! warning ""
    This guide is a work-in-progress

## Components

Our default solar panel proposal is a [Voltaic Systems 6W 6V Solar Panel](https://voltaicsystems.com/6-watt-panel/). The solar panel is totally water proof, and we recommend using [extension cable](https://voltaicsystems.com/3511-ext-10ft/) and [open leads cabling](https://voltaicsystems.com/extension-with-exposed-leads/) for connecting it to our MPTT proposal, the [MPTT DF Robot DFR0559](https://wiki.dfrobot.com/Solar_Power_Manager_5V_SKU__DFR0559). We also recommend using the [solar panel bracket](https://voltaicsystems.com/bracket/) for attachment to walls or lampposts.

| Item | Source | Information|
|:-    |:-     |:-  |
| 6W 6V Solar Panel | Voltaic Systems | [Link](https://voltaicsystems.com/6-watt-panel/) |
| Xxtension cable | Voltaic Systems | [Link](https://voltaicsystems.com/3511-ext-10ft/) |
| Open leads cabling | Voltaic Systems | [Link](https://voltaicsystems.com/extension-with-exposed-leads/) |
| Mounting bracket | Voltaic Systems | [Link](https://voltaicsystems.com/bracket/) |
| MPTT  | DF Robot DFR0559| [Link](https://wiki.dfrobot.com/Solar_Power_Manager_5V_SKU__DFR0559) | 
| Battery  | DF Robot DFR0559 | [Link](https://wiki.dfrobot.com/Solar_Power_Manager_5V_SKU__DFR0559) | 

## Installation

### Physical installation

Use the bracket to install the panel according to the panel orientation below. The SCK can be up to 3m away from the solar panel. This example image shows how the panel should look once in place:

![](https://cdn11.bigcommerce.com/s-6ubn8z08et/images/stencil/500x659/products/185/1049/Bracket_Pole_Mount-6_Watt_Panel__96828.1583444808.jpg)
Image credit: [Voltaic Systems](https://voltaicsystems.com)

### Panel orientation

It is important to orient the solar panel properly to get the maximum amount of sunlight in the proper angle.

!!! info "Reference"
    [This is a nice calculator](http://www.solarelectricityhandbook.com/solar-angle-calculator.html) for your location.

Solar panels should always face **true south in the Northern Hemisphere** and **North in the Southern Hemisphere**. The orientation of the solar panel with respect to the horizontal plane should be at a degree equal to your latitude plus 15 degrees in winter, or minus 15 degrees in summer (roughly). A bit more advanced tweaking, could achieve better efficiency for fixed solar panels. Since the winter season has the least sun, you want to make the most of it. In this case, the tilt should be designed so that the panel points directly at the sun at noon. To calculate, multiply your latitude by 0.9, and add 30 degrees.

The 6W 6V solar panel that we suggest using, is calculated for having enough amount of insolation during winter in Spain's latitude, considering the amount of hours/day there is sun in winter. A larger solar panel can be used for higher latitudes (or further south), with less hours/day of insolation.
