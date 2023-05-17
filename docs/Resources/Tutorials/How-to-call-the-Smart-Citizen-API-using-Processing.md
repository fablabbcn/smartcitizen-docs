# How to call the Smart Citizen API using Processing

![](/assets/images/2xtIx82.png)

This is a tutorial that goes over a sketch in processing that asks via API the data of a specific device and sensor and plots it. There is no need for any specific library. 

It can be easily modified to change the device, the sensor and other elements. 

!!! info "Version used"

    This tutorial was done in 2023 with the version 4.2 for windows of Processing
    
!!! info "Processing file"

    
    You can find the code used in this tutorial here: https://github.com/fablabbcn/smartcitizen-docs/blob/master/docs/assets/pde/SmartCitizenAPIreadings/SmartCitizenAPIreadings.pde
    
    
## The API

The Smartcitizen V0 API is a publicly available interface allowing anyone to develop applications and experiments on top of the Smartcitizen platform.

![](/assets/images/PV4YkRD.png)


The summary of what the API does is that you ask the API for information using a specific URL and the API is going to answer you with data ordered in a JSON. In this tutorial we're going to do that and then print what we have found. 

!!! info "More information about the API"

    For more detailed information about the API visit https://developer.smartcitizen.me
    
## The steps

In this sketch we're going to construct a URL with some example kit (that you can modify to ask about your own device). 

Then we're going to execute the call and finally we're going to process the JSON so we can plot it. 


## Constructing the URL

!!! info "more info"

    Here we're using the historical readings.For more info you can check out the API documentation here: https://developer.smartcitizen.me/#get-historical-readings

In the sketch we are using these variables. In the code are documented and explained one by one. 

#### deviceID

The Device ID is the identifier of a specific kit. You can see it in the URL on the map. Example here: https://smartcitizen.me/kits/15822 

``` java
int deviceId = 15822;
``` 

#### SensorId

SensorId is the way to identify a specific sensor from a Smart Citizen Kit

For your specific sensors of your KIT you can see this: https://api.smartcitizen.me/devices/15822 *substitute 15822 with your device ID* 

For more details of the sensors in the sensor visit here:
https://developer.smartcitizen.me/?shell#get-all-sensors
or here in JSON form
https://api.smartcitizen.me/v0/sensors

``` java
int sensorId = 53;
```

#### Rollup 

In order to get the measures, we need to specify what is the roll up of them. This means if we want the each measure by each day or each 20 seconds. 

In order to get that we need 2 parts of a string. A unit in abbreviation and the amount of that (1 is the most common because we might have a roll up of 1 minute or 1 hour or 1 day). The abbreviations are the following



| Abbreviation | Meaning | 
| -------- | -------- |
|y |    years|
|M |    months|
|w  |weeks|
|d |    days|
|h  |hours|
|m |    minutes|
|s |    seconds|
|ms |   milliseconds|

You can see more info here:
https://developer.smartcitizen.me/?shell#rollup-measurements

``` java
int rollUpNumber = 1;
String rollUpUnit = "m";
```


#### Dates


From Date and To date 

These variables store the information o the starting date in format yyyy-MM-dd

``` java

int fromYear = 2023;
int fromMonth = 1;
int fromDay = 11;


int toYear = 2023;
int toMonth = 1;
int toDay = 12;
``` 

### Assembling

Finally this is the URL that uses all the variables described before. 
``` java
String resourceURL = "https://api.smartcitizen.me/v0/devices/"+deviceId+"/readings?sensor_id="+sensorId+"&rollup="+rollUpNumber+rollUpUnit+"&from="+fromYear+"-"+fromMonth+"-"+fromDay+"&to="+toYear+"-"+toMonth+"-"+toDay;
```

In this case ends up being this url:

https://api.smartcitizen.me/v0/devices/15822/readings?sensor_id=53&rollup=1m&from=2023-1-11&to=2023-1-12

## Making the API call

For this we created a function called get data that gets the data and prepares it. The step of getting the data is this part:

```java
  JSONObject sckData = loadJSONObject(resourceURL);

  JSONArray readings = sckData.getJSONArray("readings");  // This contains your requested device info and data.
```

We have to use JSONObject and JSONArray to get the information. For more information about this objects here you can find the documentation of processing for [JSONArray](https://processing.org/reference/JSONArray.html) and [JSONObject](https://processing.org/reference/JSONObject.html)

## Process the data

The data is stored in a response in JSON that follows a specific structure dictated by the API. You can see it in the API documentation in the **response** table https://developer.smartcitizen.me/#get-historical-readings

![](/assets/images/JqNuJfd.png)

In this sketch we fill a generic array of float numbers using a for loop. 

```java
  readingsFloats = new float[readings.size()];
  for (int i=0; i<readings.size(); i++) {
   readingsFloats[i] = readings.getJSONArray(i).getFloat(1);
  }
```

## Plot the data

Using that array with numbers the program in the setup finds the minimum and the maximum to get a range. 

Then for each value is going to create a small dot (elipse 2,2) and if it's not the first item, it's going to draw a line between that point to the one before. 

``` java
  float minValue = min(readingsFloats);
  float maxValue = max(readingsFloats);
  for (int i = 0; i < readingsFloats.length; i++){
   float x= map(i, 0, readingsFloats.length, 0, width);
   float y= map(readingsFloats[i], maxValue, minValue, 0, height);
   if(i>0) {
     stroke(250);
     line(x,y, map(i-1, 0, readingsFloats.length, 0, width),map(readingsFloats[i-1], maxValue, minValue, 0, height)); 
   }
   ellipse(x, y ,2,2); 

  }
``` 

And this is the result

![](/assets/images/ldi4dcS.png)
