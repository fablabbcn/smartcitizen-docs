# Welcome!

Welcome to the **Smart Citizen project** documentation! This page is a compilation of all the project's experience and knowledge on the technology and tools for environmental monitoring that it develops. The project touches upon many fields, so we really hope these resources are useful for anyone wanting to learn about what we do: **open hardware, software, sensors knowledge, data, platforms, and much more**.

Feel free to keep reading about the different [sections](#get-started) or go directly to our [guides](#guides).

<img src="https://live.staticflickr.com/65535/52716091733_8512429e01_k.jpg" alt="Laboratorio Ciudadano de Salud Urbana - by LICHEN">

## Get started

If you don't know where to go, take a look at the **sections** below:

TODO: Improve design of this

* **Main:** Contains the hardware, firmware and data documentation:
    * **Hardware:** Here you will find the [**Smart Citizen Kit**](Smart Citizen Kit) and [**Smart Citizen Stations**](Smart Citizen Station) documentation to help you get started. Visit the [Hardware](/Components/) page to understand a bit better how you can better use all the SCK possibilities, or check the [wide range of sensors](/Components/Auxiliary Connector/) the project supports.
    * **Firmware:** Here you will find information about the [firmware architecture](/Components/Firmware/) and the [onboard flash storage](/Components/Flash Storage/)
    * **Data:** Contains all the documentation on data, from collection, storage to analysis and calibration:
        * **Platform:** Contains all the documentation on the [**online sensors platform**](/Data/Sensor Platform) where data is collected, stored and visualised
        * **API:** the documentation of our [RESTFUL API](/Data/Smart Citizen API/) and how to interact with it
        * **Data Analysis:** Contains all the documentation on the tools you can use for data analysis. From [basic web tools](/Data/Data Analysis#web-tools), to [creative coding](/Data/Data Analysis#creative-coding), [visual programming](/Data/Data Analysis#visual-programming), or our [data post-processing framework](/Data/Data Analysis#advanced)
* **Knowledge:** Probably one of our most valuable resources. [This section](/Components/sensors/) contains documentation on all the sensors we have used: [air quality](/Components/sensors/air/), [water](/Components/sensors/water/) and [soil](/Components/sensors/soil). You will also find a [performance summary](/Components/sensors/performance/) where you can read about how different sensors perform. Other [valuable resources](/Components/sensors/resources/) from other projects can be found there too
* **Guides:** Contains step-by-step [**guides**](/Guides/) for different aspects of the project, [how to get started](/Guides/getting started/Onboarding sensors/), [use the shell](/Guides/getting started/Using the Shell/), [making your own enclosures](/Guides/enclosures/Making your own enclosures/) or make some [data analysis](/Guides/data/) of the sensor readings!
* **Resources:** Last but not least, a compilation of project results such as the [Citizen Sensing Toolkit](/Resources/Citizen Sensing Toolkit/), [Research](/Resources/Research/) and [Education](/Resources/Education/) projects, [Webinars](/Resources/Webinars/) and, finally, links to other [initiatives and friend projects](/Resources/References/)

## Guides

The documentation contains multiple [guides](/Guides/) as step-by-step tutorials to perform essential tasks as installing a kit or upgrading it's firmware:

![](/assets/images/feS0bZ8.jpg)

!!! info "Example guides"

    * [Installing the Smart Citizen Kit](/Guides/deployments/Deploying SCK/)
    * [Installing the Smart Citizen Station](/Guides/deployments/Deploying Air Station/)
    * [Installing the Smart Citizen Kit 1.0 / 1.1](/Components/legacy/)
    * [Onboarding new Sensors](/Guides/getting started/Onboarding Sensors)
    * [Uploading SD Card Data](/Guides/getting started/Uploading SD Card Data)
    * [Update the Firmware](/Guides/firmware/Update the firmware)
    * [Edit the Firmware](/Guides/firmware/Edit the Firmware)

![](https://i.imgur.com/feS0bZ8.jpg)

## Open Source

**We're against black boxes!**

The entire project is released under open source licenses:

* Hardware components: [CERN Open Hardware License v1.2](https://www.ohwr.org/licenses/cern-ohl/license_versions/v1.2)
* Core firmware and data tools: [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
* Software platform: [GNU AGLP v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

!!! info
    Check the **Source files** section for each component and explore the software source code and the hardware blueprints.

    ![](https://i.imgur.com/X1fUET3.png)


## About

The Smart Citizen project aims to provide tools for anyone willing to use technology in a critical way. By developing environmental sensing tools, branching out in various fields such as open hardware, software, data, social innovation and digital fabrication, our main contribution is the amount of resources that this documentation hopes to compile. The project was born in [Fab Lab Barcelona](https://fablabbcn.org) which, up until now, is the main maintainer of the project. However, the project is [released under **free** and **open source** licenses](#open-source), hoping that anyone can contribute to it, reuse it, adapt it and improve it in any way needed.

!!! info "A note about funding"

    One important aspect to mention in the front page of our documentation is that we have received public funding in several ocasions, including the European Commission funds in H2020 and Horizon Projects. In the [funding page](/About/funding/) you can find a complete list of these projects, for which we are thankful and that we hope that we have been able to deliver results accordingly. For publicly funded projects, information on the project numbers is available through the links in the `ID` column.

!!! info "A note about versions"

    <a href="https://www.iscapeproject.eu/"><img class="logo" src="https://i.imgur.com/ud8lUOo.png" width="120" alt=""></a>

    The new [**Smart Citizen Kit**](Smart Citizen Kit) and the [**Smart Citizen Station**](Smart Citizen Station) development was possible thanks to  [iSCAPE](https://www.iscapeproject.eu/), a project under European Community’s H2020 Programme (Grant Agreement No. [689954](https://cordis.europa.eu/project/rcn/202639/en))