# Making your own enclosures

This page compiles instructions on how to make your own enclosures. We normally use digital fabrication techniques that can be found in a Fablab such a 3D printing, laser cut or CNC machines. Have a look at the best option for your possibilities. We also encourage you to modify any of them and contribute it back to the community in the [enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures/).

!!! info "Where to print/cut?"
    Have a look at [Hubs](https://www.hubs.com/) or look for a [Fablab near you](https://fablabs.io/labs)!

## CNC Enclosure

This enclosure is made out of a mix of HDPE, acrylic and 3D printed compontents. All the design files can be find in various formats in the [enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle).

![](https://raw.githubusercontent.com/fablabbcn/smartcitizen-enclosures/master/SmartCitizen%20Outdoor%20Cases%20V2.0-2.1/Milled%20HDPE/final_render.png)

### 3D printing parts

**Clip**

![](/assets/images/clip-front.jpg)

The SCK and the PMS5003 are held together by a 3D printed clip. No support is needed for this part. The clip is attached to the base with screws.

<img src="https://live.staticflickr.com/65535/48439505406_c313e7eda3_h.jpg" alt="SCK 2.1 Outdoor enclosure">

There are **two versions** of the clip:

- One for big batteries that uses an o-ring to hold the battery in place. You can also use a rubber band, but it won't last long under the sun - [clip_big_batt.stl](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/clip_big_batt.stl)
- One for smaller batteries that uses the PMS5003 cable to hold the battery (valid for default battery of 2000mAh) - [clip_wo_oring.stl](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/clip_no_oring.iges)

**Cable gland**

There is a small cable gland (part [1](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/CAP1.stl) and [2](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/CAP2.stl))that fits into the HDPE blue base to hold the cable in place. It's split into two, so that the USB head can go through.

**Foam cover**

An additional [foam cover](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/CLIP-FOAM.stl) has been included for high humidity environments. The print settings in [SliC3r](https://slic3r.org) need to be adapted with:

- 0.2mm layer height
- Detect thin walls

### CNC'ed parts

CNC milling of 15mm HDPE sheets for the base (we make it in blue), and 10mm for the top (we make it in white).

**Base**

The [base](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/base.step) is made out of a ouble sided milling on blue HDPE. The holes are for self-tightening screws (such as [these ones](https://www.celofixings.es/tornillos-rosca-plasticos/2834-tornillo-rosca-plastico-cl81z-celoplast-cabeza-alomada-pz.html?ref=4112CL81Z&attr=3861)). The bottom side has a channel for avoid water dripping into the sensors and break the flow. It also has small machined slots for easier disassembly:

<img src="https://live.staticflickr.com/65535/48439649822_7c7b6a8101_h.jpg" alt="SCK 2.1 Outdoor enclosure">

An additional cap is added to cover the hole in case no cable is needed.

**Top cover**

The [top cover](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/top.step) is a single sided milling in white HDPE. The part has a stepped milling for letting heat out, without letting water in.

### Sheet metal

This [plate](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/drawing_metal_sheet.pdf) is meant for attaching the whole system to a wall or pole, as well as supporting the installation of an external power supply in an IP65 box. The sheet is 1mm stainless steel with laser cutting and bent in two edges 90º.

<img src="https://live.staticflickr.com/65535/48439649392_67e981db3b_h.jpg" alt="SCK 2.1 Outdoor enclosure">

## 3D printed Enclosure(s)

This enclosure is meant to be fully 3D printed in PLA in a normal desktop 3D printed machine. 

!!! info ""
    This design is not aiming to be the best design in the world, but one that anyone can make and modify such as [our contributors](https://github.com/fablabbcn/smartcitizen-enclosures/tree/master/SmartCitizen%20Air%20Enclosures#community-contributed-enclosures).

![](https://raw.githubusercontent.com/fablabbcn/smartcitizen-enclosures/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/3D%20Printed%20square/case_render.png)

### Printing settings

![](https://raw.githubusercontent.com/fablabbcn/smartcitizen-enclosures/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/3D%20Printed%20square/printing_base.png)

We have tested the 3D printed components with both PLA or ABS. Good results are achieved with a normal 0.4mm nozzle and 0.2 layer height. No raft or brim are needed.

### Components

**Clip**

The SCK and the PMS5003 are held together by a [3D printed clip](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/HDPE%20circle/components/CLIP_NO_ORING.stl). No support is needed for this part. 

**Base and top covers**

[Base](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/3D%20Printed%20square/components/base.stl) and [cover parts](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/3D%20Printed%20square/components/cover.stl) at [different sizes too](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/3D%20Printed%20square/components/cover-xl.stl) or [transparent](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20Air%20Enclosures/SmartCitizen%20Kit/SCK2.1_PMS5003/3D%20Printed%20square/components/cover-acrylic.stl). Support is not needed for these part. A gasket can be added to the joint with adhesive foam. You can increase the top's thickness if you need better isolation, or use the foam provided with the SCK's box as an insulator. Also, tin foil is quite a good reflective material and helps with sun radiation.

## A _very_ DIY enclosure

!!! warning
    Keep in mind that casing is designed for short outdoor deployments. If you want a case for long exhibitions abroad, we will soon have a much more rugged enclosure ready! Also, feel free to explore all our [enclosures repository](https://github.com/fablabbcn/smartcitizen-enclosures) for this and other versions of our hardware.

!!! example "Step by step"

    **First, you will need the two 3D printed clips. You can [download the STL](https://github.com/fablabbcn/smartcitizen-enclosures/blob/master/SmartCitizen%20DIY%20Clips%20V2.0-2.1/3D%20Print%20Clips.stl) file and print them easily on any RepRap or similar FDM printer. If you don't know how to find a 3D printer, you can look for your nearest [Fab Lab](https://www.fablabs.io/labs) or use [3D Hubs](https://www.3dhubs.com/3dprint).**

    <script src="https://embed.github.com/view/3d/fablabbcn/smartcitizen-enclosures/master/SmartCitizen%20DIY%20Clips%20V2.0-2.1/3D%20Print%20Clips.stl"></script>


    1.Use scissors to cut an empty plastic bottle at about 12 cm from the top

    ![](/assets/images/heo8cwW.jpg)

    2.Use the rubber band to fix it using the bottle cap

    ![](/assets/images/CjKDBBl.jpg)

    3.Place the Kit inside and use the rubber band to hold it

    ![](/assets/images/8KzbAqV.jpg)

    4.You have now a simple enclosure to use your Kit outdoors for short measurement periods!

    ![](/assets/images/IhGxV67.jpg)

    ![](/assets/images/0kV6gie.jpg)
