# A modular tool for citizen action

The guides in this section are aimed at creating a set of tools and resources around the SCK. This allows communities to develop their own sensing frameworks and strategies for participatory sensing. Find here guides that will help with making the best use of the Smart Citizen Kit, from a step-by-step guide on how to [set up your kit](/Guides/getting started/Onboarding Sensors) to more advanced features like [data analysis](/Guides/data/Install the framework/) or using the [SCK's shell](/Guides/getting started/Using the Shell).

![](https://camo.githubusercontent.com/53ece1879090c116a1be2e3998df2960afc9fa12/68747470733a2f2f63646e2e7261776769742e636f6d2f6661626c616262636e2f736d617274636974697a656e2d746f6f6c6b69742f32346233353431382f696d672e6a7067)

## How to get around in the guides?

The guides here are meant to help you with many aspects regarding the sensors and getting specific step-by-step information. Since there are a lot of different guides, here there is a small summary for each type of device:

!!! info "What are the differences between the sensor units?"
	The hardware, being designed in a modular way, allows for a lot of customisation. We call [**Smart Citizen Kit** ](/Smart Citizen Kit/) to the different variants of devices that have a [Data Board](/Components/boards/Data Board/), an [Urban Board](/Components/boards/Urban Board/) and a [PMS5003 Particulate matter sensor](/Components/sensors/air/PM Sensors/).
	Adding any additional sensor to the Smart Citizen Kit, with or without Urban Board, is what we call a [**Smart Citizen Station**](/Smart Citizen Station/). The **Stations** amount of sensors could range from 1 to virtually any number. There are some **Stations** that are meant for air quality measurements, and some that take water measurements. Some of them have only one additional CO2 sensor, and some Stations have up to 16 analog measurements in parallel. Check the guides compilation below to make sure you follow the different steps for the configuration of your particular unit.

### Smart Citizen Kit

<img src="https://live.staticflickr.com/65535/48992224646_bd32af64ae_k.jpg" width="2000" height="1333" alt="SCK 2.1 - Street 2">

- [ ] If you haven't started yet to collect data, check the [onboarding sensors](/Guides/getting%20started/Onboarding%20Sensors/) guide
- [ ] If you are about to place the sensor outdoors, check the [deploying Smart Citizen Kit](/Guides/deployments/Deploying%20SCK/) guide
- [ ] Check the [updating the firmware](/Guides/firmware/Update%20the%20firmware/) guide to get the latest version of the firmware in the SCK
- [ ] Moving location? Check the [updating the WiFi](/Guides/getting%20started/Updating%20the%20Wi-Fi/) guide
- [ ] More advanced features? Check the [using the Shell](/Guides/getting%20started/Using%20the%20Shell/) guide


### Smart Citizen Air Quality Stations

<img src="https://live.staticflickr.com/65535/50977149367_922fc1c478_k.jpg" width="2000" height="1333" alt="Smart Citizen Station v3">

- [ ] If you haven't started yet to collect data, check the [onboarding sensors](/Guides/getting%20started/Onboarding%20Sensors/) guide, and **make sure you select the correct blueprint** as explained in the [advanced kit selection](/Guides/getting started/Onboarding Sensors/#advanced-kit-selection) guide. In the Stations that measure chemical composition with electrochemical sensors (i.e. CO, NO2, NO, SO2, O3, etc.), you will also need to follow the [handling calibration information](/Guides/data/Handling%20calibration%20data/) guide
- [ ] To place the sensors outdoors, follow the [deploying Smart Citizen Station](/Guides/deployments/Deploying%20Smart%20Citizen%20Station/) guide
- [ ] Similar to the SCK, check the [updating the firmware](/Guides/firmware/Update%20the%20firmware/), [updating the WiFi](/Guides/getting%20started/Updating%20the%20Wi-Fi/) and [using the Shell](/Guides/getting%20started/Using%20the%20Shell/) guides for keeping your sensor up to date
- [ ] If you are working with the data: [check how to access to the data](/Guides/getting started/Downloading the Data/).
- [ ] If your Station has a CO2 sensor, check the [Calibration of CO2 sensors](/Guides/calibration/SCD30 CO2 sensor/) guide
- [ ] If you have small Stations (only with the Urban board, the PMS5003, and with CO2, or two small A-series Alphasense Electrochemical sensors), check the [assembly of the stations](/Guides/enclosures/Assembling Smart Citizen Stations/) guide

!!! warning ""
	Note that if your unit has electrochemical sensors, data needs to be postprocessed outside of the units (in the platform). By following the [handling calibration information](/Guides/data/Handling%20calibration%20data/) guide, you are set with the default processing. However, if you want to perform custom algorithms in an automated way, follow the [Data processing](/Guides/data/Custom%20data%20processing/) guide to set it up

### Smart Citizen Water Stations

<img src="https://live.staticflickr.com/65535/51124639732_90241111a9_k.jpg" width="2048" height="1365" alt="Water Station - Patí Científic">

- [ ] If you haven't started yet to collect data, check the [Onboarding sensors](/Guides/getting%20started/Onboarding%20Sensors/)
- [ ] If you are setting up your own unit from scratch, follow the [Smart Citizen Water Station Setup Guide](/Guides/deployments/Water sensors/)
- [ ] Similar to the SCK, check the [updating the firmware](/Guides/firmware/Update%20the%20firmware/), [updating the WiFi](/Guides/getting%20started/Updating%20the%20Wi-Fi/) and [using the Shell](/Guides/getting%20started/Using%20the%20Shell/) guides for keeping your sensor up to date
- [ ] For information on the water probes calibration, go to the [Calibrating water sensors](/Guides/calibration/Water%20sensors/) guide