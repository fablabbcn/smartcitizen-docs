Sensor Analysis Framework
=========================

[![DOI](https://zenodo.org/badge/97752018.svg)](https://zenodo.org/badge/latestdoi/97752018)

When dealing with sensor data, specially with low cost sensors, a great part of the effort needs to be dedicated to data analysis. After a careful data collection, this stage of our experiments is fundamental to extract meaningful conclusions and prepare reports from them. For this reason, we have developed a data analysis framework that we call the **Sensor Analysis Framework**. In this section, we will detail how this framework is built, how to install it, use it and build on top of it!

![](https://imgs.xkcd.com/comics/the_data_so_far.png)

_Image source: [xkcd](https://xkcd.com/373/)_

The framework is writen in [Python](http://www.python.org), and can be run using [Jupyter Notebooks](http://jupyter.org/) or [Jupyter Lab](https://github.com/jupyterlab/jupyterlab). It is intended to provide an state-of-the art data analysis environment, adapted for the uses within the Smart Citizen Project, but that can be easily expanded for other use cases.

!!! info "More familiar with R?"
    [R](https://www.r-project.org/) users won't be left stranded. [R2PY](https://rpy2.bitbucket.io/) provides functionality to send data from _python_ to _R_ quite easily!

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-iscape-data" aria-label="Check the source code">Check the source code</a>

## How we use it

The _Sensor Analysis Framework_ is mainly used to:

- Handle sensor data acquisition, either from local CSV files or the API
- Perform data cleaning and anomaly detection
- Apply sensor models for actual pollutant concentration calculations
- Create reports, plots and visualisations

![](https://i.imgur.com/siufqdY.png)

The framework can be used in an interactive manner, using the example notebooks in the [repository](https://github.com/fablabbcn/smartcitizen-iscape-data/tree/master/notebooks/src_ipynb), but it can be also used to process data in _batch_. This is described in [the batch analysis secion of this documentation](/Sensor%20Analysis%20Framework/guides/Analyse%20your%20data%20in%20batch) and is a quite handy, fast and scalable way of processing the data.

!!! info "Want to make a lot of plots, of a lot of SCKs?"
    Visit [here](/Sensor%20Analysis%20Framework/guides/Analyse%20your%20data%20in%20batch)!

### A deeper look

Have a look at the features within the framework: 

- Tools to **retrieve data** from the Smart Citizen's API or to load them from local sources (in csv format, compatible with the SCK SD card data)
- A **data handling framework** based on the well known [Pandas](http://www.pandas.org) package
- An **exploratory data analysis** tools to study sensor behaviour and correlations with different types of plots
- A **sensor model calibration toolset** with classical statistical methods such as linear regression, ARIMA, SARIMA-X, as well as more modern Machine Learning techniques with the use of LSTM networks, RF (Random Forest), SVR (Support Vector Regression) models for sequential data prediction and forecasting
- Methods to statistically validate and study the performance of these models, export and store them
- As a bonus, an interface to convert the python objects into the statistical analysis language R

!!! tip "Step by step guides"
	* [Install the framework](/Sensor%20Analysis%20Framework/guides/Install%20the%20framework/)
	* [Use Machine Learning to Create Models for Sensors Calibration](/Sensor%20Analysis%20Framework/guides/Creating%20Models%20for%20Sensors%20Calibration/)
	* [Organise your data](/Sensor Analysis Framework/guides/Organise your data/)
    * [Batch analysis of your data](/Sensor%20Analysis%20Framework/guides/Analyse%20your%20data%20in%20batch)

#### Loading and managing the data

Data can be downloaded from the SmartCitizen API with the KIT IDs or using csv. In order to tidy up the data, the recordings are organised around the concept of **test**, an entity containing all the kits' references, sensors and general information regarding the conditions at which the measurements were carried out:

- Test Location, date and author
- Kit type and reference
- Sensor calibration data or reference
- Availability of reference equipment measurement and type

A brief schema of the test structure is specified below:

<div style="text-align:center">
<image src="https://i.imgur.com/CSi5tL4.png" width="500px"/>
</div>

All this structure is filled up at the test creation with a dedicated script, saving future time to understand mismatching reading units, timestamps formats and so on.

!!! info "Create your tests"
    Visit the guide on [organising your data](/Sensor%20Analysis%20Framework/guides/Organise%20your%20data) 

#### Exploratory data analysis

The device's data can be explored visually with different types of plots. It can also be generated in batch with descriptor files, as shown in the [guide](/Sensor%20Analysis%20Framework/guides/Analyse%20your%20data%20in%20batch).
 Some of the functionalities implemented are:

- Time series visualisation
- Correlation plot and pairs plot
- Correlogram
- Heatmaps
- Violin plots

This section uses interactive plotting frameworks as [Plotly](http://plot.ly) and the well known [matplotlib](http://matplotlib.org/) to serve different exploratory analysis tools.

#### Data models

The data models section includes tools to prepare, train and evaluate models coming from different devices within a test in order to calibrate your sensors. It provides an interface with common statistics and machine learning frameworks such as [sci-kit learn](http://scikit-learn.org/), [tensorflow](https://www.tensorflow.org), [keras](http://keras.io/), and [stats models](http://www.statsmodels.org/dev/tsa.html#module-statsmodels.tsa). These frameworks provide tools to perform:

**Pre-processing stage:**

- **Outliers** detection with Holt-Winters methods (triple exponential smoothing) and XGBoost Regressors
- Data study and analysis for **multicollinearity** and **autocorrelation** in order to determine significant variables and avoid model overfit with non-significant exogenous variables
- **Trend decomposition** and **seasonality** analysis

**Model stage:**

- **Baseline model** estimations in order to assess minimum targets for model quality (using naive regression models)
- **Ordinary Linear Regression** techniques for univariate and multivariate linear and non-linear independent variables
- **ARIMA-X** (Autorregresive, Integrated, Moving Average) models with exogenous variables using Box-Jenkis parameter selection methods
- **Supervised learning** techiques:
    - Single and multiple layers **LSTM** (Long-Thort Term Memory) networks with configurable structure
    - Random Forest and Support Vector methods for regression

An example of the model is shown below for the estimation of the SGX4514 CO with the use of the rest of the Kit's available sensor, using a single layer LSTM network only two weeks of training:

![](https://i.imgur.com/Sdy5vWy.png)

Depending on the model selected, different validation techniques are implemented, in order to verify models' assumptions and avoid data misinterpretation (i.e. *Durbin Watson* or *Jacque Bera* test for linear regression). Finally, it is important to follow carefully the instructions as stated in the notebook, in order to avoid low model quality.

#### Model import/export and storage

Once the model is analysed and validated, it can be saved and exported. This allows using the model in the future with the same variables in other sensor studies. The model objects are serialised with [joblib](https://github.com/joblib/joblib) and can be uploaded to the [Models Github Repository](https://github.com/fablabbcn/smartcitizen-iscape-models) for later use.

## Source files

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-iscape-data/archive/master.zip" data-icon="octicon-cloud-download" aria-label="Download from GitHub">Download</a>

<a class="github-button" data-size="large" href="https://github.com/fablabbcn/smartcitizen-iscape-data" aria-label="Check the source code">Check the source code</a>