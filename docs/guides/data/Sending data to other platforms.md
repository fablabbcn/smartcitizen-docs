TODO

# Sending data to a different platform

In case you don't want to use the Smart Citizen Platform, you can also configure the kit to send the data to a different location via MQTT. This [guide](/guides/getting started/Using the Shell#changing-mqtt-or-ntp-servers), explains how to do so. You will need to ingest data listening to the following MQTT topics:

- Sensor readings: `device/sck/<token>/readings` (old firmware versions) or `device/sck/<token>/readings/raw` (newer firmware versions) with the following format:

	```
	{
		t:<ISO8601 TIMESTAMP>
		<sensor_id>: <sensor_value>,
		...
	}
	```

	Example:

	```
	{
		t:2020-04-05T20:01:10Z,
		55: 22.1,
		102: 43.11
	}
	```

	Note that the JSON representation is not standard, as it does not use quotes. Also, note that the definition of what sensor the `sensor_id` refers to can be found in the [sensors endpoint](https://api.smartcitizen.me/v0/sensors).

- Device info: `device/sck/<token>/info`. Information about the kit, such as firmware versions, or debugging information:

	```
	TODO
	```
