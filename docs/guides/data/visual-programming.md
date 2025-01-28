# Visual programming

In this guide we will show how to use visual programming tools for accessing data from the SC API. In particular, we will work with the [Orange data mining](https://orangedatamining.com) tool. This can be quite useful to introduce people to data in contexts when you don't want to code, but maybe web dashboards are too simple. This can be a great tool to teach math in class!

![](/assets/images/nobupdR.png)

## Installation

For this guide you will need to download [Orange data mining](https://orangedatamining.com/download/). In principle with the installation bundle you will be OK, no need to install it via CLI unless you want to develop some modules yourself.

Once you have Orange, you will need to install the following add-ons:

* `Mecoda-orange`
* `Timeseries`
* `Geo` (only in the case of using a GPS)

!!!example "Installing add-ons"

    The process for installing add-ons is simple, but we detail it here for first-timers:

    1. Go to **Options** -> **Add-ons...** and you will see a window like this. Hit "**Add more...**"
    2. You will see a pop-up window asking for the name.

        ![](/assets/images/ArwCdi7.png)

    3. Write **"mecoda-orange"** and we press **add**.
    4. Do the same process for `timeseries` and `geo`.
    5. Check the boxes as below. The _Action_ column should say `Install`. Hit **OK**.

        ![](/assets/images/smH9ABz.png)

    6. It may take some time to install the packages.

        ![](/assets/images/15f1HX9.png)

    7. You may need to restart `Orange` for the changes to take effect.

        ![](/assets/images/qbxH6I4.png)

    8. If all went well, in the panel to the left you will see new widgets available: `MECODA`, `Time Series`, `Geo`
    9. If you open MECODA, you will find the widgets for Smart Citizen (`Smart citizen Search` and `Smart Citizen Data`) among others.

## Using the widgets

There are two widgets available for interacting with the Smart Citizen API: `Smart Citizen Search` and `Smart Citizen Data`. With the first, we will look for devices, and with the second we will get their data.

![](/assets/images/orange-widgets.png)

### Searching devices

This the menu of the _Smart Citizen Search_:

![](/assets/images/H2OGEBv.png)

The **info** panel will get updated with data fetched from the Smart Citizen API once you hit "Search devices". In the bottom part also you can see how many devices have you retrieved from your query.

!!!info "Search all?"
	If you press Search devices while there is no filter it's going to retrieve all the devices in the database, which is not necessarily a bad thing because you can filter/find yours after that.

The **Search filters** apply some filters in case that you rather get a list of devices, instead of a specific one:

* **City**: the city where devices are. First letter is uppercase and with the local denomination.
* **Tags**: tags can be input here separated with commas. If you look for _indoor, online_ the widget is going to get all the kits that at least one of their tags are either _indoor_ **or** _online_
* **User name**: the user that owns the device.
* **Kit ID**: filters by `kit id` (i.e. the type of kit)

!!! info "Already know the ID?"
    If you know the **Device ID**, you can input in the `Device ID` field. This will override any other search filter. Alternatively you can use the search filters to get a list of devices `Device ID` in a table and then lock the ID of the kit that you need information about

### Getting the data

The _Smart Citizen Data_ widget will retrieve the data from **one device**. It needs to have an Smart Citizen device as an input.

![](/assets/images/HNGLmeB.png)

This is the menu of Smart Citizen Data:

![](/assets/images/vLQySNB.png)

The **info** panel gets updated with the device basic information. If it's not connected it will be empty. When you press _Get data_, this panel will also how many rows it has retrieved from the API. In order to customise data frequency and dates, you can use the **Get data at a specific fequency** and **Filter by date** fields

![](/assets/images/xAgiWG7.png)

!!! success "Options meaning"
	The options are y for years, M for months, w for weeks, d for days, h for hours, m for minutes, s for seconds and ms for milliseconds

!!! warning "No frequency, no data"
	This frequency is mandatory to be filled for the widget to work.

!!! info "No date, all data"
	If this field is empty, the widget retrieves all the data on the record.

Finally, the **resample data** checkbox fills the missing data if it doesn't exist. Left unchecked will only get the data that is available.

!!! example "Differences in rollup"
    Example without resampling in a datatable: (rollout of 30 minutes)

    ![](/assets/images/C3R2mqU.png)

    Same example with resampling in a datatable: (rollout of 30 minutes)

    ![](/assets/images/WQsnbro.png)

!!! info "Mecoda"
    [Mecoda](https://github.com/eosc-cos4cloud/mecoda-orange) is a package of widgets for Orange to access data from [Minka](https://minka-sdg.org/), [Odour Collect](https://odourcollect.eu/), [canAIRio](https://canair.io/), [Ictio](https://ictio.org/), [Natusfera](https://natusfera.gbif.es/) or [Smart Citizen]({{ extra.urls.main.link }}).

    Installation steps are also explained [here](https://github.com/eosc-cos4cloud/mecoda-orange/blob/master/docs/installation_and_user_guide.md).

## Examples

We will now look at some examples. You can get all example files from [here](https://github.com/fablabbcn/smartcitizen-docs/tree/master/docs/assets/ows).

### Basic example

Start with this example is you haven't used `Orange` at all. It will create a very simple, but powerful, workflow.

!!! info "Example file"
    This _basic example_ uses the workflow file [here](/assets/ows/example_plot.ows)

#### Search devices

* Click on the widget of `Smart Citizen Search` (on the widgets menu) from the **MECODA** extension. It will create the widget on the canvas on the right:

    ![](/assets/images/NdgHPlx.png)

* If you double click on the widget, a window will pop up with the available options:

    ![](/assets/images/H2OGEBv.png)

* As explained in the [searching devices section](#searching-devices), there are several options to find a kit.In this case we have already know which kit we'll use: https://smartcitizen.me/kits/15618 (in this case `15618`).

    ![](/assets/images/oAhSFjX.png)

* Hit search. You will get one result:

    ![](/assets/images/bLJAjMN.png)

!!!info "Play around with it"
    You can find many other interesting devices with this widget. You can display the devices with a `Data Table`.

#### Get data

* Add another the `Smart Citizen Data` widget and connect both of them:

    ![](https://i.imgur.com/DD63yLw.png)

* To see if everything is correct we can click on `Smart Citizen Data` and check it out. In the `Info panel` you will see the data we are about to load.

* Next, define what data we want to download. In this example we're getting the data every 10 minutes and we want to get just data for one month. From 01/10/2022 to 30/10/2022. To do all that, we will **set the rollup** to **10** and the **rollup units** in **m** (minutes). We will set the **Initial Date** to **2022-10-01** and **End Date** to **2022-11-01**. Keep the **Resample data** unchecked. You will have something like this:

    ![](https://i.imgur.com/cOLbgFN.png)

* Now we have to **press Get data** to fetch the data. It will take some seconds to fetch the data from the platform. Once it's done the Info panel will read: `Device 15618 data downloaded!`

!!! tip "Data in a table"

    As an _optional_ step, you can display the data in a table format. Place a `Data table`` widget from the left menu in `Data` and connect it to the `Smart Citizen Data`` widget:

    ![](/assets/images/HZxxq7s.png)

    If you double click on it, you'll see the data that you have downloaded:

    ![](/assets/images/tog47oH.png)

!!! info "More info?"
	The `Data tables` have more properties that are explained here https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/data/datatable.html

#### Plot it

* To plot data, we need to first convert it to a `timeseries`. Add a `As Timeseries` widget in the `Time series` menu. Connect it to the output of `Smart Citizen Data`:

    ![](/assets/images/0tYVHq5.png)

!!! warning "Timeseries not found?"
    Remember that `timeseries` is an extra add-on that you need to download.

* Lastly, add a `Line chart` (in the `Time Series` menu) and connect it to the `As timeseries`. If the `edit links` windows shows up, select time series to time series as shown. If we click on `Line Chart`, it will show something like this:

![](/assets/images/zdDOrR9.png)

!!! info "Orange docs"
	For more information about this you can visit Orange documentation: https://orange3-timeseries.readthedocs.io/en/latest/widgets/line_chart.html#line-chart

*  Now you can select what data to plot. The chart below is done with one of the columns (in this case `Temperature`). On the left we can `Add more plots` to compare them. For example to compare temperature and humidity:

    ![](/assets/images/iZPmUda.png)

!!! success "Done for today?"
	To save it and reuse later, or sharing your work, you can save the file as a _.ows_

### Geolocated data

!!! info "Example file"
    This _geolocated example_ uses [this workflow file](/assets/ows/example_map.ows)

Building upon the previous example, we will now plot geolocated data on a map. Our basic setup is the same, except that this time we will use another device: `14471`.

!!! tip "How to find other devices?"
    You can use the `Smart Citizen Search` to find other devices

    ![](/assets/images/widggps.png)

    By placing a `Data Table` before the `Smart Citizen Data`, you can look at the search results:

    ![](/assets/images/widgtable.png)

    Then, select the row, and click on the `Send automatically` checkbox:

    ![](/assets/images/widgtablesel.png)

    This will send the selected kit to the `Smart Citizen Data` widget.

Now, you can go to the `Geo` panel to the left and click on `Geo Map` widget:

![](/assets/images/GJK2UbR.png)

It will look like this:

![](/assets/images/mmPkXPj.png)

Then, connect the `Data table` into the `Geo Map`. If you double click on the `geo map`, you should see a nice looking map!:

![](/assets/images/ThxWa1x.png)

!!! info "Changing colours and variables"

    We can adjust colors, sizes and parameters using the attributes on the left part of the GUI.

	For changing the colour palletes use the widget `Color` between the `Data Table` and the `Geo Map`.

!!! warning ""
	All the data that doesn't have latitude and longitude is ignored by default by the widget Geomap

### Derivatives and averages

Finally, we can use `Orange` to understand, plot and tinker with math concepts such as averages and derivatives.

!!! info "Orange workflow file"
	You can find this example [here](/assets/ows/example_averages_and_derivatives.ows)

We will use data from an existing kit in Uruguay (`14671`). We will focus on the `temperature` data, but these tools are aplicable to any type of `timeseries` data. In this case we're getting the information in a rollup of 1 minute from 05/February to 28/February:

![](/assets/images/cIO2Osg.png)

As before, we will add a `Data table`, and then plot it (`As timeseries` + `Line Chart`):

![](/assets/images/i3oh3sE.png)

To see the `temperature` data we can open the line chart and choose to see the temperatures. We can see that we have som variations from day and night!

![](/assets/images/4peaS4J.png)

!!! info "How to see the x-axis"
    To see the `x-axis` grid you need to _right click_ on the graph, then `plot options>grid` and `Show X grid`.

    ![](/assets/images/1pxxH9d.png)

#### Data aggregation by date

We will now use the `Moving transform` widget and connect it to the widget `Form timeseries`:

![](/assets/images/7PU0VlS.png)

Inside `Moving transform` we can access to several types of aggregation/transformation. For the temperatures we're going to aggregate by `1 day` and have a chart that takes the average of that day. We then select on the left column the `Aggregate time periods` and `Days`. Select `Temperature` in the column in the center, and in the column on the right `Mean value`.

![](/assets/images/evdWpwe.png)

Check that the output will be `23` (we have 23 days total) from the **32.5k total readings** (wow!). If we plot them using another `line chart` we'll see that now we have taken out all the signal noise and we now have a cleaner plot:

![](/assets/images/2Ie936S.png)

!!! info "Other averages"

    We can also average by hour. We can get some slight reduction on the noise but you will still get almost all the information about the peaks:

    ![](/assets/images/n1g24np.png)

    Now is time to explore! Maybe explore an average every 2 hours:

    ![](/assets/images/83Og4xF.png)

    And these are the plots comparing the original with the 2 hours average.

    ![](/assets/images/tu1ex3M.png)

#### Using derivatives

If we want to plot _derivatives_, we can do it in two different ways: directly on the graph, or using widgets. We're going to use the widgets.

!!! warning "Continuity"

    For the derivative to be accurate, we need continuity. For data that is not continuous, we use some linear interpolation to fill the missing data. In this case we're not missing a lot of data but maybe your data needs more interpolation!

Select the `Derivative` widget from the menu. Then connect it to the `Data table` and then to the `Line Chart`:

![](/assets/images/weOE529.png)

Next, select the options for the derivative (difference in the widget). In our case we're doing it on `Temperature` (over time):

![](/assets/images/4VLEwB6.png)

Now, open the `Line Chart` and pick `DeltaTemperature`. It'll very likely be a very noisy chart (this is because here we are recording each minimum and maximum):

![](/assets/images/Ac8NgUd.png)

To make it a bit nicer, let's differenciate the arrays of `averages` that we did earlier on. Simply copy and paste the widgets of `differenciation` (or move the connection) to the other part of the outline (note that if you copy the widgets, you need to redo the configuration of the widget.)

![](/assets/images/AlUKIIC.png)

Finally, go to the `line chart` and compare between both signals, the original and the derivative:

![](/assets/images/sSZkMOb.png)

Finally, we can use the plot that we did before with the average hours, which will be a bit more detailed.

![](/assets/images/gnD29rw.png)

![](/assets/images/BCa3YcQ.png)

!!! success "Information about derivatives"

    We can get the information here about the maxima and the minima. **Each time the line of the derivative crosses 0 there is a local maxima or minima**.

    As a basic math concept, when the derivative is positive, it means that the temperature is rising, and when it's negative, it means temperature is decreasing.
