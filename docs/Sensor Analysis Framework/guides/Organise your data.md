Organise your data
=========================

When downloading the framework, the following folder structure is copied:

```
├── environment.yml
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── src.egg-info
├── test_environment.py
├── tox.ini
└── urls.txt
├── data
│   ├── export
│   ├── interim
│   ├── processed
│   ├── raw
│   └── scripts
├── docs
├── models
├── notebooks
├── references
├── reports
├── src
├── tasks
```

The `data` directory will be the place where we will organise our data. Each of the sub-directories is explained below:

- `export`: we will export processed data or images here
- `interim`: we will place files used internally for the framework, such as sensor calibration data
- `processed`: the most important folder of our data directory. This will contain a hierarchy with the different tests after loading into our database. The tests in this folder will have an unified format to easily navigate them. It's the folder we will load our data from, once we have [created a test](#Create a test).
- `raw`: raw sdcard data can be placed here. It will feed our test creation script below
- `scripts`: a compilation of handy scripts to parse excel files, concatenate csvs and more

## The test

We have mentioned several times that we will organise our data in tests. The concept is very simple. A test is a collection of devices (SCKs or not), that have a common purpose. They can be located in the same spot (co-location) or not, and the main idea is that we centralise the data in a common instance for easy analysis.

<div style="text-align:center">
<image src="https://i.imgur.com/CSi5tL4.png" width="500px"/>
</div>

Tests have dates, authors, can have comments (for us to remember what we did), a report attached and can be in different conditions (outdoor, indoor)... We will put all this metadata in a `yaml` file to help use look for the tests later on. 

Tests can also have different sources. They could be csv files, xls files or data from the Smart Citizen API. For the local files, we will first pre-process them with the scripts in the `data/scripts` folder and then place them in the `data/raw` folder, in csv format. We use this format because it's a common usable format and, although it is not the most efficient way of archiving the data, it can be easily explored by other common applications.

### Pre-process the sd card data

We can concatenate all the sd card data from a device with the `concat_script.py` in the `data/scripts` folder.

We can access the script's help by typing in the terminal:

```
(smartcitizen-data) ➜  scripts git:(master) ✗ python concat_script.py -h
usage: concat_script.py [-h] [--output OUTPUT] [--index INDEX] [--keep]
                        [--ignore IGNORE] [--directory DIRECTORY]

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        Output file name, including extension
  --index INDEX, -i INDEX
                        Final name of time index
  --keep, -k            Keep full CSV header
  --ignore IGNORE, -ig IGNORE
                        Ignore files in concatenation
  --directory DIRECTORY, -d DIRECTORY
                        Directory for csv files to concatenate
```

Create a directory (`FILES`) and put the sd card data of one device in it. Then, run the script with:

```
(smartcitizen-data) ➜  scripts git:(master) ✗ python concat_script.py -k -d FILES
Using files in /Users/macoscar/Documents/04_Projects/02_FabLab/01_SmartCitizen/01_Repositories/DataAnalysis/smartcitizen-iscape-data/data/scripts/FILES
Files to concat:
18-11-08.CSV
18-11-09.CSV
18-11-13.CSV
18-11-14.CSV
18-11-15.CSV
18-11-16.CSV
18-11-17.CSV
18-11-18.CSV
Updating header
Saving file to: Log_Concat.csv
```

And if we now navigate to the `FILES` directory:

```
(smartcitizen-data) ➜  FILES git:(master) ✗ ls
18-11-08.CSV   18-11-13.CSV   18-11-15.CSV   18-11-17.CSV   Log_Concat.csv
18-11-09.CSV   18-11-14.CSV   18-11-16.CSV   18-11-18.CSV
```

We can find our concatenated file!

### Create a test

Once we have all our concatenated files, we can proceed to create our test. For this, you can launch `jupyter lab` and open the `notebooks/test_creation.ipynb` notebook.

In it, we can follow the instructions in the notebook by filling up the input data. 

!!! info "A note about the timestamps"
    To synchronise our tests, we will **always** need to specify the location. This means that all our tests will be in 'UTC'.

