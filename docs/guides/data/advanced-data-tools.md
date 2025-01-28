# Python, R and Jupyter

This guide will help set up and start working with more advanced data tools. We recommend using these tools for accessing and performing operations on the data coming from multiple devices, visualising it, or _maybe_ testing sensor calibration models.

There are two options for this:
- A couple of advanced `python` packages for accessing the data from the [Smart Citizen API]({{ extra.urls.api.link }})
- A more simple `R` package for those that prefer it (although not so advanced as the `python` ones...)

!!!info "Rather watch a video?"
    You can check [our webinars on the topic](https://www.youtube.com/watch?v=wNrGuTGbo5w&list=PL33KKs9g8Y1IWsTZZmDc-46yFuuIRZEmi&index=19&t=1s)!

Both, `python` and `R` packages can be used with [Jupyter Notebooks](https://jupyter.org/) or [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/), although it is not mandatory. For `R` users, you can of course use [RStudio](https://www.rstudio.com/categories/rstudio-ide/).

## Python package

### Requirements

The framework runs in python 3.6 or later. Download and install python following [this guide](https://docs.python-guide.org/starting/installation/) if you don't already have it.

### Installation

Open your favourite shell on the directory you have your project. _(`cmd.exe` on windows)_

```
pip install scdata
```

You can now check if it all works by:

```
python
>>> import scdata as sc
>>> ...
```

### Development instructions (advanced)

You can `clone` the repository in a directory you like:

```
git clone https://github.com/fablabbcn/smartcitizen-data.git
...
cd smartcitizen-data
```

!!! warning "Want to stay up-to-date?"
    The framework is being constantly updated and the only version that will always be up-to-date is in the [master branch of the github repository](https://github.com/fablabbcn/smartcitizen-data). We do not recommend to simply download the repository but to clone it with `git`. If you want to learn more about `git` and why it can help you in your projects, check [here](https://www.quora.com/What-is-Git-and-why-should-I-use-it)

To install it, you can run the command below. You can use a virtual environment if you like as well.

```
python setup.py install
```

### Examples

We have an entire repository of examples, which can be checked out at the [scdata Github repository](https://github.com/fablabbcn/smartcitizen-data/blob/master/examples).

## R

The R _package_ (not really a CRAN package, but does the job), lives in [smartcitizen-R-data](https://github.com/fablabbcn/smartcitizen-R-data). It should be easily installed by:

```
library(devtools)
install_github("fablabbcn/smartcitizen-R-data")
```

You can then check the [example file](https://github.com/fablabbcn/smartcitizen-R-data/blob/master/example.R), or the [example notebook file](https://github.com/fablabbcn/smartcitizen-R-data/blob/master/notebook_example.ipynb) (see the README for installing kernel in jupyter):

```
# source("R/apidevice.R")
load_all()

# Input here device ID
device_id <- 14675
d <- ScDevice$new(id = device_id)

# This gets sensor and metrics names
d$get_names()
d$names

# Some metadata of the device...
d$get_json()
d$json

# Request the data of the device
# You can also pass rollup, min_date and max_date as an argument (see help)
d$get_device_data()

# Tabular data
data <- d$data
```
