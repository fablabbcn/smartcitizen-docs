# Organise your data

!!! warning "Step by step"
    Go through the [installation guide](/Guides/data/Install the framework) first before jumping into this guide.

When you first run `scdata`, it will create a `scdata` folder in your `~/.cache` directory containing the following structure:

- `export`: we will export processed data or images here
- `interim`: we will place files used internally for the framework, such as sensor calibration data
- `processed`: the most important folder of our data directory. This will contain a hierarchy with the different tests after loading into our database. The tests in this folder will have an unified format to easily navigate them. It's the folder we will load our data from, once we have [created a test](/#create-a-test).
- `raw`: raw sdcard data can be placed here. It will feed our pre-processing script below
- `reports`: reports will be generated here. Have a look at the [the section below](#make-reports-of-your-data)
- `tasks`: tasks will be loaded from here
- `uploads`: directory to put information when uploading data to zenodo. Have a look at 

!!! info "Configure this"
    An additional `scdata` folder with a `config.yaml` file is created in your `~/.config` directory. 
    Visit the [readme in the github repository](https://github.com/fablabbcn/smartcitizen-data#tokens-and-config) for more information about configuring this.

## Data structure

Two main ways to access and organise the data:

- `device`: data representation of a single device holding information from different sources. Learn how to use it [in the examples](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples)
- `test`: intended for experimentation with the data and posterior reproducibility. See [below](#test).

### Test

The concept is very simple. A `test` is a collection of devices (SCKs or not), that have a gathered data with a common purpose. They can be located in the same spot (co-location) or not, and the main idea is that we centralise the data in a common data representation for easy analysis.

Tests have dates, authors, can have comments (for us to remember what we did), a report attached and, can be in different conditions (outdoor, indoor)... We will put all this metadata in a `yaml` file to help use look for the tests later on. 

Data fed into tests can also have different sources. They could be `csv` files, or data from the APIs such as the Smart Citizen API. For the local files, we will first pre-process them and then place them in the `raw` folder, in csv format. We use this format because it's a common usable format and, although it is not the most efficient way of archiving the data, it can be easily explored by other common applications.

### Pre-processing of sd-card data

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

When you create a test, it will have all the information needed to represent what all those devices together mean to you. This is a very powerful way of storing data, because in the future we will be able to access it and remember what happened. In addition, if you use a `jupyter notebook`, you can easily make data visualisations, process data, and many more things. Make sure you check the examples in [the repository](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/README.md).

## Making reports of your data

If you have created a `test`, and you want to make a nice looking website from your `notebook`, there are some tools you can use to generate some nice reports, with a custom template. These are generated with the `jupyter nbconvert` using the preprocessor and tools in the `notebooks` and `template` folder. 

To generate a report, follow the steps:

1. Tag the cells in your notebook. You can use the [Jupyter Lab Celltags](https://github.com/jupyterlab/jupyterlab-celltags) extension. Don't tag the cells you want to hide, and tag the ones you want to show with `show_only_output`. This can be changed and add more tags, but we keep it this way for simplicity

2. Go to the notebooks folder:

```
cd notebooks
```

3. Type the command:

```
jupyter nbconvert --config sc_nbconvert_config.py notebook.ipynb --sc_Preprocessor.expression="show_only_output" --to html --TemplateExporter.template_file=./templates/full_sc --output-dir=../reports --output=OUTPUT_NAME
```

Where:

- `sc_nbconvert_config.py` is the config
- `notebook.ipynb` is the notebook you want
- `"show_only_output"` is a boolean expression that is evaluated for each of the cells. If true, the cell is shown
- `./templates/full_sc` is the default template we have created
- `../reports` is the directory where we will put the `html` report
- `OUTPUT_NAME` is the name for the export

This generates an html export containing only the mkdown or code cell outputs, without any code. Examples can be found in [the source code repository](https://github.com/fablabbcn/smartcitizen-iscape-data/tree/master/data/reports).

!!! info "Don't like the template?"
    You can modify these templates in the [templates folder](https://github.com/fablabbcn/smartcitizen-iscape-data/tree/master/notebooks/templates)

And here is the result!

![](https://i.imgur.com/XNBnRUr.png)

## Upload data to Zenodo

Uploading results to [Zenodo](https://zenodo.org/) is also possible if you use the `test` data representation.

![](https://about.zenodo.org/static/img/logos/zenodo-black-1000.png)

Once you have your data organised in a `test`, you can upload the dataset and all it's metadata directly to [Zenodo](https://zenodo.org) and share it with others. An example of this is provided in the [example notebook](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/06_upload_to_zenodo.ipynb).

### Set it up

For this to work, we need to have a [token](https://zenodo.org/account/settings/applications/) in an environment variable called `ZENODO_TOKEN`. Once you have it, open up a terminal and add it to your environment like:

```
export ZENODO_TOKEN=fake-zenodo-token
```

In the same terminal, check it's there:

```
echo $ZENODO_TOKEN
fake-zenodo-token
```

Then launch `jupyter-lab` or start using your python scripts.

Alternatively, you can store a `.env` file in a place of your liking with your token:

```
ZENODO_TOKEN='yourtokenhere'
```

And then load it like:

```
export $(grep -v '^#' .env | xargs -0)
```

### Prepare the data

Next, you can define a `upload.yaml` file to describe the upload (see one example [here](https://github.com/fablabbcn/smartcitizen-iscape-data/blob/master/data/uploads/example_zenodo_upload.yaml):

```
example_upload_1.json: 
  title: 'Example Data 1'
  description: 'This field accepts <strong>HTML</strong>'
  upload_type: 'dataset'
  keywords: ['Low-Cost Sensors', 'Air Quality', 'Citizen Science']
  creators: [{'name': 'Author 1', 'affiliation': 'Affiliation 1', 'orcid': '0000-0000-0000-0001'}, 
            {'name': 'Author 2', 'affiliation': 'Affiliation 2', 'orcid': '0000-0000-0000-0002'}] 
  tests: ['TEST_1', 'TEST_2']
  access_right: 'open'
  options: 
    include_processed_data: false
    include_footer_doi: true
  communities: [{ "identifier": "community_in_zenodo"}]
  grants: [{"id": "GRANT_ID"}]
  report: ['report.pdf']
example_upload_2.json: 
  title: 'Example Data 2'
  description: 'This field accepts <strong>HTML</strong>'
  upload_type: 'dataset'
  keywords: ['Low-Cost Sensors', 'Air Quality', 'Citizen Science']
  creators: [{'name': 'Author 1', 'affiliation': 'Affiliation 1', 'orcid': '0000-0000-0000-0001'}, 
            {'name': 'Author 2', 'affiliation': 'Affiliation 2', 'orcid': '0000-0000-0000-0002'}] 
  tests: ['TEST_3', 'TEST_4']
  access_right: 'open'
  options: 
    include_processed_data: false
    include_footer_doi: false
  communities: [{ "identifier": "community_in_zenodo"}]
  grants: [{"id": "GRANT_ID"}]
  report: ['report_2.pdf']
```

!!! info
    All the keys below are linked to the [zenodo documentation](https://developers.zenodo.org/)

Different uploads can be defined by each main key: `example_upload_1.json` and `example_upload_2.json`. Each of them contains the following information (all of them can be later modified or added in the web interface in [zenodo.org](https://zenodo.org))

**Metadata for Zenodo**

- `title`: Name for the dataset
- `description`: dataset description (mandatory). This field accepts HTML
- `upload_type`: 'dataset' (mandatory - always, for now)
- `keywords`: list of keywords, such as `['Low-Cost Sensors', 'Air Quality', 'Citizen Science']`
- `creators`: dictionary containing the authors. Can contain the name, the affiliation and an [orcid](https://orcid.org/)
- `access_right`: 'open' (other options in the [zenodo documentation](https://developers.zenodo.org/))
- `communities`: id for the zenodo data community
- `grants`: grant id

**Upload**

- `tests`: `['TEST_1', 'TEST_2']`
- `options`: 
    + `include_processed_data`: true or false. Whether or not to include the processed data from the _processed_ folder in the test directory
    + `include_footer_doi`: true. If there is a report attached, add a nice footer to it with the DOI
- `report`: list of reports to attach. Must be also in the `data/uploads` folder

To upload the datasets, we can use the zenodo sandbox and a dry_run, to check everything is running well. Then, make these defaults to `False` to actually upload it:

```
# You can use the sandbox.zenodo.org for tests, as well as a dry_run. When you are happy with your upload, set these variables to False
# Then go to uploads in the zenodo section and publish whenever you are ready
data.upload_to_zenodo('example_zenodo_upload', sandbox = False, dry_run = True)
```

!!! warning
    Note that a `.json` file will be created in the data/uploads folder containing the metadata necessary for the upload (as liked by zenodo API). You can securely delete this file once you are done. Note that, in case `include_footer_doi=true`, the actual pdf to upload will be `report_doi.pdf`

Finally, **to actually deploy the dataset**, you need to visit the [deposit section](https://zenodo.org/deposit) and aprove it manually.

!!! info 
    Get the [iSCAPE](https://iscapeproject.eu/) datasets from Zenodo here:

    - https://zenodo.org/record/3570700
    - https://zenodo.org/record/3570680
    - https://zenodo.org/record/3570688
