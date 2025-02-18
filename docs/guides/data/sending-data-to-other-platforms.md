# Sending data to a different platform

You can have data in real-time on your own data platform in two different ways.

## Directly from the device

In case you don't want to use the Smart Citizen Platform, you can also configure the kit to send the data to a different location via MQTT. This [guide](/guides/getting-started/using-the-shell#changing-mqtt-or-ntp-servers), explains how to do so. You will need to ingest data listening to the following MQTT topics:

- Sensor readings: `device/sck/<token>/readings` (old firmware versions) or `device/sck/<token>/readings/raw` (newer firmware versions) with the following format:

	```
	{
		t:<ISO8601 TIMESTAMP>,
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
	{
		"time":<ISO8601 TIMESTAMP>
		"hw_ver":<HW VERSION>,
		"id":"<HW ID>",
		"sam_ver":<SAM_FW_VERSION-COMMIT>,
		"sam_bd":<SAM_FW_BUILD_DATE>,
		"mac":<MAC_ADDRESS>,
		"esp_ver":<ESP_FW_VERSION-COMMIT>,
		"esp_bd":<ESP_FW_BUILD_DATE>
	}
	```

	Example:

	```
	{
		"time":"2025-02-14T16:20:33Z",
		"hw_ver":"2.1",
		"id":"AAAXXXAAA",
		"sam_ver":"0.9.5-a91f850",
		"sam_bd":"2019-08-20T13:25:01Z",
		"mac":"AA:22:11:AA:22:11",
		"esp_ver":"0.9.2-a91f850",
		"esp_bd":"2019-08-20T13:17:16Z"
	}
	```

## Forwarding from the data platform

You can also forward data from the Smart Citizen Platform itself, with a more complete payload, ready to ingest with a whole lot of additional metadata and information. Check the [data forwarding documentation]({{extra.urls.developer.link}}#data-forwarding).