#### Test information

```
# Is you are creating a new test (True) or if the test is going to be updated (False)
isnewtest = True

# Date when you performed the test in 'YYYY-MM-DD' format
date = '2019-06-19'

# INTernal or EXTernal test (made by your organisation or others)
who = 'INT' 

# Short title for the test
short_name = 'DISPERSION_EVALUATION'

# Comment for your test. Make this as long as you need to describe fully the purpose of this test
comment = '''Evaluation of 20 kits for dispersion analysis. Performed in Fablab BCN during June 2019. During this test, we also checked the effect of CCS811 burn in'''

# Project
project = 'SmartCitizen'

# Firmware version
commit = '0.9.5'

# Who made the test
author = 'Oscar'

# Test type (indoor, outdoor, anything that helps you organise later on)
type_test = 'outdoor'

# If you are going to document the results somewhere, you can put a link below
report = ''
```

#### Add device information

An example for each type of device is given below. A test can contain as many devices you need, each with an unique identifier.

* Data of a simple SC `KIT` from the API, downloading all the available data, with a frequency of 1Min:

```
newtest.add_device('8739',
                   device_type = 'KIT',
                   location = 'Europe/Madrid',
                   pm_sensor = 'PMS5003',
                   device_files = {'device_id': '8739', 
                                   'frequency': '1Min',
                                   'source': 'api',
                                   'min_date': None,
                                   'max_date': None})
```

* Data of a simple SC `KIT` from the API, downloading the data from a certain date, up to the last available data: 

```
newtest.add_device('8739',
                   device_type = 'KIT',
                   location = 'Europe/Madrid',
                   pm_sensor = 'PMS5003',
                   device_files = {'device_id': '8739', 
                                   'frequency': '1Min',
                                   'source': 'api',
                                   'min_date': '2019-07-12',
                                   'max_date': None})
```

