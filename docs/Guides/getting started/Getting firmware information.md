Getting firmware information
============================

There are two ways to get the firmware version:

1. [Using the shell](../Using the Shell/)
2. Following the steps below:

!!! example "Getting firmware information"
    1. Set your kit in setup mode by pressing the ON/OFF button
    ![](https://live.staticflickr.com/65535/48439505516_d210ce2c8a_h.jpg)
    2. **Connect to the kit** with your mobile device as you did during the installation process. You will need to search for a **Wi-Fi network** called `SmartCitizen[···]`. If you have multiple kits `[···]` is the unique identifier of your kit.
    3. Next, go to http://sck.me on your mobile device and click on the top right corner icon:
    ![](/assets/images/sck_2/esp_force_upload_1.png)
    4. Here you go!
    ![](/assets/images/firmware_version_phone.png)

!!! tip "Obtain your firmware version remotely (advanced)"

	If you are an advance user managing a big deployment of devices you can obtain remotely the version of all the Kits you have registered by looking at the `hardware_info` property of each of your devices using the platform API `/v0/devices/`. When your Kit is in Wi-Fi mode, it publishes the information daily.

	```
	"hardware_info": {
		"id": "DFD098A750515157382E3120FF101D12",
		"mac": "B6:E6:2D:66:47:6D",
		"time": "2020-04-14T03:00:24Z",
		"esp_bd": "",
		"hw_ver": "2.1",
		"sam_bd": "2019-11-27T12:49:13Z",
		"esp_ver": "",
		"sam_ver": "0.9.6-4e90c77"
	}
	```

	More info in the platform [API documentation](https://developer.smartcitizen.me/#devices).