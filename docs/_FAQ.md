Frequently asked questions
==========================

![](https://i.imgur.com/iI3Bu6F.jpg)

## Can the sensors be placed outdoors?
Yes. The sensor is designed for both indoors and outdoors use. But if you’re planning to use it outdoors, you will have to consider purchasing also a rainproof enclosure.

## Can I make my own rainproof enclosure?
Of course! The manufacturing files for the 3D printed enclosure will be available to download. Throughout the history of the Smart Citizen project, we’ve seen many inventive solutions for placing the sensor outdoors.

## Can I charge the sensors with a solar panel?
Sure! But note that the sensor requires a 5V solar panel to work properly. Keeping that in mind, you can buy one of the photovoltaic panels that we provide, or run your own tests.

## Can I add external sensors to the system?
Yes. The sensor has an independently configurable auxiliary bus at 3.3V with a SEEED Grove connector. The Bus has native support for I2C, but it can also be setup on firmware as a GPIO or UART. It can supply power up to 750mA, and it can be enabled or disabled by software.

## What happens if there is a loss of network connectivity?
If the sensor is working in network mode and at any time the network is not available, it will store the data on its internal memory and publish all the collected data as soon as the network is available again.

## Which external sensors can be added?
For the moment, the list of supported sensors includes some Atlas Scientific probes, some Seeed Grove sensors, and the Chirp moisture sensor, but the options are almost endless. We will add tutorials to use the additional sensors listed above in our documentation.However, in the short term we will only offer support for them via our custom hardware development services.

## Will I be able to access the collected data?
Of course! The data collected by your sensor is available for anyone on the Smart Citizen platform, and you can download it at any time as a CSV file. Besides, you can also use the API to built custom applications to interact with your device.

## How does the sensors record the data?
The sensor can work in network and SD card modes. In network mode, the sensor publish data to the SC platform over Wi-Fi every minute. In SD card mode, all the collected data is stored locally in CSV format, and it can be later uploaded manually to the platform using the “Manual Data Upload” option.

## Is there a mobile phone that lets me view the data?
Currently, there is an android app available, but we are working to make the website fully mobile device friendly, so that no mobile phone app is required. We would rather focus the time of our small team on the kits themselves instead of maintaining apps. So our final aim is to be app free, but fully mobile friendly.

## How accurate are the measurements?
Weather, noise, light and PM sensor measurements have been calibrated and validated against reference sensors through both in-house and external validations and they provide accurate data. Chemical gas sensors are to be considered qualitatively rather than quantitatively while calibration algorithms are developed for data accuracy improvement.

## Will the global platform be maintained after the project finishes release?
Yes, it will be maintained just as it has been for the past five years. Also, the platform is fully open source so the community can take over the maintenance if at some point the Smart Citizen core team can no longer run it.

## Are there any notable case studies using similar sensors?
Yes! A particularly interesting case study is the Making Sense project at Plaça del Sol in Barcelona, where a group of 15 technology enthusiasts and environmentalists joined a community of neighbours from a middle-class district that has been suffering from noise issues due to the nightlife in the square. You can find more information about this case study at: www.making-sense.eu

## What happens if i want to move the device or give it to someone else?
With just one press of a button you can fully reset your sensor and configure it again using your account or a new one. All your previous data will remain available on the platform as it was before the reset.

## What about using other wireless technologies?
We are working closely with Barcelona’s The Things Network community to develop a TTN enabled sensor. A LoRA prototype has been tested, but we don’t have dates for the final version yet. BLE, Zigbee, or others are not currently supported, and except for G5, we are not planning to implement them unless there is a custom hardware integration demand.

## Can I remove my data from the platform?
Of course. You are the owner of the data that you collect, and you can download and/or delete all your sensor data at any time.