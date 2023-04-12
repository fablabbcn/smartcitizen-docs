

/*

 SmartCitizen API - Procressing.org basic example
 
 This example demonstrate how to do a basic call to the SmartCitizen API 
 to retrieve the latest data from one device. 
 
 For more info:
 http://developer.smartcitizen.me/#devices
 
 This code is under public domain.
*/

/*
deviceID

The Device ID is the identifier of a specific kit. You can see it in the URL on the map. 

https://smartcitizen.me/kits/15822

*/
int deviceId = 15822;


/*
SensorId is the way to identify a specific sensor from a Smart Citizen Kit

For your specific sensors of your KIT you can see this: https://api.smartcitizen.me/devices/15822 *substitute 15822 with your device ID* 

For more details of the sensors in the sensor visit here:
https://developer.smartcitizen.me/?shell#get-all-sensors
or here in JSON form
https://api.smartcitizen.me/v0/sensors

*/
int sensorId = 53;


/*
Roll up are split int 2 parts, the unit (w for week, h for hour, s for second, etc) and the amount (integer)



You can see mor info here:
https://developer.smartcitizen.me/?shell#rollup-measurements

*/
int rollUpNumber = 1;
String rollUpUnit = "m";

/*
From Date
These variables store the information o the starting date in format yyyy-MM-dd
*/
int fromYear = 2023;
int fromMonth = 1;
int fromDay = 11;

/*
To Date


These variables store the information o the starting date in format yyyy-MM-dd
*/
int toYear = 2023;
int toMonth = 1;
int toDay = 12;

/*
Here we are appending the URL with the variables done before. 
*/
String resourceURL = "https://api.smartcitizen.me/v0/devices/"+deviceId+"/readings?sensor_id="+sensorId+"&rollup="+rollUpNumber+rollUpUnit+"&from="+fromYear+"-"+fromMonth+"-"+fromDay+"&to="+toYear+"-"+toMonth+"-"+toDay;
float readingsFloats[] =null;

void setup() {
  println(resourceURL);
  getData();
  size(800,600);
  background(128);
  textAlign(LEFT);
  fill(0);
  text("DeviceId:"+deviceId, 10,10);
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
}

void draw() {



}

void getData() {

  JSONObject sckData = loadJSONObject(resourceURL);

  JSONArray readings = sckData.getJSONArray("readings");  // This contains your requested device info and data.
  readingsFloats = new float[readings.size()];
  for (int i=0; i<readings.size(); i++) {
   readingsFloats[i] = readings.getJSONArray(i).getFloat(1);
  }
  



}
