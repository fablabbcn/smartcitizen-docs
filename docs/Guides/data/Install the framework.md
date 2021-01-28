How to install the framework
============================

The following data analysis framework is a set of tools built on Python 3.7 to help you analyse your data. It can be used with [Jupyter Notebooks](https://jupyter.org/) or [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/), although it is not mandatory.

## Before getting started

The framework runs in python 3.6 or more. Download and install python following [this guide](https://docs.python-guide.org/starting/installation/) if you don't already have it.

## Installation

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

`clone` the repository in a directory you like:

```
git clone https://github.com/fablabbcn/smartcitizen-data.git
...
cd smartcitizen-data
```

!!! warning "Want to stay up-to-date?"
    The framework is being constantly updated and the only version that will always be up-to-date is in the [master branch of the github repository](https://github.com/fablabbcn/smartcitizen-data). We do not recommend to simply download the repository but to clone it with `git`. If you want to learn more about `git` and why it can help you in your projects, check [here](https://www.quora.com/What-is-Git-and-why-should-I-use-it)

To install it, you can simply run the command below. You can use a virtual environment if you like as well.

```
python setup.py install
```