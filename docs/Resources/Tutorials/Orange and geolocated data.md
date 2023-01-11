# Creating a map workflow in orange

This is a tutorial meant for someone who hasn't used orange at all to create a very simple, but powerful, workflow that has some geographical data. 

**Requirements**:

* Having installed orange and the add-ons of mecoda-orange  and time series. [Here you can find instructions about how to do it](/Resources/Tutorials/Configure%20Orange%20Data%20Analysis.md)
* Using a kit that has a GPS installed
* Knowing the kit and the timespan that you want to analyse

## Look for the kit that you want to use

We're starting from a new file, a white canvas for this example. 

To start using it we need to click on it in the widgets menu on the left for the widget of Smart Citizen Search. We **select** the **Smart Citizen Search** widget from the **MECODA** extension. 

It will create the widget on the canvas on the right

![](https://i.imgur.com/NdgHPlx.png)

If you click on it it will pop up a window with the available options

![](https://i.imgur.com/H2OGEBv.png)

We need to press "Search devices" in order to get some data. 

Here you can try to find your Kit. There are several options  to retrieve this information but in this case we have the URL of our kit

https://smartcitizen.me/kits/14471

This URL tells us the Device ID that we want at the end of the URL (in this case 14471).

!!! info "Using the map?"
	If you want to use the map to find your kit follow this instructions.
	
	Go to 
	
	https://smartcitizen.me/kits/
	
	Find your kit in the map and select it. 
	
	For example: 
	
	![](https://i.imgur.com/zXmz53a.png)
	
	When you select it the URL of the site will change, in this case to: https://smartcitizen.me/kits/15618
	
	Here you have the device id in the URL at the end. In this case it's 15618.

Once we have it we type it or paste it in Device ID and press "Search Devices"

![](https://i.imgur.com/k55Czxv.png)


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

![](https://i.imgur.com/q7Q39tn.png)


If the Info panel from the image above says the same that yours it will mean that it's working. 

Now we're setting up the data that we want to collect. In this example we're getting all the data, so we can leave it as it is and just **press Get data** to fetch the data. 


It will take some seconds to fetch the data from the back end of smart citizen and it will have in the Info panel "Device 14471 data downloaded!"

## See the data in a table

The next step we can look at it as a table. To do that we need to use the widget **Data table** from the left menu in "Data"

![](https://i.imgur.com/7Bdt52b.png)

We click on it as we have clicked on other widgets and it will appear on the canvas

![](https://i.imgur.com/BO803hU.png)

We connect it to the Smart Citizen Data dragging the data from the Smart Citizen Data to the Data Table like this:

![](https://i.imgur.com/HZxxq7s.png)

If we open it we'll see the data that we have gathered clicking on it. If we scroll to the right using the scroll at the bottom we'll see that we have a column with Latitude and other with Longitude

![](https://i.imgur.com/SsyHdiv.png)

The Data tables have more propierties that are explained here: 
https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/data/datatable.html

Now we add one more widget to print this data in a map. 

## Create the map using Geo Map widget

Now we go to the panel on the left that says "Geo" and we click on Geo Map to add the Geo Map widget. 

![](https://i.imgur.com/GJK2UbR.png)

It will look like this

![](https://i.imgur.com/mmPkXPj.png)

As we have done before, we **connect the data table into the Geo Map** dragging from the right of the data table (the output) to the left of the geo map (the input)

We can open it and we'll see something like this

![](https://i.imgur.com/ThxWa1x.png)

In this case we can see the timing of different samples in colour being the bluest the oldest and the most yellow the newest. 

We can adjust ussing the attributes on the left part of the GUI to see where are the places with, i.e more temperature.

!!! warning ""
	All the data that doesn't have latitude and longitude is ignored by default
