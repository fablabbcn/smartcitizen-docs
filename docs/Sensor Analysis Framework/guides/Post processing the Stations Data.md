Post processing the Stations Data
=================================

The stations data can be fully processed within the [sensor analysis framework](https://docs.iscape.smartcitizen.me/Sensor%20Analysis%20Framework/) provided. In this guide, we will go through a working _live_ example that will use available data from a permanent Smart Citizen Station in **Fablab BCN**. The available sensors are listed [here](https://docs.iscape.smartcitizen.me/Living%20Lab%20Station/).

#### Load in the data

So first, we will load in the data from this station. The device number is the **4748**, and is available in [here](https://smartcitizen.me/kits/4748).

We will use the available interface in our *framework* to load the station data. In this case, we will load all the available data into our notebook, but if we wanted, we could use the interface to set up time limits, should the timeframe desired be different:

![](https://i.imgur.com/TIkpY72.png)

!!! info
	In the field _Kit list_ we can also input a comma separated list of devices such as: `4748, 4565, 4587` and we will load all the data for you.

We can now explore the available readings in our test with something like:

```python
## This will output the devices we have in the selected test
print readings['STATION_FABLAB_BCN']['devices'].keys()
```
**Output**:
```
[u'4748']
```

If we want to have access to the actual data, we can go under:

```python
## This will output the dataframe's first 4 lines
print readings['STATION_FABLAB_BCN']['devices']['4748']['data'].head(4)
```
**Output**:
```
                           BATT  CO_MICS_RAW    EXT_HUM   EXT_TEMP     GB_1A  \
2018-08-24 17:00:00+02:00   0.0    73.441111  47.652222  30.663333  4.517778
2018-08-24 17:10:00+02:00   0.0   129.049000  46.632000  31.209000  3.905000
2018-08-24 17:20:00+02:00   0.0    53.738333  45.901667  31.616667  3.808333
2018-08-24 17:30:00+02:00  74.5   122.405000  45.655000  31.810000  3.925000 ...
```

Or if we want to see the available recordings:
```python
## This will output the dataframe columns
print readings['STATION_FABLAB_BCN']['devices']['4748']['data'].columns
```
**Output**:
```
Index([u'BATT', u'CO_MICS_RAW', u'EXT_HUM', u'EXT_TEMP', u'GB_1A', u'GB_1W',
       u'GB_2A', u'GB_2W', u'GB_3A', u'GB_3W', u'HUM', u'LIGHT',
       u'NO2_MICS_RAW', u'PM_1', u'PM_10', u'PM_25', u'PM_DALLAS_TEMP',
       u'PRESS', u'TEMP'],
      dtype='object')
```

For more information about the **test structure**, all the fields are detailed in [here](https://docs.iscape.smartcitizen.me/Sensor%20Analysis%20Framework/#loading-in-the-data).

If the device is an station, we will have to input the sensor references for the alphasense devices. We have prepared the framework to input this easily:

```python
## This will output the structure for inputing the alphasense sensor refs
print readings['STATION_FABLAB_BCN']['devices']['4748']['alphasense']
```
**Output**:
```
{'O3': 'TEMPORARY_O3', 'SLOTS': 'TEMPORARY_SLOTS', 'CO': 'TEMPORARY_CO', 'NO2': 'TEMPORARY_NO2'}
```

As you can see, we have no data in this struct, but we can easily fill it put by:

```python
readings['STATION_FABLAB_BCN']['devices']['4748']['alphasense']['O3'] = 204560316
readings['STATION_FABLAB_BCN']['devices']['4748']['alphasense']['NO2'] = 202160413
readings['STATION_FABLAB_BCN']['devices']['4748']['alphasense']['CO'] = 162031257
readings['STATION_FABLAB_BCN']['devices']['4748']['alphasense']['SLOTS'] = ('NO2', 'CO', 'O3')

print readings['STATION_FABLAB_BCN']['devices']['4748']['alphasense']

```
**Output**:
```
{'O3': 204560316, 'SLOTS': ('NO2', 'CO', 'O3'), 'CO': 162031257, 'NO2': 202160413}
```

Note that each of these fields is necessary for our posterior calculations. Each of the `O3`, `NO~2~`, `CO` fields relate to the manufacturer's reference of each of the sensors, whilst the `SLOTS` field relates to the order at which the sensors are placed. **Normally**, the stations are delivered with the SLOTS field as: `('CO', 'NO~2~', 'O3')`, meaning that the _CO sensor_ is in the slot #1, the _NO~2~ sensor_ in the slot #2 and the _O3 sensor_ in the slot #3.

!!! info
	Normally we refer to the OX-B431 sensor as O3, although it measures both, O3+NO~2~ mixing ratios, and therefore we use O3 or OX indistinctively.

!!! warning
	You might have noticed that the slots we have input are not matching to our own description... Our bad!

#### Explore the data

We can now have a look at the station's data. We can go to the Section `Exploratory Data Analysis` and use the range of available interfaces for the data analysis. We would like to serve this as a flexible tool, in which the priority is to generate proper analysis. For this, we have some interesting interactive plots as:

- Time Series Plot
- Back2Back correlation plots
- Correlogram
- Heat maps

Let's run a simple example. We will plot all the concerned `alphasense` signals using the interface. We could also do this by code, but we find it less time consuming and more data analysis dedicated:

![](https://i.imgur.com/TTfFF9w.png)

We can select within the channels available in the dataframe, for each of the devices within a test. All the devices are supossed to have overlapping timestamps, so they can be compared easily. Hence, here is where the concept of test is interesting, since all the devices within a test can be easily grouped and compared:

![](https://i.imgur.com/R4fK2cX.png)

In this example we have selected all three alphasense sensors available data  and plotted them with the working and auxiliary electrodes. We can here explore with the [plotly](http://plot.ly) integrated commands to review the data.

Here, it is important to see how the **sensors adapt to the environment** once they have their power restored after a power cut, or after the first use. For example, in the case of the `CO` measurement, after the power restorage on 31st of August, the sensor is clearly experiencing an stabilisation that has to be discarded in our calculations:

![](https://i.imgur.com/GyG1KbL.jpg)

We can also see how some metrics correlate among themselves and analyse potential sources for multicollinearity in our model. For this, we will study how every two measurments correlate among themselves in the following interface:

![](https://i.imgur.com/s5CYIDW.png)

We will use a very straightforward example: let's see how temperature and relative humidity correlate and see if there might be variations in the absolute humidity that might affect the variations in the relative humidity that are not explained by the temperature. If we select our channels and _Check_ on `Crop Data in X axis` and input our dates we will have the following:

![](https://i.imgur.com/ZS7Xnfs.png)

Here, we can see that both are anticorrelated (Pearson = -0.61) and although they have a clear inverse trend, their R2 is low:

![](https://i.imgur.com/lvWtVUq.png)

This might indicate that the variations in the humidity are not fully explained by the temperature variations and, that there might be variations in the absolute humidity that we could account for in our models.

#### Adding calculated channels

Let's then add the partial vapour pressure in our dataset. Based on the definition of the relative humidity (RH):

$$
RH ( \% )= 100 {P_{H2O} \over P^*_{H2O}}
$$

Where $P_{H_2O}$ is the partial vapour pressure and $P^*_{H_2O}$ is the equilibrium vapour pressure at a certain pressure and temperature. This equilibrium vapour pressure can be determined by the [Arden Buck Equation](https://en.wikipedia.org/wiki/Relative_humidity#Measurement) and goes like:

$$
P^*_{H2O} (mbar) = (1,0007+3,46x10^{-6}xP)x6.1121e^{17,520T/(240,97+T)}
$$

Where $P$ is the absolute pressure in mbar and $T$ is the temperature in degC. Having the partial vapour pressure, we can then calculate both values in the implemented calculator in our notebook:

![](https://i.imgur.com/iz29E8Y.png)


Here, the formula is:

```python
## Calculate equilibrium vapour pressure
P_H2O_EQ = (1.0007 + 3.46*1e-6*PRESS*10)*6.1121*np.exp(17.502*TEMP/(240.97+TEMP))
```

Note that we can input any type of expression in the `Formula Field` that can be subject to evaluation as in a Python formula. Note as well that `numpy` operations are allowed and that they can be written in line.

!!! info
	If you want to calculate this formula for several devices within a test, select all of them and the calculator will make the available in the dropdowns the common metrics.

Now, we can calculate de partial vapour pressure as, since it's available within our channels:

![](https://i.imgur.com/uqVhEkR.png)

```python
## Calculate partial vapour pressure
P_H2O_VAP= HUM*P_H2O_EQ/100
```
We can now verify that the partial pressure is not constant and plotting it with the other channels:

![](https://i.imgur.com/E8SRwJk.png)

If we analyse the data in periods where the partial vapour pressure is fairly constant (i.e. 31st of Aug, we see that variations of the temperature are directly correlated with the relative humidity, whilst days as the 2nd of September show greater variations in both, temperature and partial vapour pressure that provoke a lower correlation in the temperature and humidity:

![](https://i.imgur.com/L2jdyt0.jpg)

#### Calculating the actual pollutant concentrations

Now that we know how to get around in the notebook, explore data and add channels in a simple way, lets calculate actual pollutant concentrations. For this, we will use the section `AlphaSense Baseline Calibration`. In this block, we will apply the methodology exlained in [this section](https://docs.iscape.smartcitizen.me/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors/) in order to calculate actual pollutant concentrations.

For this, in the above mentioned section, if we run the cell, we will see an output like the following:

![](https://i.imgur.com/Zg8qtRa.png)


This will list all the available devices that contain alphasense data. Remember to include the calibration data mentioned before in the `dict` so that we can calculate the final concentrations.

For reference, all the alphasense data is under [this repository](https://github.com/fablabbcn/smartcitizen-iscape-data/blob/master/calData/AlphaSense.json), which looks like:

```jsonld
{"Target 2": "na", "Target 1": "CO", "Serial No": "162031254", "Sensitivity 1": "568.3", "Sensitivity 2": "0", "Zero Current": "-34", "Aux Zero Current": "-20.8"}
{"Target 2": "na", "Target 1": "CO", "Serial No": "162031257", "Sensitivity 1": "493.1", "Sensitivity 2": "0", "Zero Current": "-69.4", "Aux Zero Current": "-18.6"}
{"Target 2": "na", "Target 1": "CO", "Serial No": "162031256", "Sensitivity 1": "601.9", "Sensitivity 2": "0", "Zero Current": "-68.1", "Aux Zero Current": "-13.9"}
{"Target 2": "na", "Target 1": "CO", "Serial No": "162581706", "Sensitivity 1": "581.4", "Sensitivity 2": "0", "Zero Current": "-72.8", "Aux Zero Current": "-35.3"}
{"Target 2": "na", "Target 1": "CO", "Serial No": "162581707", "Sensitivity 1": "605", "Sensitivity 2": "0", "Zero Current": "-56.7", "Aux Zero Current": "-46.3"}
```

In the cell output, we can select the tests that contain alphasense devices and that are subject to be calculated. A brief explanation of all the checkboxes is detailed below:

- *Decomp*: attemps to decompose the trends found in the day-to-day data. This is a common technique used in time series analysis in order to avoid regression including trend. It is normally not needed since the periods that are used for the data calculacions are short enough to have no significant trend (one day + overlap*)
- *Plots Inter*: checking this plots intermediary plots of all the calculations performed within the method. Use with caution
- *Verbose*: checking this includes extra information during the calculation process. Use with caution
- *Plots Results*: plots the final calculation per pollutant and all relevant intermediary calculation. Default is to be Checked
- *Print Stats*: prints interesting statistics about the dataset for later use

Now, let's calculate the pollutants. We don't need to worry about the manufacturer data, since it will automatically retrieved during the process.

**CO results**

The methodology used here is not the baseline model, but the application of this formula, as explained in [here](https://docs.iscape.smartcitizen.me/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors/#application-on-4-electrode-sensors):

$$
Concentration \ [ppm] = {I_{WE}-n(I_{AE}) \ [nA] \over Sensitivity \ [nA/ ppm]}
$$

![](https://i.imgur.com/5EmpUhK.png)

As we can see, the initial data is not to be considered due to the sensor stabilisation time. If we focus on the usable data, we can already get some insights about what hours are more polluted and the difference between working days and weekends:

![](https://i.imgur.com/H9suXGA.jpg)

**NO~2~ results**

For this metric, we will be using the above mentioned baseline methodology

If we have a look at the data, we see that the sensor still requires stabilisation, as the CO electrode:

![](https://i.imgur.com/CVIYfua.jpg)

Zooming in, we can see the most polluted hours are those in the morning:

![](https://i.imgur.com/p0zohNs.jpg)

!!! warning
	OX sensor in this station is not giving good results (probably it's ageing has provoked a sensitivity loss), and therefore, the data will not be shown here.