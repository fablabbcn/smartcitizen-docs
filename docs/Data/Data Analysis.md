Sensor Analysis Framework
=========================

[![DOI](https://zenodo.org/badge/97752018.svg){: align=left !important}](https://zenodo.org/badge/latestdoi/97752018)
<br>
[![Binder](https://mybinder.org/badge_logo.svg){: align=left !important}](https://mybinder.org/v2/gh/fablabbcn/smartcitizen-data-framework/master?filepath=%2Fexamples%2Fnotebooks)
<br>
[![PyPI version](https://badge.fury.io/py/scdata.svg){: align=left !important}](https://badge.fury.io/py/scdata)
<br>

When dealing with sensor data, specially with low cost sensors, a great part of the **effort needs to be dedicated to data analysis**. After a careful data collection, this stage of our experiments is fundamental to extract meaningful conclusions and prepare reports from them. For this reason, we have developed a data analysis framework that we call the **Sensor Analysis Framework**. In this section, we will detail how this framework is built, how to install it, and make most use of it.

![](/assets/images/saf_schema.png)

## We care for open science

The framework is written in [Python](http://www.python.org), and can be easily installed on any computer with simple `pip install scdata`. It is intended to provide an **state-of-the art data analysis environment**, adapted for the uses within the Smart Citizen Project, but that can be easily expanded for other use cases. The ultimate purpose of the framework is to allow for reproducible research by providing a set of tools that can be replicable, and expandable among researchers and users alike, contributing to [FAIR data principles](https://www.nature.com/articles/sdata201618). 

<p><a href="https://commons.wikimedia.org/wiki/File:FAIR_data_principles.jpg#/media/File:FAIR_data_principles.jpg"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/FAIR_data_principles.jpg/1200px-FAIR_data_principles.jpg" alt="FAIR data principles.jpg"></a><br>By <a href="//commons.wikimedia.org/w/index.php?title=User:SangyaPundir&amp;action=edit&amp;redlink=1" class="new" title="User:SangyaPundir (page does not exist)">SangyaPundir</a> - <span class="int-own-work" lang="en">Own work</span>, <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a></p>

!!! info "Raw and processed data"
    All the raw sensor data from the devices is sent to the Platform and processed outside of the sensors. **Raw data is never deleted**, and the postprocessing of it can be traced back to it's origin by using the sensor blueprint information. This way, we guarantee openness and accesibility of the data for research purposes.

    Check [this guide](/Guides/data/Custom data processing) to learn more about how we postprocess the data of the sensors and how to make it your own way.

The framework integrates with the [Smart Citizen API](/Data/Smart Citizen API) and helps with the analysis of **large amounts of data in an efficient way**. It also integrates functionality to **generate reports** in _html_ or _pdf_ format, and to **publish datasets** and documents to [Zenodo](https://zenodo.org).

!!! info "More familiar with R?"
    [R](https://www.r-project.org/) users won't be left stranded. [RPY2](https://pypi.org/project/rpy2/) provides functionality to send data from _python_ to _R_ quite easily.

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-iscape-data" aria-label="Check the source code">Check the source code</a>

## How we use it

The main purpose of the framework is to make our lives easier when dealing with various sources of data. Let's see different use cases:

**Get sensor data and visualise it**

This is probably the most common use case: exploring data in a visual way. The framework allows **downloading data** from the **Smart Citizen API** or **other sources**, as well as to load local csv files. Then, different data explorations options are readily available, and not limited to them due to the [great visualisation tools in python](https://pyviz.org/high-level/index.html). Finally, you can generate html, or pdf **reports** for sharing the results.

![](/assets/images/saf_schema_basic.png)

!!! info "Examples"
    Check [the examples](https://github.com/fablabbcn/smartcitizen-data/tree/master/examples) in the Github Repository

**Organise your data**

Handling a lot of different sensors can be at times difficult to organise and have traceability. For this, we created the concept of _test_, which groups a set of devices, potentially from various sources. This is convenient since metadata can be addeed to the test instance describing, for instance, what was done, the calibration data for the device, necessary preprocessing for the data, etc. This test can be later loaded in a separate analysis session, modified or expanded, keeping all the data findable.

![](/assets/images/saf_schema_test.png)

Some example metadata that can be stored would be:

- Test Location, date and author
- Kit type and reference
- Sensor calibration data or reference
- Availability of reference equipment measurement and type

!!! info "Check the guide"
    Check the guide on how to [organise sensor data](/Guides/data/Organise your data/)

**Clean sensor data**

Sensor data never comes clean and tidy in the real world. For this reason, data can be cleaned with simple, and not that simple algorithms for later processing. Several functions are already implemented (filtering with convolution, [Kalman filters](https://en.wikipedia.org/wiki/Kalman_filter), anomaly detection, ...), and more can be implemented in the source files.

![](/assets/images/saf_schema_cleaning.png)

**Model sensor data**

Low cost sensor data needs calibration, with more or less complex regression algorithms. This can be done at times with a simple linear regression, but it is not the only case. Sensors generally present non-linearities, and linear models might not be the bests at handling the data robustly. For this, a set of models ir rightly implemented, using the power of common statistics and machine learning frameworks such as [sci-kit learn](http://scikit-learn.org/), [tensorflow](https://www.tensorflow.org), [keras](http://keras.io/), and [stats models](http://www.statsmodels.org/dev/tsa.html#module-statsmodels.tsa).

![](/assets/images/saf_schema_models.png)

!!! info "Guidelines on sensor development"
    Check our [guidelines](/Guides/deployments/) on sensor deployment to see why this is important in some cases.

**Batch analysis**

Automatisation of all this tools can be very handy at times, since we want to spend less time programming analysis tools than actually doing analysis. Tasks can be programmed in batch to be processed automatically by the framework in an autonomous way. For instance, some interesting use cases of this could be:

- Downloading data from many devices, do something (clean it) and export it to .csv
- Downloading data and generate plots, extract metrics and generate reports for many devices
- Testing calibration models with different hyperparameters, modeling approaches and datasets

![](/assets/images/saf_schema_batch.png)

**Share data**

One important aspect of our research is to share the data so that others can work on it, and build on top of our results, validate the conclusions or simply disseminate the work done. For this, integration with [zenodo](https://zenodo.org) is provided to share datasets and reports:

![](/assets/images/saf_schema_zenodo.png)

Have a look at the features within the framework: 

- Tools to **retrieve data** from the Smart Citizen's API or to load them from local sources (in csv format, compatible with the SCK SD card data)
- A **data handling framework** based on the well known [Pandas](http://www.pandas.org) package
- An **exploratory data analysis** tools to study sensor behaviour and correlations with different types of plots
- A **sensor model calibration toolset** with classical statistical methods such as linear regression, ARIMA, SARIMA-X, as well as more modern Machine Learning techniques with the use of LSTM networks, RF (Random Forest), SVR (Support Vector Regression) models for sequential data prediction and forecasting
- Methods to statistically validate and study the performance of these models, export and store them
- As a bonus, an interface to convert the python objects into the statistical analysis language R

!!! info
    Check the guide on how to set it up [here](/Guides/data/Upload data to zenodo/)

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-data/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-data" aria-label="Check the source code">Check the source code</a>
