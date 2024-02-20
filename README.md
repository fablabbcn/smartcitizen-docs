# smartcitizen-docs

The project main documentation available at https://docs.smartcitizen.me/

## Related Smart Citizen repositories

* Platform Core API [github.com/fablabbcn/smartcitizen-api](https://github.com/fablabbcn/smartcitizen-api)
* Platform Web [github.com/fablabbcn/smartcitizen-web](https://github.com/fablabbcn/smartcitizen-web)
* Platform Onboarding [github.com/fablabbcn/smartcitizen-onboarding-app](https://github.com/fablabbcn/smartcitizen-onboarding-app)
* Kit Enclosures [github.com/fablabbcn/smartcitizen-enclosures](https://github.com/fablabbcn/smartcitizen-enclosures)
* Useful software resources for communities [github.com/fablabbcn/smartcitizen-toolkit](https://github.com/fablabbcn/smartcitizen-toolkit)

## Usage

### Install Python 3

Python newies! Read the following [guide](https://realpython.com/installing-python/).

### Setup

`pip install -r requirements.txt`

_In Windows if it fails use `pip install -r requirements.txt --user` instead._

### Edit

`mkdocs serve`

_In Windows if it fails use `python -m mkdocs serve` instead._

### Deploy

Deploy is done by default via Github Action. See `/.github/workflows/main.yml`. 

For custom installations you can use `mkdocs gh-deploy`.
