This page is a compilation of information regarding the operation in the field of the Smart Citizen Station. Since there are different versions, please, refer to their section accordingly.

## Living Lab Station V2

!!! warning "WIP"
    This version is in production stage and no information is currently available.

##  iScape Living Lab Station V1

### The Pack

![](https://i.imgur.com/zVPlOcz.jpg)

* iSCAPE Living Lab Station
    * Urban Board 2.0
    * Data Board 2.0
    * PM Board 2.0 + 2 PM sensors
    * Gas Pro Board 2.0 with 3 EC sensors
    * 6Ah Battery

* Accessories
    * MicroSD card 512MB
    * USB Charger
    * MicroSD to SD card adapter
    * USB Power Supply
    * 2m 3 Wire 220V cable
    * Mounting brackets and screws
    * Mounting tools (1x Wrench + 2 Allen Keys)

### Instructions

#### On boarding

To start the installation simply visit the setup website [**stations.iscape.smartcitizen.me**](https://stations.iscape.smartcitizen.me).

![](https://i.imgur.com/9slH1Ze.png)

!!! warning
    :warning: We will need you to send us the following information once you are done with the setup: the *device ID*, which appears in the URL of your device https://smartcitizen.me/kits/*XXXX* and the physical station ID that corresponds to that *device ID*, which can be found in a sticker underneath.

    ![](https://i.imgur.com/ARC6V42.jpg)

#### Get data from the SD card

You will need to access the Kit in order to get the SD card. For this, first unscrew the **two white layers at the top of the station** with the keys provided in the Pack:

![](https://i.imgur.com/WPb3tnr.jpg)

Then turn off your Kit by pressing the button for **5 seconds** and remove the micro SD card. You can plug the card on your computer using a Micro SD card reader.

![](https://i.imgur.com/DfRiI4s.jpg)

!!! warning 
    Handle the SD card with care! It might drop inside the station

You will find inside a `YYYY-MM-DD.CSV` with all the data. You can follow the [**Manual CSV data upload**](/Sensor%20Platform/guides/Uploading%20SD%20Card%20Data/) guide to manually upload the data to the platform.

!!! info "Power it back on!"
    Once you are done uploading the data and you want to keep on logging, put the SD card back in with the Kit OFF and press the button. It will come back to life!

### Outdoor installation

Use the perforated steel tape and the M6 provided to mount the Station on any street light or pole. The Pack also includes the required wrench:

![](https://i.imgur.com/36El7ds.jpg)

Also, a temperature probe needs to be extracted from the bottom of the station:

![](https://i.imgur.com/HIwz1yG.jpg)

And it should look like this:
 
![](https://i.imgur.com/hXtS4Gq.jpg)

#### Umbrella cover installation

Due to some issues with the waterproofness of the Living Lab Station, we have developed a solution to protect it from the rain. This solution is shown in the pictures below, and it's meant to solve these problems for the current version of the LLS. The newer version of the LLS has a simpler setup, already including such cover to protect it from the rain or sun radiation.

![](https://i.imgur.com/abJOKRa.jpg)

!!! warning "Beware of collisions"
    As you can see, the cover is a rugged piece and it's only meant for the current version of the station. Please, be careful and do not fit it in places where people could bump into it.

This is what you get in the package (except the wrench):

![](https://i.imgur.com/ftZRoT6.jpg)

!!! example "Step by step"

    * If you have the 3D printed cover on the Smart Citizen Kit, it's time to remove it. 

    * There is no need to remove the two top white layers (in the pictures we did it without them)

        ![](https://i.imgur.com/4BRDnQO.jpg)

    * Insert the threads in the already mounted t-slots. The distance between them is ~50mm

        ![](https://i.imgur.com/zRh2JJI.jpg)

        ![](https://i.imgur.com/44Y2WjZ.jpg)

        ![](https://i.imgur.com/jn8XnVD.jpg)

    * Insert the 4x flat spacer in the threads

        ![](https://i.imgur.com/a4NRjmz.jpg)

    * Place the cover on the station

        ![](https://i.imgur.com/v2CKMtr.jpg)

        ![](https://i.imgur.com/EqZDdzy.jpg)

    * Place the serrated spacers, with the serrated side on the outer part (they help to hold the station in place)

        ![](https://i.imgur.com/EOG8UvW.jpg)

    * Place the perforated steel stripe in one of the sides. Don't tight it too much, so that you have room to place it in the pole

        ![](https://i.imgur.com/EOG8UvW.jpg)

        ![](https://i.imgur.com/JJmuU7d.jpg)

    * Put the station in it's final location, and tighten it with the perforated steel stripes. Play with both sides, so that the stripes are tight on the pole

        ![](https://i.imgur.com/IKfu75D.jpg)

        ![](https://i.imgur.com/lkWg556.jpg)

    * You are done!

### Power supply

The Station can be directly powered at 220-240V AC (Max. consumption with the AC supply is 5W). It can also be powered via USB, with a normal phone charger (5V and 750mA max). However, there is a bit to do in order to change it. Let's see how!

![](https://i.imgur.com/S8cVo9z.jpg)

!!! warning "Batteries"
    The Living Lab Station has a higher consumption, mostly due to the fans on the two PM sensors.

    That means the internal battery last just for 20h, and it is only aimed at providing backup power.

    _For example, we can connect the station on the street light electric line, so the Station gets charged during the night when the lights are on._

!!! info "Solar Panel"
    Unfortunately, we are having some problems with the PV Solar Panel system to power the Station independently. The system is currently under tests, and it will be available in the next few months.

    ![](https://i.imgur.com/vfp6nB5.jpg)

#### Changing power supplies

Before we start, some tools that will be helpful during the process:

![](https://i.imgur.com/GiZkuwe.jpg)

!!! danger
    
    Unplug the station before starting this process from any type of external supply

!!! example "Step by step"

    * Remove the two covers using the allen keys as explained on the setup instructions.

        ![](https://i.imgur.com/4BRDnQO.jpg)

    * Remove the layer which contains the kit. The kit is attached to the layers below, as seen in the image

        ![](https://i.imgur.com/nP9aqsk.jpg)

    * Unplug the different connectors in the kit: I2C, battery and USB

        ![](https://i.imgur.com/pXTL3ku.jpg)

    * You can use nose pliers for the USB and the battery

        ![](https://i.imgur.com/9j6GznE.jpg)

        ![](https://i.imgur.com/2STYawe.jpg)

    * Time to get to the power layer, this time, two blue layers will come off

        ![](https://i.imgur.com/X4RlUqr.jpg)

    * Unscrew the cover for the power area

        ![](https://i.imgur.com/4cfxCZv.jpg)

    * Make sure there is no energy left in the power supply by checking that there is no LED on in it. Then, remove the cables from the power supply and the white brackets

        ![](https://i.imgur.com/h9iufVc.jpg)

        ![](https://i.imgur.com/1yulbbU.jpg)

    * Extract the cable from the base's cable gland

        ![](https://i.imgur.com/jJF9VbJ.jpg)

    * Cover the cable gland again and remove the square cable gland on the other side

        ![](https://i.imgur.com/P3m4q7Q.jpg)

    * Exchange the rubber in the cable gland with the one provided with a hole

        ![](https://i.imgur.com/NiUeiJ5.jpg)

        ![](https://i.imgur.com/IXMLkM4.jpg)

        ![](https://i.imgur.com/OrNZRyT.jpg)

    * Put the cable in and fix the gland in place. Leave sufficient overhead in the cable to be able to connect it to the kit

        ![](https://i.imgur.com/28wLcXA.jpg)

        ![](https://i.imgur.com/STZ0Yu8.jpg)

    * Put the power cover back on

        ![](https://i.imgur.com/2GTVg90.jpg)

    * Put the kit's layer back on and pass the cables through

        ![](https://i.imgur.com/UO5OmbK.jpg)

    * Connect everything in this order: first, the I2C connector, second, the battery, third, the USB

        ![](https://i.imgur.com/pXTL3ku.jpg)

    * Put the kit's layer on again. Verify that the o-ring fit's in properly. Close everything and put both layers back on on

        ![](https://i.imgur.com/yeh1enO.jpg)

        ![](https://i.imgur.com/4BRDnQO.jpg)

    * Now, you can use the USB power supply or the battery pack!

        ![](https://i.imgur.com/9iIflcg.jpg)

        ![](https://i.imgur.com/ZPzbFI9.jpg)

### Dimensions

![](https://i.imgur.com/udiYnTe.png)

### Troubleshooting

#### Before setup

Before configuring the Station setup make sure the LED is red. If not, press the button multiple times until the LED turns red.

![](https://i.imgur.com/uJ0JJIb.jpg)

#### The station does not respond

If the station does not respond or does not work properly you can do two things:

!!! info "Reboot your Station"
    You can fully reboot your Station by pressing the reset button located under the sensors board as seen on the picture.
    That will not delete any configuration, it will simply restart your device.
    Press the `RESET` button for a second. The light will go off and on and the device will start again.

    ![](https://i.imgur.com/tAofJ0g.png)

    You can also perform a reboot by disconnecting the battery and the USB cable so that the station is restarted. In this way we will not lose any data and configuration except the time in case of being in **SD mode**.

    ![](https://i.imgur.com/uJ0JJIb.jpg)


!!! info "Factory reset your Station"

    You can fully reset the Station to the default settings so you can register again your device. Press the main button for **15 seconds**.

    ![](https://i.imgur.com/uJ0JJIb.jpg)

    After 5 seconds the light will go off and will go on again after 15 seconds. Then you can release the button and your device will be fully resetted as a brand new Station.


#### The LED does not turn on and the station does not work

First of all, push the station button. Maybe it's simply off.

If this does not work, surely the station has been left without battery. You will have to charge it using the USB charger. Any other mobile charger will also work.

We will know that it is charging when the LED emits <span class="led orange blink"></span> orange pulses and once the battery is charged it will emit green <span class = "led green blink"> </ span>

### The station does not store the data on the SD card.

Some SD cards may have problems over time. We can try [formatting it]() but in case it does not work any micro SD card we buy at any mobile or computer store it will work. The size is not important and any micro SD or micro SDHC 512MB card up to 32GB will work.

![](https://i.imgur.com/h2db2Ch.jpg)

### Sensor Evaluation Campaign

Prior to sensor deployment for the intervention monitoring, some of the Living Lab Stations will be evaluated and compared against reference measurement under different conditions. They will be deployed in several cities among the iScape partners in order to *1.* develop models for sensor calibration under different climatic and pollutant exposure conditions and *2.* assess data quality. This campaign intends to evaluate the Living Lab Station before it's deployment, and trying to prevent concerns raised about data quality that other low-cost sensor platforms [^2] [^3] [^4]. 

This evaluation will focus on the **real-world conditions calibration**, under wide range of exposure and climatic conditions, rather than developing tests in controlled conditions, as prior studies show discrepancies in the accuracy resulting from evaluation in laboratory conditions, versus that of outdoor conditions [^2] [^5] [^6]. The tests will be conducted by co-location of at least two stations per site with high-end sensors under the conditions indicated in [the test section](/Living%20Lab%20Station/#test) below.
 
The duration of the tests will be of 2,5 months, with two location changes. This is a compromise between the indications given in [^1] for at least 3-months campaign and the availability of high-end sensors for the evaluation. Nevertheless, this campaign intends to cover a range of conditions by the deployment of the Living Lab Station in diverse conditions, not only climatic but also exposure-wise. The location changes will also intend to evaluate how well the sensors are able to adapt to these exposure and climatic changes [^10]. The data will be uploaded to the [SmartCitizen Platform](http://www.smartcitizen.me) and will be analysed using the [Sensor Analysis Framework](/Sensor%20Analysis%20Framework). The results of this evaluation in terms of models will be uploaded to a dedicated [repository](https://github.com/fablabbcn/smartcitizen-iscape-models) and will be implemented on the SmartCitizen Platform for on-the-fly sensor data processing. This processing aims to provide an open platform for sensor analysis using data analysis techniques, need which has been highlighted by [^2] [^5] [^6] [^9].

As well, as stated in [^2] [^10] [^11], it is necessary to perform individual field calibration for low-cost sensors if measurements comparable to those of high-end solutions are targeted. However, this calibration might not always be feasible in a wide range of conditions, leading to non-generalised models which can perform badly out of the training datasets. This test campaign also aims to study this concern, with an evaluation for a cross calibration methodology, in which results from a limited subset of observations are applied to the complete dataset [^7]. If successful, this would be set ground for the development of calibration strategies where the sensors are co-located with a high-end sensor and posteriorly deployed for citizen-science activities, or long term monitoring of the iScape Living Labs interventions, where high end sensors might not be available. This co-location could be performed in a recurrent manner, performing sequences of calibration-deployment-calibration, using merging calibrations as suggested in [^11].

As a summary, this field campaign aims to cover the following points:

- Assess data quality levels and positioning with respect to the DQO set by the European Air Quality Directive
- Stablish match scores for the different range of sensors available in the Living Lab Station
- Validation and assessment of  [EC sensor methodology](/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors/#sensor-calibration) for NO2 and O3 compounds in urban conditions (urban background and traffic) in various sites
- Validation of PMS PM raw data accuracy and effect of climatic conditions
- Calibration of Alphasense’s EC sensors and PMS PM sensors for model quality improvement accounting for climatic conditions
- Feasibility assessment for the calibration of metal oxide sensor models with the use of reference data and/or Living Lab station data
- Validation of climatic sensors of the station itself (temperature, humidity, pressure)
- Drifts and stability:
    - Drifts and possible root causes for EC sensor sensitivities variations over time
    - Calibration stability for SGX MOS sensors
    - Sensor decay and recoverability of PMS sensors due to dust accumulation or others

#### Test 

The table below shows a description of the proposed test campaign:

| Stage | Duration | Exposure | Reference equipment | Purpose |
|:---|:---:|:---:|:---:|:---:|
| Pre-test| 2 weeks| Urban Background| No| Stabilise electrochemical sensors to urban background on site.  and verify overall functioning| 
| Low Exposure test | 1 month | Urban Background | Yes | Evaluate response in low transient areas and evaluate repeatability of urban background measurements in higher exposure testing phases | 
| High Exposure test | 1 month | Urban with traffic (canyon or junction) | Yes | Evaluate response in high transient / high concentration areas and validate current model and post-processing approach. Propose further models with more variables |

The sites at which these calibration deployments are planned are:

| Site | Season | Reference equipment | Duration | 
|:---|:---:|:---:|:---:|
|Bologna (Italy) |Summer| YES | 1 month |
|Guildford (England)| Autumn| YES | 2.5 months |
|Dublin (Ireland)| Autumn| YES | 2.5 months |
|Bottrop (Germany)|Autumn| YES | 2.5 months |
|Barcelona (Spain)|Spring| YES | >3 months |

#### Sensor Installation

Guidelines for representativeness of the results are given below:

**Height**

Between 2,5 and 3,5m. Not reachable by hand.

**Reference equipment position**

Within <2m and with similar exposure, air flow (both either on wall, or lamppost) [^7]

**Desirable measurements**

- Chemical compounds (higher priority above): 
    - NO2
    - CO, O3
    - NOx, NO
    - NMHC

- Particulate Matter (higher priority above)
    - PM 2.5
    - PM 1.0, PM 10

- Climatic conditions (higher priority above)
    - Temperature and relative humidity
    - Wind speed and direction

!!! warning "Important Guidelines"

    Please, refer to the [sensor considerations section](/Living%20Lab%20Station/#sensor-considerations) for general information about the sensors. As well, take into account the following:

    - Avoid direct exposure to intense sunlight for long periods of time, since this can severely affect the measurements (direct sun or intense transients).
    
    - Avoid locations where high temperature or humidity transients are present since the sensor response is affected by these rapid changes.
    
    - Avoid locations with low air flow or with direct exposure to air conditioning exhausts.

### References

[^1]: [**Spinelle L., Aleixandre M., Gerboles M.** - 2013: Protocol of Evaluation and Calibration of Low-cost Gas Sensors for the Monitoring of Air Pollution. Joint Research Centre (Report EUR 26112 EN)]('http://refhub.elsevier.com/S0160-4120(16)30998-9/rf0225')

[^2]: [**Nuria Castell, Franck R. Dauge, Philipp Schneider, Matthias  Vogt, Uri Lerner, Barak Fishbain, David Broday, Alena Bartonova** - 2018: Can commercial low-cost sensor platforms contribute to air quality monitoring and exposure estimates?](https://www.sciencedirect.com/science/article/pii/S0160412016309989)

[^3]: [**Snyder E., Watkins T., Solomon P., Thoma E.,Williams R., Hagler G., Shelow D., Hindin D., Kilaru V., Preuss P.** - 2013: The changing paradigm of air pollution monitoring. Environ. Sci. Technol. 47, 11369–11377]('http://refhub.elsevier.com/S0160-4120(16)30998-9/rf0210')

[^4]:  [**Lewis A., Edwards P.** - 2016: Validate personal air-pollution sensors](https://www.nature.com/news/validate-personal-air-pollution-sensors-1.20195)

[^5]:  [**Spinelle L., Gerboles M., Villani M.G., Aleixandre M., Bonavitacola F.** - 2015: Field calibration of a cluster of low-cost available sensors for air quality monitoring: Part A: Ozone and nitrogen dioxide](https://www.sciencedirect.com/science/article/pii/S092540051500355X)

[^6]: [**Spinelle L., Gerboles M., Villani M.G., Aleixandre M., Bonavitacola F.** - 2015: Field calibration of a cluster of low-cost available sensors for air quality monitoring: Part B: NO, CO and CO2](https://www.sciencedirect.com/science/article/pii/S092540051631070X#)

[^7]: [**David H. Hagan, Gabriel Isaacman-VanWertz, Jonathan P. Franklin, Lisa M. M. Wallace, Benjamin D. Kocar, Colette L. Heald, Jesse H. Kroll** - 2018: Calibration and assessment of electrochemical air quality sensors by co-location with regulatory-grade instruments](https://www.atmos-meas-tech.net/11/315/2018/)

[^8]: [**Olalekan A.M.Popoola, Gregor B.Stewart, Mohammed I.Mead, Roderic L.Jones** - 2016: Development of a baseline-temperature correction methodology forelectrochemical sensors and its implications for long-term stability](https://www.sciencedirect.com/science/article/pii/S1352231016308317?via%3Dihub)

[^9]: [**Sun L., ChunWong K., Wei P., Ye S., Huang H., Yang F.,Westerdahl D., Louie P.K.K., Luk C.W.Y., Ning Z.** - 2016. Development and application of a next generation air sensor network for the Hong Kong Marathon 2015. Air quality monitoring. Sensors 16, 211–229](http://refhub.elsevier.com/S0160-4120(16)30998-9/rf0140)

[^10]: [**A. Ripoll , M. Viana, M. Padrosa, X. Querol, A.Minutolo, K.M. Houc, J.M. Barcelo-Ordinas, J. Garcia-Vidal** - 2018: Testing the performance of sensors for ozone pollution monitoring in a citizen science approach](https://doi.org/10.1016/j.scitotenv.2018.09.257)

[^11]: [**Philip J. D. Peterson, Amrita Aujla, Kirsty H. Grant, Alex G. Brundle, Martin R. Thompson, Josh Vande Hey and Roland J. Leigh** - 2017: Practical Use of Metal Oxide Semiconductor Gas Sensors for Measuring Nitrogen Dioxide and Ozone in Urban Environments, Sensors 2017, 17, 1653](http://www.mdpi.com/1424-8220/17/7/1653)