This page compiles examples of sensors for soil and water monitoring, developed during the [GROW](https://growobservatory.org) project.

!!! info "A note about versions"

    The following research has been funded by the [Grow Observatory](https://growobservatory.org/) project under European Community’s H2020 Programme under Grant Agreement No. [690199](https://cordis.europa.eu/project/rcn/203271/en).

<div style="text-align: center">
<img src="https://live.staticflickr.com/65535/47957156716_6354656db3_k.jpg" width="800" alt="SCK Grow Observatory Protoype">
</div>

## Moisture Sensor

The Chirp Sensor is a low cost moisture and temperature sensor developed by [WeMakeThings](https://wemakethings.net/chirp/): a hackers and engineers collective based in Vilnius, Lithuania. Their hardware and software are fully open-source, and it can be easily integrated but also replicated and customized for new projects. 

![Chirp](/assets/images/chirp.png)

The sensor uses capacitive sensing to measure soil's moisture. A 1MHz square wave is output from the chip through a resistor into a big pad that, together with the surrounding ground plane, it forms a parasitic capacitor. The resistor and the capacitor create a low pass filter which cut-off frequency changes with changing capacitance. The soil around the sensor acts as an electrolyte whose dielectric constant changes depending on the amount of moisture in it, so the capacitance of our makeshift capacitor changes too. The filtered square wave is then fed into a peak detector formed of out a diode and a capacitor. An ADC measures this voltage in the microcontroller. The sensor also includes a temperature sensor with a calculated absolute measurement accuracy around 2%.

There are different versions of the Chirp sensor, and for this application we chose the Chirp I2C sensor. The sensor was integrated on to the SCK's firmware, and it is automatically recognized by the board once it is plugged into the SCK using the Aux sensor connector. A Grove 4 pin Female Jumper to Grove will need to be used with the sensor to connect it to the SCK. The original Chirp sensors come coated with PRF202 - a moisture resistant varnish for electronics, but it is not enough for actual deployment. For such, one must add additional protection to the whole sensor. We suggest polyester or epoxy resin. However, you must note that sensitivity of the sensor will decrease depending on how thick the layer you are going to apply and might need to be recalibrated. We also recommend covering the electronics with heat shrink to fully waterproof the sensor. Some versions already include a pre-ruggedized sensor, which is a recommended solution for a faster use.

![](/assets/images/chirp_01.jpg)

### Sensor calibration

The soil moisture sensor can be used for schedule irrigations (i.e. determine when to water the plants); or for calculating soil water deficit to work out how much water to apply. Depending on the application, the sensor would need to be calibrated in with different procedures, but as a general guideline, we need to normalise its readings. Without this process, the raw sensor readings will be meaningless to the user and only some trends could be analysed. This section is a digest of some of these procedures, and more information is given in the notes below.

!!! info "More references"
    - [Capacitance probe calibration](https://www.daf.qld.gov.au/__data/assets/pdf_file/0018/55170/Capacitance-Probe-Calibration.pdf)
    - [The importance of soil moisture sensor calibration](https://www.edaphic.com.au/soil-water-compendium/soil-moisture-sensor-calibration/)

In case of **irrigation scheduling**, it is generally sufficient to simply match the raw readings from each sensor at both 0% (held in air) and 100% water levels (submerged in water). This is, of course, an approximation and will need some further analysis from the user to determine when to irrigate. When a **more accurate measurement is required**, the sensor needs to be calibrated with the actual soil where it's going to be deployed, since different types of soil will have different capacities. A [valid approach](https://www.edaphic.com.au/soil-water-compendium/soil-moisture-sensor-calibration/) is to prepare different samples of the soil with different levels of saturation, and adapt the sensor readings for it.

<div style="text-align: center">
<img src="/assets/images/calibration_soil_buckets.jpg">
</div>
_Image Source: [Edaphic Scientific](https://www.edaphic.com.au/soil-water-compendium/soil-moisture-sensor-calibration/)_

!!! example "Calibrate your sensor"
    If we are not aiming to get a full-fledged sensor reading, we will only need to measure the sensor in dry air and fully submerged in water. For that, **we will use**:

	- A laptop with a serial interface. For instance, the [Arduino IDE](https://www.arduino.cc/en/Main/Software)
	- Our sensor
	- A cup filled up with water and a napkin

    The sensor can be calibrated [using the shell interface](/Components/Firmware/guides/Using the Shell/). The process is as follows:

    1. Connect your kit to a computer and open the terminal for the SCK. If you use the Arduino IDE, go to Tools > Serial Monitor and select `115200 baud` at the bottom right corner
    ![](https://i.imgur.com/hs5Ny7Q.png)
	<br>
    2. If you use the IDE type `sensor` on the top and click `Send`
    3. Check if the output has something like `Soil Moisture Raw (60 sec)` after `Enabled`
    4. If it's `Enabled`, **dry the sensor** and type in: `read soil moisture raw`. Repeat this command 5-10 times until you get an stable output (repeat command with _arrow up_)
    5. Put the sensor in a cup of water (until the line). Then read the value again `read soil moisture raw` several times.
    6. Once you have both values, type in: `control moisture cal XXX YYY` where XXX and YYY are the dry and wet values that you just measured
    7. Check that the reading is OK by: `read soil moisture percent`. You should receive an answer in rh%
    8. Now you should see the data online (if in network mode):

	![](https://i.imgur.com/4Lrv62R.png)

!!! info "Find out more"
	Check the project source code [files](https://github.com/fablabbcn/smartcitizen-grow/tree/master/soil-moisture).

### Sensor validation

![](/assets/images/chirp_02.jpg)

Three Chirp sensors were compared to the [Parrot](https://www.parrot.com/) Flower Power (now discontinued). The Flower Power can measure several metrics, such as light, temperature, fertilizer and soil moisture. In this test, we compared the soil moisture readings for three Flower Parrot sensors, compared to three Chirp sensors. Both sensors show a good behaviour and the values can be correlated with good R2 scores. The approach for this low-cost sensors, in general, should be more qualitative than quantitative (analyse the trends rather than the absolute values), since their values appear to differ between sensors, even when normalised. In the particular case of the Chirp sensor, the sensor seems to be fairly normalised with simply a two calibration values (water and air) as a first approach.

![](/assets/images/chirp_test.png)

!!! info "Full analysis here"
    Find the full analysis [here](https://github.com/fablabbcn/smartcitizen-iscape-data/raw/master/reports/development/1910_moisture_sensor_analysis.pdf)!

## Tensiometer

!!! danger "WIP"
    This version is a WIP but is not fully functional with the SCK 2.1. It is shown here as a showcase of the project's capabilities. Have a look at the forum or drop us an email to discuss this. Check the source [files](https://github.com/fablabbcn/smartcitizen-grow/tree/master/soil-water-tension).


Soil Moisture data as the one provided by the Chirp Moisture Sensor is interesting for research, but when it comes to crops irrigation management, we usually like to know the soil water tension (SWT). That is because Soil Moisture in water is not directly related to the water plants roots might be able to extract because it is deeply affected by the soil composition. Even soil irrigation can be inferred from soil moisture when the soil type is known we think a soil tensiometer. Also when it is a simple solution, it is a useful tool for crops management.

![Watermark Tensionmeter Demo](/assets/images/watermark.png)

The design is entirely open source and it is deeply inspired by the work of Reinier Van der Lee from the [Vinduino project](http://vanderleevineyard.com/vineyard-blog.html), using an already calibrated commercial probe like the **Watermark 200SS9**. The sensor itself is straightforward and it consists of two stainless steel screws that work as electrodes cast inside a piece of plaster and covered by a plastic mesh to prevent erosion. As water is added more electrons can pass between the electrodes of the probe reducing the amount of resistance between them. By using this range of values, you can determine the amount of water that exists in your soil. To avoid interferences and degradation of the electrodes the design only applies voltage for a very short time and uses alternating electric polarities. For the sensor to work, we need a minimal circuit that uses two resistors and two diodes. The resistors work together with the electrodes to build a voltage divider. We can calculate the resistance value between the two electrodes by knowing the value of the resistors and the voltage. However to be able to alternate the electric current we need to duplicate the circuit and add two diodes. In total, we need 4 Pins to be connected to a microcontroller like the Arduino or the Smart Citizen Kit.