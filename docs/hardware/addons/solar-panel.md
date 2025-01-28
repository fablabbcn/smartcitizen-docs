---
card: true
name: Solar Panel
feature_img: https://cdn11.bigcommerce.com/s-6ubn8z08et/images/stencil/500x659/products/185/1049/Bracket_Pole_Mount-6_Watt_Panel__96828.1583444808.jpg
custom_color: black
type:
    - addon
excerpt: Solar Panels can be a good option for powering your Smart Citizen Kit or Station.
---

# {{ name }}

{{ excerpt }}

![]({{ feature_img }})
> Image credit: [Voltaic System](https://voltaicsystems.com/6-watt-panel/).

## Hardware

We recommend a Solar Panel from [Voltaic Systems](https://voltaicsystems.com/). You can buy a complete system or build your own from other components. Check the [BOM](#bom) below for options.

### Calculating the system

To calculate the system, you will need to estimate the hardware energy consumption and the solar radiation in your area. With that, you will be able to estimate thesize of your solar panel and the batteries needed. Bigger batteries can be used as a back-up, but in certain locations, there may be need for large size pannels. Depending on your budget, you will need to maybe compromise data frequency, or in some panel/battery/hardware and location combinations, the devices may be offline.

!!! info "Check the discussion"
    Check the discussion with our recommendations on the [forum](https://forum.smartcitizen.me/t/solar-panel-estimations/1805).

### BOM

Our default solar panel proposal is the [Voltaic Systems 6W 6V Solar Panel](https://voltaicsystems.com/6-watt-panel/). This is enough to power the SCK in places like Barcelona, Spain. In other locations, or with other hardware, you may need to increase the size of the solar panel (see [above](#calculating-the-system)). The solar panel is totally waterproof, and we recommend using proper extension cables as indicated in the tables below. We also recommend using the [solar panel bracket](https://voltaicsystems.com/bracket/) for attachment to walls or lampposts.

=== "MPTT option"

    This option is recommended for **small hardware setups**, like the SCK with small add-ons (like a temperature sensor). This setup uses a [DF Robot MPTT Sunflower Solar power manager 5V](https://wiki.dfrobot.com/Solar_Power_Manager_5V_SKU__DFR0559) for managing the solar input with an additional 2Ah battery. It is fitted inside the enclosure with a small laser cut (or 3D printed if not available) flange. You can find all the design files in the [online repository](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Power%20Options/Solar).

    ![](/assets/images/dfrobot.jpeg)

    | Item | Source | Information|
    |:-    |:-:     |:-:  |
    | 6W 6V Solar Panel (or other f) | Voltaic Systems | [Link](https://voltaicsystems.com/6-watt-panel/) |
    | Extension cable | Voltaic Systems | [Link](https://voltaicsystems.com/3511-ext-10ft/) |
    | Open leads cabling | Voltaic Systems | [Link](https://voltaicsystems.com/extension-with-exposed-leads/) |
    | Mounting bracket | Voltaic Systems | [Link](https://voltaicsystems.com/bracket/) |
    | MPTT  | DF Robot DFR0559| [Link](https://wiki.dfrobot.com/Solar_Power_Manager_5V_SKU__DFR0559) |
    | Battery  | Any 2000mAh LiPo | [Link](/assets/datasheets/batteries/PL804050_2000mAh/PL804050_2000mAh_Datasheet.pdf) |
=== "Battery pack option"

    For bigger setups, you can choose a complete [solar panel system](https://voltaicsystems.com/iot/), or break it down as below:

    | Item | Source | Information|
    |:-    |:-:     |:-:  |
    | 6W 6V Solar Panel | Voltaic Systems | [Link](https://voltaicsystems.com/6-watt-panel/) |
    | Extension cable | Voltaic Systems | [Link](https://voltaicsystems.com/3511-ext-10ft/) |
    | Open leads cabling | Voltaic Systems | [Link](https://voltaicsystems.com/extension-with-exposed-leads/) |
    | Mounting bracket | Voltaic Systems | [Link](https://voltaicsystems.com/bracket/) |
    | Battery Pack  | Voltaic Systems | [Link](https://voltaicsystems.com/iot-battery-packs/) |

!!! info "Source files"
    Find all the information [here](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Power%20Options#solar-panel)

## Handling

### Physical installation

Use the bracket to install the panel according to the recommended [panel orientation for your location](#panel-orientation). The SCK can be up to 3m away from the solar panel. This example image shows how the panel should look once in place:

![](https://cdn11.bigcommerce.com/s-6ubn8z08et/images/stencil/500x659/products/185/1049/Bracket_Pole_Mount-6_Watt_Panel__96828.1583444808.jpg)
> Image credit: [Voltaic Systems](https://voltaicsystems.com)

### Panel orientation

It is important to orient the solar panel properly to get the maximum amount of sunlight in the proper angle.

!!! info "Reference"
    [This is a nice calculator](http://www.solarelectricityhandbook.com/solar-angle-calculator.html) to orient the panel depending on your location.

Solar panels should always face **true south in the Northern Hemisphere** and **North in the Southern Hemisphere**. The orientation of the solar panel with respect to the horizontal plane should be _roughly_ at a degree equal to your latitude plus 15 degrees in winter, or minus 15 degrees in summer. Some more fine tuning can achieve better efficiency for fixed solar panels. Since the winter season has the least amount of sun, you want to make the most of it. In this case, the tilt should be designed so that the panel points directly at the sun at noon. To calculate, multiply your latitude by 0.9, and add 30 degrees.
