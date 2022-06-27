# Organise your data

!!! warning "Step by step"
    Go through the [installation guide](/Guides/data/Install the framework) first before jumping into this guide.

When you first run `scdata`, it will create a `scdata` folder in your `~/.cache` directory containing the following structure:

- `export`: we will export processed data or images here
- `interim`: we will place files used internally for the framework, such as sensor calibration data
- `processed`: the most important folder of our data directory. This will contain a hierarchy with the different tests after loading into our database. The tests in this folder will have an unified format to easily navigate them. It's the folder we will load our data from, once we have [created a test](/#create-a-test).
- `raw`: raw sdcard data can be placed here. It will feed our pre-processing script below
- `reports`: reports will be generated here. Have a look at the [guide](/Guides/data/Make reports of your data/)
- `tasks`: tasks will be loaded from here (WIP)
- `uploads`: directory to put information when uploading data to zenodo

!!! info "Configure this"
  An additional `scdata` folder with a `config.yaml` file is created in your `~/.config` directory. 
  Visit the [readme in the github repository](https://github.com/fablabbcn/smartcitizen-data#tokens-and-config) for more information about configuring this.

## Data structure

Two main ways to access and organise the data:

- device: single device holding information from different sources. Learn how to use it [in the examples](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples)
- test: intended for experimentation with the data and posterior reproducibility. See [below](#test).

### Test

The concept is very simple. A test is a collection of devices (SCKs or not), that have a common purpose. They can be located in the same spot (co-location) or not, and the main idea is that we centralise the data in a common instance for easy analysis.

Tests have dates, authors, can have comments (for us to remember what we did), a report attached and can be in different conditions (outdoor, indoor)... We will put all this metadata in a `yaml` file to help use look for the tests later on. 

Tests can also have different sources. They could be csv files, xls files or data from the Smart Citizen API. For the local files, we will first pre-process them with the scripts in the `data/scripts` folder and then place them in the `data/raw` folder, in csv format. We use this format because it's a common usable format and, although it is not the most efficient way of archiving the data, it can be easily explored by other common applications.

### Pre-process the sd card data

!!! warning "Direct upload also available"
    You can directly upload SD card data following the example [here](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/09_load_and_post.ipynb)

In order to make our files usable, we will need to have them in a format like `YY-MM-DD.CSV`. However, if the kit has been reset, we can find some files like: `YY-MM-DD.01`, `YY-MM-DD.02` and they should be something like `YY-MM-DD_01.CSV`, `YY-MM-DD_02.CSV`...

!!! info "Pro-tip"
    We can rename them manually, but if we have many of them, we can use this one-liner (works in oh-my-zsh):
    
    ```
    autoload -Uz zmv
    zmv '(*).(0*)' '$1_$2.CSV'
    ```

We can now concatenate all the sd card data from a device with the `concat_script.py` in the [scripts](https://github.com/fablabbcn/smartcitizen-data/tree/master/scdata/utils/other) folder.

We can access the script's help by typing in the terminal:

```
python concat_script.py -h
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
python concat_script.py -k -d FILES
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
ls
18-11-08.CSV   18-11-13.CSV   18-11-15.CSV   18-11-17.CSV   Log_Concat.csv
18-11-09.CSV   18-11-14.CSV   18-11-16.CSV   18-11-18.CSV
```

We can find our concatenated file!

### Create a test

Once we have all our concatenated files, we can proceed to create our test. For this, you can launch `jupyter lab` and open the [examples notebooks](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/01_getting_started.ipynb). In it, we can follow the instructions in the notebook by filling up the input data. 

!!! info "A note about the timestamps"
    To synchronise our tests, we will **always** need to specify the location. This means that all our tests will be in 'UTC'.

!!! info "There's a lot more to it"
    Check the examples in [the repository to](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/README.md#index-of-examples):
    
      - Plot data
      - Process
      - Calibrate sensors
      - Upload it to zenodo
