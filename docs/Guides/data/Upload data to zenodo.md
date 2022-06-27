# Upload data to Zenodo

Uploading results to [Zenodo](https://zenodo.org/) is also possible using the data analysis framework.

![](https://about.zenodo.org/static/img/logos/zenodo-black-1000.png)

Once you have your data organised in a test, you can upload it directly to Zenodo and share it with others. An example of this is provided in the [example notebook](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples/notebooks/06_upload_to_zenodo.ipynb).

## Set it up

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

## Prepare the data

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
