# Creating a workflow with averages and derivatives with Orange

We can use `Orange data mining` to understand, plot and tinker with math concepts such as averages and derivatives. In this tutorial we're going to explore a workflow that uses data from the SmartCitizen for it.

!!! info "Orange workflow file"
	This tutorial orange file can be downloaded from the repository in this folder: https://github.com/fablabbcn/smartcitizen-docs/tree/master/docs/assets/ows
	The name of the file of this workflow is `example_averages_and_derivatives.ows `


## Requirements

- Understand the basics of `Orange Data Mining` ([check out the other tutorials of Orange Data Mining with Smart Citizen](https://docs.smartcitizen.me/Resources/Tutorials/#visual-programming))
- Have Orange Data Mining with `Time Series` and `Mecoda-orange` add-ons installed ([here is the tutorial to install them](https://docs.smartcitizen.me/Resources/Tutorials/Configure%20Orange%20Data%20Analysis/))

## Get data

We need to set the 3 basic widgets:
- Smart Citizen Search
- Smart Citizen Data
- Data table.

In this workflow we're using data from a existing Smart Citizen in Uruguay.

For the Smart Citizen Search the ID is 14671:

![](/assets/images/Y8TmTY3.png)

Remember to click on `Search devices` to get the information.

Next step is to download the data. In this case we're getting the information in a rollup of 1 minute from 05/February to 28/February:

| Input | value | 
| -------- | -------- | 
| Rollup:    | 1    | 
| Rollup units:    | m  | 
| Initial Date:    | 2023-02-05    | 
| Final Date:    | 2023-02-28    | 
| Resample data:    | **unchecked**    | 

![](/assets/images/cIO2Osg.png)

Remember to click on `Get data` to download the information from the server. 

Next, we connect it to a `Data table` and check that you have all the data. In the bottom part of the window it should say the number of rows that you have (in this case 32.5k)

![](/assets/images/XEHrCYJ.png)

Now we add another widget of `As timeseries` from the `Timeseries` menu and a`Line Chart` to see if everything is correct. This will be the outline of these widgets:

![](/assets/images/i3oh3sE.png)

In this tutorial we're going to focus on the `temperature` but these tools are aplicable to any type of `timeseries` data. 

To see the `temperature` data we can open the line chart and choose to see the temperatures

![](/assets/images/4peaS4J.png)

We can see that we have som variations from day and night. 

!!! info "How to see the x-axis"
    To see the `x-axis` grid you need to _right click_ on the graph, then `plot options>grid` and `Show X grid`. 

![](/assets/images/1pxxH9d.png)


## Aggregate data by date

For doing this we are using the widget `Moving transform` and connect it to the widget `Form timeseries`:

![](/assets/images/7PU0VlS.png)

Inside `Moving transform` we can access to several types of aggregation/transformation. For the temperatures we're going to aggregate by `1 day` and have a chart that takes the average of that day. We then select on the left column the `Aggregate time periods` and `Days`. Select `Temperature` in the column in the center, and in the column on the right `Mean value`.

![](/assets/images/evdWpwe.png)

Check that the output will be `23` (we have 23 days total) from the 32.5k total readings. If we plot them using another `line chart` we'll see that now we have taken out all the signal noise and we now have a cleaner plot:

![](/assets/images/2Ie936S.png)
_Top: raw data. Bottom: daily average_

!!! info "Other averages"

    We can also average by hour. We can get some slight reduction on the noise but you will still get almost all the information about the peaks:

    ![](/assets/images/n1g24np.png)

    Now is time to explore! Maybe explore an average every 2 hours:

    ![](/assets/images/83Og4xF.png)

    And these are the plots comparing the original with the 2 hours average.

    ![](/assets/images/tu1ex3M.png)
    

!!! success "Battery life"

    You can use also mins for detecting when the SCK's battery of the is lower than a certain threshold.


## Using derivatives

If we want to plot derivatives, we can do it in two different ways: directly on the graph, or using widgets. We're going to use the widgets. 

!!! success "Continuity"

    For the derivative to be accurate, we need continuity. For data that is not continuous, we use some linear interpolation to fill the missing data. In this case we're not missing a lot of data but maybe your data needs more interpolation


Now, select the `Derivative` widget from the menu. Then connect it to the  `data table` and then to the `Line Chart`:

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

!!! info "Information about derivatives"

    We can get the information here about the maximums and the minimums. **Each time the line of the derivative crosses 0 there is a local maximum or minimum**.

    When the derivative is positive, it means that the temperature is rising, and when it's negative, it means temperature is decreasing.