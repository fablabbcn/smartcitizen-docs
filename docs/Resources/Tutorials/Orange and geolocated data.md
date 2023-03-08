# Creating a map workflow in orange

This is a tutorial meant for someone who hasn't used `Orange` at all. It will create a very simple, but powerful, workflow for geographical data. 

!!! info "Orange workflow file"
	This tutorial orange file can be downloaded from the repository in this folder: https://github.com/fablabbcn/smartcitizen-docs/tree/master/docs/assets/ows
	The name of the file of this workflow is `example_map.ows `

**Requirements**:

* Having installed `Orange` and the add-ons of `mecoda-orange` and `geo`. [Here you can see the tutorial](Configure%20Orange%20Data%20Analysis.md)
* Knowing the particular device and the time range that you want to analyse
* Using a kit that has a GPS installed

## Look for the kit that you want to use

We're starting from scratch, a white canvas for this example. 

Click on the widget of `Smart Citizen Search` (on the widgets menu) from the **MECODA** extension. It will create the widget on the canvas on the right:

![](https://i.imgur.com/NdgHPlx.png)

If you click on the new widget that just have appeared in the canvas, a window will pop up with the available options:

![](https://i.imgur.com/H2OGEBv.png)

Here you can search for your Kit. There are several options to retrieve this information but in this case we have the URL of our kit: https://smartcitizen.me/kits/14471. This URL tells us the Device ID that we want at the end of the URL (in this case `15618`).

Once we have it, we type it or paste it in Device ID and press _Search Devices_:

![](https://i.imgur.com/k55Czxv.png)

It will tell us that we have just one result: 

![](https://i.imgur.com/bLJAjMN.png)

Now we found our device, we will get the data that is stored in it!

## Get the data from the kit

We will now add another widget: this time, the `Smart Citizen Data`:

![](https://i.imgur.com/HNGLmeB.png)

It will be set in the canvas near the other widget of `Smart Citizen Search` that we have already configured:

![](https://i.imgur.com/Ds2PQ2b.png)

Now, we will **connect both of them** by pressing the dotted lines on the right of the `Smart Cizizen Search` and dragging the cursor into the `Smart Citizen Data`. Once you have it would look like this: 

![](https://i.imgur.com/DD63yLw.png)

To see if everything is correct we can click on `Smart Citizen Data` and check it out:

![](https://i.imgur.com/3jTD66H.png)

In the `Info panel` you will see the data we are about to load.

Now we will define what data we want to collect. In this example we're getting the data that we have every 10 minutes and we want to get just from one month. From 01/10/2022 to 30/10/2022. To do all that, we will **set the rollup** to **10** and the **rollup units** in **m** (minutes). _(That's the setting by default)_. Then we set **Initial Date** to **2022-10-01** and **End Date** to **2022-11-01**. And we **tick off** the box of **Resample data**. You will have something like this:

![](https://i.imgur.com/cOLbgFN.png)

Now we have to **press Get data** to fetch the data.

![](https://i.imgur.com/Ukd7KVq.png)

It will take some seconds to fetch the data from the platform. Once it's done the Info panel will read: `Device 15618 data downloaded!`

## See the data in a table

As an _optional_ step, we can look at the data in a table format. Place a **Data table** widget from the left menu in `Data`:

![](https://i.imgur.com/7Bdt52b.png)

We click on it as we have clicked on other widgets and it will appear on the canvas:

![](https://i.imgur.com/BO803hU.png)

We connect it to the `Smart Citizen Data` by dragging it's output to the `Data Table` like this:

![](https://i.imgur.com/HZxxq7s.png)

If we open it, we'll see the data that we have gathered. If we scroll to the right (using the scroll at the bottom) we'll see that we have a column with Latitude and other with Longitude:

![](https://i.imgur.com/SsyHdiv.png)

!!! info "More info?"
	The `Data tables` have more properties that are explained here https://orange3.readthedocs.io/projects/orange-visual-programming/en/latest/widgets/data/datatable.html

Now we add one more widget to print this data in a map. 

## Create the map using Geo Map widget

Now, go to the "Geo" panel on the left and click on `Geo Map` widget:

![](https://i.imgur.com/GJK2UbR.png)

It will look like this:

![](https://i.imgur.com/mmPkXPj.png)

As we have done before, we **connect the data table into the Geo Map** dragging from the right of the `data table` (the output) to the left of the `geo map` (the input). When we click on the `geo map`, we see this:

![](https://i.imgur.com/ThxWa1x.png)

We can adjust colors, sizes and parameters using the attributes on the left part of the GUI.

!!! warning ""
	All the data that doesn't have latitude and longitude is ignored by default
