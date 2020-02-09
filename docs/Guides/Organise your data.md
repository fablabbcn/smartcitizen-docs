Organise your data
=========================

!!! warning "Step by step"
    Go through the [installation guide](/Guides/Install the framework) first before jumping into this guide.

When downloading the framework, the following folder structure is copied:

```
├── environment.yml
├── LICENSE
├── README.md
├── src.egg-info
├── data
│   ├── export
│   ├── interim
│   ├── processed
│   ├── raw
│   ├── resports
│   └── scripts
├── docs
├── models
├── notebooks
├── references
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

we will organise our data in tests. The concept is very simple. A test is a collection of devices (SCKs or not), that have a common purpose. They can be located in the same spot (co-location) or not, and the main idea is that we centralise the data in a common instance for easy analysis.

<div style="text-align:center">
<image src="https://i.imgur.com/CSi5tL4.png" width="500px"/>
</div>

Tests have dates, authors, can have comments (for us to remember what we did), a report attached and can be in different conditions (outdoor, indoor)... We will put all this metadata in a `yaml` file to help use look for the tests later on. 

Tests can also have different sources. They could be csv files, xls files or data from the Smart Citizen API. For the local files, we will first pre-process them with the scripts in the `data/scripts` folder and then place them in the `data/raw` folder, in csv format. We use this format because it's a common usable format and, although it is not the most efficient way of archiving the data, it can be easily explored by other common applications.

### Pre-process the sd card data

In order to make our files usable, we will need to have them in a format like `YY-MM-DD.CSV`. However, if the kit has been reset, we can find some files like: `YY-MM-DD.01`, `YY-MM-DD.02` and they should be something like `YY-MM-DD_01.CSV`, `YY-MM-DD_02.CSV`...

!!! info "Pro-tip"
    We can rename them manually, but if we have many of them, we can use this one-liner (works in oh-my-zsh):
    
    ```
    autoload -Uz zmv
    zmv '(*).(0*)' '$1_$2.CSV'
    ```

We can now concatenate all the sd card data from a device with the `concat_script.py` in the `data/scripts` folder.

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

Once we have all our concatenated files, we can proceed to create our test. For this, you can launch `jupyter lab` and open the [examples/test_creation.ipynb](https://github.com/fablabbcn/smartcitizen-iscape-data/blob/master/examples/test_creation.ipynb) notebook.

In it, we can follow the instructions in the notebook by filling up the input data. 

!!! info "A note about the timestamps"
    To synchronise our tests, we will **always** need to specify the location. This means that all our tests will be in 'UTC'.

#### Test information

```
#----
# Is you are creating a new test (True) or if the test is going to be updated (False)
isnewtest = True
# Date when you performed the test in 'YYYY-MM-DD' format
date = '2020-01-24'
# INTernal or EXTernal test (made by your organisation or others)
who = 'INT' 
# Short title for the test
short_name = 'AMAZING_TEST'
# Comment for your test. Make this as long as you need to describe fully the purpose of this test
comment = '''
'''
# Project
project = 'SmartCitizen'
# Firmware version
commit = ''
# Who made the test
author = 'Myself'
# Test type (indoor, outdoor, anything that helps you organise later on)
type_test = 'outdoor'
# If you are going to document the results somewhere, you can put a link below
report = ''
notes = ''
#----
```

#### Add device information

An example for each type of device is given below. A test can contain as many devices you need, each with an unique identifier.

* Data of a simple SC `KIT` from the API, downloading all the available data, with a frequency of 1Min:

```
device_1 = device_wrapper({'device_id': '8739',
                'type': 'KIT', 
                'version': '2.1', 
                'pm_sensor': 'PMS5003', 
                'location': 'Europe/London',
                'frequency': '1Min',
                'source': 'api'})
```

* Data of a simple SC `KIT` from the API, downloading the data from a certain date, up to the last available data: 

```
device_2 = device_wrapper({'device_id': '8739',
                'type': 'KIT', 
                'version': '2.1', 
                'pm_sensor': 'PMS5003', 
                'location': 'Europe/London',
                'frequency': '1Min',
                'source': 'api',
                'min_date': '2019-07-12',
                'max_date': None})
```

* Data of a SC `STATION` from the local csv data, located in London. The csv file is in `data/raw/5527.csv`. Also, the device is archived in the device history calibration described in [this section](#Devices calibration):

```
device_3 = device_wrapper({'name': '5527',
                'type': 'STATION', 
                'version': '2.1', 
                'pm_sensor': 'PMS5003', 
                'location': 'Europe/London',
                'frequency': '1Min',
                'device_history': '5527',
                'source': 'csv_new',
                'fileNameRaw': device_name + '.csv', 
                'fileNameInfo': ''})
