# Soil Moisture Sensor Calibration

The soil moisture sensor can be used for schedule irrigations (i.e. determine when to water the plants); or for calculating soil water deficit to work out how much water to apply. Depending on the application, the sensor would need to be calibrated in with different procedures, but as a general guideline, we need to normalise its readings. Without this process, the raw sensor readings will be meaningless to the user and only some trends could be analysed. This section is a digest of some of these procedures, and more information is given in the notes below.

!!! info "More references"
    - [Capacitance probe calibration](https://www.daf.qld.gov.au/__data/assets/pdf_file/0018/55170/Capacitance-Probe-Calibration.pdf)
    - [The importance of soil moisture sensor calibration](https://www.edaphic.com.au/soil-water-compendium/soil-moisture-sensor-calibration/)

In case of **irrigation scheduling**, it is generally sufficient to simply match the raw readings from each sensor at both 0% (held in air) and 100% water levels (submerged in water). This is, of course, an approximation and will need some further analysis from the user to determine when to irrigate. When a **more accurate measurement is required**, the sensor needs to be calibrated with the actual soil where it's going to be deployed, since different types of soil will have different capacities. A [valid approach](https://www.edaphic.com.au/soil-water-compendium/soil-moisture-sensor-calibration/) is to prepare different samples of the soil with different levels of saturation, and adapt the sensor readings for it.

![](/assets/images/calibration_soil_buckets.jpg)

_Image Source: [Edaphic Scientific](https://www.edaphic.com.au/soil-water-compendium/soil-moisture-sensor-calibration/)_

## Calibration

If we are not aiming to get a full-fledged sensor reading, we will only need to measure the sensor in dry air and fully submerged in water. For that, **we will use**:

- A laptop with a serial interface. For instance, the [Arduino IDE](https://www.arduino.cc/en/Main/Software)
- Our sensor
- A cup filled up with water and a napkin

The sensor can be calibrated [using the shell interface](/Components/Firmware/guides/Using the Shell/). The process is as follows:

1. Connect your kit to a computer and open the terminal for the SCK. If you use the Arduino IDE, go to Tools > Serial Monitor and select `115200 baud` at the bottom right corner
![](/assets/images/hs5Ny7Q.png)

2. If you use the IDE type `sensor` on the top and click `Send`
3. Check if the output has something like `Soil Moisture Raw (60 sec)` after `Enabled`
4. If it's `Enabled`, **dry the sensor** and type in: `read soil moisture raw`. Repeat this command 5-10 times until you get an stable output (repeat command with _arrow up_)
5. Put the sensor in a cup of water (until the line). Then read the value again `read soil moisture raw` several times.
6. Once you have both values, type in: `control moisture cal XXX YYY` where XXX and YYY are the dry and wet values that you just measured
7. Check that the reading is OK by: `read soil moisture percent`. You should receive an answer in rh%
8. Now you should see the data online (if in network mode):

![](/assets/images/4Lrv62R.png)

!!! info "Find out more"
    Check the project source code [files](https://github.com/fablabbcn/smartcitizen-grow/tree/master/soil-moisture).