* Data of a SC `STATION` from the local csv data, located in London. The csv file is in `data/raw/5527.csv`. Also, the device is archived in the device history calibration described in [this section](#Devices calibration):

```
newtest.add_device('5527', 
                device_type = 'STATION', 
                sck_version = '2.0', 
                pm_sensor = 'PMS5003', 
                device_history = '5527',
                location = 'Europe/London',
                device_files = {'fileNameRaw': '5527.csv', 
                                  'fileNameInfo': '', 
                                  'frequency': '1Min',
                                  'source': 'csv_new'})
```

* Data of a SC `STATION` from the API, located in London. The device is archived in the device history calibration:

```
newtest.add_device('8739',
                   device_type = 'STATION',
                   location = 'Europe/London',
                   pm_sensor = 'PMS5003',
                   device_history = '8739',
                   device_files = {'device_id': '8739', 
                                   'frequency': '1Min',
                                   'source': 'api',
                                   'min_date': '2019-06-18',
                                   'max_date': None})
```

* Data of another device (reference equipment in this case), with local csv file, with frequency of 15Min. Extra information has to be given so that we can process the units of the different channels, the time index format and the location.

```
newtest.add_reference('CITY_COUNCIL', 
                  fileNameRaw = 'CITY_COUNCIL.csv', 
                  index = {'name' : 'Time',
                           'format' : '%Y-%m-%d %H:%M:%S',
                           'frequency' : '15Min'}, 
                  channels = {'pollutants' : ('CO', 'SO2', 'NO2', 'NO', 'NOX'), 
                              'units' : ('ppm', 'ppb', 'ppb', 'ppb', 'ppb'),
                              'names' : ('CO_ppm', 'SO2_ppb', 'NO2_ppb', 'NO_ppb', 'NOx_ppb')
                             },
                  location = 'Europe/Dublin')
```

* Data of another device (reference equipment in this case), with local csv file, with frequency of 1 day.

```
newtest.add_reference('CITY_COUNCIL_DAY', 
                  fileNameRaw = 'CITY_COUNCIL_DAY.csv', 
                  index = {'name' : 'Time',
                           'format' : '%d/%m/%Y',
                           'frequency' : '1D'}, 
                  channels = {'pollutants' : ['PM10'], 
                              'units' : ['ugm3'],
                              'names' : ['PM10']
                             },
                  location = 'Europe/Dublin')
```

#### Process everything

Once we have all the information, we can then process the files:

```
newtest.process_files()
```

## Devices history and calibration

Each device can have different sensors throughout it's life and, for each sensor, we can have different calibration parameters. These two sets of information are stored in `data/interim`. 

### Devices History

Stored in `data/interim/sensorData.yaml`, it's a file to be manually filled with all the devices ID's you want to manage. It contains basic references of the internal sensors that can be later on used in the different calibration files. An example of a Smart Citizen Station is shown below. Since the device can have different sensors at different times, the dates are also important. The ID (below `4773`), should be the same as in the test defined above in the field `device_history`:

```
'4773':
  hardware_id: '8ce207d2-504e4b4b-372e314a-ff03180c'
  sck_id: 'SCK2118080014'
  id: 'SCS21001'
  type: 'station'
  mac: '07D7'
  internal_ref: 'DEMO'
  date_from: '2018-09-17'
  date_to: '2018-09-21'
  gas_pro_board: 
    CO: 162581720
    NO2: 202160405
    O3: 204160159
    slots: !!python/tuple [CO, NO2, O3]
  pm_board:
    PMS5003_1: 2017123000701
    PMS5003_2: 2017123000703
```

### Devices calibration

Stored in `data/interim/CalibrationData/`, each json file contains a descriptor file for each sensor calibration data. An example for Alphasense's Electrochemical sensors is shown below:

```
{"Serial No": "162031254", "Target 2": "na", "Target 1": "CO", , "Sensitivity 1": "568.3", "Sensitivity 2": "0", "Zero Current": "-34", "Aux Zero Current": "-20.8"}
{"Serial No": "162031257", "Target 2": "na", "Target 1": "CO", , "Sensitivity 1": "493.1", "Sensitivity 2": "0", "Zero Current": "-69.4", "Aux Zero Current": "-18.6"}
```

!!! info "Calibration data"
    Currently, we store unique calibrations only for Alphasense sensors. This calibration is provided by the manufacturer directly and stored in this file.

## Load the data

We have two main methods to load data into the framework: a test (coming from sd card data or API), and the API, directly. Run the following piece of code in your `notebook`:

```
%run src_ipynb/init.ipynb
```

And then:

```
%run src_ipynb/load_data.ipynb
```

This will open an interface to load data from either source, explained below.

### Loading data from a test

![](https://i.imgur.com/ymKMWMu.png)

If you have local tests created as defined [here](/Sensor Analysis Framework/guides/Organise your data/#create-a-test), the tests will appear in the selection box. You can select as many as you want, and select the `target frequency` and what to do with `NaN` values.

!!! warning "Decide this now"
    It is better to decide this now and not when we create the test. Better to have the information available always and process it each time on load than vice-versa.

The set of options below will try to: 

- Load the process CSV files: in case you have some previous work done, it will load it (it should be in the processed folder of each test)

- Load cached API data: if you have loaded this test previously, and if you have previously marked the option below, it will load the data directly from your disk, to avoid loading it again from the API

- Save API data: will try to cache this data in the disk for later use.

Then we can click on `Load` and it will proceed to load your test. A normal output is shown below:

```
Test Load
Loading test 2018-01_INT_BOLOGNA_RELEASE
Comment: Pre Bologna release validation with 6 sensors (4 kits and 2 alphasenses)
Device ID SCK73FD
No metadata found - skipping
Kit SCK73FD located Europe/Madrid
Kit SCK73FD has been loaded
...
```

!!! info "Pro-tip"
    If you have a lot of tests, you can click on `Preview` with one test selected and you can preview it's comment.

    ```
    Test Preview
    Loading test 2018-02_EXT_BOLOGNA_TESTS_MA
    Comment: First iteration of iScape Station in Feb-2018 in Bologna. Two stations and two kits with chimney styled casing.
    ```

### Loading data from the API

In this case, we can input a comma-separated list of devices in the `Kit List` field. The devices are the devices IDs from: `https://smartcitizen.me/kits/1234`. An example is shown below:

![](https://i.imgur.com/d0azsMs.png)

You will need to input a name for the test (note that this is only creating it for the session, but it won't save it), and select the frequency, `NaN` processing and date range. When you click load, you should see something like this:

```
HELLO_WORLD
Loading device 5261 from API
Kit ID 19
    From Date 2019-08-01 to Date 2019-08-10
    Device located in Europe/Dublin
    Sensor IDs
    [14, 10, 65, 64, 96, 80, 79, 53, 58, 62, 61, 68, 67, 73, 72, 71, 89, 88, 87, 99, 100, 101, 104, 102, 103, 77, 76, 75, 105, 106, 107, 110, 108, 109, 56, 55]
    Device ID says it had alphasense sensors, loading them...
    Loading Sensor Done
    ...
```

Note that if the device ID is in the [devices history](/Sensor Analysis Framework/guides/Organise your data/#devices-history), it will also load the calibration data for you.

!!! info "Pro-tip"
    If you want to include your API devices in a test that you created, you can select it in the `Merge with...` drop-down. Remember that this won't update the test.

## Modify data

The data structure is based on a python dictionary, which contains a lot of information regarding the devices. The devices in a test can be accesed with:

```
print (records.readings['TEST_NAME']['devices'].keys())
```

The data for a particular device can be accessed like:

```
print (records.readings['TEST_NAME']['devices']['DEVICE_NAME']['data'])
```

In it, we have a [pandas](http://www.pandas.org) dataframe. We can check the columns in it by:

```
print (records.readings['TEST_NAME']['devices']['DEVICE_NAME']['data'].columns)
```

We can manipulate the dataframe at will. However, we have added a handy calculator:

```
%run src_ipynb/calculator.ipynb
```

Here you should see something like:

![](https://i.imgur.com/6C5OShB.png)

When you select a test, the devices will show in the selection box. If you select multiple devices, the common channels will be selectable in the drop down below. You can select each term (up to 4) and create a formula in the bottom-right text box. This accepts common expressions, as well as numpy expressions. An example is shown in the image above. When you hit `Calculate`, you should see:

```
Formula New_Channel Added in test 2018-01_INT_BOLOGNA_RELEASE, device SCK73FD
```

And if we list the columns in the device, we should see:

```
Index(['Battery-%', 'Input voltage-V', 'Noise-dBc', 'Humidity-%',
       'Temperature-C', 'Light-Lux', 'Carbon monoxide-kOhm/ppm',
       'Carbon monoxide heat current-mA',
       'Carbon monoxide heat supply voltage-mV',
       'Carbon monoxide heat drop voltage-mV',
       'Carbon monoxide load resistance-Ohms', 'Nitrogen dioxide-kOhm/ppm',
       'Nitrogen dioxide heat current-mA',
       'Nitrogen dioxide heat supply voltage-mV',
       'Nitrogen dioxide heat drop voltage-mV',
       'Nitrogen dioxide load resistance-Ohms', 'New_Channel'],
      dtype='object')
```

## Export data

Once we have concluded our analysis, we can export the process data. 

```
%run src_ipynb/export.ipynb
```

You should see something like this:

![](https://i.imgur.com/ahniTGT.png)

In the drop down you can select the desired test. Below, you can select one or many devices, and we will create a CSV file for each. Input a path below and hit `Export file` to generate them.

Some options are available:

- Copy to test folder: it will export the csv to the `/processed` folder in the test
- Include All / Raw / Processed: Options to include all the channels in your test, or only the ones tagged as `raw` or `processed` from the descriptor file in: `data/interim/sensorNamesExport.json`
- Rename channels: if you want to rename channels with the descriptor file mentioned above

!!! example "Step by step"
    If you want to download a lot of devices from the API, you can do this:
    
    1. Input the URLs in the `Kit List` Box in the `Data Import section`
    2. Input a `test name`
    3. Go to the export section and export the data for all the devices. Leave All channels marked
    4. That's it!



