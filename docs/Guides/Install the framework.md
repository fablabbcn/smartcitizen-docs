How to install the framework
============================

The following data analysis framework is a set of tools built on Python 3.7 to help you analyse your data. It can be used with [Jupyter Notebooks](https://jupyter.org/) or [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/), although it is not mandatory. 

## Prerequisites

We recommend you use these two tools for managing the different versions of the framework and keep it updated.

1. Download and install `git` from [here](https://git-scm.com/)
2. Download and install `Anaconda` for Python 3.7 from [here](https://www.anaconda.com/distribution/)

## Installation

Open your favourite shell on the directory you have your project. _(`cmd.exe` on windows)_

### Get the repo

Make a directory and `clone` the repository in it:

```
➜  mkdir data_analysis
➜  cd data_analysis
➜  git clone https://github.com/fablabbcn/smartcitizen-iscape-data.git
...
```

!!! warning "Want to stay up-to-date?"
    The framework is being constantly updated and the only version that will always be up-to-date is in the [master branch of the github repository](https://github.com/fablabbcn/smartcitizen-iscape-data). We do not recommend to simply download the repository but to clone it with `git`. If you want to learn more about `git` and why it can help you in your projects, check [here](https://www.quora.com/What-is-Git-and-why-should-I-use-it)

### Create the environment

Navigate to the cloned repository and create an environment for anaconda. We provide an `environment.yml` file to help with the process:

```
➜  cd smartcitizen-iscape-data
➜  smartcitizen-iscape-data git:(master) ✗ conda env create -f environment.yml
```

**Alternatively**, you can open Anaconda Navigator and `Import` an environment in the `Environment section`:

![](https://i.imgur.com/aAsrDXz.png) 

!!! info "Note about different platforms"
    Different platforms (Windows, Mac, Linux...) may have different dependencies for each package. We have tried to make the environment as clean as possible, but there might be still some `ModuleNotFound Errors`. Please, use the [issue tracker](https://github.com/fablabbcn/smartcitizen-iscape-data/issues) in the project to help us improve!

### Finish it up

The code in the framework is managed as internal dependencies. To activate this, you can run:

```
➜  pip install --editable . --verbose
```

Additional commands to install jupyter lab extensions are given in the `.dotfile`:

```
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.0
jupyter labextension install @jupyterlab/toc
jupyter labextension install jupyterlab-plotly@1.0.0
conda install -c conda-forge jupyter_nbextensions_configurator
```

With an optional one for plotly chart studio:

```
jupyter labextension install jupyterlab-chart-editor@1.2
```

You can run it by:

```
➜  chmod +x .dotfile
➜  ./.dotfile
```

## Run

You should now be ready to go! You can verify the installation by either running this command:

```
(smartcitizen-data) ➜  ~ jupyter lab --version
1.0.2
```

Or opening Anaconda Navigator: 

![](https://i.imgur.com/THpoxd1.png)

To run the framework, in your terminal type:

```
(smartcitizen-data) ➜  smartcitizen-iscape-data git:(master) ✗ jupyter lab
```

This will open a web browser instance (by default [localhost:8888/lab]()) which gives access to the tools in the framework.

!!! note "Learn More"
	Still wondering what this is? Read this introduction to [Jupyter](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html)