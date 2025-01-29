# Analyse your data in batch

Sometimes we have a lot of devices to process, and the interfaces for analysis in [{{ extra.urls.platform.name }}]({{ extra.urls.platform.link }}) or in the `jupyter notebook` might not be the most efficient way to do it. For this reason, we have developed a functionality to process the data in batches, defining the tasks to perform in a `json` descriptor file.

The descriptor file can be placed in the `src/tasks` directory (or any, actually). An example of how to run it is shown in [`examples/batch_analysis.ipynb`](https://github.com/fablabbcn/smartcitizen-iscape-data/blob/master/examples/batch_analysis.ipynb):

```
# Load the object
from src.models.batch import batch_analysis",
tasks_file = '../tasks/batch.json'",
batch_session = batch_analysis(tasks_file, verbose = True)

# Run the analysis
batch_session.run()
```

## Functionality

These tasks are intended to automatise data analysis tasks as the following:

- Load, process and export processed data
- Generate models and apply them, extracting metrics and comparing if they extrapolate to different set of sensors in different datasets, without having to run extra code
- Make plots for different metrics in an automatic way, and export their renders

## Workflow

![](https://i.imgur.com/eDBftEx.png)

## Json task description

The descriptor file loaded is a `json` containing keys for each task to be run. Several tasks can be included and will be run consecutively:

```
{
    "TASK_1":{...},
    "TASK_2":{...},
    "TASK_3":{...}
}
```

Each of the `tasks` contains different fields, depending on what the process is.

### Define data

In case **no model needs to be calculated**, the data can be specified directly in the task:

```
{
    "TASK_1":{
        "data":{
            "datasets": {
                "TEST_1": ["DEVICE_11","DEVICE_12"],
                "TEST_2": ["DEVICE_21", "DEVICE_22", "DEVICE_23"],
                ...
                        },
            "data_options": {"avoid_processed": true,
                            "frequency": "1Min",
                            "clean_na": true,
                            "use_cache": true,
                            "clean_na_method": "drop",
                            "min_date": null,
                            "max_date": null,
                            "export_data": null,
                            "rename_export_data": false}
                    }
}
```

If a model is to be calculated, the data is defined within the model key as seen below. 

#### Data loading options

- `frequency`: frequency at which load the data (as defined in `pandas` [here](https://stackoverflow.com/questions/35339139/where-is-the-documentation-on-pandas-freq-tags
))
- `clean_na`: clean or not NaN
- `clean_na_method`: `drop` or `fill` with back-forward filling
- `use_cache`: whether or not to use file chaching for the analysis. This adds a `cached` folder in the corresponding `test` directory, which allows faster download from the `API`. It is implemented so that the only data to be downloaded is the one that is not cached
- `min_date`, `max_date`: for limitting the amount of data to be loaded
- `export_data`: if the processed data (after pre-processing and modeling) has to be exported. It will be saved in the corresponding `test` folder, under `processed`. Options are:
    + `None`: don't export anything
    + `All`: all channels in the `pandas dataframe`
    + `Only Generic`: Export only channels that are under the `data/interim/sensorNamesExport.json`
    + `Only Processed`: Export only channels that are tagged as `processed` under the `data/interim/sensorNamesExport.json`
- `rename_export_data`: Rename the exported channels for better readability using the file `data/interim/sensorNamesExport.json`

!!! info "None?"
    In `json`, we specify the `python` `None` as `null`.

!!! tip "Want to save time?"
    Enable `use_cache` and we will save some time by checking if the data we have downloaded previously from the API can be used. This also applies for pre-processing functions.

<!-- ### Pre-process data

Different preprocessing options can be defined. The most common one, for the sensors in the _Smart Citizen Project_ are the analysis of the _electrochemical sensors_ but others can be used and implemented, for later call from `/src/models/batch.py`.

```
    "TASK_1": {
        "pre-processing": {
                "alphasense": {"baseline_method": "deltas",
                                "parameters": [30, 45, 5],
                                "methods": {"CO": ["classic", "na"],
                                            "NO2": ["baseline", "single_aux"],
                                            "O3": ["baseline", "single_aux"]
                                            },
                                "overlapHours": 0
                            }
            },
    }
```

**Note**: this section is currently project specific for electrochemical sensors defined [here](https://docs.smartcitizen.me/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors)

- `baseline_method`: baseline method used to calculate pollutant concentration, as defined in [the documentation](https://docs.smartcitizen.me/Components/Gas%20Pro%20Sensor%20Board/Electrochemical%20Sensors/#sensor-calibration). It can be `deltas` or `als`, using the methodology described in [here](https://doi.org/10.1016/j.atmosenv.2016.10.024) for `deltas` or [here](https://zanran_storage.s3.amazonaws.com/www.science.uva.nl/ContentPages/443199618.pdf) for the Asymmetric Least Squares Smoothing (ALS). 
- `parameters`: parameters for the baseline determination:
    + in case of `deltas` method, is a `list` with [`min_delta`, `max_delta`, `interval`]
    + in case of `als` method, is another `dict` containing `lambda` and `p` parameters
- `methods`: a dict containing which method to use for each pollutant calculation (see example above). options for the calculation are `classic` from Alphasense Ltd. recommendations, or `baseline`, using the `baseline_method` specified before. Each of them can use different baselines (`single_aux`, `single_temp` or `single_hum`). -->

### Model

!!! warning "Recommended to just get in touch"
        This can be overwhelming at first. Just get in touch at [{{ extra.urls.support.name }}]({{ extra.urls.support.link }}).

In the `model` sub-task, currently three possibilities are implemented:

- Linear methods: `OLS` or `RLM` regression
- Random Forest (`RF`) or Support Vector Regressor `SVR`
- XGBoost

In the case of having a `model` task, the `data` defined above is ignored, and only the one under `model: {"data":{}}` is used. 

!!! warning "One model per task"
    It is better to generate only one model per task, since the memory used by the models can be very large.

An example is shown below:

```
"model": {
        "model_name": "Random_Forest_100",
        "model_type": "RF",
        "model_target": "ALPHASENSE",
                    "data": {"train": {"TEST_1": {"devices": ["DEVICE_1"],
                                                 "reference_device":"REF_DEVICE_1"}},
                            "test": {"TEST_1": {"devices": ["DEVICE_1", "DEVICE_2"],
                                                 "reference_device":"REF_DEVICE_2"},
                                     "TEST_2": {"devices": ["DEVICE_3"],
                                                "reference_device": "REF_DEVICE_3"},
                                     "TEST_3": {"devices": ["DEVICE_4"],
                                                "reference_device": "REF_DEVICE_4"},
                                     "TEST_2": {"devices": ["DEVICE_5"],
                                                "reference_device": "REF_DEVICE_5"}},
                "features": {"REF": "NO2_REF",
                            "A":  "GB_2W",
                            "B": "GB_2A",
                            "C": "HUM"
                            }
                "data_options": {"export_data": "All",
                            "rename_export_data": false,
                            "target_raster": 1Min",
                            "clean_na": true,
                            "clean_na_method": "fill",
                            "min_date": null,
                            "max_date": null,
                            "use_cache": true}
                },
        "hyperparameters": {"ratio_train": 0.75,
                            "n_estimators": 100,
                            "shuffle_split": true
                            },
        "model_options": {"session_active_model": false,
                    "export_model": false,
                    "export_model_file": false,
                    "extract_metrics": true,
                    "save_plots": false,
                    "show_plots": false
                    }
        },

```

- `model_name`: model name to be saved
- `model_type`: 'RF', 'SVR', 'LSTM' or 'OLS'
- `model_target`: if the model is to be stored under a specific category of models under the `models/` folder
- `data`: dict containing the data to use for training, and features description. Under `train`, we define which of the tests and devices is to be used for the model definition, with the format `{"TEST": "devices": ["DEVICE"], "reference_device": "REF_DEVICE_1"}`. Under `test`, we define a series of `test` in which we'll evaluate the model extracted from the `train` dataset:
    + `devices`: list of devices to use
    + `reference_device`: `device` that contains the reference data

!!! info
        Multiple training datasets are possible as well, by combining them.

Additionally:
    + `features`: dict of `devices` tagged as `REF`, `A`, `B`, `C`... to define the features of the model, being `REF` the reference channel in the `reference_device`
- `hyperparameters`: dict containing different hyperparameters, depending on the type of model:
    + For all:
        *  `ratio_train`: generic, train-test split ratio
    +  OLS:
        *  `formula_expresion`: stats models formula type, accepting `numpy` expressions This formula has to reference the features described under the `data` section. Example: `REF ~ A * B + np.log(C/2)`
    + Random Forest:
        * `n_estimators`: only for `RF`. number of forests to use
        * `shuffle_split`: only for `RF`. whether or not use shuffle split
    + LSTM:
        * `n_lags`: number of lags to account in the LSTM input
        * `epochs`: number of epochs (100 or more recommended)
        * `batch_size`: batch size (72 recommended)              
        * `verbose`: verbose output during training
        * `loss`: loss function ('mse' or others)
        * `optimizer`: optimizer to use (`adam` or others)
        * `layers`: specific layer structure. Example below:

        ```
        "layers": [{"type": "lstm",
                    "neurons": 100,
                    "return_seq": true
                },
                {
                    "type": "dropout",
                    "rate": 0.05
                },
                {
                    "type": "lstm",
                    "neurons": 100,
                    "return_seq": true
                },
                {
                    "type": "lstm",
                    "neurons": 50,
                    "return_seq": false
                },
                {
                    "type": "dropout",
                    "rate": 0.05
                },
                {
                    "type": "dense",
                    "neurons": 1,
                    "activation": "linear"
                }
            ]},
        ```

- `model_options`: different options for the model calculated
    + `session_active_model`: keep the model active after the task is completed
    + `export_model`: export the model (parameters, hyperparameters, weights) to the `model/model_type` folder after the task is completed
    + `export_model_file`: export the model file (not recommended for `RF`) fo the same folder as above
    + `export_metrics`: export metrics for the model or not
    + `save_plots`: save model plots or not
    + `show_plots`: show model plots or not

### Plots

The plot sub-task accepts two different libraries: `matplotlib` and `plotly`. The first one generates static images, that we can export for nice quality graphs, while `plotly` is more meant for exploratory analysis.

!!! info "Many plots? No problem"
    In the case of the models, we only wanted one model per task, but it's not the case in the plots.

```
"plot": {
    "2": {"plot_type": "timeseries",
        "plotting_library": "matplotlib",
        "data": {"test": "TEST_1",
                "traces": {"1": {"device": "5262",
                                "channel" : "EXT_PM_10",
                                "subplot": 1},
                            "2": {"device": "5262",
                                "channel" : "EXT_PM_25",
                                "subplot": 2}}},
        "options": {"show_plot": false,
                    "separate_device_plots": false,
                    "target_raster": "10Min",
                    "max_date": null,
                    "min_date": null,
                    "export_path": "/Users/mac/Desktop",
                    "file_name": "plot_pm"},
        "formatting": {"xlabel": "Date (-)",
                        "ylabel": {"1": "Temp degC",
                                    "2": "Hum (%rh)"},
                        "yrange": {"1": [0, 40], 
                                    "2": [0, 100]},
                        "title": "PM",
                        "sharex":true,
                        "grid": true,
                        "height": 10,
                        "width": 12}
    },
```

#### General description

This description is suitable for timeseries plots. Check below for other types:

![](https://i.imgur.com/p6qogrD.png)

- `plot_type`: the plot type to be used. Currently we support `timeseries`, `violin`, `scatter_matrix`, `correlation_plot`, `heatmap`, `barplot`, `coherence_plot`
- `plotting_library`: `matplotlib` or `plotly`
- `data`: the data to represent. This data has to be loaded previously. This is only to define the plot:
    + `test`: each plot can only represent data from a single `test`
    + `traces`: numbered entries to specify the `device`, `channel` and, if applicable, the subplot (only for timeseries)

!!! info "Same plot for many devices?"
    Set "`device`: 'all'" and  `"separate_device_plots": true`, and we will make separate plots for each device.

- `options`: 
    + `show_plot`: whether or not to show the plot. Not recommended for large amounts
    + `separate_device_plots`: `true` in case we want a single plot for each device in `traces: devices`. `false` in case we want to merge all the devices in a single plot (for comparison purposes). Applicable for timeseries
    + `target_raster`: the frequency of the data to plot. Reduces processing time
    + `min_date`, `max_date`: if not `null`, they crop the data with those dates
    + `export_path`: where to put the plot. If `null`, we won't export anything
    + `file_name`: how to name the plot. We will append the trace name in case `separate_device_plots` is set to `true`
- `formatting`: 
    + `xlabel`: Name to tag the x axis of the plot
    + `ylabel`: Name to tag the y axis(es) of the plot. It can be more than one value in a `json` style
    + `yrange`: Range fro the y axis(es). Same as above
    + `title`: plot title
    + `grid`: to show the grid or not
    + `height`, `width`: plot height and width

#### Plots specifics

**Heatmap**

![](https://i.imgur.com/bKyX7fb.png)

```
"1" : {"plot_type": "heatmap",
        "plotting_library": "matplotlib",
        "data": {"test": "TEST_1",
                "traces": {"1": {"device": "all",
                                "channel" : "NOISE_A",
                                "subplot": 1}}},
        "options": {"show_plot": false,
                    "separate_device_plots": true,
                    "target_raster": "10Min",
                    "min_date": null,
                    "max_date": "2019-01-03",
                    "relative": false,
                    "export_path": "/Users/macoscar/Desktop",
                    "file_name": "heatmap_noise"},
        "formatting": {"title": "Magnificent plot",
               "grid": true,
               "height": 10,
               "width": 15,
               "frequency_hours": 6}
        }
```

!!! warning ""
    Note that in this case it only makes sense to put one trace. If we define `"device": "all"`, then `"separate_device_plots": true`

- `plotting_library`: recommended library is `matplotlib` (although we actually use seaborn)
- `formatting`:
    + `frequency_hours`: to choose between 1, 2, ..., 6, 12, 24. Resamples the data to make it fit in bins of that size to create the heatmap

**Correlation plot**

![](https://i.imgur.com/ACxGP9n.png)

```
"1" : {"plot_type": "correlation_plot",
       "plotting_library": "matplotlib",
       "data": {"test": "TEST_1",
                       "traces": {"1": {"device": "5261",
                                       "channel" : "NOISE_A",
                                       "subplot": 1},
                                 "2": {"device": "5262",
                                      "channel": "TEMP",
                                      "subplot": 1}}},
       "options": {"show_plot": True,
                   "separate_device_plots": false,
                   "export_path": "/Users/macoscar/Desktop", 
                   "file_name": "plot_corr",
                   "target_raster": '10Min',
                   "min_date": None,
                   "max_date": None},
       "formatting": {"jpkind": 'scatter',
                      "title": "Magnificent plot",
                      "xrange": [0, 100],
                      "yrange": [0, 40],
                      "grid": True,
                      "height": 10,
                      "width": 15}
       }
```

Note that in this case it only makes sense to put two traces, in the same subplot.

- `formatting`: 
    + `jpkind`: type as defined in [sns.jointplot documentation](https://seaborn.pydata.org/generated/seaborn.jointplot.html), to choose from { “scatter” | “reg” | “resid” | “kde” | “hex” 



**Scatter plot matrix**

 The big brother of the `correlation plot`:

![](https://i.imgur.com/IfLLAUg.jpg)

```
"1" : {"plot_type": "scatter_matrix",
        "plotting_library": "matplotlib",
        "data": {"test": "TEST_1",
                        "traces": {"1": {"device": "5262",
                                        "channel" : "GB_2W",
                                        "subplot": 1},
                                  "2": {"device": "5262",
                                       "channel": "TEMP",
                                       "subplot": 1},
                                  "3": {"device": "5262",
                                       "channel": "HUM",
                                       "subplot": 1}}},
        "options": {"show_plot": True,
                    "separate_device_plots": False,
                    "export_path": "/Users/macoscar/Desktop", 
                    "file_name": "plot_scatter",
                    "target_raster": '10Min',
                    "min_date": None,
                    "max_date": None},
        "formatting": {"title": "Magnificent plot",
                       "grid": True,
                       "height": 4,
                       "width": 4}
        }
```

 **Coherence plot**

![](https://i.imgur.com/DmvnwBj.png)

This plot it's used to plot the coherence between x and y. Coherence is the normalized cross spectral density. More info [here](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.cohere.html):

```
"1" : {"plot_type": "coherence_plot",
        "plotting_library": "matplotlib",
        "data": {"test": "TEST_1",
                        "traces": {"1": {"device": "5262",
                                        "channel" : "GB_2W",
                                        "subplot": 1},
                                  "2": {"device": "5262",
                                       "channel": "TEMP",
                                       "subplot": 1}}},
        "options": {"show_plot": True,
                    "separate_device_plots": False,
                    "export_path": "/Users/macoscar/Desktop", 
                    "file_name": "plot_coherence",
                    "target_raster": '10Min',
                    "min_date": None,
                    "max_date": None},
        "formatting": {"title": "Magnificent plot",
                       "grid": True,
                       "height": 10,
                       "width": 15}
        }
```

 **Violin plot**

 ![](https://i.imgur.com/3d8j0qa.png)

 This plot shows the signal distribution. 

```
"1" : {"plot_type": "violin",
        "plotting_library": "matplotlib",
        "data": {"test": "TEST_1",
                        "traces": {"1": {"device": "5262",
                                          "channel" : "DALLAS_TEMP",
                                        "subplot": 1},
                                    "2": {"device": "5262",
                                           "channel" : "HUM",
                                           "subplot": 1},
                                     "3": {"device": "5262",
                                           "channel" : "TEMP",
                                           "subplot": 1},
                                     "4": {"device": "5262",
                                           "channel" : "GB_2W",
                                           "subplot": 1},
                                     "5": {"device": "5262",
                                           "channel" : "GB_2A",
                                           "subplot": 1},
                                     "6": {"device": "5262",
                                           "channel" : "GB_3W",
                                           "subplot": 1}}},
        "options": {"show_plot": True,
                    "separate_device_plots": False,
                    "export_path": "/Users/macoscar/Desktop", 
                    "file_name": "plot_violin",
                    "target_raster": '10Min',
                    "min_date": None,
                    "max_date": '2019-01-03',
                    "relative": False,
                    "ylabel": {1: "External temperature",
                               2: "Humidity (%RH)",
                               3: "Temperature (degC)",
                               4: "Wir",
                               5: "Wor",
                               6: "Wur"},
                    "yrange": {1: [0, 90],
                               2: [300, 2000],
                               3: [0, 60],
                               4: [0, 60],
                               5: [0,60],
                               6: [0,60]},
                   },
        "formatting": {"title": "Magnificent plot",
                       "grid": True,
                       "height": 10,
                       "width": 15}
        }
```