```

* Data of a SC `STATION` from the API, located in London. The device is archived in the device history calibration:

```
device_4 = device_wrapper({'device_id': 5262,
                'type': 'STATION', 
                'version': '2.1', 
                'device_history': '5262', 
                'pm_sensor': 'PMS5003', 
                'location': 'Europe/London',
                'frequency': '1Min',
                'source': 'api'})
```

* Data of another device (reference equipment in this case), with local csv file, with frequency of 15Min. Extra information has to be given so that we can process the units of the different channels, the time index format and the location. The framework will conver the names from the `source_channel_names` to `target_channel_names`, and convert the `units`, in case they are available.

```
device_5 = device_wrapper({'name': 'PARROT_3',
                'type': 'OTHER', 
                'location': 'Europe/London',
                'fileNameRaw': 'grow_parrot_u6dODj2Dnm1570629407808.csv', 
                'fileNameInfo': '',
                'source': 'csv',
                'equipment': 'PARROT_SENSOR',
                'index': {'name' : 'Time','format' : '%Y-%m-%d %H:%M:%S', 'frequency' : '15Min'}, 
                'channels': {'source_channel_names' : ('air_temperature_celsius', 'battery_percent', 'calibrated_soil_moisture_percent', 'fertilizer_level', 'light', 'soil_moisture_percent', 'water_tank_level_percent'), 
                           'units' : ('degC', '%', '%', '-', 'lux', '%', '%'),
                           'target_channel_names' : ('TEMP', 'BATT', 'Cal Soil Moisture', 'Fertilizer', 'Soil Moisture', 'Water Level')
                              },
                'location': 'Europe/Madrid'})
```

#### Process everything

Once we have all the information, we can then process the files:

```
list_devices = [device_1, device_2, device_3, device_4, device_5]
newtest.create(details, list_devices)
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

!!! info
    Check how to load [test data in this example](https://github.com/fablabbcn/smartcitizen-iscape-data/blob/master/examples/load_test_data.ipynb) and how to [download data from the API in this one](https://github.com/fablabbcn/smartcitizen-iscape-data/blob/master/examples/load_device_API.ipynb)

### Loading data from a test

If you have local tests created as defined [here](/Guides/Organise your data/#create-a-test), the tests will be accessible when you do:

```
[print (test) for test in data.get_tests(data.dataDirectory).keys()]
```

You can load as many as you want, and select the `frequency` and what to do with `NaN` values.

!!! warning "Decide this now"
    It is better to decide this now and not when we create the test. Better to have the information available always and process it each time on load than vice-versa.

The set of options below will try to: 

```
options = {'clean_na': True, 'clean_na_method': 'drop', 'frequency': '3Min', 'load_cached_API': True, 'store_cached_API': True}
```

- Clean NaNs and how (`drop` or `fill`)
- Frequency for the data (`frequency`)
- Save API data (`store_cached_API`) : will try to cache this data in the disk for later use, and faster load next time (see next option)
- Load cached API data (`load_cached_API`): if you have loaded this test previously, and if you have previously marked the above option, it will load the data directly from your disk, to avoid loading it again from the API

A normal output is shown below:

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

### Loading data from the API

The devices are the devices IDs from: `https://smartcitizen.me/kits/1234`. An example is shown below:

```
device = api_device('1234', verbose = True)
device.get_device_data(start_date = None, end_date = None, frequency = '1Min', clean_na = False, clean_na_method = None);
```

You should see something like this:

```
Loading device 1234 from API
Kit ID 19
...
```

Note that if the device ID is in the [devices history](/Guides/Organise your data/#devices-history), it will also load the calibration data for you.

!!! info
  A more advanced guide can be found [here](https://github.com/fablabbcn/smartcitizen-iscape-data/blob/master/examples/advanced_load_data_API.ipynb)

## Data structure

Data is organised internally using tests. Each test can contain multiple devices. Each device, can contain data from one single source, either an API, or CSV files.

```
# Tests
data.tests.keys()
```

Devices within a test.
```
data.tests[testname].devices.keys()
```

Data inside the device:

```
data.tests[testname].devices[device_name].readings
```

We can check the columns in it by:

```
data.tests[testname].devices[device_name].readings.columns
```

## Export data

Once we have concluded our analysis, we can export the process data. 

```
# Test name where the device is
testname = 'mytest'
# List of devices to export
devices = list(data.tests[mytest].devices.keys())
# Example exporting only the first. We can iterate over devices with a for loop and export them all in separate CSV files
devicename = devices[0]
# Export it
data.export_data(testname, devicename, export_path = '/path/to/folder', all_channels = True, forced_overwrite = True)s
```

Some options are available:

- Copy to test folder: it will export the csv to the `/processed` folder in the test
- Include All / Raw / Processed: Options to include all the channels in your test, or only the ones tagged as `raw` or `processed` from the descriptor file in: `data/interim/sensorNamesExport.json`
- Rename channels: if you want to rename channels with the descriptor file mentioned above