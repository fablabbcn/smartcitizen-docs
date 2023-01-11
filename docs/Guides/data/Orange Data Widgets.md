# MECODA Smartcitizen widgets

**Requisites:**

* Having installed orange and the add-ons. [Here you can check the instructions](/Resources/Tutorials/Configure%20Orange%20Data%20Analysis.md)
* Internet connection

The mecoda-orange add-on includes 2 widgets:

![](https://i.imgur.com/mJ3hdYf.png)

* Smart Citizen Search. This widget looks for the kits in the Smart Citizen kits. Here you select the kit which data you're going to work with

![](https://i.imgur.com/HNGLmeB.png)

* Smart Citizen Data. This widget gets the data from that widget

## Smart Citizen Search

![](https://i.imgur.com/mJ3hdYf.png)

Smart Citizen Search is a widget that gets information about kits, but not the data gathered by those kits. This the menu of the Smart Citizen Search:

![](https://i.imgur.com/H2OGEBv.png)

The **info** panel is going to get updated with data fetched from the Smart Citizen back end. If you don't press "Search devices" is not going to fetch anything. 

!!! info "Search all?"
	If you press Search devices while there is no filter it's going to retrieve all the devices in the database, which is not necessarily a bad thing because you can filter/find yours after that. 

The **Search filters** are going to apply some filters in case that you want to find one specific Kit

* **City** states the city that you are looking for. Remember to spell it with the first letter in upper case and with the local denomination. 
* **Tags** looks for tags separated with commas with the logical operator "OR". That means that if you look for _indoor, online_ the widget is going to get all the kits that at least one of their tags are either _indoor_ or _online_
* **User name** the user that it is linked to. 
* **Kit-ID** refers to the type of kit that is your smart citizen kit. 
![](https://i.imgur.com/4aeaKhP.png)

And lastly if you know the **Device ID** (unique to your specific kit) you can find the kit that you need. You can find the ID of your kit in the last part of the URL of your kit. For example this kit from this URL https://smartcitizen.me/kits/15618 has the Device ID of 15618.

!!! info ""
	Alternatively you can use this search to find the `deviceID` in a table and then lock the ID of the kit that you need information about

The **Search devices** button makes the request to the database so it's important to press it. 

In the bottom part also you can see how many devices have you retrieved from your query. 

### Smart Citizen Data

![](https://i.imgur.com/HNGLmeB.png)

The widget Smart Citizen Data from the data of one (and just one per widget) it will retrieve the data that one device has gathered. 

It requires to be connected as an input one Smart Citizen device. 

This is the menu of Smart Citizen Data:

![](https://i.imgur.com/vLQySNB.png)

* The **info** panel is going to get updated with the data that is connected to. If it's not connected it will be empty. It will show you also when you press _Get data_ how many rows has it retrieved. 

* The **Get data a specific fequency** is the panel where we state the data frequency that we want to get. Rollup is the amount and the Rollup units is the time units that you can choose from.

![](https://i.imgur.com/xAgiWG7.png)

!!! success "Options meaning"

	The options are y for years, M for months, w for weeks, d for days, h for hours, m for minutes, s for seconds and ms for milliseconds

!!! warning "No frequency, no data"
	This frequency is mandatory to be filled for the widget to work. 

* The **Filter by Date (YYYY-MM-DD)** is a panel where you can select a subset of all the dates in format YYYY-MM-DD (Year-month-day). From initial date 00:00 up to end date 00:00 (so the end date is not taken in a complete loop) 

!!! info "No date, all data"
	If this field is empty, the widget retrieves all the data on the record.

* The checkbox **resample data** if checked fills the missing data from the rollup so you will have al the lines from the rollup even if it doesn't exist with empty cells. If it's unchecked is only going to get the data that is available.

Example without resampling in a datatable: (rollout of 30 minutes)

![](https://i.imgur.com/C3R2mqU.png)

Same example with resampling in a datatable: (rollout of 30 minutes)

![](https://i.imgur.com/WQsnbro.png)
