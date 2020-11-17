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

### Development instructions (advanced)

1. Get the repo

Make a directory and `clone` the repository in it:

```
mkdir smartcitizen-data
cd smartcitizen-data
git clone https://github.com/fablabbcn/smartcitizen-data.git

```

!!! warning "Want to stay up-to-date?"
    The framework is being constantly updated and the only version that will always be up-to-date is in the [master branch of the github repository](https://github.com/fablabbcn/smartcitizen-data). We do not recommend to simply download the repository but to clone it with `git`. If you want to learn more about `git` and why it can help you in your projects, check [here](https://www.quora.com/What-is-Git-and-why-should-I-use-it)

2. Finish it up

The code in the framework is managed as internal dependencies. To activate this, you can run:

```
python setup.py install
```

## Run

You should now be ready to go! You can verify the installation by either running this command:

```
jupyter lab --version
```

To run `jupyter lab`, in your terminal type:

```
jupyter lab
```

This will open a web browser instance (by default [localhost:8888/lab]()) which gives access to the tools in the framework.

!!! note "Learn More"
	Still wondering what this is? Read this introduction to [Jupyter](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html)
