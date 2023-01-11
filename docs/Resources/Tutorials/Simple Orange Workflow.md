# Simple workflow for data analysis in Orange

This is a tutorial meant for someone who hasn't used Orange at all to create a very simple, but powerful, workflow. 

**Requirements**:

* Having installed orange and the add-ons of mecoda-orange  and time series. [Here you can see the tutorial](Configure%20Orange%20Data%20Analysis.md)
* Knowing the kit and the timespan that you want to analyse

## Look for the kit that you want to use

We're starting from a new file, a white canvas for this example. 

To start using it we need to click on it in the widgets menu on the left for the widget of Smart Citizen Search. We **select** the **Smart Citizen Search** widget from the **MECODA** extension. 

It will create the widget on the canvas on the right

![](https://i.imgur.com/NdgHPlx.png)

If you click on it it will pop up a window with the available options

![](https://i.imgur.com/H2OGEBv.png)

We need to press _Search Devices_ in order to get some data. 

Here you can try to find your Kit. There are several options  to retrieve this information but in this case we have the URL of our kit: https://smartcitizen.me/kits/15618. This URL tells us the Device ID that we want at the end of the URL (in this case 15618).

!!! info "Using the map?"
	If you want to use the map to find your kit follow these instructions.
	
	* Go to https://smartcitizen.me/kits/
	* Find your kit in the map and select it. For example: 
	
	![](https://i.imgur.com/zXmz53a.png)
	
	* When you select it the URL of the site will change, in this case to: https://smartcitizen.me/kits/15618
	* Here you have the device id in the URL at the end. In this case it's 15618. 

Once we have it we type it or paste it in Device ID and press _Search Devices_

![](https://i.imgur.com/oAhSFjX.png)

It will tell us that we have just one data because the icon of exit says that there is only one data. 

![](https://i.imgur.com/bLJAjMN.png)

Now that we have only just one device we need to retrieve the data that is stored in it. 

## Get the data from the kit

Now we need to add another widget from the tools that we have on the left. To do that we **click** ond the widget **Smart Citizen Data** 

![](https://i.imgur.com/HNGLmeB.png)

When we press it it will be set in the canvas near the other widget of Smart Citizen Search that we have already configured.

![](https://i.imgur.com/Ds2PQ2b.png)

We need to **connect both of them** pressing the dotted lines on the right of the Smart Cizizen Search and dragging the cursor into the Smart Citizen Data. Once you have it would look like this: 

![](https://i.imgur.com/DD63yLw.png)

To see if everything is correct we can click on Smart Citizen Data and we can click on it and check it out

![](https://i.imgur.com/3jTD66H.png)

If the Info panel from the image above says the same that yours it will mean that it's working. 

Now we're setting up the data that we want to collect. In this example we're getting the data that we have every 10 minutes (10 minutes) and we want to get just from one month. From first of october of 2022 to the last day of that month. 

To do that we **set** **rollup** in **10** and the **rollup units** in m (minutes). _(that's the setting by default)_ Then we set **Initial Date** to **2022-10-01** and **End Date** to **2022-11-01**. And we **tick off** the box of **Resample data**. You will have something like this:

![](https://i.imgur.com/cOLbgFN.png)

Now we have to **press Get data** to fetch the data. 

![](https://i.imgur.com/Ukd7KVq.png)

It will take some seconds to fetch the data from the back end of smart citizen and it will have in the Info panel "Device 15618 data downloaded!"

## See the data in a table

As an _optional_ step we can look at it as a table. To do that we need to use the widget **Data table** from the left menu in "Data"

![](https://i.imgur.com/7Bdt52b.png)

We click on it as we have clicked on other widgets and it will appear on the canvas

![](https://i.imgur.com/BO803hU.png)

We connect it to the Smart Citizen Data dragging the data from the Smart Citizen Data to the Data Table like this:

![](https://i.imgur.com/HZxxq7s.png)

If we open it we'll see the data that we have gathered clicking on it. 

![](https://i.imgur.com/tog47oH.png)

The Data tables have more propierties that are explained here: 
https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/data/datatable.html

## Set the data as a timeseries

To plot it properly we need to set this data as a timeseries. To do that we need to go to the menu on the left and click on **As Timeseries** in the menu "Time Series". 

![](https://i.imgur.com/r9ONvBD.png)

!!! warning "Timeseries not found?"
	Remember that timeseries is an extra add-on that you need to download. [Link to the docs about how to do it]

We **click it** and it will appear in the canvas

![](https://i.imgur.com/XZOXoy8.png)

We **connect it** to the Smart Citizen Data dragging the data from the Smart Citizen Data to the As Timeseries like this:

![](https://i.imgur.com/0tYVHq5.png)

## Plot the results

Lastly, we create one more widget. **Line chart**. To do that we need to go to the menu on the left and click on **Line chart** in the menu "Time Series". 

![](https://i.imgur.com/vDGjMKa.png)

We **click it** and it will appear in the canvas

![](https://i.imgur.com/k0VH1OP.png)

We **connect it** to the As Timeseries dragging the data from the As Timeseries to the Line chart like this:

![](https://i.imgur.com/nobupdR.png)

If the edit links windows shows up, select time series to time series as shown.

Now we press on the Line Chart and we can see the Chart through time.

## Plot the results and tinker it

If we click on Line Chart it will show something like this:

![](https://i.imgur.com/zdDOrR9.png)

!!! info "Orange docs"
	To more information about this you can visit Orange documentation: https://orange3-timeseries.readthedocs.io/en/latest/widgets/line_chart.html#line-chart

This chart is done with one of the columns (in this case Temperature) and we can see the changes from one day to another and we can see also on the left part of the chart the data that we have missing. 

On the left we can Add more plots to compare them For example to compare temperature and humidity. 

![](https://i.imgur.com/iZPmUda.png)

We can close them to get rid of them usin ghe x arrow. 

To select the type of data that we want to check we need only to get the appropiate sensor and select it. 

To save it or retrieve it again we can save the file as a _.ows_ and retrieve it again. 
