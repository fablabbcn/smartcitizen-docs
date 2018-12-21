How to install the framework
============================

The following data analysis framework is built on Python 2.7 and Jupyter Notebooks. Here we will show you how to install it:

1. Dowload and Install Anaconda for Python 2.7 https://www.continuum.io/downloads

2. Visit [Github](https://github.com/fablabbcn/smartcitizen-iscape-data) to download the project folder or simply use `git`.


3. Open the **Anaconda Navigator** app and launch the **Jupyter Notebook**.

![](https://i.imgur.com/IBR56I7.png)

![](https://i.imgur.com/5Hlnmxh.png)

4. Using the **Jupyter Notebook** website browse your computer to find the project folder.

![](https://i.imgur.com/66901MG.png)


!!! note "Ready"
	Go and check [How to use the notebook](/Sensor Analysis Framework)

!!! note "Learn More"
	Still wondering what this is? Read this introduction to [Jupyter](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html)


!!! note "Advanced Installation"
	If you are already familiar with Python and you like to avoid installing **Anaconda** and follow the [Advanced users installation](#advanced-users-installation)

!!! note "Worried about your existing Python?"
	Do you have already a Python environment you use for other work and you are worried about updating some packages?

	Learn how to [load a dedicated environment](#how-to-run-the-project-isolated-from-your-python-environment)

## Advanced installation features

### How to run the project isolated from your Python environment

_Do you have already a Python environment you use for other work and you are worried about updating some packages?_

**Conda** can load a dedicated environment for you to run **Python** and **Jupyter** based on the `environment.yml` configuration file we provide.

Open your favourite shell on the directory you have your project. _(`cmd.exe` on windows)_

Run the following commands:

* This will install and load the Python environment we prepared for iSCAPE

    `conda env create -f environment.yml`

* Now activate the environment

    `source activate iscape`

*  Ready, run to run Jupyter

    `jupyter notebook`


### Advanced users installation

If you do not want to install **Anaconda** you can install all the dependencies manually. Just follow the steps above:

#### Install Python

Python is the main programming language we will use for Data Analysis.

- On Windows download and run the [installer](https://www.python.org/downloads/windows/) for Python 2.7
- Mac cames directly with python built in. However you can install the latest version using [Hombrew](https://brew.sh/) and then run `$ brew install python`
- On Linux simply use your distribution package manager like `$ apt` in Debian or Ubuntu.

#### Install Pip

Pip is the packet manager Python uses and it comes installed by default. If you have any issues you can download pip [here](https://pip.pypa.io/en/stable/installing/).

#### Installl Jupyter

Jupyter Notebooks allows us to quickly learn, develop and improve our tools by providing a common convenient framework and UI.

Simply run `pip install jupyter` on your terminal to install it.

#### Download the source

[Download](https://github.com/fablabbcn/smartcitizen-iscape-data) from Github or simply use `git`

```
git clone https://github.com/fablabbcn/smartcitizen-iscape-data.git
```

#### Run the notebook

On your terminal go to the folder where tou downloaded your files and then run `jupyter notebook` this will open a new webpage and you will be available to run your code there.
